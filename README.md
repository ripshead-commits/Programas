# Plantillas FUR / FRG (ADRES) — Guía de ejecución local

Aplicación web para diligenciar y descargar las plantillas oficiales del **SOAT / ADRES** de Colombia:
**FUR Primera Vez**, **FUR Servicios** y **FRG (Respuesta a Glosa)**.

- **Frontend**: React 19 + Shadcn UI + Tailwind
- **Backend**: FastAPI + openpyxl
- **Base de datos**: MongoDB

---

## 1. Pre-requisitos

| Software | Versión recomendada | Cómo verificar |
|----------|--------------------|----------------|
| Python   | 3.10 o superior    | `python --version` |
| Node.js  | 18 o superior      | `node --version` |
| Yarn     | 1.22 o superior    | `yarn --version` (si no lo tienes: `npm install -g yarn`) |
| MongoDB  | 5 o superior       | `mongod --version` |

> ⚠️ **Usa siempre `yarn`** para el frontend. **NO uses `npm`** (rompe dependencias).

---

## 2. Instalar y arrancar MongoDB

Tienes tres opciones — elige una:

### Opción A — MongoDB local (Windows / Mac / Linux)
1. Descarga [MongoDB Community Server](https://www.mongodb.com/try/download/community).
2. Instálalo siguiendo el asistente.
3. Arráncalo:
   - **Windows**: se inicia como servicio automáticamente, o ejecuta `net start MongoDB`.
   - **Mac (Homebrew)**: `brew services start mongodb-community`.
   - **Linux**: `sudo systemctl start mongod`.

### Opción B — Docker (la más rápida)
```bash
docker run -d --name mongo-fur -p 27017:27017 mongo:7
```

### Opción C — MongoDB Atlas (en la nube, gratis)
1. Crea un cluster gratuito en [https://www.mongodb.com/atlas](https://www.mongodb.com/atlas).
2. Copia la cadena de conexión, algo como:
   `mongodb+srv://usuario:password@cluster0.xxx.mongodb.net`

---

## 3. Configurar y ejecutar el **Backend**

```bash
cd backend

# 3.1 Crear y activar entorno virtual
python -m venv venv

# En Linux/Mac:
source venv/bin/activate
# En Windows (PowerShell):
.\venv\Scripts\Activate.ps1
# En Windows (CMD):
venv\Scripts\activate.bat

# 3.2 Instalar dependencias
pip install -r requirements.txt
```

### Editar `backend/.env`
Abre el archivo `backend/.env` y reemplaza por tu configuración local:

```env
MONGO_URL="mongodb://localhost:27017"
DB_NAME="fur_frg"
CORS_ORIGINS="http://localhost:3000"
```

> Si usas **Atlas**, pon ahí la cadena `mongodb+srv://...`

### Arrancar el backend
```bash
uvicorn server:app --reload --host 0.0.0.0 --port 8001
```

Deberías ver:
```
INFO:     Uvicorn running on http://0.0.0.0:8001
INFO:     Application startup complete.
```

✅ **Prueba**: abre `http://localhost:8001/api/modules` en el navegador. Debe devolver un JSON con los 3 módulos.

---

## 4. Configurar y ejecutar el **Frontend**

Abre **otra terminal** (deja el backend corriendo):

```bash
cd frontend

# 4.1 Instalar dependencias (usa yarn, NO npm)
yarn install
```

### Editar `frontend/.env`
Reemplaza el contenido por:

```env
REACT_APP_BACKEND_URL=http://localhost:8001
WDS_SOCKET_PORT=0
```

### Arrancar el frontend
```bash
yarn start
```

El navegador se abrirá en `http://localhost:3000` automáticamente. Si no, ábrelo manualmente.

---

## 5. Verificar que todo funciona

1. En el dashboard verás **3 tarjetas**: FUR Primera Vez, FUR Servicios, FRG.
2. Haz clic en **"FUR Servicios"** (el más pequeño, 13 campos) para una prueba rápida.
3. Llena los campos y haz clic en **"Descargar Plantilla XLSX"** → debe descargarse el archivo.
4. Vuelve al dashboard → en **"Historial reciente"** debe aparecer el registro nuevo.

---

## 6. Comandos útiles

| Acción | Comando |
|--------|---------|
| Reiniciar backend | `Ctrl+C` y volver a `uvicorn server:app --reload --port 8001` |
| Reiniciar frontend | `Ctrl+C` y volver a `yarn start` |
| Limpiar caché frontend | `rm -rf node_modules .cache && yarn install` |
| Ver registros en Mongo | `mongosh fur_frg --eval "db.submissions.find().pretty()"` |
| Borrar todos los registros | `mongosh fur_frg --eval "db.submissions.deleteMany({})"` |

---

## 7. Problemas comunes

### ❌ "ModuleNotFoundError: openpyxl" o similar
Te faltó instalar dependencias del backend. Asegúrate de tener el `venv` activado:
```bash
pip install -r requirements.txt
```

### ❌ "Network Error" / la página no carga datos
- Verifica que el backend esté corriendo en `http://localhost:8001`.
- Revisa que `frontend/.env` tenga `REACT_APP_BACKEND_URL=http://localhost:8001`.
- Reinicia el frontend después de editar `.env` (`Ctrl+C` y `yarn start`).

### ❌ MongoDB connection refused
- Verifica que MongoDB esté corriendo: `mongosh` (debe entrar al shell).
- En Linux: `sudo systemctl status mongod`.
- Si usas Atlas, revisa que tu IP esté en la whitelist.

### ❌ Puerto 8001 o 3000 ocupado
- Backend: cambia a `--port 8002` y actualiza `REACT_APP_BACKEND_URL=http://localhost:8002`.
- Frontend: `PORT=3001 yarn start` (Linux/Mac) o configura en `package.json`.

### ❌ CORS error en la consola del navegador
Verifica que `backend/.env` tenga `CORS_ORIGINS="http://localhost:3000"` (sin el slash final).

---

## 8. Estructura del proyecto

```
.
├── backend/
│   ├── server.py              ← FastAPI app + endpoints
│   ├── field_schemas.py       ← Definición de los 3 módulos
│   ├── requirements.txt       ← Dependencias Python
│   ├── .env                   ← Configuración (Mongo, CORS)
│   └── templates/             ← Plantillas XLSX originales
│       ├── Plantilla_FUR_Primera_Vez.xlsx
│       ├── Plantilla_SER.xlsx
│       └── Plantilla_FRG.xlsx
└── frontend/
    ├── package.json           ← Dependencias JS
    ├── .env                   ← URL del backend
    ├── public/index.html
    └── src/
        ├── App.js
        ├── index.js
        ├── index.css
        ├── lib/
        │   ├── api.js         ← Cliente HTTP
        │   └── sections.js    ← Colores por sección
        ├── pages/
        │   ├── Dashboard.jsx  ← Pantalla de selección + historial
        │   └── ModuleForm.jsx ← Formulario dinámico
        └── components/ui/     ← Componentes Shadcn
```

---

## 9. Endpoints de la API (referencia rápida)

| Método | Endpoint | Descripción |
|--------|----------|-------------|
| GET    | `/api/modules` | Lista los 3 módulos |
| GET    | `/api/modules/{id}/schema` | Esquema de campos del módulo |
| POST   | `/api/modules/{id}/submissions` | Guarda un registro |
| GET    | `/api/modules/{id}/submissions` | Lista historial |
| GET    | `/api/modules/{id}/submissions/{sub_id}` | Obtiene un registro |
| DELETE | `/api/modules/{id}/submissions/{sub_id}` | Elimina un registro |
| POST   | `/api/modules/{id}/download` | Genera y descarga el XLSX diligenciado |

Documentación interactiva disponible en `http://localhost:8001/docs` cuando el backend está corriendo.

---

## 10. Despliegue en producción (opcional)

- **Backend**: cualquier host con Python (Railway, Render, Fly.io, AWS EC2, etc.) — usa `gunicorn -k uvicorn.workers.UvicornWorker server:app`.
- **Frontend**: `yarn build` genera carpeta `build/` que sirves con cualquier CDN (Vercel, Netlify, Cloudflare Pages) o detrás de Nginx.
- **Mongo**: Atlas free tier sirve perfectamente.
- Recuerda ajustar `REACT_APP_BACKEND_URL` y `CORS_ORIGINS` con las URLs públicas.

---

**¿Dudas?** Revisa la sección 7 (Problemas comunes) o pídeme ayuda 💚
