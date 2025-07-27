<template>
  <div class="min-h-screen flex flex-col items-center justify-center bg-gradient-to-br from-green-100 via-white to-green-200 text-gray-800 p-6">
    <div class="max-w-3xl text-center space-y-6">
      <img src="/Logo.jpg" alt="TeaFarmGIS" class="w-32 h-32 mx-auto" />

      <h1 class="text-4xl md:text-5xl font-extrabold text-green-800">
        Welcome to TeaFarmGIS 🌱
      </h1>

      <p class="text-lg md:text-xl text-gray-700">
        Monitor tea deliveries, manage expenses, visualize farm and truck data, and track real-time weather and soil data —
        all in one intuitive platform built for tea farmers and cooperatives.
      </p>

      <div class="flex flex-col md:flex-row justify-center gap-4 pt-4">
        <button
          @click="goToLogin"
          class="bg-green-600 hover:bg-green-700 text-white px-6 py-3 rounded-lg shadow-md transition"
        >
          Login
        </button>

        <button
          @click="goToSignup"
          class="bg-white border-2 border-green-600 text-green-700 hover:bg-green-100 px-6 py-3 rounded-lg shadow-md transition"
        >
          Sign Up
        </button>
      </div>
    </div>

    <footer class="absolute bottom-4 text-sm text-gray-500">
      &copy; 2025 TeaFarmGIS. All rights reserved.
    </footer>
  </div>
</template>

<script setup>
import { useRouter } from 'vue-router'
const router = useRouter()

const goToLogin = () => router.push('/login')
const goToSignup = () => router.push('/signup')
</script>