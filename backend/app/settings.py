from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    DATABASE_URL: str = ""
    CORS_ORIGINS: str = "*"
    SECRET_KEY: str = "change-me-in-production"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24  # 24h
    
    # Cookie settings para cross-domain
    COOKIE_SAMESITE: str = "none"  # "none" para cross-domain, "lax" para same domain
    COOKIE_DOMAIN: str = ""        # ".monifly.app" cuando uses dominios custom


settings = Settings()
