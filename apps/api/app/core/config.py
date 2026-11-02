"""Application configuration."""

from pathlib import Path
from typing import List

from pydantic_settings import BaseSettings

REPO_ROOT = Path(__file__).resolve().parents[4]


class Settings(BaseSettings):
    model_config = {
        "env_file": str(REPO_ROOT / ".env"),
        "env_file_encoding": "utf-8",
    }

    # Application
    app_env: str = "development"
    app_base_url: str = "http://localhost:3000"
    secret_key: str = "change-me-in-production"

    # Database
    database_url: str = "postgresql+asyncpg://cyberme:password@127.0.0.1:15432/cyberme"

    # Redis
    redis_url: str = "redis://127.0.0.1:6379/0"

    # S3
    s3_endpoint: str = ""
    s3_bucket: str = ""
    s3_access_key: str = ""
    s3_secret_key: str = ""

    # AI Providers
    openai_api_key: str = ""
    anthropic_api_key: str = ""
    deepseek_api_key: str = ""
    deepseek_base_url: str = "https://api.deepseek.com/v1"

    # Budget
    default_model_route: str = "evidence_qa.default"
    monthly_budget_limit: float = 50.0

    # GitHub
    github_token: str = ""

    # Yuketang (Changjiang) — read-only integration
    ykt_region: str = "changjiang"
    ykt_sessionid: str = ""
    ykt_refresh_minutes: int = 15

    # Sync
    sync_max_file_mb: int = 10
    raw_archive_upload: bool = False

    # CORS
    @property
    def cors_origins(self) -> List[str]:
        if self.is_development:
            return [
                "http://localhost:3000",
                "http://127.0.0.1:3000",
                "http://localhost:5173",
                "http://127.0.0.1:5173",
                # Capacitor bundled WebView origins (debug/local use).
                "http://localhost",
                "https://localhost",
                "capacitor://localhost",
            ]
        return [self.app_base_url]

    @property
    def is_development(self) -> bool:
        return self.app_env == "development"


settings = Settings()
