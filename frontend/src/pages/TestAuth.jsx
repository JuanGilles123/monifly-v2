import { useState } from 'react'
import { api } from '../lib/api'

export default function TestAuth() {
  const [email, setEmail] = useState('')
  const [password, setPassword] = useState('')
  const [name, setName] = useState('')
  const [message, setMessage] = useState('')
  const [user, setUser] = useState(null)

  const handleRegister = async (e) => {
    e.preventDefault()
    try {
      await api.post('/auth/register', { email, name, password })
      setMessage('✅ Usuario registrado correctamente')
    } catch (error) {
      setMessage(`❌ Error: ${error.response?.data?.detail || 'Error de registro'}`)
    }
  }

  const handleLogin = async (e) => {
    e.preventDefault()
    try {
      await api.post('/auth/login', { email, password })
      setMessage('✅ Login exitoso')
      // Obtener datos del usuario
      const response = await api.get('/auth/me')
      setUser(response.data)
    } catch (error) {
      setMessage(`❌ Error: ${error.response?.data?.detail || 'Error de login'}`)
    }
  }

  const handleLogout = async () => {
    try {
      await api.post('/auth/logout')
      setUser(null)
      setMessage('✅ Sesión cerrada')
    } catch (error) {
      setMessage('❌ Error al cerrar sesión')
    }
  }

  const testHealthz = async () => {
    try {
      const response = await api.get('/healthz')
      setMessage(`✅ Backend OK: ${JSON.stringify(response.data)}`)
    } catch (error) {
      setMessage(`❌ Backend no responde: ${error.message}`)
    }
  }

  return (
    <div className="min-h-screen bg-slate-900 text-white p-6">
      <div className="max-w-md mx-auto space-y-6">
        <h1 className="text-2xl font-bold text-center">🧪 Test MoniFly Auth</h1>
        
        {/* Test de conectividad */}
        <button 
          onClick={testHealthz}
          className="w-full bg-blue-600 hover:bg-blue-700 py-2 px-4 rounded"
        >
          🔍 Test Backend Connection
        </button>

        {/* Formulario de registro/login */}
        {!user ? (
          <form className="space-y-4">
            <input
              type="email"
              placeholder="Email"
              value={email}
              onChange={(e) => setEmail(e.target.value)}
              className="w-full p-3 bg-slate-800 rounded border border-slate-700"
            />
            <input
              type="text"
              placeholder="Nombre"
              value={name}
              onChange={(e) => setName(e.target.value)}
              className="w-full p-3 bg-slate-800 rounded border border-slate-700"
            />
            <input
              type="password"
              placeholder="Contraseña"
              value={password}
              onChange={(e) => setPassword(e.target.value)}
              className="w-full p-3 bg-slate-800 rounded border border-slate-700"
            />
            <div className="grid grid-cols-2 gap-3">
              <button
                type="button"
                onClick={handleRegister}
                className="bg-emerald-600 hover:bg-emerald-700 py-2 px-4 rounded"
              >
                📝 Registrar
              </button>
              <button
                type="button"
                onClick={handleLogin}
                className="bg-blue-600 hover:bg-blue-700 py-2 px-4 rounded"
              >
                🔐 Login
              </button>
            </div>
          </form>
        ) : (
          <div className="bg-slate-800 p-4 rounded">
            <h3 className="font-semibold">👤 Usuario conectado:</h3>
            <p>ID: {user.id}</p>
            <p>Email: {user.email}</p>
            <p>Nombre: {user.name}</p>
            <button
              onClick={handleLogout}
              className="mt-3 bg-red-600 hover:bg-red-700 py-2 px-4 rounded"
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
      </div>
    </div>
  )
}
