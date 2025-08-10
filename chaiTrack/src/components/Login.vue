<template>
  <div class="min-h-screen flex items-center justify-center bg-white p-4">
    <div class="border-2 border-brown-500 p-8 w-full max-w-md rounded-xl shadow-lg">
      <h2 class="text-2xl font-bold mb-6 text-center text-brown-700">Login</h2>
      
      <form @submit.prevent="login" class="space-y-4">
        <input 
          v-model="username" 
          type="text" 
          placeholder="Username" 
          class="w-full border-2 border-brown-500 p-3 rounded-lg focus:outline-none focus:ring-2 focus:ring-green-500"
        />
        <input 
          v-model="password" 
          type="password" 
          placeholder="Password" 
          class="w-full border-2 border-brown-500 p-3 rounded-lg focus:outline-none focus:ring-2 focus:ring-green-500"
        />
        
        <button 
          type="submit" 
          class="w-full bg-green-600 text-white py-3 rounded-lg font-bold shadow-md hover:bg-green-700 transition duration-300 glow-green"
        >
          Login
        </button>
      </form>
      
      <p v-if="error" class="text-red-500 mt-4 text-center">{{ error }}</p>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import api from '../services/axios'
import { useRouter } from 'vue-router'

const username = ref('')
const password = ref('')
const error = ref(null)
const router = useRouter()

const login = async () => {
  try {
    const response = await api.post('login/', {
      username: username.value,
      password: password.value
    })
    localStorage.setItem('token', response.data.access)
    router.push('/')
  } catch (err) {
    error.value = 'Invalid credentials or user not found.'
    console.error(err)
  }
}
</script>

<style scoped>
.glow-green {
  box-shadow: 0 0 10px rgba(34, 197, 94, 0.6), 0 0 20px rgba(34, 197, 94, 0.4);
}
.text-brown-700 {
  color: #6b4226;
}
.border-brown-500 {
  border-color: #8b5e3c;
}
</style>
