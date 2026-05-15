// Maps a section name (Spanish) to a CSS modifier class for colour-coding
export function sectionClass(name = "") {
  const n = name.toLowerCase();
  if (n.includes("prestador")) return "section-prestador";
  if (n.includes("víctima") || n.includes("victima")) return "section-victima";
  if (n.includes("vehículo") || n.includes("vehiculo")) return "section-vehiculo";
  if (n.includes("propietario")) return "section-propietario";
  if (n.includes("conductor")) return "section-conductor";
  if (n.includes("evento") || n.includes("sitio")) return "section-evento";
  if (n.includes("atención") || n.includes("atencion")) return "section-atencion";
  if (n.includes("remisión") || n.includes("remision")) return "section-remision";
  if (n.includes("transporte")) return "section-transporte";
  if (n.includes("servicio")) return "section-servicio";
  if (n.includes("reclamación") || n.includes("reclamacion")) return "section-reclamacion";
  if (n.includes("glosa")) return "section-glosa";
  if (n.includes("auditor")) return "section-auditor";
  return "section-prestador";
}

export function sectionIconName(name = "") {
  const n = name.toLowerCase();
  if (n.includes("prestador")) return "Building2";
  if (n.includes("víctima") || n.includes("victima")) return "UserRound";
  if (n.includes("vehículo") || n.includes("vehiculo")) return "Car";
  if (n.includes("propietario")) return "BadgeCheck";
  if (n.includes("conductor")) return "Steering";
  if (n.includes("evento") || n.includes("sitio")) return "MapPin";
  if (n.includes("atención") || n.includes("atencion")) return "Stethoscope";
  if (n.includes("remisión") || n.includes("remision")) return "Ambulance";
  if (n.includes("transporte")) return "Truck";
  if (n.includes("servicio")) return "ClipboardList";
  if (n.includes("reclamación") || n.includes("reclamacion")) return "FileText";
  if (n.includes("glosa")) return "AlertCircle";
  if (n.includes("auditor")) return "ShieldCheck";
  return "FileText";
}

// Stable slug for HTML anchors
export function slugify(s = "") {
  return s
    .toLowerCase()
    .normalize("NFD").replace(/[\u0300-\u036f]/g, "")
    .replace(/[^a-z0-9]+/g, "-")
    .replace(/^-|-$/g, "");
}
