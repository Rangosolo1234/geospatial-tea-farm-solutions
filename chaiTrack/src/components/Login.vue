<template>
  <div class="p-4">
    <h2 class="text-xl mb-4">Login</h2>
    <form @submit.prevent="login">
      <input v-model="username" type="text" placeholder="Username" class="border p-2 mb-2 w-full" />
      <input v-model="password" type="password" placeholder="Password" class="border p-2 mb-2 w-full" />
      <button type="submit" class="bg-green-500 text-white px-4 py-2">Login</button>
    </form>
    <p v-if="error" class="text-red-600 mt-2">{{ error }}</p>
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
