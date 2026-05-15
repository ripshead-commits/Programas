import axios from "axios";

const BACKEND_URL = process.env.REACT_APP_BACKEND_URL;
export const API = `${BACKEND_URL}/api`;

export const api = axios.create({ baseURL: API });

export async function fetchModules() {
  const { data } = await api.get("/modules");
  return data;
}

export async function fetchSchema(moduleId) {
  const { data } = await api.get(`/modules/${moduleId}/schema`);
  return data;
}

export async function listSubmissions(moduleId) {
  const { data } = await api.get(`/modules/${moduleId}/submissions`);
  return data;
}

export async function getSubmission(moduleId, id) {
  const { data } = await api.get(`/modules/${moduleId}/submissions/${id}`);
  return data;
}

export async function deleteSubmission(moduleId, id) {
  const { data } = await api.delete(`/modules/${moduleId}/submissions/${id}`);
  return data;
}

export async function saveSubmission(moduleId, payload) {
  const { data } = await api.post(`/modules/${moduleId}/submissions`, payload);
  return data;
}

export async function downloadFilledTemplate(moduleId, payload, filename) {
  const response = await api.post(`/modules/${moduleId}/download`, payload, {
    responseType: "blob",
  });
  const url = window.URL.createObjectURL(new Blob([response.data]));
  const link = document.createElement("a");
  link.href = url;
  link.setAttribute("download", filename || "plantilla.xlsx");
  document.body.appendChild(link);
  link.click();
  link.remove();
  window.URL.revokeObjectURL(url);
}
