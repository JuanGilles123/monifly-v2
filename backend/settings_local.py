from pydantic_settings import BaseSettings
import os


class Settings(BaseSettings):
    # Para desarrollo local, usa SQLite
    DATABASE_URL: str = "sqlite+aiosqlite:///./test.db"
    CORS_ORIGINS: str = "http://localhost:3000,http://127.0.0.1:3000"
    SECRET_KEY: str = "dev-secret-key-change-in-production"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24  # 24h

    class Config:
        env_file = ".env"


settings = Settings()
