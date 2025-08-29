from logging.config import fileConfig
from sqlalchemy import pool
from sqlalchemy import engine_from_config
from alembic import context
import os

config = context.config

if config.config_file_name is not None:
    fileConfig(config.config_file_name)

target_metadata = None
# Importar modelos para migraciones automáticas
try:
    import sys
    import os
    sys.path.append(os.path.dirname(os.path.dirname(__file__)))
    from app.models import Base
    target_metadata = Base.metadata
except ImportError:
    # Si no se pueden importar los modelos, usar None
    target_metadata = None

url = os.environ.get("DATABASE_URL")
if url and "sslmode" not in url:
    url += ("&" if "?" in url else "?") + "sslmode=require"

def run_migrations_offline():
    context.configure(url=url, target_metadata=target_metadata,
                      literal_binds=True)
    with context.begin_transaction():
        context.run_migrations()

def run_migrations_online():
    connectable = engine_from_config(
        {"sqlalchemy.url": url}, poolclass=pool.NullPool
    )
    with connectable.connect() as connection:
        context.configure(connection=connection,
                          target_metadata=target_metadata)
        with context.begin_transaction():
            context.run_migrations()

if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
