"""Punto de entrada de la aplicación de escritorio."""
import sys
from pathlib import Path

import customtkinter as ctk

# Para que PyInstaller resuelva imports relativos correctamente
sys.path.insert(0, str(Path(__file__).parent))

import db
from ui.dashboard import Dashboard
from ui.module_form import ModuleForm
from ui.theme import COLORS, FONT_FAMILY


class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Plantillas FUR / FRG — ADRES")
        self.geometry("1280x800")
        self.minsize(1024, 700)
        self.configure(fg_color=COLORS["bg"])

        # Modo claro forzado, paleta personalizada
        ctk.set_appearance_mode("light")
        ctk.set_default_color_theme("blue")  # base; sobreescribimos con colores propios

        try:
            self.iconbitmap(default="")  # opcional, sin icono externo
        except Exception:
            pass

        db.init_db()

        self.current_view = None
        self._show_dashboard()

    # ------------------------------------------------------------------ nav
    def _show_dashboard(self):
        if self.current_view is not None:
            self.current_view.destroy()
        self.current_view = Dashboard(self, on_open_module=self._open_module)
        self.current_view.pack(fill="both", expand=True)

    def _open_module(self, module_id, prefill_id=None):
        if self.current_view is not None:
            self.current_view.destroy()
        self.current_view = ModuleForm(
            self,
            module_id=module_id,
            on_close=self._show_dashboard,
            prefill_submission_id=prefill_id,
        )
        self.current_view.pack(fill="both", expand=True)


def main():
    app = App()
    app.mainloop()


if __name__ == "__main__":
    main()
