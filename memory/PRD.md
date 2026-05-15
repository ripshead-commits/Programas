# PRD — Plantillas FUR / FRG (ADRES)

## Problema original
> Los pdf son la normativa, y los xlsx son las plantillas. Desarrolla una página web que actúe como un formulario, donde yo pueda rellenar la información de cada formulario y me permita descargar cada plantilla con toda su información. Manéjalos aparte por módulo cada formulario tanto en FUR como en FUR_SERVICIOS y FRG. Que yo pueda elegir un módulo y él solo despliegue los campos de ese módulo para yo poder llenarlo. Agrega un botón para limpiar los campos, otro para descargar la plantilla y otro para cerrar el módulo. Los campos con lista predefinida (tipo de documento, tipo de vehículo, etc.) según la normativa. Responsive, intuitiva, clara, coherente, funcional, homogénea, armónica, con código de colores.

## Decisiones del usuario
- Persistencia: Sí, guardar registros en MongoDB con historial.
- Stack: React + FastAPI + MongoDB + openpyxl.
- Listas: extraídas del Diccionario de Campos (PDF normativa) — 100% oficiales.
- Validación: estricta.
- Idioma UI: Español.

## Arquitectura
- **Frontend**: React 19 + Shadcn UI + Tailwind. Vista única con switch dashboard/módulo.
- **Backend**: FastAPI con esquema de campos en `field_schemas.py`. Endpoints `/api/modules`, `/api/modules/{id}/schema`, `/api/modules/{id}/submissions` (CRUD), `/api/modules/{id}/download` (genera XLSX con openpyxl).
- **DB**: MongoDB collection `submissions` (id, module_id, data, label, created_at, updated_at).
- **Templates**: `/app/backend/templates/Plantilla_FUR_Primera_Vez.xlsx`, `Plantilla_SER.xlsx`, `Plantilla_FRG.xlsx` (originales, fila 1 encabezados; el sistema escribe en fila 2).

## User personas
- Personal administrativo de IPS / prestador de salud que radica reclamaciones SOAT ante ADRES.
- Auditor médico que responde glosas.

## Requisitos núcleo (estáticos)
- 3 módulos independientes con sus campos y validaciones.
- Selección por módulo, formulario dinámico, validación estricta server+client.
- Generación de XLSX preservando el formato original de la plantilla.
- Historial persistente en MongoDB.
- Responsive (mobile + desktop).

## Implementado (2026-02-15)
- ✅ Esquema completo de 3 módulos (FUR 62 campos, SER 13, FRG 63) en `field_schemas.py`.
- ✅ Listas oficiales con todos los valores de la normativa: tipo de documento, tipo de vehículo, naturaleza del evento, condición víctima, zona, estado aseguramiento, población especial, tipos de transporte, atención inicial, tipo de servicio, etc.
- ✅ Backend FastAPI con CRUD de submissions y endpoint de descarga (openpyxl) + validación.
- ✅ Frontend con dashboard (3 tarjetas + historial), módulo con sidebar de secciones color-coded, barra sticky con los 3 botones requeridos (Limpiar, Descargar XLSX, Cerrar módulo) + Guardar.
- ✅ Diseño Organic & Earthy (verde bosque + terracota), tipografía Work Sans + IBM Plex Sans.
- ✅ Toast notifications (sonner), data-testid en todos los elementos interactivos.
- ✅ Testing: 15/15 pytest backend + E2E frontend (100%).

## Backlog priorizado
### P1 (mejoras de UX)
- Botón "Duplicar registro" desde historial para reusar datos.
- Filtros y búsqueda en el historial.
- Exportar historial a CSV.
- Modo edición: reabrir un registro previo, editar y volver a descargar.

### P2 (escalabilidad y features avanzadas)
- Endpoint agregado `/api/submissions` para listar de los 3 módulos en una sola query (Dashboard hace N llamadas).
- Auto-guardado de borrador cada X segundos.
- Subida masiva: ingestar un CSV/XLSX y generar varias plantillas.
- Autenticación multiusuario (por ahora sin login).
- Catálogo DIVIPOLA (municipios) con buscador en lugar de input numérico libre.
- Validación de NIT con dígito de verificación.
- Internacionalización (i18n) si se requiere otro idioma.

### P3 (gobernanza)
- Auditoría: quién/cuándo modificó cada registro.
- Roles y permisos.
- Integración SIA / radicación directa con ADRES vía API.
