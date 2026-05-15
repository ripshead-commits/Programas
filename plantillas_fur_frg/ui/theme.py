"""Paleta y constantes visuales de la app."""
# Modo light por defecto, paleta verde bosque + terracota
COLORS = {
    "bg": "#F7FAF8",
    "surface": "#FFFFFF",
    "surface_alt": "#EEF3F0",
    "primary": "#2C5E4E",
    "primary_hover": "#234B3E",
    "primary_text": "#FFFFFF",
    "accent": "#E27D5F",
    "accent_hover": "#C66547",
    "danger": "#C0392B",
    "danger_hover": "#A4291C",
    "warning": "#B8862E",
    "success": "#1F8B5C",
    "text_main": "#111827",
    "text_muted": "#5B6B65",
    "border": "#D8E1DC",
    "border_strong": "#A7D0C0",
}

SECTION_COLORS = {
    "Datos del Prestador": {"bg": "#E8F3EE", "text": "#1A4031", "border": "#A7D0C0"},
    "Datos de la Víctima": {"bg": "#FDF6E3", "text": "#594411", "border": "#F3D89D"},
    "Datos del Sitio donde Ocurrió el Evento": {"bg": "#FDECEC", "text": "#6B1F1F", "border": "#F0B3B3"},
    "Datos del Vehículo": {"bg": "#F5E6E0", "text": "#5C2C1F", "border": "#E3AFA0"},
    "Datos del Propietario": {"bg": "#E6EEF2", "text": "#224A5E", "border": "#A1C2D4"},
    "Datos del Conductor": {"bg": "#E8EAF4", "text": "#2B2F5E", "border": "#ADB4D4"},
    "Datos de Atención de la Víctima": {"bg": "#F3E8EE", "text": "#542742", "border": "#D5A9C4"},
    "Datos de Remisión": {"bg": "#EAF4E8", "text": "#1F4F1A", "border": "#B0D3A6"},
    "Datos Transporte y Movilización": {"bg": "#E4F0F1", "text": "#1F4D52", "border": "#A5CFD3"},
    "Datos del Servicio": {"bg": "#FFF1E0", "text": "#6E3A0F", "border": "#FACDA1"},
    "Datos de la Reclamación": {"bg": "#EFEAF8", "text": "#3A2A6E", "border": "#C3B6E6"},
    "Datos de la Glosa": {"bg": "#FCEDE3", "text": "#6F3414", "border": "#F2C2A4"},
    "Datos del Auditor": {"bg": "#EAF1FA", "text": "#1F3A66", "border": "#B0C7E2"},
}

DEFAULT_SECTION_COLOR = {"bg": "#E8F3EE", "text": "#1A4031", "border": "#A7D0C0"}


def section_color(name: str) -> dict:
    return SECTION_COLORS.get(name, DEFAULT_SECTION_COLOR)


FONT_FAMILY = "Segoe UI"  # disponible nativamente en Windows
