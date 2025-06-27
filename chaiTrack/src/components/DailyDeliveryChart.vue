<template>
  <div class="bg-white p-6 rounded-lg shadow w-full">
    <h2 class="text-xl font-semibold text-green-700 mb-4">📈 Daily Tea Delivery Summary</h2>

    <div class="grid grid-cols-1 sm:grid-cols-3 gap-4 mb-6">
      <div class="bg-green-100 p-4 rounded text-green-800">
        <p class="text-sm">Total KGs Delivered</p>
        <p class="text-2xl font-bold">{{ totalKg }}</p>
      </div>
      <div class="bg-blue-100 p-4 rounded text-blue-800">
        <p class="text-sm">Average Daily Delivery</p>
        <p class="text-2xl font-bold">{{ averageKg }}</p>
      </div>
      <div class="bg-yellow-100 p-4 rounded text-yellow-800">
        <p class="text-sm">Highest Delivery Day</p>
        <p class="text-2xl font-bold">{{ peakDay }}</p>
      </div>
    </div>

    <div class="h-72">
      <Line :data="chartData" :options="chartOptions" />
    </div>
  </div>
</template>

<script setup>
import { Line } from 'vue-chartjs'
import {
  Chart as ChartJS,
  Title,
  Tooltip,
  Legend,
  LineElement,
  PointElement,
  CategoryScale,
  LinearScale,
} from 'chart.js'
import { ref, onMounted } from 'vue'
import api from '../services/axios'

ChartJS.register(Title, Tooltip, Legend, LineElement, PointElement, CategoryScale, LinearScale)

const chartData = ref({
  labels: [],
  datasets: [
    {
      label: 'KG Delivered',
      data: [],
      borderColor: '#16a34a',
      backgroundColor: '#bbf7d0',
      fill: true,
      tension: 0.3,
    },
  ],
})

const chartOptions = ref({
  responsive: true,
  maintainAspectRatio: false,
  plugins: {
    legend: { position: 'top' },
    title: {
      display: true,
      text: 'Daily Tea Delivery (KG)',
      font: { size: 16 }
    },
  },
  scales: {
    y: {
      beginAtZero: true,
      title: { display: true, text: 'Kilograms' }
    },
    x: {
      title: { display: true, text: 'Date' }
    }
  }
})

// Stats
const totalKg = ref(0)
const averageKg = ref(0)
const peakDay = ref('-')

onMounted(async () => {
  const res = await api.get('deliveries/')
  const deliveries = res.data

  const dates = deliveries.map(d => d.date)
  const quantities = deliveries.map(d => d.quantity_kg)

  chartData.value.labels = dates
  chartData.value.datasets[0].data = quantities

  // Summary Calculations
  const total = quantities.reduce((sum, val) => sum + val, 0)
  totalKg.value = total.toFixed(2)
  averageKg.value = (total / quantities.length).toFixed(2)

  const maxIndex = quantities.indexOf(Math.max(...quantities))
  peakDay.value = dates[maxIndex]
})
</script>

<style scoped>
/* Optional: You can add custom styles here */
</style>
