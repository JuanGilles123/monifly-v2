# MoniFly v2

Aplicación de finanzas personales construida con Python (FastAPI) + React + Tailwind CSS.

## Arquitectura

- **Backend**: FastAPI + SQLAlchemy + Alembic + PostgreSQL
- **Frontend**: React + Vite + Tailwind CSS + Framer Motion
- **Deployment**: DigitalOcean App Platform

## Estructura

```
monifly-v2/
├── backend/           # FastAPI API
│   ├── app/
│   │   ├── main.py    # Aplicación FastAPI
│   │   ├── db.py      # Configuración base de datos
│   │   └── alembic/   # Migraciones
│   ├── requirements.txt
│   └── alembic.ini
├── frontend/          # React SPA
│   ├── src/
│   │   ├── main.jsx
│   │   ├── pages/
│   │   └── index.css
│   ├── package.json
│   └── vite.config.js
└── README.md
```

## Desarrollo Local

### Backend
```bash
cd backend
pip install -r requirements.txt
uvicorn app.main:app --reload --port 8080
```

### Frontend
```bash
cd frontend
npm install
npm run dev
```

## Deployment en DigitalOcean

### 1. Web Service (Backend)
- Source Directory: `backend`
- Build Command: `pip install -r requirements.txt && alembic upgrade head || true`
- Run Command: `uvicorn app.main:app --host 0.0.0.0 --port 8080`
- Health Check: `/healthz`
- Domain: `api.monifly.app`

### 2. Static Site (Frontend)
- Source Directory: `frontend`
- Build Command: `npm ci && npm run build`
- Output Directory: `dist`
- Domain: `app.monifly.app`

## Variables de Entorno

### Backend
- `DATABASE_URL`: URL de PostgreSQL (automáticamente inyectada por DO)
- `CORS_ORIGINS`: `https://app.monifly.app`

### Frontend
- `VITE_API_URL`: `https://api.monifly.app`

## DNS (Name.com)

```
CNAME app -> xxx.ondigitalocean.app (Static Site)
CNAME api -> yyy.ondigitalocean.app (Web Service)
```

## Endpoints

- `GET /` - Info de la API
- `GET /healthz` - Health check