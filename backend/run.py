#!/usr/bin/env python3
import subprocess
import sys
import os


def main():
    print("🚀 MoniFly Backend Starting...")
    
    # Install dependencies
    print("📦 Installing dependencies...")
    subprocess.run([
        sys.executable, "-m", "pip", "install", 
        "--no-cache-dir", "-r", "requirements.txt"
    ], check=True)
    
    # Run migrations if DATABASE_URL exists
    if os.getenv("DATABASE_URL"):
        print("🗄️ Running migrations...")
        try:
            subprocess.run(["alembic", "upgrade", "head"], check=False)
        except Exception:
            print("⚠️ Migrations skipped")
    
    # Start server - CRITICAL: Set PYTHONPATH to current directory
    port = os.getenv("PORT", "8080")
    print(f"🎯 Starting server on port {port}...")
    
    # Add current directory to Python path
    os.environ["PYTHONPATH"] = "."
    
    subprocess.run([
        sys.executable, "-m", "uvicorn",
        "main:app",
        "--host", "0.0.0.0",
        "--port", port
    ], check=False)


if __name__ == "__main__":
    main()
