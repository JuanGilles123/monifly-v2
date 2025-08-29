import { motion } from 'framer-motion'

export default function App(){
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
          <a className="text-center rounded-lg bg-white/10 hover:bg-white/20 py-2" href="#">
            Ingresar
          </a>
          <a className="text-center rounded-lg bg-emerald-500 hover:bg-emerald-600 text-white py-2" href="#">
            Crear cuenta
          </a>
        </div>
        <p className="mt-4 text-center text-xs text-white/50">
          MVP React + Tailwind listo.
        </p>
      </motion.div>
    </div>
  )
}
