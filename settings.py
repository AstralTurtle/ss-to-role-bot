from pydantic_settings import BaseSettings, SettingsConfigDict

from functools import cache


class Settings(BaseSettings):
    guild_id: int
    token: str
    role: str

    model_config = SettingsConfigDict(env_file=".env")


@cache
def get_settings() -> Settings:
    return Settings()
