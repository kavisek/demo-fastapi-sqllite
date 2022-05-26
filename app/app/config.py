# This file container the base configuration of the API.
# - API Configuration.

from functools import lru_cache

from pydantic import BaseSettings


class Settings(BaseSettings):
    """Base configuration details.

    Args:
        BaseSettings (_type_): pydantic base class.
    """

    app_name: str = "solana tracker"
    env_name: str = "Local"
    base_url: str = "http://localhost:8000"
    db_url: str = "sqlite:///./local.db"


@lru_cache
def get_settings() -> Settings:
    """Retrieve configuration settings."""
    settings = Settings()
    print(f"Loading settings for: {settings.env_name}")
    return settings
