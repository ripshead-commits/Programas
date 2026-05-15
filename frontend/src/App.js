import React, { useState } from "react";
import { Toaster } from "./components/ui/sonner";
import Dashboard from "./pages/Dashboard";
import ModuleForm from "./pages/ModuleForm";
import "./App.css";

export default function App() {
  // view: { type: 'dashboard' } | { type: 'module', moduleId, prefillId? }
  const [view, setView] = useState({ type: "dashboard" });

  const openModule = (moduleId, prefillId) =>
    setView({ type: "module", moduleId, prefillId });
  const goDashboard = () => setView({ type: "dashboard" });

  return (
    <div className="App">
      {view.type === "dashboard" ? (
        <Dashboard onOpenModule={openModule} />
      ) : (
        <ModuleForm
          key={`${view.moduleId}-${view.prefillId || "new"}`}
          moduleId={view.moduleId}
          prefillSubmissionId={view.prefillId}
          onClose={goDashboard}
        />
      )}
      <Toaster position="top-right" richColors closeButton />
    </div>
  );
}
