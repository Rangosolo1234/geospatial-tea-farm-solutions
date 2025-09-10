<template>
  <div class="p-4">
    <h1 class="text-xl font-semibold">Deliveries</h1>
    <!-- ========================Loop through delivery data ======================== -->
    <ul>
      <li v-for="d in deliveries" :key="d.id">{{ d.name }}</li>
    </ul>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import api from '../services/axios'

const deliveries = ref([])

onMounted(async () => {
  const res = await api.get('deliveries/')
  deliveries.value = res.data
})
</script>
