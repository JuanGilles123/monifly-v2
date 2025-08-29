import { useState } from 'react'
import { motion } from 'framer-motion'
import TestAuth from './TestAuth'
import Login from './Login'

export default function App(){
  const [currentView, setCurrentView] = useState('home') // 'home', 'test', 'login'

  if (currentView === 'test') {
    return <TestAuth />
  }

  if (currentView === 'login') {
    return <Login />
  }

  return (
    <div className="min-h-[100dvh] grid place-items-center p-6">
      <motion.div 
        initial={{opacity:0, y:10}} 
        animate={{opacity:1,y:0}}
        transition={{duration:0.4}}
        className="w-full max-w-md rounded-2xl border border-white/10 bg-white/5 backdrop-blur p-6"
      >
        <h1 className="text-3xl font-bold text-center">MoniFly</h1>
        <p className="text-center text-white/70">Finanzas personales, simple.</p>
        <div className="mt-6 grid grid-cols-2 gap-3">
          <button
            onClick={() => setCurrentView('login')}
            className="text-center rounded-lg bg-white/10 hover:bg-white/20 py-2"
          >
            Ingresar
          </button>
          <button
            onClick={() => setCurrentView('login')}
            className="text-center rounded-lg bg-emerald-500 hover:bg-emerald-600 text-white py-2"
          >
            Crear cuenta
          </button>
        </div>
        
        {/* Botón para testing */}
        <button
          onClick={() => setCurrentView('test')}
          className="mt-4 w-full text-center rounded-lg bg-blue-600 hover:bg-blue-700 text-white py-2 text-sm"
        >
          🧪 Test Authentication
        </button>
        
        <p className="mt-4 text-center text-xs text-white/50">
          MVP React + Tailwind + Auth listo.
        </p>
      </motion.div>
    </div>
  )
}
