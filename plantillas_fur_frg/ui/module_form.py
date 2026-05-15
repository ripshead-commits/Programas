"""Formulario dinámico de un módulo."""
from __future__ import annotations

import re
from datetime import datetime
from pathlib import Path
from tkinter import filedialog, messagebox

import customtkinter as ctk

import db
import xlsx_export
from field_schemas import get_module, get_sections
from ui.theme import COLORS, FONT_FAMILY, section_color


DATE_REGEX = re.compile(r"^\d{4}-\d{2}-\d{2}$")
TIME_REGEX = re.compile(r"^\d{2}:\d{2}$")


class ModuleForm(ctk.CTkFrame):
    def __init__(self, master, module_id: str, on_close, prefill_submission_id: str | None = None):
        super().__init__(master, fg_color=COLORS["bg"])
        self.module = get_module(module_id)
        self.module_id = module_id
        self.on_close = on_close
        self.sections = get_sections(module_id)
        self.widgets: dict[str, dict] = {}  # key -> {'var': ..., 'widget': ..., 'error_lbl': ...}
        self.error_labels: dict[str, ctk.CTkLabel] = {}

        self._build()

        if prefill_submission_id:
            sub = db.get_submission(prefill_submission_id)
            if sub:
                self._set_values(sub["data"])

    # ------------------------------------------------------------------ build
    def _build(self):
        # ============ Header sticky ============
        header = ctk.CTkFrame(self, fg_color=COLORS["surface"], height=70, corner_radius=0)
        header.pack(fill="x", side="top")
        header.pack_propagate(False)

        inner = ctk.CTkFrame(header, fg_color="transparent")
        inner.pack(fill="both", expand=True, padx=16, pady=10)

        ctk.CTkButton(
            inner, text="←  Volver", width=80, height=30,
            fg_color="transparent", hover_color=COLORS["surface_alt"],
            text_color=COLORS["text_muted"], border_width=0,
            command=self._handle_close, font=(FONT_FAMILY, 12),
        ).pack(side="left")

        ctk.CTkLabel(inner, text="│", text_color=COLORS["border"]).pack(side="left", padx=6)

        title_box = ctk.CTkFrame(inner, fg_color="transparent")
        title_box.pack(side="left", padx=4)
        ctk.CTkLabel(
            title_box, text=self.module["name"],
            font=(FONT_FAMILY, 15, "bold"),
            text_color=COLORS["primary"], anchor="w",
        ).pack(anchor="w")
        ctk.CTkLabel(
            title_box, text=self.module["description"],
            font=(FONT_FAMILY, 10), text_color=COLORS["text_muted"], anchor="w",
        ).pack(anchor="w")

        # Botones de acción
        actions = ctk.CTkFrame(inner, fg_color="transparent")
        actions.pack(side="right")

        ctk.CTkButton(
            actions, text="🧹  Limpiar campos", width=130, height=32,
            fg_color="transparent", hover_color="#FDECEC",
            text_color=COLORS["danger"], border_width=1, border_color="#F0B3B3",
            font=(FONT_FAMILY, 11, "bold"), command=self._handle_clear,
        ).pack(side="left", padx=3)

        ctk.CTkButton(
            actions, text="💾  Guardar", width=110, height=32,
            fg_color="transparent", hover_color="#E8F3EE",
            text_color=COLORS["primary"], border_width=1, border_color=COLORS["border_strong"],
            font=(FONT_FAMILY, 11, "bold"), command=self._handle_save,
        ).pack(side="left", padx=3)

        ctk.CTkButton(
            actions, text="⬇  Descargar XLSX", width=150, height=32,
            fg_color=COLORS["primary"], hover_color=COLORS["primary_hover"],
            text_color="white", font=(FONT_FAMILY, 11, "bold"),
            command=self._handle_download,
        ).pack(side="left", padx=3)

        ctk.CTkButton(
            actions, text="✕  Cerrar módulo", width=120, height=32,
            fg_color="transparent", hover_color=COLORS["surface_alt"],
            text_color=COLORS["text_muted"], border_width=0,
            font=(FONT_FAMILY, 11), command=self._handle_close,
        ).pack(side="left", padx=3)

        # ============ Body (sidebar + form scrollable) ============
        body = ctk.CTkFrame(self, fg_color=COLORS["bg"])
        body.pack(fill="both", expand=True)

        # Sidebar
        sidebar = ctk.CTkFrame(body, fg_color=COLORS["surface"], width=240, corner_radius=0)
        sidebar.pack(side="left", fill="y")
        sidebar.pack_propagate(False)

        ctk.CTkLabel(
            sidebar, text="SECCIONES",
            font=(FONT_FAMILY, 10, "bold"), text_color=COLORS["text_muted"], anchor="w",
        ).pack(fill="x", padx=18, pady=(18, 8))

        sidebar_scroll = ctk.CTkScrollableFrame(sidebar, fg_color=COLORS["surface"])
        sidebar_scroll.pack(fill="both", expand=True, padx=8, pady=(0, 12))

        self.section_anchors: dict[str, ctk.CTkFrame] = {}
        self.sidebar_buttons: dict[str, ctk.CTkButton] = {}

        # Scrollable form
        self.form_scroll = ctk.CTkScrollableFrame(body, fg_color=COLORS["bg"])
        self.form_scroll.pack(side="left", fill="both", expand=True)

        # Build sections in form
        for sec in self.sections:
            sec_color = section_color(sec["name"])
            self._build_section(sec, sec_color)
            # sidebar button
            btn = ctk.CTkButton(
                sidebar_scroll, text=sec["name"], height=34,
                fg_color="transparent", hover_color=COLORS["surface_alt"],
                text_color=COLORS["text_main"], anchor="w",
                font=(FONT_FAMILY, 11),
                command=lambda n=sec["name"]: self._scroll_to_section(n),
            )
            btn.pack(fill="x", pady=2)
            self.sidebar_buttons[sec["name"]] = btn

        # Bottom action bar
        bottom = ctk.CTkFrame(self.form_scroll, fg_color="transparent")
        bottom.pack(fill="x", padx=20, pady=20)
        ctk.CTkButton(
            bottom, text="🧹  Limpiar", height=34,
            fg_color="transparent", hover_color="#FDECEC",
            text_color=COLORS["danger"], border_width=1, border_color="#F0B3B3",
            command=self._handle_clear,
        ).pack(side="right", padx=4)
        ctk.CTkButton(
            bottom, text="⬇  Descargar Plantilla XLSX", height=34,
            fg_color=COLORS["primary"], hover_color=COLORS["primary_hover"],
            text_color="white", font=(FONT_FAMILY, 12, "bold"),
            command=self._handle_download,
        ).pack(side="right", padx=4)
        ctk.CTkButton(
            bottom, text="Cerrar módulo", height=34,
            fg_color="transparent", hover_color=COLORS["surface_alt"],
            text_color=COLORS["text_muted"], border_width=1, border_color=COLORS["border"],
            command=self._handle_close,
        ).pack(side="right", padx=4)

    def _build_section(self, sec, colors):
        # Tarjeta de sección
        card = ctk.CTkFrame(
            self.form_scroll, fg_color=COLORS["surface"], corner_radius=14,
            border_width=1, border_color=colors["border"],
        )
        card.pack(fill="x", padx=20, pady=10)
        self.section_anchors[sec["name"]] = card

        # Header
        hdr = ctk.CTkFrame(card, fg_color=colors["bg"], corner_radius=14, height=42)
        hdr.pack(fill="x")
        hdr.pack_propagate(False)
        ctk.CTkLabel(
            hdr, text=sec["name"],
            font=(FONT_FAMILY, 12, "bold"), text_color=colors["text"], anchor="w",
        ).pack(side="left", padx=16, pady=10)
        ctk.CTkLabel(
            hdr, text=f"{len(sec['fields'])} campo(s)",
            font=(FONT_FAMILY, 10), text_color=colors["text"], anchor="e",
        ).pack(side="right", padx=16)

        # Grid de campos
        grid = ctk.CTkFrame(card, fg_color=COLORS["surface"])
        grid.pack(fill="x", padx=14, pady=14)
        grid.grid_columnconfigure(0, weight=1, uniform="col")
        grid.grid_columnconfigure(1, weight=1, uniform="col")

        row = 0
        col = 0
        for fld in sec["fields"]:
            is_long = fld["type"] == "textarea" or (fld.get("length") and fld["length"] >= 100)
            if is_long and col == 1:
                # mover a la siguiente fila a span 2
                row += 1
                col = 0
            colspan = 2 if is_long else 1
            cell = self._build_field(grid, fld)
            cell.grid(row=row, column=col, columnspan=colspan, sticky="ew", padx=6, pady=6)
            if is_long:
                row += 1
                col = 0
            else:
                col += 1
                if col >= 2:
                    col = 0
                    row += 1

    def _build_field(self, parent, fld):
        wrap = ctk.CTkFrame(parent, fg_color="transparent")

        # label
        label_row = ctk.CTkFrame(wrap, fg_color="transparent")
        label_row.pack(fill="x", pady=(0, 4))

        label_text = fld["label"] + ("  *" if fld["required"] else "")
        ctk.CTkLabel(
            label_row, text=label_text,
            font=(FONT_FAMILY, 11, "bold"), text_color=COLORS["text_main"], anchor="w",
        ).pack(side="left")

        if fld.get("length"):
            counter = ctk.CTkLabel(
                label_row, text=f"0/{fld['length']}",
                font=(FONT_FAMILY, 9), text_color=COLORS["text_muted"],
            )
            counter.pack(side="right")
        else:
            counter = None

        # widget
        var = ctk.StringVar()

        def on_change(*_a):
            if counter and fld.get("length"):
                counter.configure(text=f"{len(var.get())}/{fld['length']}")
            # limpiar error si existía
            if fld["key"] in self.error_labels:
                self._clear_field_error(fld["key"])

        var.trace_add("write", on_change)

        if fld["type"] == "select":
            values_labels = [lbl for _, lbl in (fld.get("options") or [])]
            widget = ctk.CTkComboBox(
                wrap, values=values_labels, variable=var,
                height=34, state="readonly",
                button_color=COLORS["primary"], button_hover_color=COLORS["primary_hover"],
                border_color=COLORS["border"], dropdown_hover_color=COLORS["surface_alt"],
            )
            widget.set("")  # vacío por defecto
        elif fld["type"] == "textarea":
            widget = ctk.CTkTextbox(
                wrap, height=80, border_width=1, border_color=COLORS["border"],
                fg_color=COLORS["surface"], wrap="word",
            )
            # CTkTextbox doesn't bind StringVar directly, we'll read via .get()
            def _sync_var(event=None, k=fld["key"]):
                self.widgets[k]["_text_value"] = widget.get("1.0", "end").rstrip("\n")
                if counter and fld.get("length"):
                    counter.configure(text=f"{len(self.widgets[k]['_text_value'])}/{fld['length']}")
                if fld["key"] in self.error_labels:
                    self._clear_field_error(fld["key"])
            widget.bind("<KeyRelease>", _sync_var)
        else:
            widget = ctk.CTkEntry(
                wrap, textvariable=var, height=34,
                border_color=COLORS["border"], fg_color=COLORS["surface"],
            )
            if fld.get("length"):
                # limitar longitud
                def vcmd(P, max_len=fld["length"]):
                    return len(P) <= max_len
                widget.configure(validate="key", validatecommand=(widget.register(vcmd), "%P"))
            if fld["type"] == "date":
                widget.configure(placeholder_text="AAAA-MM-DD")
            elif fld["type"] == "time":
                widget.configure(placeholder_text="HH:MM")

        widget.pack(fill="x")

        # error label (oculto inicialmente)
        err = ctk.CTkLabel(
            wrap, text="", text_color=COLORS["danger"],
            font=(FONT_FAMILY, 10), anchor="w",
        )
        err.pack(fill="x", pady=(2, 0))

        self.widgets[fld["key"]] = {"var": var, "widget": widget, "field": fld, "counter": counter}
        self.error_labels[fld["key"]] = err
        return wrap

    # ------------------------------------------------------------------ values
    def _get_widget_value(self, key):
        w = self.widgets[key]
        fld = w["field"]
        if fld["type"] == "select":
            lbl = w["var"].get()
            # mapear de label → value
            for v, l in (fld.get("options") or []):
                if l == lbl:
                    return v
            return ""
        if fld["type"] == "textarea":
            return w.get("_text_value", w["widget"].get("1.0", "end").rstrip("\n"))
        return w["var"].get()

    def _set_widget_value(self, key, value):
        w = self.widgets[key]
        fld = w["field"]
        if value is None:
            value = ""
        if fld["type"] == "select":
            for v, l in (fld.get("options") or []):
                if str(v) == str(value):
                    w["var"].set(l)
                    return
            w["var"].set("")
        elif fld["type"] == "textarea":
            w["widget"].delete("1.0", "end")
            w["widget"].insert("1.0", str(value))
            w["_text_value"] = str(value)
        else:
            w["var"].set(str(value))

    def _get_all_values(self) -> dict:
        return {k: self._get_widget_value(k) for k in self.widgets}

    def _set_values(self, data: dict):
        for k, v in data.items():
            if k in self.widgets:
                self._set_widget_value(k, v)

    # ------------------------------------------------------------------ errors
    def _show_field_error(self, key, msg):
        if key not in self.error_labels:
            return
        self.error_labels[key].configure(text=f"⚠  {msg}")
        w = self.widgets[key]["widget"]
        try:
            w.configure(border_color=COLORS["danger"])
        except Exception:
            pass

    def _clear_field_error(self, key):
        if key in self.error_labels:
            self.error_labels[key].configure(text="")
            w = self.widgets[key]["widget"]
            try:
                w.configure(border_color=COLORS["border"])
            except Exception:
                pass

    def _clear_all_errors(self):
        for k in list(self.error_labels.keys()):
            self._clear_field_error(k)

    # ------------------------------------------------------------------ validate
    def _validate(self) -> tuple[dict, list[str]]:
        self._clear_all_errors()
        data = self._get_all_values()

        # mapear cada error a su campo (heurística: contiene 'label' del campo)
        errors = xlsx_export.validate_data(self.module_id, data)
        field_to_error = {}
        for fld in self.module["fields"]:
            for err in errors:
                if f"'{fld['label']}'" in err:
                    field_to_error[fld["key"]] = err.split("'")[-1].strip(". ").strip() or err
                    field_to_error[fld["key"]] = err

        for k, e in field_to_error.items():
            # mensaje compacto
            msg = e
            if "es obligatorio" in e: msg = "Campo obligatorio"
            elif "excede la longitud" in e: msg = "Excede longitud máxima"
            elif "debe ser numérico" in e: msg = "Debe ser numérico"
            elif "no es un valor válido" in e: msg = "Valor no permitido"
            elif "AAAA-MM-DD" in e: msg = "Formato AAAA-MM-DD"
            elif "HH:MM" in e: msg = "Formato HH:MM"
            self._show_field_error(k, msg)

        return data, errors

    # ------------------------------------------------------------------ scroll
    def _scroll_to_section(self, section_name: str):
        anchor = self.section_anchors.get(section_name)
        if not anchor:
            return
        # Forzar update geometría
        self.form_scroll.update_idletasks()
        # Calcular posición relativa
        try:
            canvas = self.form_scroll._parent_canvas  # type: ignore[attr-defined]
            y = anchor.winfo_y()
            total = self.form_scroll._scrollbar_frame.winfo_height()  # type: ignore[attr-defined]
            if total <= 0:
                total = anchor.winfo_reqheight() * max(1, len(self.sections))
            frac = max(0.0, min(1.0, y / max(1, total)))
            canvas.yview_moveto(frac)
        except Exception:
            pass

    # ------------------------------------------------------------------ actions
    def _handle_clear(self):
        if not messagebox.askyesno("Limpiar campos", "¿Está seguro que desea limpiar todos los campos?"):
            return
        for k, w in self.widgets.items():
            fld = w["field"]
            if fld["type"] == "select":
                w["var"].set("")
            elif fld["type"] == "textarea":
                w["widget"].delete("1.0", "end")
                w["_text_value"] = ""
            else:
                w["var"].set("")
            if w.get("counter") and fld.get("length"):
                w["counter"].configure(text=f"0/{fld['length']}")
        self._clear_all_errors()
        messagebox.showinfo("Limpio", "Todos los campos fueron limpiados.")

    def _handle_save(self):
        data, errors = self._validate()
        if errors:
            messagebox.showerror(
                "Faltan campos",
                f"Se encontraron {len(errors)} error(es). Revise los campos marcados en rojo.",
            )
            return
        db.create_submission(self.module_id, data)
        messagebox.showinfo("Guardado", "Registro guardado correctamente en el historial.")

    def _handle_download(self):
        data, errors = self._validate()
        if errors:
            messagebox.showerror(
                "Faltan campos",
                f"Se encontraron {len(errors)} error(es). Corrija los campos marcados antes de descargar.",
            )
            return

        # Diálogo guardar archivo
        default_name = self.module["download_filename"]
        path = filedialog.asksaveasfilename(
            title="Guardar plantilla diligenciada como…",
            defaultextension=".xlsx",
            filetypes=[("Excel", "*.xlsx")],
            initialfile=default_name,
        )
        if not path:
            return

        try:
            xlsx_export.fill_template(self.module_id, data, Path(path))
        except FileNotFoundError as e:
            messagebox.showerror("Plantilla no encontrada", str(e))
            return
        except Exception as e:
            messagebox.showerror("Error al generar XLSX", f"Detalle: {e}")
            return

        db.create_submission(self.module_id, data, downloaded=True)
        if messagebox.askyesno(
            "Descarga exitosa",
            f"Plantilla guardada en:\n{path}\n\n¿Desea cerrar el módulo y volver al menú?",
        ):
            self._handle_close()

    def _handle_close(self):
        # confirmar si hay datos sin guardar
        has_data = any(self._get_widget_value(k) for k in self.widgets)
        if has_data:
            if not messagebox.askyesno(
                "Cerrar módulo",
                "¿Está seguro de cerrar el módulo? Los cambios no guardados se perderán.",
            ):
                return
        self.on_close()
