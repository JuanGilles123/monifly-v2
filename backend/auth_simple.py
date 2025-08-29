from fastapi import APIRouter

# Router básico para testing
router = APIRouter(prefix="/auth", tags=["auth"])

@router.get("/test")
async def test_auth():
    """Test endpoint para verificar que el router funciona"""
    return {"message": "Auth router working", "status": "ok"}

@router.post("/register")
async def register():
    """Registro de usuario - implementación básica"""
    return {"message": "Register endpoint", "todo": "implement with database"}

@router.post("/login") 
async def login():
    """Login de usuario - implementación básica"""
    return {"message": "Login endpoint", "todo": "implement with database"}

@router.get("/me")
async def me():
    """Obtener perfil de usuario"""
    return {"message": "Profile endpoint", "todo": "implement with auth"}
