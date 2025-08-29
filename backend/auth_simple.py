from fastapi import APIRouter, Response, Request, HTTPException
from pydantic import BaseModel, EmailStr

# Importar settings para cookies
try:
    from app.settings import settings
except ImportError:
    # Fallback si no encuentra app.settings
    class Settings:
        COOKIE_SAMESITE = "none"
        COOKIE_DOMAIN = ""
    settings = Settings()

# Router básico para testing
router = APIRouter(prefix="/auth", tags=["auth"])


class UserRegister(BaseModel):
    email: EmailStr
    name: str = ""
    password: str


class UserLogin(BaseModel):
    email: EmailStr
    password: str


def set_auth_cookie(resp: Response, token: str):
    """Configurar cookie de autenticación"""
    resp.set_cookie(
        "access_token",
        token,
        httponly=True,
        secure=True,
        samesite=settings.COOKIE_SAMESITE,
        domain=(settings.COOKIE_DOMAIN or None),
        max_age=60 * 60 * 24,
        path="/",
    )


@router.get("/test")
async def test_auth():
    """Test endpoint para verificar que el router funciona"""
    return {"message": "Auth router working", "status": "ok"}


@router.post("/register")
async def register(user: UserRegister):
    """Registro de usuario - implementación básica"""
    # TODO: Implementar con base de datos real
    return {
        "ok": True,
        "message": f"Usuario {user.email} registrado",
        "user": {"email": user.email, "name": user.name}
    }


@router.post("/login")
async def login(user: UserLogin, response: Response):
    """Login de usuario con cookie"""
    # TODO: Validar credenciales con base de datos
    
    # Por ahora, simular login exitoso
    fake_token = f"fake-jwt-token-for-{user.email}"
    set_auth_cookie(response, fake_token)
    
    return {
        "ok": True,
        "message": "Login exitoso",
        "user": {"email": user.email, "id": 1}
    }


@router.get("/me")
async def me(request: Request):
    """Obtener perfil de usuario"""
    token = request.cookies.get("access_token")
    
    if not token:
        raise HTTPException(401, "No autenticado")
    
    # TODO: Decodificar JWT real
    # Por ahora, extraer email del token fake
    if token.startswith("fake-jwt-token-for-"):
        email = token.replace("fake-jwt-token-for-", "")
        return {
            "id": 1,
            "email": email,
            "name": "Usuario Demo",
            "token_info": "Cookie recibida correctamente"
        }
    
    raise HTTPException(401, "Token inválido")


@router.post("/logout")
async def logout(response: Response):
    """Cerrar sesión"""
    response.delete_cookie("access_token", path="/")
    return {"ok": True, "message": "Sesión cerrada"}
