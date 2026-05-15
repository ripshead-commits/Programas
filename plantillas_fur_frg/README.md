# Plantillas FUR / FRG (ADRES) — Aplicación de Escritorio Windows

Aplicación de escritorio en Python (CustomTkinter + SQLite + openpyxl) para
diligenciar y descargar las plantillas oficiales del SOAT/ADRES de Colombia:
**FUR Primera Vez**, **FUR Servicios** y **FRG (Respuesta a Glosa)**.

Se distribuye como un **único archivo `PlantillasFURFRG.exe`** que se puede
ejecutar con doble clic, sin instalar Python en la máquina destino.

---

## 📦 Estructura del proyecto

```
plantillas_fur_frg/
├── app.py                ← punto de entrada de la app
├── app.spec              ← configuración de PyInstaller
├── build.bat             ← script para compilar a .exe (ejecutar en Windows)
├── db.py                 ← persistencia SQLite (historial)
├── field_schemas.py      ← definición de los 3 módulos + listas oficiales
├── xlsx_export.py        ← validación y generación del XLSX
├── requirements.txt      ← dependencias Python
├── templates/            ← plantillas XLSX originales
│   ├── Plantilla_FUR_Primera_Vez.xlsx
│   ├── Plantilla_SER.xlsx
│   └── Plantilla_FRG.xlsx
└── ui/
    ├── theme.py          ← paleta y colores por sección
    ├── dashboard.py      ← pantalla de selección + historial
    └── module_form.py    ← formulario dinámico
```

---

## 🚀 Cómo compilar el `.exe` en tu Windows

### Pre-requisito (una sola vez)
Instala **Python 3.10 o superior** desde [python.org/downloads](https://www.python.org/downloads/).
> ⚠️ Durante la instalación marca la casilla **"Add Python to PATH"**.

### Compilar
1. Copia toda la carpeta `plantillas_fur_frg/` a tu PC Windows.
2. Haz **doble clic** en `build.bat` (o ejecútalo desde una `cmd`).
3. Espera 2–5 minutos (la primera vez descarga dependencias).
4. Al terminar tendrás:
   ```
   plantillas_fur_frg\dist\PlantillasFURFRG.exe
   ```

¡Listo! Puedes copiar ese `.exe` a cualquier PC Windows y ejecutarlo con doble clic.

---

## 🖥 Cómo ejecutar la app

### Opción A — Usar el `.exe`
- Doble clic en `PlantillasFURFRG.exe`.
- La primera vez se crea automáticamente el archivo `plantillas_fur_frg.db`
  junto al ejecutable (es tu historial local).

### Opción B — Modo desarrollo (sin compilar)
```bash
cd plantillas_fur_frg
python -m venv .venv
.venv\Scripts\activate           # Windows
pip install -r requirements.txt
python app.py
```

---

## ✅ Funcionalidades

- **3 módulos** independientes con sus campos oficiales:
  - **FUR Primera Vez**: 62 campos en 9 secciones.
  - **FUR Servicios**: 13 campos en 2 secciones.
  - **FRG (Respuesta a Glosa)**: 63 campos en 12 secciones.
- **Listas oficiales** extraídas del Diccionario de Campos (Tipo de Vehículo, Tipo de Documento, Naturaleza del Evento, etc.).
- **Validación estricta**: campos obligatorios, longitudes, tipos (número/fecha/hora), valores permitidos en selects.
- **Historial local** en SQLite (`plantillas_fur_frg.db`).
- **3 botones por módulo**: 🧹 Limpiar campos, ⬇ Descargar Plantilla XLSX, ✕ Cerrar módulo (más 💾 Guardar opcional).
- **Reabrir** registros del historial para editarlos.
- **Color-coding** por sección para una vista armónica.
- Diseño responsive (ventana redimensionable, mínimo 1024×700).

---

## 📂 ¿Dónde se guardan mis datos?

- **Historial**: archivo `plantillas_fur_frg.db` **junto al `.exe`** (SQLite).
- **Plantillas descargadas**: el cuadro de diálogo te deja elegir dónde guardar
  cada `.xlsx`. Por defecto sugiere un nombre como `Plantilla_FUR_..._Diligenciada.xlsx`.

Para hacer una copia de seguridad de tu historial, solo copia el archivo `.db`.

---

## 🛠 Problemas comunes

| Problema | Solución |
|----------|----------|
| `python no se reconoce…` al ejecutar `build.bat` | Instala Python desde python.org marcando **"Add Python to PATH"**, reinicia la cmd. |
| `build.bat` se queda en "Instalando dependencias" | Revisa conexión a internet, vuelve a ejecutarlo. |
| Antivirus marca el .exe como sospechoso | Es falso positivo típico de PyInstaller. Añade excepción o firma el ejecutable. |
| No aparecen las plantillas al descargar | Asegúrate de que la carpeta `templates/` esté junto al `app.py` antes de compilar. |
| Texto cortado en pantallas pequeñas | La ventana es redimensionable; usa scroll o maximízala. |

---

## 🔄 Distribución a otros usuarios

Solo necesitas el archivo `dist\PlantillasFURFRG.exe`. **No** requieren tener
Python instalado. La aplicación funciona en Windows 10 y Windows 11 (x64).

Para una distribución más limpia, también puedes empaquetarla con un
instalador como [Inno Setup](https://jrsoftware.org/isinfo.php) o
[NSIS](https://nsis.sourceforge.io/) — solo tienes que apuntarlos al `.exe`
generado en `dist\`.

---

## 📝 Notas técnicas

- **Lenguaje**: Python 3.10+
- **UI**: [CustomTkinter](https://github.com/TomSchimansky/CustomTkinter) 5.2.2
- **Excel**: [openpyxl](https://openpyxl.readthedocs.io/) 3.1.5 (preserva formato del XLSX original; los valores se escriben en la fila 2)
- **DB**: SQLite estándar de Python (sin servidor)
- **Empaquetado**: [PyInstaller](https://pyinstaller.org/) 6.20.0 con `--onefile`

Listas oficiales basadas en:
- *Diccionario de Campos FUR y FUR Servicios — ADRES (Mayo 2026)*
- *Documento Circular para Formularios (ADRES)*

---

**Hecho con 💚 para la gestión eficiente de reclamaciones SOAT.**
