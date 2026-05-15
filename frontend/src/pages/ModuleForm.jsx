import React, { useEffect, useMemo, useRef, useState } from "react";
import { fetchSchema, downloadFilledTemplate, getSubmission, saveSubmission } from "../lib/api";
import { sectionClass } from "../lib/sections";
import { Button } from "../components/ui/button";
import { Input } from "../components/ui/input";
import { Label } from "../components/ui/label";
import { Textarea } from "../components/ui/textarea";
import {
  Select, SelectContent, SelectItem, SelectTrigger, SelectValue,
} from "../components/ui/select";
import { toast } from "sonner";
import {
  ArrowLeft, Download, Eraser, Save, AlertTriangle, ChevronRight,
  Building2, UserRound, Car, BadgeCheck, MapPin, Stethoscope, Ambulance,
  Truck, ClipboardList, FileText, AlertCircle, ShieldCheck, CircleUser,
} from "lucide-react";

const ICONS = {
  "Datos del Prestador": Building2,
  "Datos de la Víctima": UserRound,
  "Datos del Sitio donde Ocurrió el Evento": MapPin,
  "Datos del Vehículo": Car,
  "Datos del Propietario": BadgeCheck,
  "Datos del Conductor": CircleUser,
  "Datos de Atención de la Víctima": Stethoscope,
  "Datos de Remisión": Ambulance,
  "Datos Transporte y Movilización": Truck,
  "Datos del Servicio": ClipboardList,
  "Datos de la Reclamación": FileText,
  "Datos de la Glosa": AlertCircle,
  "Datos del Auditor": ShieldCheck,
};

const slug = (s) => s.toLowerCase().normalize("NFD").replace(/[\u0300-\u036f]/g, "").replace(/[^a-z0-9]+/g, "-");

