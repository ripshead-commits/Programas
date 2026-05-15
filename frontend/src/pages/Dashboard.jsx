import React, { useEffect, useState } from "react";
import { fetchModules, listSubmissions, deleteSubmission } from "../lib/api";
import { Button } from "../components/ui/button";
import { Card } from "../components/ui/card";
import { FileText, ClipboardList, AlertCircle, Clock, Trash2, ArrowRight } from "lucide-react";
import { toast } from "sonner";

const MODULE_ICONS = {
  fur: FileText,
  ser: ClipboardList,
  frg: AlertCircle,
};

const MODULE_ACCENT = {
  fur: { from: "from-emerald-50", border: "border-emerald-200", icon: "text-emerald-700", chip: "bg-emerald-100 text-emerald-800" },
  ser: { from: "from-amber-50", border: "border-amber-200", icon: "text-amber-700", chip: "bg-amber-100 text-amber-800" },
  frg: { from: "from-orange-50", border: "border-orange-200", icon: "text-orange-700", chip: "bg-orange-100 text-orange-800" },
};

export default function Dashboard({ onOpenModule }) {
  const [modules, setModules] = useState([]);
  const [history, setHistory] = useState([]);
  const [loading, setLoading] = useState(true);

  const loadAll = async () => {
    try {
      setLoading(true);
      const mods = await fetchModules();
      setModules(mods);
      const allHist = [];
      for (const m of mods) {
        const subs = await listSubmissions(m.id);
        subs.slice(0, 5).forEach((s) => allHist.push({ ...s, module_name: m.name }));
      }
      allHist.sort((a, b) => b.created_at.localeCompare(a.created_at));
      setHistory(allHist.slice(0, 8));
    } catch (e) {
      toast.error("No se pudo cargar la información.");
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => { loadAll(); }, []);

  const handleDelete = async (moduleId, id) => {
    try {
      await deleteSubmission(moduleId, id);
      toast.success("Registro eliminado.");
      loadAll();
    } catch {
      toast.error("No se pudo eliminar.");
    }
  };

  return (
    <div className="dashboard-bg min-h-screen">
      {/* Header */}
      <header className="border-b border-emerald-100/80 bg-white/70 backdrop-blur-sm sticky top-0 z-30">
        <div className="max-w-7xl mx-auto px-6 lg:px-10 py-4 flex items-center gap-3">
          <div className="w-10 h-10 rounded-xl bg-emerald-700 grid place-items-center text-white font-bold shadow-sm" data-testid="app-logo">
            <span className="font-[Work_Sans]">FR</span>
          </div>
          <div className="flex-1">
            <h1 className="text-lg font-semibold text-emerald-900">Plantillas FUR / FRG</h1>
            <p className="text-xs text-slate-500">Diligenciamiento y descarga de formularios (SOAT / ADRES)</p>
          </div>
          <span className="hidden sm:inline-flex items-center gap-1 text-xs text-emerald-700 bg-emerald-50 px-3 py-1 rounded-full border border-emerald-100">
            <span className="w-1.5 h-1.5 bg-emerald-500 rounded-full"></span>
            Normativa Colombia
          </span>
        </div>
      </header>

      <main className="max-w-7xl mx-auto px-6 lg:px-10 py-10 lg:py-14">
        <section className="mb-10">
          <p className="text-xs uppercase tracking-[0.18em] text-emerald-700 font-semibold mb-2">Seleccione un módulo</p>
          <h2 className="text-3xl sm:text-4xl lg:text-5xl font-bold text-emerald-950 mb-3 max-w-3xl leading-tight">
            Diligencie y descargue sus plantillas <span className="text-[#E27D5F]">FUR / FRG</span> en minutos.
          </h2>
          <p className="text-slate-600 max-w-2xl">
            Cada módulo despliega únicamente sus campos, con listas oficiales y validación estricta. Las plantillas XLSX se generan respetando la estructura original.
          </p>
        </section>

        {/* Module cards */}
        <section className="grid grid-cols-1 md:grid-cols-3 gap-6 mb-14">
          {modules.map((m) => {
            const Icon = MODULE_ICONS[m.id] || FileText;
            const accent = MODULE_ACCENT[m.id] || MODULE_ACCENT.fur;
            return (
              <Card
                key={m.id}
                className={`card-tile cursor-pointer p-6 bg-gradient-to-br ${accent.from} to-white ${accent.border} border-2 rounded-2xl`}
                onClick={() => onOpenModule(m.id)}
                data-testid={`module-card-${m.id}`}
              >
                <div className="flex items-start justify-between mb-5">
                  <div className={`w-12 h-12 rounded-xl bg-white grid place-items-center shadow-sm ${accent.icon}`}>
                    <Icon className="w-6 h-6" />
                  </div>
                  <span className={`text-xs px-2.5 py-1 rounded-full font-medium ${accent.chip}`}>
                    {m.field_count} campos
                  </span>
                </div>
                <h3 className="text-xl font-semibold text-slate-900 mb-1.5">{m.name}</h3>
                <p className="text-sm text-slate-600 mb-6 leading-relaxed">{m.description}</p>
                <Button
                  className="w-full bg-emerald-800 hover:bg-emerald-900 text-white"
                  data-testid={`btn-open-${m.id}`}
                >
                  Abrir módulo
                  <ArrowRight className="ml-2 w-4 h-4" />
                </Button>
              </Card>
            );
          })}
        </section>

        {/* History */}
        <section>
          <div className="flex items-center justify-between mb-4">
            <div className="flex items-center gap-2">
              <Clock className="w-5 h-5 text-emerald-700" />
              <h3 className="text-lg font-semibold text-emerald-950">Historial reciente</h3>
            </div>
            <button onClick={loadAll} className="text-sm text-emerald-700 hover:underline" data-testid="btn-refresh-history">
              Actualizar
            </button>
          </div>

          <Card className="rounded-2xl border-emerald-100 bg-white">
            {loading ? (
              <div className="p-8 text-center text-slate-500 text-sm">Cargando…</div>
            ) : history.length === 0 ? (
              <div className="p-10 text-center" data-testid="history-empty">
                <p className="text-slate-500 text-sm">Aún no hay registros guardados. Diligencie un módulo para verlo aquí.</p>
              </div>
            ) : (
              <ul className="divide-y divide-emerald-50">
                {history.map((h) => (
                  <li key={h.id} className="p-4 flex items-center gap-4 hover:bg-emerald-50/40 transition" data-testid={`history-item-${h.id}`}>
                    <div className="w-9 h-9 rounded-lg bg-emerald-50 text-emerald-700 grid place-items-center">
                      <FileText className="w-4 h-4" />
                    </div>
                    <div className="flex-1 min-w-0">
                      <p className="text-sm font-medium text-slate-900 truncate">
                        {h.label || `Registro ${h.module_name}`}
                      </p>
                      <p className="text-xs text-slate-500">
                        {h.module_name} · {new Date(h.created_at).toLocaleString("es-CO")}
                      </p>
                    </div>
                    <Button
                      variant="ghost" size="sm"
                      onClick={() => onOpenModule(h.module_id, h.id)}
                      data-testid={`btn-reopen-${h.id}`}
                    >
                      Reabrir
                    </Button>
                    <button
                      onClick={() => handleDelete(h.module_id, h.id)}
                      className="text-slate-400 hover:text-red-600 p-2 rounded-lg hover:bg-red-50"
                      data-testid={`btn-delete-${h.id}`}
                      title="Eliminar"
                    >
                      <Trash2 className="w-4 h-4" />
                    </button>
                  </li>
                ))}
              </ul>
            )}
          </Card>
        </section>

        <footer className="text-center text-xs text-slate-400 mt-14 pb-4">
          Construido con ❤ para la gestión de reclamaciones SOAT — ADRES · Normativa 2026
        </footer>
      </main>
    </div>
  );
}
