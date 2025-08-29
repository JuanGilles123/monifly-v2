from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    CORS_ORIGINS: str = "*"  # luego lo pondremos en https://app.monifly.app


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


@app.get("/")
async def root():
    return {"ok": True, "name": "MoniFly API"}


@app.get("/healthz")
async def healthz():
    return {"status": "ok"}