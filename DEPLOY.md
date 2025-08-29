# DigitalOcean App Platform Configuration

Este archivo contiene las configuraciones exactas para crear la app en DigitalOcean.

## 🌐 Web Service (Backend API)

**Configuración:**
- **Name**: `monifly-api`
- **Source**: GitHub `JuanGilles123/monifly-v2`
- **Branch**: `master`
- **Source Directory**: `backend`
- **Build Command**: `pip install -r requirements.txt && alembic upgrade head || true`
- **Run Command**: `uvicorn app.main:app --host 0.0.0.0 --port 8080`
- **Port**: `8080`
- **Health Check Path**: `/healthz`

**Environment Variables:**
```
DATABASE_URL=(auto-injected by DO when you attach the database)
CORS_ORIGINS=https://app.monifly.app
```

**Domain:**
- Add domain: `api.monifly.app`

## 🎨 Static Site (Frontend)

**Configuración:**
- **Name**: `monifly-frontend`
- **Source**: GitHub `JuanGilles123/monifly-v2`
- **Branch**: `master`
- **Source Directory**: `frontend`
- **Build Command**: `npm ci && npm run build`
- **Output Directory**: `dist`

**Environment Variables:**
```
VITE_API_URL=https://api.monifly.app
```

**Domain:**
- Add domain: `app.monifly.app`

## 🗄️ Database

- **Type**: Attach existing Managed PostgreSQL
- **Name**: Tu base de datos existente
- ✅ DO inyectará automáticamente la `DATABASE_URL`

## 🌍 DNS Configuration (Name.com)

Después de crear la app, DO te dará las URLs. Crea estos CNAME en Name.com:

```
CNAME api → xxxxxxx.ondigitalocean.app (del Web Service)
CNAME app → xxxxxxx.ondigitalocean.app (del Static Site)
```

## ✅ Verification Checklist

1. ✅ Backend responde en `/healthz`
2. ✅ Frontend carga correctamente
3. ✅ CORS funciona (desde frontend a backend)
4. ✅ SSL habilitado en ambos dominios
5. ✅ Database conectada sin errores
