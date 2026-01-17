from functools import lru_cache

from pydantic_settings import BaseSettings

DB_FILENAME = "database.db"


@lru_cache
def get_settings():
    return Settings()


class Settings(BaseSettings):
    db_url: str = "sqlite:///{DB_FILENAME}"