export default function ModuleForm({ moduleId, onClose, prefillSubmissionId }) {
  const [schema, setSchema] = useState(null);
  const [values, setValues] = useState({});
  const [errors, setErrors] = useState({});
  const [activeSection, setActiveSection] = useState(null);
  const [submitting, setSubmitting] = useState(false);
  const formRef = useRef(null);

  useEffect(() => {
    (async () => {
      try {
        const sch = await fetchSchema(moduleId);
        setSchema(sch);
        setActiveSection(sch.sections[0]?.name || null);
        if (prefillSubmissionId) {
          const sub = await getSubmission(moduleId, prefillSubmissionId);
          setValues(sub.data || {});
          toast.info("Datos cargados desde el historial.");
        }
      } catch (e) {
        toast.error("No se pudo cargar el esquema del módulo.");
      }
    })();
  }, [moduleId, prefillSubmissionId]);

  const allFields = useMemo(() => (schema ? schema.sections.flatMap((s) => s.fields) : []), [schema]);

  const handleChange = (key, val) => {
    setValues((prev) => ({ ...prev, [key]: val }));
    if (errors[key]) {
      setErrors((prev) => {
        const c = { ...prev }; delete c[key]; return c;
      });
    }
  };

  const validate = () => {
    const errs = {};
    for (const f of allFields) {
      const v = values[f.key];
      const empty = v === undefined || v === null || (typeof v === "string" && v.trim() === "");
      if (f.required && empty) { errs[f.key] = "Campo obligatorio"; continue; }
      if (empty) continue;
      if (f.length && String(v).length > f.length) { errs[f.key] = `Máximo ${f.length} caracteres`; continue; }
      if (f.type === "number" && isNaN(Number(String(v).replace(",", ".")))) {
        errs[f.key] = "Debe ser numérico";
      }
      if (f.type === "date" && !/^\d{4}-\d{2}-\d{2}$/.test(v)) {
        errs[f.key] = "Formato AAAA-MM-DD";
      }
      if (f.type === "time" && !/^\d{2}:\d{2}$/.test(v)) {
        errs[f.key] = "Formato HH:MM";
      }
    }
    setErrors(errs);
    if (Object.keys(errs).length > 0) {
      // Scroll a primer error
      const firstKey = Object.keys(errs)[0];
      const el = document.querySelector(`[data-field="${firstKey}"]`);
      if (el) el.scrollIntoView({ behavior: "smooth", block: "center" });
      toast.error(`Faltan ${Object.keys(errs).length} campo(s) por corregir.`);
    }
    return Object.keys(errs).length === 0;
  };

  const handleDownload = async () => {
    if (!validate()) return;
    setSubmitting(true);
    try {
      await downloadFilledTemplate(moduleId, { data: values }, `${schema.name.replace(/\s+/g, "_")}.xlsx`);
      toast.success("Plantilla descargada y guardada en historial.");
    } catch (e) {
      const detail = e?.response?.data?.detail;
      if (detail?.errors) toast.error(detail.errors[0]);
      else toast.error("Error al descargar la plantilla.");
    } finally {
      setSubmitting(false);
    }
  };

  const handleSave = async () => {
    if (!validate()) return;
    setSubmitting(true);
    try {
      await saveSubmission(moduleId, { data: values });
      toast.success("Registro guardado en el historial.");
    } catch (e) {
      const detail = e?.response?.data?.detail;
      if (detail?.errors) toast.error(detail.errors[0]);
      else toast.error("No se pudo guardar.");
    } finally {
      setSubmitting(false);
    }
  };

  const handleClear = () => {
    if (Object.keys(values).length === 0) { toast.info("Los campos ya están vacíos."); return; }
    if (window.confirm("¿Está seguro que desea limpiar todos los campos?")) {
      setValues({}); setErrors({});
      toast.success("Campos limpiados.");
    }
  };

  const scrollToSection = (name) => {
    setActiveSection(name);
    const el = document.getElementById(`sec-${slug(name)}`);
    if (el) el.scrollIntoView({ behavior: "smooth", block: "start" });
  };

  if (!schema) {
    return <div className="min-h-screen grid place-items-center text-slate-500">Cargando módulo…</div>;
  }

  const missingCount = Object.keys(errors).length;

  return (
    <div className="min-h-screen bg-[#F7FAF8]">
      {/* Sticky header */}
      <header className="sticky top-0 z-30 bg-white/95 backdrop-blur-sm border-b border-emerald-100 shadow-sm">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-3 flex items-center gap-3 flex-wrap">
          <button
            onClick={onClose}
            className="flex items-center gap-1.5 text-sm text-slate-600 hover:text-emerald-800 transition"
            data-testid="btn-back-dashboard"
          >
            <ArrowLeft className="w-4 h-4" /> Volver
          </button>
          <div className="h-5 w-px bg-slate-200" />
          <div className="flex-1 min-w-0">
            <h1 className="text-base sm:text-lg font-semibold text-emerald-950 truncate" data-testid="module-title">
              {schema.name}
            </h1>
            <p className="text-xs text-slate-500 hidden sm:block">{schema.description}</p>
          </div>
          {missingCount > 0 && (
            <span className="text-xs bg-red-50 text-red-700 px-2.5 py-1 rounded-full border border-red-200 flex items-center gap-1">
              <AlertTriangle className="w-3 h-3" /> {missingCount} pendiente(s)
            </span>
          )}
          <div className="flex items-center gap-2">
            <Button
              variant="ghost"
              onClick={handleClear}
              className="text-red-700 hover:bg-red-50 hover:text-red-800"
              data-testid="btn-clear-fields"
            >
              <Eraser className="w-4 h-4 mr-1.5" /> Limpiar
            </Button>
            <Button
              variant="outline"
              onClick={handleSave}
              disabled={submitting}
              className="border-emerald-300 text-emerald-800 hover:bg-emerald-50"
              data-testid="btn-save-submission"
            >
              <Save className="w-4 h-4 mr-1.5" /> Guardar
            </Button>
            <Button
              onClick={handleDownload}
              disabled={submitting}
              className="bg-emerald-800 hover:bg-emerald-900 text-white"
              data-testid="btn-download-template"
            >
              <Download className="w-4 h-4 mr-1.5" /> Descargar XLSX
            </Button>
            <Button
              variant="ghost"
              onClick={onClose}
              className="text-slate-600 hover:text-slate-900"
              data-testid="btn-close-module"
            >
              Cerrar módulo
            </Button>
          </div>
        </div>
      </header>

      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-6 lg:py-8 grid grid-cols-1 lg:grid-cols-[260px_minmax(0,1fr)] gap-6 lg:gap-8">
        {/* Sidebar (desktop) */}
        <aside className="hidden lg:block">
          <div className="sticky top-24">
            <p className="text-xs uppercase tracking-wider text-slate-400 mb-2 px-2">Secciones</p>
            <nav className="space-y-1" data-testid="form-sidebar">
              {schema.sections.map((s) => {
                const Ic = ICONS[s.name] || FileText;
                const hasError = s.fields.some((f) => errors[f.key]);
                return (
                  <div
                    key={s.name}
                    onClick={() => scrollToSection(s.name)}
                    className={`sidebar-link ${activeSection === s.name ? "active" : ""}`}
                    data-testid={`sidebar-${slug(s.name)}`}
                  >
                    <Ic className="w-4 h-4 shrink-0" />
                    <span className="flex-1 truncate">{s.name}</span>
                    {hasError && <span className="w-1.5 h-1.5 rounded-full bg-red-500" />}
                    <ChevronRight className="w-3 h-3 opacity-50" />
                  </div>
                );
              })}
            </nav>
          </div>
        </aside>

        {/* Form */}
        <main ref={formRef} className="space-y-6 max-w-4xl">
          {/* Mobile section quick nav */}
          <div className="lg:hidden -mx-1 overflow-x-auto pb-2">
            <div className="flex gap-2 px-1">
              {schema.sections.map((s) => (
                <button
                  key={s.name}
                  onClick={() => scrollToSection(s.name)}
                  className={`text-xs px-3 py-1.5 rounded-full border whitespace-nowrap ${
                    activeSection === s.name
                      ? "bg-emerald-700 text-white border-emerald-700"
                      : "bg-white text-slate-700 border-slate-200"
                  }`}
                >
                  {s.name}
                </button>
              ))}
            </div>
          </div>

          {schema.sections.map((sec) => {
            const Ic = ICONS[sec.name] || FileText;
            return (
              <div
                key={sec.name}
                id={`sec-${slug(sec.name)}`}
                className={`section-card ${sectionClass(sec.name)}`}
                data-testid={`section-${slug(sec.name)}`}
              >
                <div className="section-header">
                  <Ic className="w-4 h-4" />
                  <span>{sec.name}</span>
                  <span className="ml-auto text-xs opacity-70 font-normal">
                    {sec.fields.length} campo(s)
                  </span>
                </div>
                <div className="p-5 sm:p-6 grid grid-cols-1 sm:grid-cols-2 gap-4 sm:gap-5">
                  {sec.fields.map((field) => (
                    <FieldInput
                      key={field.key}
                      field={field}
                      value={values[field.key] ?? ""}
                      error={errors[field.key]}
                      onChange={(v) => handleChange(field.key, v)}
                    />
                  ))}
                </div>
              </div>
            );
          })}

          <div className="flex items-center justify-end gap-2 pt-2">
            <Button variant="ghost" onClick={handleClear} data-testid="btn-clear-fields-bottom" className="text-red-700">
              <Eraser className="w-4 h-4 mr-1.5" /> Limpiar campos
            </Button>
            <Button onClick={handleDownload} disabled={submitting} className="bg-emerald-800 hover:bg-emerald-900" data-testid="btn-download-template-bottom">
              <Download className="w-4 h-4 mr-1.5" /> Descargar Plantilla XLSX
            </Button>
            <Button variant="outline" onClick={onClose} data-testid="btn-close-module-bottom">Cerrar módulo</Button>
          </div>
        </main>
      </div>
    </div>
  );
}

