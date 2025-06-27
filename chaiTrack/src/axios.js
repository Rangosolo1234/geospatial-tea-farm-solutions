// src/axios.js
import axios from 'axios'

// Create an instance
const api = axios.create({
  baseURL: 'http://localhost:8000/api/', // Backend runs on this locally
})

// Add token if exists
const token = localStorage.getItem('token')
if (token) {
  api.defaults.headers.common['Authorization'] = `Bearer ${token}`
}

export default api