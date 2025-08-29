#!/usr/bin/env python3
"""
Script para desarrollo local de MoniFly backend
Usa SQLite en lugar de PostgreSQL para pruebas rápidas
"""
import sys
import os
import subprocess
from pathlib import Path

def main():
    print("🚀 MoniFly Local Development Server")
    print("==================================")
    
    # Cambiar al directorio del script
    os.chdir(Path(__file__).parent)
    
    # Instalar aiosqlite para SQLite async
    print("📦 Installing aiosqlite...")
    subprocess.run([sys.executable, "-m", "pip", "install", "aiosqlite"], check=True)
    
    # Configurar variables de entorno para desarrollo local
    os.environ["DATABASE_URL"] = "sqlite+aiosqlite:///./test.db"
    os.environ["CORS_ORIGINS"] = "http://localhost:3000,http://127.0.0.1:3000"
    os.environ["SECRET_KEY"] = "dev-secret-key-for-local-testing"
    
    print("🗄️  Using SQLite database: ./test.db")
    print("🌐 CORS enabled for: http://localhost:3000")
    print("🔑 Using development secret key")
    print()
    
    # Ejecutar migraciones si existen
    try:
        print("📋 Running database migrations...")
        subprocess.run(["alembic", "upgrade", "head"], check=False)
        print("✅ Migrations completed")
    except Exception as e:
        print(f"⚠️  Migration skipped: {e}")
    
    print()
    print("🎯 Starting FastAPI server on http://localhost:8000")
    print("📚 API docs available at: http://localhost:8000/docs")
    print("🔍 Health check: http://localhost:8000/healthz")
    print()
    print("Press Ctrl+C to stop")
    print("-" * 50)
    
    # Iniciar servidor
    subprocess.run([
        sys.executable, "-m", "uvicorn", 
        "main:app", 
        "--host", "0.0.0.0", 
        "--port", "8000",
        "--reload"
    ])

if __name__ == "__main__":
    main()
