from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from .settings import settings


db_url = settings.DATABASE_URL
if db_url and "sslmode" not in db_url:
    sep = "&" if "?" in db_url else "?"
    db_url = f"{db_url}{sep}sslmode=require"

engine = create_async_engine(db_url, pool_pre_ping=True)
SessionLocal = async_sessionmaker(engine, expire_on_commit=False)
