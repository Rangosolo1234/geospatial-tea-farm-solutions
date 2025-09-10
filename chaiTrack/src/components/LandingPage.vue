<template>
  <div class="min-h-screen flex flex-col bg-gradient-to-br from-green-100 via-white to-green-200 text-gray-800">
    <!-- Header -->
    <div class="max-w-6xl mx-auto text-center py-8 px-6">
      <img src="/Logo.jpg" alt="TeaFarmGIS" class="w-32 h-32 mx-auto" />
      <h1 class="text-4xl md:text-5xl font-extrabold text-green-800 mt-4">
        Welcome to TeaFarmGIS 🌱
      </h1>
      <p class="text-lg md:text-xl text-gray-700 mt-4">
        Monitor tea deliveries, manage expenses, visualize farm & truck data, and track real-time weather & soil conditions — 
        all in one intuitive platform for tea farmers and cooperatives.
      </p>
    </div>

    <!-- Custom Carousel -->
    <div class="relative w-full max-w-6xl mx-auto overflow-hidden rounded-xl shadow-lg">
      <div
        class="flex transition-transform duration-700"
        :style="{ transform: `translateX(-${currentSlide * 100}%)` }"
      >
        <div
          v-for="(slide, index) in slides"
          :key="index"
          class="min-w-full h-[400px] bg-cover bg-center relative"
          :style="{ backgroundImage: `url(${slide.image})` }"
        >
          <div class="absolute inset-0 bg-black bg-opacity-40 flex items-center justify-center">
            <div class="text-center px-6 text-white animate-fadeIn">
              <h2 class="text-2xl md:text-3xl font-bold mb-2">{{ slide.title }}</h2>
              <p class="text-lg">{{ slide.description }}</p>
            </div>
          </div>
        </div>
      </div>

      <!-- Controls -->
      <button
        @click="prevSlide"
        class="absolute left-4 top-1/2 transform -translate-y-1/2 bg-green-600 p-2 rounded-full text-white hover:bg-green-700"
      >
        ‹
      </button>
      <button
        @click="nextSlide"
        class="absolute right-4 top-1/2 transform -translate-y-1/2 bg-green-600 p-2 rounded-full text-white hover:bg-green-700"
      >
        ›
      </button>

      <!-- Indicators -->
      <div class="absolute bottom-4 left-1/2 transform -translate-x-1/2 flex gap-2">
        <span
          v-for="(slide, index) in slides"
          :key="index"
          @click="goToSlide(index)"
          class="w-3 h-3 rounded-full cursor-pointer"
          :class="currentSlide === index ? 'bg-white' : 'bg-gray-400'"
        ></span>
      </div>
    </div>

    <!-- Buttons -->
    <div class="flex flex-col md:flex-row justify-center gap-4 pt-8">
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

    <!-- Footer -->
    <footer class="mt-auto py-4 text-sm text-gray-500 text-center">
      &copy; 2025 TeaFarmGIS. All rights reserved.
    </footer>
  </div>
</template>

<script setup>
import { ref, onMounted, onBeforeUnmount } from 'vue'
import { useRouter } from 'vue-router'

const router = useRouter()
const currentSlide = ref(0)
const slides = [
  {
    image: '/carousel/deliveries.jpg',
    title: 'Track Tea Deliveries',
    description: 'Real-time delivery logs to improve accountability and efficiency.',
  },
  {
    image: '/carousel/expenses.jpg',
    title: 'Manage Farm Expenses',
    description: 'Monitor costs and maximize profit margins with easy reports.',
  },
  {
    image: '/carousel/maps.jpg',
    title: 'Visualize Farms & Trucks',
    description: 'Interactive maps showing farm locations and truck movements.',
  },
  {
    image: '/carousel/weather.jpg',
    title: 'Real-Time Weather & Soil Data',
    description: 'Make better farming decisions with accurate environmental insights.',
  },
]

let autoSlideInterval

const nextSlide = () => {
  currentSlide.value = (currentSlide.value + 1) % slides.length
}

const prevSlide = () => {
  currentSlide.value = (currentSlide.value - 1 + slides.length) % slides.length
}

const goToSlide = (index) => {
  currentSlide.value = index
}

onMounted(() => {
  autoSlideInterval = setInterval(nextSlide, 5000)
})

onBeforeUnmount(() => {
  clearInterval(autoSlideInterval)
})

const goToLogin = () => router.push('/login')
const goToSignup = () => router.push('/signup')
</script>

<style scoped>
@keyframes fadeIn {
  from { opacity: 0; transform: translateY(10px); }
  to { opacity: 1; transform: translateY(0); }
}
.animate-fadeIn {
  animation: fadeIn 0.8s ease-in-out;
}
</style>
