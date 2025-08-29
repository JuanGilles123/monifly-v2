import { useState } from "react";
import { api } from "../lib/api";

export default function Login(){
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [name, setName] = useState("");
  const [me, setMe] = useState(null);
  const [message, setMessage] = useState("");
  const [loading, setLoading] = useState(false);

  const onRegister = async () => {
    setLoading(true);
    try {
      const response = await api.post("/auth/register", { email, name, password });
      setMessage(`✅ ${response.data.message}`);
    } catch (error) {
      setMessage(`❌ Error: ${error.response?.data?.detail || error.message}`);
    }
    setLoading(false);
  };

  const onLogin = async () => {
    setLoading(true);
    try {
      const loginResponse = await api.post("/auth/login", { email, password });
      setMessage(`✅ ${loginResponse.data.message}`);
      
      // Obtener perfil del usuario
      const profileResponse = await api.get("/auth/me");
      setMe(profileResponse.data);
    } catch (error) {
      setMessage(`❌ Error: ${error.response?.data?.detail || error.message}`);
    }
    setLoading(false);
  };

  const onLogout = async () => {
    try {
      await api.post("/auth/logout");
      setMe(null);
      setMessage("✅ Sesión cerrada");
    } catch (error) {
      setMessage(`❌ Error logout: ${error.message}`);
    }
  };

  const testBackend = async () => {
    try {
      const response = await api.get("/auth/test");
      setMessage(`✅ Backend: ${response.data.message}`);
    } catch (error) {
      setMessage(`❌ Backend error: ${error.message}`);
    }
  };

  return (
    <div className="min-h-screen bg-slate-900 text-white p-6">
      <div className="max-w-md mx-auto space-y-6">
        <h1 className="text-2xl font-bold text-center">🔐 MoniFly Login</h1>
        
        {/* Test Backend */}
        <button 
          onClick={testBackend}
          className="w-full bg-blue-600 hover:bg-blue-700 py-2 px-4 rounded"
        >
          🔍 Test Backend Connection
        </button>

        {/* Usuario no logueado */}
        {!me && (
          <div className="space-y-4">
            <input
              type="email"
              placeholder="Email"
              value={email}
              onChange={(e) => setEmail(e.target.value)}
              className="w-full p-3 bg-slate-800 rounded border border-slate-700 text-white"
            />
            <input
              type="text"
              placeholder="Nombre (opcional)"
              value={name}
              onChange={(e) => setName(e.target.value)}
              className="w-full p-3 bg-slate-800 rounded border border-slate-700 text-white"
            />
            <input
              type="password"
              placeholder="Contraseña"
              value={password}
              onChange={(e) => setPassword(e.target.value)}
              className="w-full p-3 bg-slate-800 rounded border border-slate-700 text-white"
            />
            <div className="grid grid-cols-2 gap-3">
              <button
                onClick={onRegister}
                disabled={loading || !email || !password}
                className="bg-emerald-600 hover:bg-emerald-700 disabled:bg-gray-600 py-2 px-4 rounded"
              >
                {loading ? "..." : "📝 Registrar"}
              </button>
              <button
                onClick={onLogin}
                disabled={loading || !email || !password}
                className="bg-blue-600 hover:bg-blue-700 disabled:bg-gray-600 py-2 px-4 rounded"
              >
                {loading ? "..." : "🔐 Login"}
              </button>
            </div>
          </div>
        )}

        {/* Usuario logueado */}
        {me && (
          <div className="bg-slate-800 p-4 rounded">
            <h3 className="font-semibold text-emerald-400 mb-2">👤 Usuario conectado:</h3>
            <pre className="text-sm text-slate-300 mb-4">
              {JSON.stringify(me, null, 2)}
            </pre>
            <button
              onClick={onLogout}
              className="w-full bg-red-600 hover:bg-red-700 py-2 px-4 rounded"
            >
              🚪 Logout
            </button>
          </div>
        )}

        {/* Mensajes */}
        {message && (
          <div className="bg-slate-800 p-3 rounded text-sm">
            {message}
          </div>
        )}

        {/* Info técnica */}
        <div className="text-xs text-slate-500 text-center">
          <p>Backend: {import.meta.env.VITE_API_URL}</p>
          <p>Cookies: httpOnly + SameSite=None (cross-domain)</p>
        </div>
      </div>
    </div>
  );
}
