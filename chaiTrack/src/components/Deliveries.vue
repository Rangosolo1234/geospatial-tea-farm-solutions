<template>
  <div class="bg-white p-6 rounded-lg shadow w-full">
    <h2 class="text-xl font-semibold text-green-700 mb-4">📊 Daily Tea Delivery Summary</h2>

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

    <div class="h-80">
      <Bar :key="chartData.labels.join(',')" :data="chartData" :options="chartOptions" />
    </div>
  </div>
</template>

<script setup>
import { Bar } from 'vue-chartjs'
import {
  Chart as ChartJS,
  Title,
  Tooltip,
  Legend,
  BarElement,
  CategoryScale,
  LinearScale
} from 'chart.js'
import { ref, onMounted } from 'vue'
import api from '../services/axios'

ChartJS.register(Title, Tooltip, Legend, BarElement, CategoryScale, LinearScale)

const chartData = ref({
  labels: [],
  datasets: [
    {
      label: 'KG Delivered',
      data: [],
      backgroundColor: '#86efac',
      borderColor: '#22c55e',
      borderWidth: 1,
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
      font: { size: 16 },
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

const totalKg = ref(0)
const averageKg = ref(0)
const peakDay = ref('-')

onMounted(async () => {
  try {
    const res = await api.get('deliveries/')
    const deliveries = res.data

    if (!deliveries.length) {
      console.warn('No delivery data found.')
      return
    }

    const grouped = {}

    deliveries.forEach(d => {
      let parsedDate
      try {
        parsedDate = new Date(d.date)
        if (isNaN(parsedDate)) throw new Error("Invalid date")
      } catch (e) {
        console.warn("Invalid date format:", d.date)
        return
      }

      const dateKey = parsedDate.toLocaleDateString('en-GB', {
        year: 'numeric',
        month: 'short',
        day: 'numeric',
      })

      grouped[dateKey] = (grouped[dateKey] || 0) + d.quantity_kg
    })

    const dates = Object.keys(grouped)
    const quantities = dates.map(date => grouped[date])

    chartData.value.labels = dates
    chartData.value.datasets[0].data = quantities

    const total = quantities.reduce((sum, val) => sum + val, 0)
    totalKg.value = total.toFixed(2)
    averageKg.value = (total / quantities.length).toFixed(2)

    const maxIndex = quantities.indexOf(Math.max(...quantities))
    peakDay.value = dates[maxIndex]
  } catch (err) {
    console.error('Error fetching delivery data:', err)
  }
})
</script>
