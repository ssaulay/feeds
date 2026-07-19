"""Client X API v2 : token OAuth 2.0 chiffré + refresh rotatif + bookmarks.

Les refresh tokens X sont à usage unique (rotation à chaque refresh). Le token
est donc persisté dans state/token.enc, chiffré (Fernet) avec TOKEN_ENC_KEY, et
committé par la CI après chaque run — seule la clé reste en secret GitHub.
"""

import json
import time

import httpx
from cryptography.fernet import Fernet

from .config import Config

TOKEN_URL = "https://api.x.com/2/oauth2/token"
API_BASE = "https://api.x.com/2"

BOOKMARK_PARAMS = {
    "max_results": "50",
    "tweet.fields": "created_at,entities,author_id,note_tweet,referenced_tweets,attachments",
    # referenced_tweets.id ramène le texte des tweets cités/répondus, et
    # attachments.media_keys les images (du post et des tweets cités) — tout dans
    # les includes de la même réponse (pas de read facturé en plus).
    "expansions": ("author_id,referenced_tweets.id,referenced_tweets.id.author_id,"
                   "attachments.media_keys,referenced_tweets.id.attachments.media_keys"),
    "user.fields": "username,name",
    "media.fields": "type,url,preview_image_url,alt_text",
}


class XClient:
    def __init__(self, cfg: Config):
        if not cfg.client_id:
            raise SystemExit("X_CLIENT_ID manquant (voir .env.example)")
        if not cfg.token_enc_key:
            raise SystemExit("TOKEN_ENC_KEY manquant — lancer scripts/authorize.py d'abord")
        self.cfg = cfg
        self._fernet = Fernet(cfg.token_enc_key.encode())
        if not cfg.token_path.exists():
            raise SystemExit(f"{cfg.token_path} introuvable — lancer scripts/authorize.py d'abord")
        self._token = json.loads(self._fernet.decrypt(cfg.token_path.read_bytes()))

    def save_token(self, token: dict) -> None:
        token = dict(token)
        token.setdefault("expires_at", time.time() + token.get("expires_in", 7200))
        self.cfg.token_path.parent.mkdir(parents=True, exist_ok=True)
        self.cfg.token_path.write_bytes(self._fernet.encrypt(json.dumps(token).encode()))
        self._token = token

    def _refresh_if_needed(self) -> None:
        if time.time() < self._token.get("expires_at", 0) - 120:
            return
        data = {
            "grant_type": "refresh_token",
            "refresh_token": self._token["refresh_token"],
            "client_id": self.cfg.client_id,
        }
        auth = (self.cfg.client_id, self.cfg.client_secret) if self.cfg.client_secret else None
        resp = httpx.post(TOKEN_URL, data=data, auth=auth, timeout=30)
        resp.raise_for_status()
        new_token = resp.json()
        # Rotation : si X ne renvoie pas de nouveau refresh_token, garder l'actuel.
        new_token.setdefault("refresh_token", self._token["refresh_token"])
        self.save_token(new_token)

    def _get(self, path: str, params: dict | None = None) -> dict:
        self._refresh_if_needed()
        headers = {"Authorization": f"Bearer {self._token['access_token']}"}
        resp = httpx.get(f"{API_BASE}{path}", params=params, headers=headers, timeout=30)
        resp.raise_for_status()
        return resp.json()

    def me(self) -> dict:
        return self._get("/users/me")["data"]

    @staticmethod
    def _hydrate(payload: dict) -> list[dict]:
        """Résout auteurs et tweets cités/répondus depuis les includes."""
        tweets = payload.get("data", [])
        includes = payload.get("includes", {})
        users = {u["id"]: u for u in includes.get("users", [])}
        inc_tweets = {t["id"]: t for t in includes.get("tweets", [])}
        media = {m["media_key"]: m for m in includes.get("media", [])}

        def attach_media(t: dict) -> None:
            keys = (t.get("attachments") or {}).get("media_keys", [])
            t["media"] = [media[k] for k in keys if k in media]

        for tweet in tweets:
            tweet["author"] = users.get(tweet.get("author_id"), {})
            attach_media(tweet)
            referenced = []
            for ref in tweet.get("referenced_tweets", []):
                cited = inc_tweets.get(ref.get("id"))
                if not cited:
                    continue
                cited = dict(cited)
                cited["author"] = users.get(cited.get("author_id"), {})
                attach_media(cited)
                referenced.append({"type": ref.get("type"), "tweet": cited})
            tweet["referenced"] = referenced
        return tweets

    def iter_bookmark_pages(self, user_id: str):
        """Itère sur les pages de bookmarks, des plus récents aux plus anciens
        (X conserve ~800 bookmarks). Chaque page est facturée en owned reads."""
        next_token = None
        while True:
            params = dict(BOOKMARK_PARAMS)
            if next_token:
                params["pagination_token"] = next_token
            payload = self._get(f"/users/{user_id}/bookmarks", params)
            yield self._hydrate(payload)
            next_token = payload.get("meta", {}).get("next_token")
            if not next_token:
                return

    def fetch_bookmarks(self, user_id: str) -> list[dict]:
        """Retourne la première page de bookmarks (les plus récents), auteur résolu.

        À quelques bookmarks/jour, une page de 50 avec déduplication en aval
        suffit largement ; on évite de payer des reads de pagination inutiles.
        """
        return next(self.iter_bookmark_pages(user_id))