function FieldInput({ field, value, error, onChange }) {
  const isLong = field.type === "textarea" || (field.length && field.length >= 100);
  const span = isLong ? "sm:col-span-2" : "";
  const id = `f-${field.key}`;

  const baseProps = {
    id,
    "data-field": field.key,
    "data-testid": `input-${field.key}`,
    value: value ?? "",
    onChange: (e) => onChange(e.target.value),
    maxLength: field.length || undefined,
    className: error ? "border-red-400 focus-visible:ring-red-300" : "",
  };

  return (
    <div className={`flex flex-col gap-1.5 ${span}`}>
      <Label htmlFor={id} className="text-xs font-medium text-slate-700 flex items-center gap-1">
        <span className="truncate">{field.label}</span>
        {field.required && <span className="text-red-600">*</span>}
        {field.length && (
          <span className="ml-auto text-[10px] text-slate-400 font-normal">
            {String(value || "").length}/{field.length}
          </span>
        )}
      </Label>

      {field.type === "select" ? (
        <Select value={value || ""} onValueChange={onChange}>
          <SelectTrigger
            data-testid={`input-${field.key}`}
            className={error ? "border-red-400" : ""}
            id={id}
          >
            <SelectValue placeholder="Seleccione…" />
          </SelectTrigger>
          <SelectContent className="max-h-72">
            {field.options?.map((opt) => (
              <SelectItem key={opt.value} value={opt.value} data-testid={`option-${field.key}-${opt.value}`}>
                {opt.label}
              </SelectItem>
            ))}
          </SelectContent>
        </Select>
      ) : field.type === "textarea" ? (
        <Textarea {...baseProps} rows={4} />
      ) : field.type === "date" ? (
        <Input {...baseProps} type="date" />
      ) : field.type === "time" ? (
        <Input {...baseProps} type="time" />
      ) : field.type === "number" ? (
        <Input {...baseProps} inputMode="numeric" type="text" />
      ) : (
        <Input {...baseProps} type="text" />
      )}

      {error && (
        <p className="text-xs text-red-600 flex items-center gap-1" data-testid={`error-${field.key}`}>
          <AlertTriangle className="w-3 h-3" /> {error}
        </p>
      )}
    </div>
  );
}
