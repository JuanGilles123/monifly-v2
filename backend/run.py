#!/usr/bin/env python3
import subprocess
import sys
import os

def main():
    print("🚀 MoniFly Backend Starting...")
    
    # Install dependencies
    print("📦 Installing dependencies...")
    subprocess.run([sys.executable, "-m", "pip", "install", "--no-cache-dir", "-r", "requirements.txt"], check=True)
    
    # Run migrations if DATABASE_URL exists
    if os.getenv("DATABASE_URL"):
        print("🗄️ Running migrations...")
        try:
            subprocess.run(["alembic", "upgrade", "head"], check=False)
        except:
            print("⚠️ Migrations skipped")
    
    # Start server
    port = os.getenv("PORT", "8080")
    print(f"🎯 Starting server on port {port}...")
    subprocess.run([
        sys.executable, "-m", "uvicorn", 
        "app.main:app", 
        "--host", "0.0.0.0", 
        "--port", port
    ])

if __name__ == "__main__":
    main()
