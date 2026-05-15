# PRD — Plantillas FUR / FRG (Desktop App)

## Pivote del proyecto (2026-02-15)
Se eliminó la web React+FastAPI+MongoDB y se reescribió como **aplicación de escritorio Windows** distribuible como `.exe`.

## Stack final
- **Python 3.10+**
- **CustomTkinter** 5.2.2 (UI moderna estilo VSCode)
- **SQLite** (persistencia local, sin servidor)
- **openpyxl** 3.1.5 (preserva el formato del XLSX original)
- **PyInstaller** 6.20.0 (--onefile)

## Estructura
```
plantillas_fur_frg/
├── app.py, app.spec, build.bat, README.md
├── db.py, xlsx_export.py, field_schemas.py
├── requirements.txt
├── templates/  (3 XLSX originales)
└── ui/  (theme, dashboard, module_form)
```

## Distribución
1. Usuario copia la carpeta `plantillas_fur_frg` a Windows.
2. Doble clic en `build.bat` → genera `dist/PlantillasFURFRG.exe`.
3. El `.exe` se ejecuta sin Python instalado.
4. El historial se guarda en `plantillas_fur_frg.db` junto al `.exe`.

## Validaciones probadas
- ✅ AST de los 7 archivos Python (compilación correcta).
- ✅ Inicialización de SQLite + CRUD de submissions.
- ✅ Validación estricta (10 errores cuando faltan campos del SER).
- ✅ Generación de XLSX preservando encabezados en fila 1 y valores en fila 2.
- ✅ App Tk arranca y monta los 3 módulos correctamente (FUR 9 secciones/62 widgets, SER 2/13, FRG 12/63).

## Backlog
- [P1] Icono `.ico` propio y firma del binario (evita falsos positivos antivirus).
- [P1] Calendar widget con tkcalendar para campos date (actualmente input texto AAAA-MM-DD).
- [P2] Exportar historial completo a un único XLSX consolidado.
- [P2] Carga masiva: ingestar un CSV/XLSX externo y generar múltiples plantillas.
- [P2] Plantilla maestra de datos del prestador (auto-rellenado).
- [P3] Build cross-platform (.dmg para Mac, .AppImage para Linux).
