<template>
  <div class="p-4">
    <h2 class="text-xl mb-4">Sign Up</h2>
    <form @submit.prevent="signup">
      <input v-model="username" type="text" placeholder="Username" class="border p-2 mb-2 w-full" />
      <input v-model="email" type="email" placeholder="Email" class="border p-2 mb-2 w-full" />
      <input v-model="password" type="password" placeholder="Password" class="border p-2 mb-2 w-full" />
      <button type="submit" class="bg-blue-500 text-white px-4 py-2">Sign Up</button>
    </form>
    <p v-if="message" class="text-green-600 mt-2">{{ message }}</p>
    <p v-if="error" class="text-red-600 mt-2">{{ error }}</p>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import api from '../services/axios'
import { useRouter } from 'vue-router'

const username = ref('')
const email = ref('')
const password = ref('')
const message = ref(null)
const error = ref(null)
const router = useRouter()

const signup = async () => {
  try {
    await api.post('register/', {
      username: username.value,
      email: email.value,
      password: password.value
    })
    message.value = 'Account created! Redirecting to login...'
    setTimeout(() => router.push('/login'), 2000)
  } catch (err) {
    error.value = 'Signup failed. Username might be taken.'
    console.error(err)
  }
}
</script>