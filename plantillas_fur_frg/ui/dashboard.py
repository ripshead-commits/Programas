"""Pantalla principal: selección de módulo + historial."""
from __future__ import annotations

import customtkinter as ctk
from tkinter import messagebox

import db
from field_schemas import list_modules
from ui.theme import COLORS, FONT_FAMILY


class Dashboard(ctk.CTkFrame):
    def __init__(self, master, on_open_module):
        super().__init__(master, fg_color=COLORS["bg"])
        self.on_open_module = on_open_module
        self._build()

    # ------------------------------------------------------------------ build
    def _build(self):
        # Header
        header = ctk.CTkFrame(self, fg_color=COLORS["surface"], height=72, corner_radius=0)
        header.pack(fill="x")
        header.pack_propagate(False)

        inner = ctk.CTkFrame(header, fg_color="transparent")
        inner.pack(fill="both", expand=True, padx=24, pady=12)

        logo = ctk.CTkLabel(
            inner, text="FR", width=44, height=44,
            font=(FONT_FAMILY, 18, "bold"),
            text_color=COLORS["primary_text"], fg_color=COLORS["primary"], corner_radius=10,
        )
        logo.pack(side="left", padx=(0, 12))

        title_box = ctk.CTkFrame(inner, fg_color="transparent")
        title_box.pack(side="left", fill="y")
        ctk.CTkLabel(
            title_box, text="Plantillas FUR / FRG",
            font=(FONT_FAMILY, 17, "bold"), text_color=COLORS["primary"], anchor="w",
        ).pack(anchor="w")
        ctk.CTkLabel(
            title_box, text="Diligenciamiento y descarga (SOAT / ADRES)",
            font=(FONT_FAMILY, 12), text_color=COLORS["text_muted"], anchor="w",
        ).pack(anchor="w")

        badge = ctk.CTkLabel(
            inner, text="●  Normativa Colombia",
            font=(FONT_FAMILY, 11, "bold"),
            text_color=COLORS["primary"], fg_color="#E8F3EE",
            corner_radius=999, padx=12, pady=4,
        )
        badge.pack(side="right")

        # Scrollable content
        self.body = ctk.CTkScrollableFrame(self, fg_color=COLORS["bg"], corner_radius=0)
        self.body.pack(fill="both", expand=True, padx=0, pady=0)

        # Hero
        hero = ctk.CTkFrame(self.body, fg_color="transparent")
        hero.pack(fill="x", padx=40, pady=(28, 8))
        ctk.CTkLabel(
            hero, text="SELECCIONE UN MÓDULO",
            font=(FONT_FAMILY, 11, "bold"), text_color=COLORS["primary"], anchor="w",
        ).pack(anchor="w", pady=(0, 6))
        ctk.CTkLabel(
            hero,
            text="Diligencie y descargue sus plantillas FUR / FRG en minutos.",
            font=(FONT_FAMILY, 26, "bold"), text_color=COLORS["text_main"],
            anchor="w", justify="left", wraplength=900,
        ).pack(anchor="w")
        ctk.CTkLabel(
            hero,
            text="Cada módulo despliega únicamente sus campos, con listas oficiales y validación estricta. "
                 "Las plantillas XLSX se generan respetando la estructura original.",
            font=(FONT_FAMILY, 12), text_color=COLORS["text_muted"],
            anchor="w", justify="left", wraplength=900,
        ).pack(anchor="w", pady=(6, 0))

        # Module cards row
        cards_row = ctk.CTkFrame(self.body, fg_color="transparent")
        cards_row.pack(fill="x", padx=40, pady=(24, 12))
        for i, m in enumerate(list_modules()):
            card = self._make_card(cards_row, m)
            card.grid(row=0, column=i, padx=8, pady=8, sticky="nsew")
            cards_row.grid_columnconfigure(i, weight=1, uniform="cards")

        # History
        hist_header = ctk.CTkFrame(self.body, fg_color="transparent")
        hist_header.pack(fill="x", padx=40, pady=(28, 6))
        ctk.CTkLabel(
            hist_header, text="🕒  Historial reciente",
            font=(FONT_FAMILY, 16, "bold"), text_color=COLORS["primary"], anchor="w",
        ).pack(side="left")
        ctk.CTkButton(
            hist_header, text="Actualizar", width=100, height=28,
            fg_color="transparent", hover_color="#E8F3EE",
            text_color=COLORS["primary"], border_width=1, border_color=COLORS["border_strong"],
            command=self._refresh_history,
        ).pack(side="right")

        self.history_frame = ctk.CTkFrame(
            self.body, fg_color=COLORS["surface"],
            border_width=1, border_color=COLORS["border"], corner_radius=14,
        )
        self.history_frame.pack(fill="x", padx=40, pady=(0, 30))

        self._refresh_history()

    # ------------------------------------------------------------------ card
    def _make_card(self, parent, m):
        card = ctk.CTkFrame(
            parent, fg_color=COLORS["surface"], corner_radius=16,
            border_width=2, border_color=m["color"],
        )

        body = ctk.CTkFrame(card, fg_color="transparent")
        body.pack(fill="both", expand=True, padx=20, pady=18)

        # Header row: icon + chip
        head = ctk.CTkFrame(body, fg_color="transparent")
        head.pack(fill="x", pady=(0, 12))

        icon = ctk.CTkLabel(
            head, text="📄", font=(FONT_FAMILY, 22),
            width=44, height=44, corner_radius=10,
            fg_color=COLORS["surface_alt"], text_color=m["color"],
        )
        icon.pack(side="left")

        chip = ctk.CTkLabel(
            head, text=f"{m['field_count']} campos",
            font=(FONT_FAMILY, 10, "bold"),
            text_color=m["color"], fg_color=COLORS["surface_alt"],
            corner_radius=999, padx=10, pady=3,
        )
        chip.pack(side="right")

        ctk.CTkLabel(
            body, text=m["name"], font=(FONT_FAMILY, 16, "bold"),
            text_color=COLORS["text_main"], anchor="w", justify="left",
        ).pack(anchor="w", pady=(0, 4))
        ctk.CTkLabel(
            body, text=m["description"], font=(FONT_FAMILY, 11),
            text_color=COLORS["text_muted"], anchor="w", justify="left", wraplength=240,
        ).pack(anchor="w", pady=(0, 16))

        btn = ctk.CTkButton(
            body, text="Abrir módulo  →", height=36,
            fg_color=m["color"], hover_color=m["color_hover"],
            font=(FONT_FAMILY, 12, "bold"),
            command=lambda mid=m["id"]: self.on_open_module(mid),
        )
        btn.pack(fill="x")
        return card

    # ------------------------------------------------------------------ history
    def _refresh_history(self):
        for w in self.history_frame.winfo_children():
            w.destroy()

        items = db.list_submissions(limit=12)
        if not items:
            ctk.CTkLabel(
                self.history_frame,
                text="Aún no hay registros guardados. Diligencie un módulo para verlo aquí.",
                font=(FONT_FAMILY, 12), text_color=COLORS["text_muted"], height=80,
            ).pack(pady=24)
            return

        modules_map = {m["id"]: m for m in list_modules()}

        for i, h in enumerate(items):
            row = ctk.CTkFrame(self.history_frame, fg_color="transparent", height=58)
            row.pack(fill="x", padx=4, pady=2)

            mod = modules_map.get(h["module_id"], {"name": h["module_id"], "color": COLORS["primary"]})
            dot = ctk.CTkLabel(
                row, text="●", text_color=mod["color"],
                font=(FONT_FAMILY, 18), width=24,
            )
            dot.pack(side="left", padx=(12, 0))

            info = ctk.CTkFrame(row, fg_color="transparent")
            info.pack(side="left", fill="both", expand=True, padx=10, pady=10)

            title = h.get("label") or f"Registro {mod['name']}"
            ctk.CTkLabel(
                info, text=title, font=(FONT_FAMILY, 12, "bold"),
                text_color=COLORS["text_main"], anchor="w",
            ).pack(anchor="w")
            ctk.CTkLabel(
                info,
                text=f"{mod['name']} · {h['created_at']}"
                     + ("  •  descargado" if h.get("downloaded") else ""),
                font=(FONT_FAMILY, 10), text_color=COLORS["text_muted"], anchor="w",
            ).pack(anchor="w")

            actions = ctk.CTkFrame(row, fg_color="transparent")
            actions.pack(side="right", padx=12)
            ctk.CTkButton(
                actions, text="Reabrir", width=72, height=28,
                fg_color="transparent", hover_color="#E8F3EE",
                text_color=COLORS["primary"], border_width=1,
                border_color=COLORS["border_strong"], font=(FONT_FAMILY, 11),
                command=lambda hid=h["id"], mid=h["module_id"]: self.on_open_module(mid, hid),
            ).pack(side="left", padx=4)
            ctk.CTkButton(
                actions, text="🗑", width=32, height=28,
                fg_color="transparent", hover_color="#FDECEC",
                text_color=COLORS["danger"], border_width=0,
                command=lambda hid=h["id"]: self._delete(hid),
            ).pack(side="left", padx=2)

            if i < len(items) - 1:
                sep = ctk.CTkFrame(self.history_frame, fg_color=COLORS["border"], height=1)
                sep.pack(fill="x", padx=12)

    def _delete(self, sid):
        if messagebox.askyesno("Eliminar registro", "¿Está seguro de eliminar este registro?"):
            db.delete_submission(sid)
            self._refresh_history()

    # Llamado por el padre cuando se vuelve del módulo
    def refresh(self):
        self._refresh_history()
