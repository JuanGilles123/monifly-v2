import axios from "axios";

export const api = axios.create({
  baseURL: import.meta.env.VITE_API_URL,
  withCredentials: true, // para cookies httpOnly
});

// Interceptor para manejar errores globalmente
api.interceptors.response.use(
  (response) => response,
  (error) => {
    if (error.response?.status === 401) {
      // Usuario no autenticado, redirigir al login si es necesario
      console.log('Usuario no autenticado');
    }
    return Promise.reject(error);
  }
);
