#!/bin/bash
set -e

echo "🚀 Starting MoniFly Backend..."

# Instalar dependencias si no están
pip install --no-cache-dir -r requirements.txt

# Ejecutar migraciones (si hay DATABASE_URL)
if [ ! -z "$DATABASE_URL" ]; then
    echo "📦 Running database migrations..."
    alembic upgrade head || echo "⚠️  No migrations to run or DB not ready"
fi

# Iniciar servidor
echo "🎯 Starting server on port ${PORT:-8080}..."
exec python -m uvicorn app.main:app --host 0.0.0.0 --port ${PORT:-8080}
