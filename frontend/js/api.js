const BASE_URL = 'http://127.0.0.1:8000';

// ── Auth ───────────────────────────────────
async function registerUser(data) {
  const res = await fetch(`${BASE_URL}/auth/register`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(data)
  });
  return res.json();
}

async function loginUser(data) {
  const res = await fetch(`${BASE_URL}/auth/login`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(data)
  });
  return res.json();
}

// ── Projects ───────────────────────────────
async function createProject(data) {
  const res = await fetch(`${BASE_URL}/project/create`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(data)
  });
  return res.json();
}

async function getAllProjects() {
  const res = await fetch(`${BASE_URL}/project/all`);
  return res.json();
}

async function getProject(id) {
  const res = await fetch(`${BASE_URL}/project/${id}`);
  return res.json();
}

async function deleteProject(id) {
  const res = await fetch(`${BASE_URL}/project/${id}`, { method: 'DELETE' });
  return res.json();
}

// ── AI Features ────────────────────────────
async function getDashboard(id) {
  const res = await fetch(`${BASE_URL}/dashboard/${id}`);
  return res.json();
}

async function getTasks(id) {
  const res = await fetch(`${BASE_URL}/task/${id}`);
  return res.json();
}

async function getRisk(id) {
  const res = await fetch(`${BASE_URL}/risk/${id}`);
  return res.json();
}

async function getWorkload(id) {
  const res = await fetch(`${BASE_URL}/workload/${id}`);
  return res.json();
}

async function getRetrospective(id) {
  const res = await fetch(`${BASE_URL}/retrospective/${id}`);
  return res.json();
}

async function getAnalytics(id) {
  const res = await fetch(`${BASE_URL}/analytics/${id}`);
  return res.json();
}

async function getRiskPredictor(id) {
  const res = await fetch(`${BASE_URL}/risk-predictor/${id}`);
  return res.json();
}

async function generateSprint(data) {
  const res = await fetch(`${BASE_URL}/ai/generate-sprint`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(data)
  });
  return res.json();
}

// ── Token helpers ──────────────────────────
function saveToken(token) { localStorage.setItem('token', token); }
function getToken() { return localStorage.getItem('token'); }
function logout() { localStorage.clear(); window.location.href = '../login.html'; }
function isLoggedIn() { return !!getToken(); }