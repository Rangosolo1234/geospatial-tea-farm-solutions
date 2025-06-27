<template>
  <div class="min-h-screen flex items-center justify-center bg-gray-100">
    <form @submit.prevent="signup" class="bg-white p-8 rounded shadow-md w-full max-w-sm">
      <h2 class="text-2xl font-bold mb-6 text-green-700">Sign Up</h2>

      <input v-model="username" type="text" placeholder="Username" class="input" required />
      <input v-model="email" type="email" placeholder="Email" class="input" required />
      <input v-model="password" type="password" placeholder="Password" class="input" required />

      <button type="submit" class="btn-green">Create Account</button>
    </form>
  </div>
</template>

<!-- <script setup>
import { ref } from 'vue'
import axios from 'axios'

const username = ref('')
const email = ref('')
const password = ref('')

const signup = async () => {
  try {
    await axios.post('/api/users/', {
      username: username.value,
      email: email.value,
      password: password.value,
    })
    alert('Signup successful! Now login.')
  } catch (error) {
    console.error(error)
    alert('Signup failed')
  }
}
</script> -->


<!-- ######################################################################################### -->
<script setup>
import { ref } from 'vue'
import api from '@/axios' // ✅ import the custom axios instance

const username = ref('')
const email = ref('')
const password = ref('')

const signup = async () => {
  try {
    await api.post('users/', {
      username: username.value,
      email: email.value,
      password: password.value,
    })
    alert('Signup successful! Now login.')
  } catch (error) {
    console.error(error)
    alert('Signup failed')
  }
}
</script>


<!-- ######################################################################## -->

<style scoped>
.input {
  @apply mb-4 w-full px-4 py-2 border rounded;
}
.btn-green {
  @apply w-full bg-green-600 text-white py-2 rounded hover:bg-green-700;
}
</style>
