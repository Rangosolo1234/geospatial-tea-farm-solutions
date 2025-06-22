// src/services/axios.js
import axios from 'axios'

const api = axios.create({
  baseURL: 'http://127.0.0.1:8000/api/',
  headers: {
    'Content-Type': 'application/json',
    // Add more headers here if needed, e.g., Authorization
  }
})

export default api
