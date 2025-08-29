from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from pydantic_settings import BaseSettings

class DBSettings(BaseSettings):
    DATABASE_URL: str  # DO la inyecta al adjuntar la DB

s = DBSettings()
url = s.DATABASE_URL

if "sslmode" not in url:
    url += ("&" if "?" in url else "?") + "sslmode=require"

engine = create_async_engine(url, pool_pre_ping=True)
SessionLocal = async_sessionmaker(engine, expire_on_commit=False)
