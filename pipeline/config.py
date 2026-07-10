"""Configuration du pipeline : variables d'environnement + chemins du repo."""

import os
from dataclasses import dataclass, field
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent


def _load_dotenv(path: Path) -> None:
    if not path.exists():
        return
    for line in path.read_text().splitlines():
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, _, value = line.partition("=")
        os.environ.setdefault(key.strip(), value.strip())


@dataclass
class Config:
    client_id: str = ""
    client_secret: str = ""
    token_enc_key: str = ""
    anthropic_api_key: str = ""
    claude_model: str = "claude-sonnet-5"

    repo_root: Path = REPO_ROOT
    sources_dir: Path = REPO_ROOT / "sources"
    notes_dir: Path = REPO_ROOT / "notes"
    indexes_dir: Path = REPO_ROOT / "indexes"
    state_dir: Path = REPO_ROOT / "state"
    taxonomy_path: Path = REPO_ROOT / "taxonomy.yaml"
    token_path: Path = field(default=REPO_ROOT / "state" / "token.enc")

    @property
    def seen_ids_path(self) -> Path:
        return self.state_dir / "seen_ids.json"


def load_config() -> Config:
    _load_dotenv(REPO_ROOT / ".env")
    return Config(
        client_id=os.environ.get("X_CLIENT_ID", ""),
        client_secret=os.environ.get("X_CLIENT_SECRET", ""),
        token_enc_key=os.environ.get("TOKEN_ENC_KEY", ""),
        anthropic_api_key=os.environ.get("ANTHROPIC_API_KEY", ""),
        claude_model=os.environ.get("CLAUDE_MODEL", "claude-sonnet-5"),
    )
