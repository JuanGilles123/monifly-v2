from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    DATABASE_URL: str = ""
    CORS_ORIGINS: str = "*"
    SECRET_KEY: str = "change-me-in-production"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24  # 24h


settings = Settings()

app = FastAPI(title="MoniFly API")

origins = [o.strip() for o in settings.CORS_ORIGINS.split(',') if o.strip()]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins or ["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Importar y registrar routers
try:
    from auth_simple import router as auth_router
    app.include_router(auth_router)
    print("✅ Auth router loaded successfully")
except Exception as e:
    print(f"⚠️ Could not load auth router: {e}")
    # Si no se puede importar, usar endpoints básicos


@app.get("/")
async def root():
    return {"ok": True, "name": "MoniFly API"}


@app.get("/healthz")
async def healthz():
    return {"status": "ok"}