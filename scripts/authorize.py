"""Autorisation initiale OAuth 2.0 PKCE — à lancer UNE fois, en local.

Prérequis : une app sur https://developer.x.com avec OAuth 2.0 activé et
`http://localhost:8484/callback` dans les redirect URIs.

Usage :
    X_CLIENT_ID=... [X_CLIENT_SECRET=...] python scripts/authorize.py

Le script ouvre l'URL d'autorisation, récupère le code, l'échange contre un
token et l'écrit chiffré dans state/token.enc. Si TOKEN_ENC_KEY n'existe pas,
il en génère une — à conserver (secret GitHub + .env local).
"""

import base64
import hashlib
import os
import secrets
import sys
import urllib.parse

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

import httpx
from cryptography.fernet import Fernet

from pipeline.config import load_config
from pipeline.x_client import TOKEN_URL, XClient

AUTHORIZE_URL = "https://x.com/i/oauth2/authorize"
REDIRECT_URI = "http://localhost:8484/callback"
SCOPES = "tweet.read users.read bookmark.read offline.access"


def main() -> None:
    cfg = load_config()
    if not cfg.client_id:
        raise SystemExit("X_CLIENT_ID manquant (env ou .env)")

    if not cfg.token_enc_key:
        cfg.token_enc_key = Fernet.generate_key().decode()
        print("\n⚠️  Nouvelle clé de chiffrement générée. À conserver précieusement :")
        print(f"\n    TOKEN_ENC_KEY={cfg.token_enc_key}\n")
        print("→ à mettre dans .env (local) ET dans les secrets GitHub du repo.\n")

    verifier = secrets.token_urlsafe(64)
    challenge = base64.urlsafe_b64encode(
        hashlib.sha256(verifier.encode()).digest()).rstrip(b"=").decode()
    state = secrets.token_urlsafe(16)

    params = {
        "response_type": "code",
        "client_id": cfg.client_id,
        "redirect_uri": REDIRECT_URI,
        "scope": SCOPES,
        "state": state,
        "code_challenge": challenge,
        "code_challenge_method": "S256",
    }
    print("1. Ouvre cette URL dans ton navigateur et autorise l'app :\n")
    print(f"   {AUTHORIZE_URL}?{urllib.parse.urlencode(params)}\n")
    print("2. Après redirection vers localhost (la page ne chargera pas, c'est normal),")
    redirect = input("   colle ici l'URL complète de la barre d'adresse :\n   > ").strip()

    query = urllib.parse.parse_qs(urllib.parse.urlparse(redirect).query)
    if query.get("state", [""])[0] != state:
        raise SystemExit("state mismatch — recommencer")
    code = query["code"][0]

    data = {
        "grant_type": "authorization_code",
        "code": code,
        "client_id": cfg.client_id,
        "redirect_uri": REDIRECT_URI,
        "code_verifier": verifier,
    }
    auth = (cfg.client_id, cfg.client_secret) if cfg.client_secret else None
    resp = httpx.post(TOKEN_URL, data=data, auth=auth, timeout=30)
    resp.raise_for_status()
    token = resp.json()

    # Écrit le token chiffré via XClient.save_token (même format que le pipeline).
    fernet = Fernet(cfg.token_enc_key.encode())
    cfg.token_path.parent.mkdir(parents=True, exist_ok=True)
    cfg.token_path.write_bytes(fernet.encrypt(b"{}"))  # amorce pour le constructeur
    client = XClient.__new__(XClient)
    client.cfg = cfg
    client._fernet = fernet
    client.save_token(token)

    print(f"\n✓ Token écrit dans {cfg.token_path} (chiffré).")
    print("  Committer ce fichier : la CI en a besoin et le met à jour à chaque run.")


if __name__ == "__main__":
    main()
