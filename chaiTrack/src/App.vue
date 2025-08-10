<template>
  <div class="min-h-screen bg-white">
    <nav class="p-4 bg-green-200 flex gap-4">
      <router-link to="/">Home</router-link>
      <router-link to="/deliveries">Deliveries</router-link>
      <router-link to="/expenses">Expenses</router-link>
      <router-link to="/centers">Centers Map</router-link>
      <router-link to="/soil">Soil Data</router-link>
      <router-link to="/loctruck">Truck Locations</router-link>
      <router-link to="/weather">Weather Map</router-link>
      <router-link to="/signup">Sign Up</router-link>
      <router-link to="/login">Login</router-link>
    </nav>

    <!-- Content area with white background -->
    <div class="p-4">
      <router-view />
    </div>
  </div>
</template>

<script setup>
import { onMounted } from 'vue'

onMounted(() => {
  console.log('App mounted.')
})
</script>
