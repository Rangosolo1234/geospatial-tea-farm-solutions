<template>
  <div class="min-h-screen flex items-center justify-center bg-gray-100">
    <form @submit.prevent="login" class="bg-white p-8 rounded shadow-md w-full max-w-sm">
      <h2 class="text-2xl font-bold mb-6 text-green-700">Login</h2>
      <input v-model="username" placeholder="Username" class="input" required />
      <input v-model="password" type="password" placeholder="Password" class="input" required />
      <button class="btn-green">Login</button>
    </form>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import axios from 'axios'
import { useRouter } from 'vue-router'

const username = ref('')
const password = ref('')
const router = useRouter()

const login = async () => {
  try {
    const res = await axios.post('http://localhost:8000/api/token/', {
      username: username.value,
      password: password.value,
    })
    localStorage.setItem('token', res.data.access)
    axios.defaults.headers.common['Authorization'] = `Bearer ${res.data.access}`
    router.push('/')
  } catch (err) {
    alert('Login failed')
  }
}
</script>