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
import { useRouter } from 'vue-router'
import api from '@/axios'

const username = ref('')
const password = ref('')
const router = useRouter()

const login = async () => {
  try {
    const res = await api.post('token/', {
      username: username.value,
      password: password.value,
    })

    // Save token
    localStorage.setItem('token', res.data.access)

    // 👇 Immediately apply token to future requests (runtime)
    api.defaults.headers.common['Authorization'] = `Bearer ${res.data.access}`

    // Navigate to dashboard or wherever you want
    router.push('/dashboard')
  } catch (err) {
    console.error('Login error:', err)
    alert('Login failed. Please check your credentials.')
  }
}
</script>

<style scoped>
.input {
  @apply block w-full border border-gray-300 rounded px-4 py-2 mb-4;
}
.btn-green {
  @apply bg-green-600 text-white px-4 py-2 rounded hover:bg-green-700 w-full;
}
</style>
