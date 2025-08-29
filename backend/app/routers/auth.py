from fastapi import APIRouter, Depends, HTTPException, Response, Request, status
from pydantic import BaseModel, EmailStr
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from passlib.hash import bcrypt
from jose import jwt
from datetime import datetime, timedelta

from app.db import SessionLocal
from app.models import User
from app.settings import settings

router = APIRouter(prefix="/auth", tags=["auth"])


class RegisterIn(BaseModel):
    email: EmailStr
    name: str = ""
    password: str


class LoginIn(BaseModel):
    email: EmailStr
    password: str


async def get_db():
    async with SessionLocal() as s:
        yield s


def make_token(sub: str, minutes: int = settings.ACCESS_TOKEN_EXPIRE_MINUTES):
    exp = datetime.utcnow() + timedelta(minutes=minutes)
    return jwt.encode(
        {"sub": sub, "exp": exp}, 
        settings.SECRET_KEY, 
        algorithm=settings.ALGORITHM
    )


def set_auth_cookie(resp: Response, token: str):
    resp.set_cookie(
        "access_token",
        token,
        httponly=True,
        secure=True,
        samesite="lax",
        max_age=60 * 60 * 24,
        path="/"
    )


@router.post("/register")
async def register(data: RegisterIn, db: AsyncSession = Depends(get_db)):
    exists = await db.scalar(select(User).where(User.email == data.email))
    if exists:
        raise HTTPException(409, "Email ya registrado")
    
    user = User(
        email=data.email,
        name=data.name,
        password_hash=bcrypt.hash(data.password)
    )
    db.add(user)
    await db.commit()
    return {"ok": True}


@router.post("/login")
async def login(
    data: LoginIn, 
    response: Response, 
    db: AsyncSession = Depends(get_db)
):
    user = await db.scalar(select(User).where(User.email == data.email))
    if not user or not bcrypt.verify(data.password, user.password_hash):
        raise HTTPException(
            status_code=401, 
            detail="Credenciales inválidas"
        )
    
    token = make_token(str(user.id))
    set_auth_cookie(response, token)
    return {"ok": True}


@router.post("/logout")
async def logout(response: Response):
    response.delete_cookie("access_token", path="/")
    return {"ok": True}


def get_current_user_id(request: Request) -> int | None:
    token = request.cookies.get("access_token")
    if not token:
        return None
    try:
        payload = jwt.decode(
            token, 
            settings.SECRET_KEY, 
            algorithms=[settings.ALGORITHM]
        )
        return int(payload["sub"])
    except Exception:
        return None


@router.get("/me")
async def me(request: Request, db: AsyncSession = Depends(get_db)):
    uid = get_current_user_id(request)
    if not uid:
        raise HTTPException(401, "No autenticado")
    
    user = await db.get(User, uid)
    if not user:
        raise HTTPException(404, "Usuario no encontrado")
    
    return {
        "id": user.id,
        "email": user.email,
        "name": user.name
    }
