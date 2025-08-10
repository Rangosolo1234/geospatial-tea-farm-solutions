<template>
  <div class="min-h-screen flex items-center justify-center p-4 bg-white">
    <div class="p-8 w-full max-w-md rounded-2xl shadow-lg border border-brown-600 bg-white">
      <h2 class="text-2xl font-bold mb-6 text-center text-brown-700">Sign Up</h2>
      <form @submit.prevent="signup" class="space-y-4">
        <input
          v-model="username"
          type="text"
          placeholder="Username"
          class="glass-input"
        />
        <input
          v-model="email"
          type="email"
          placeholder="Email"
          class="glass-input"
        />
        <input
          v-model="password"
          type="password"
          placeholder="Password"
          class="glass-input"
        />
        <button
          type="submit"
          class="button-green w-full py-2 rounded-lg font-bold shadow-lg"
        >
          Sign Up
        </button>
      </form>
      <p v-if="message" class="text-green-700 mt-4 text-center">{{ message }}</p>
      <p v-if="error" class="text-red-600 mt-4 text-center">{{ error }}</p>
    </div>
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

<style scoped>
/* Brown bordered inputs with soft glow */
.glass-input {
  width: 100%;
  padding: 0.75rem;
  border: 2px solid #8b4513; /* SaddleBrown */
  border-radius: 0.5rem;
  outline: none;
  background: white;
  color: #5a3d1e;
  font-weight: 500;
  box-shadow: inset 0 0 5px rgba(139, 69, 19, 0.2);
  transition: all 0.3s ease;
}
.glass-input:focus {
  border-color: #228b22; /* ForestGreen */
  box-shadow: 0 0 8px rgba(34, 139, 34, 0.6);
}

/* Green glowing button */
.button-green {
  background: #228b22; /* ForestGreen */
  color: white;
  transition: all 0.3s ease;
}
.button-green:hover {
  background: #2e8b57; /* SeaGreen */
  box-shadow: 0 0 15px rgba(46, 139, 87, 0.8);
}
</style>
