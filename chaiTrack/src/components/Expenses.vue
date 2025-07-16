<template>
  <div class="p-6 bg-white rounded shadow space-y-6">
    <h2 class="text-2xl font-semibold text-green-700">💸 Expense Dashboard</h2>

    <!-- Filters -->
    <div class="grid grid-cols-1 sm:grid-cols-3 gap-4 items-end">
      <div>
        <label class="block font-medium">Farmer</label>
        <select v-model="selectedFarmer" @change="onFarmerChange" class="w-full p-2 border rounded">
          <option value="">-- All Farmers --</option>
          <option v-for="f in farmers" :key="f.id" :value="f.id">{{ f.username }}</option>
        </select>
      </div>

      <div>
        <label class="block font-medium">Farm</label>
        <select v-model="selectedFarm" @change="loadExpenses" class="w-full p-2 border rounded">
          <option value="">-- All Farms --</option>
          <option v-for="farm in farms" :key="farm.id" :value="farm.id">{{ farm.name }}</option>
        </select>
      </div>

      <div>
        <label class="block font-medium">View By</label>
        <select v-model="groupBy" @change="updateChart" class="w-full p-2 border rounded">
          <option value="weekly">Weekly</option>
          <option value="monthly">Monthly</option>
        </select>
      </div>
    </div>

    <!-- Chart -->
    <div class="h-80">
      <Bar :data="chartData" :options="chartOptions" />
    </div>

    <!-- Expense List -->
    <table class="w-full border-collapse border shadow-md">
      <thead class="bg-green-100">
        <tr>
          <th class="p-2 border">ID</th>
          <th class="p-2 border">Farm</th>
          <th class="p-2 border">Date</th>
          <th class="p-2 border">Type</th>
          <th class="p-2 border">Amount</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="exp in expenses" :key="exp.id" class="text-center">
          <td class="p-2 border">{{ exp.id }}</td>
          <td class="p-2 border">{{ exp.farm_name }}</td>
          <td class="p-2 border">{{ exp.date }}</td>
          <td class="p-2 border">{{ exp.expense_type }}</td>
          <td class="p-2 border">{{ exp.amount.toFixed(2) }}</td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script setup>
import { ref, onMounted, watch } from 'vue'
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
import api from '../services/axios'

ChartJS.register(Title, Tooltip, Legend, BarElement, CategoryScale, LinearScale)

const farmers = ref([])
const farms = ref([])  // farms of selected farmer
const expenses = ref([])

const selectedFarmer = ref('')
const selectedFarm = ref('')
const groupBy = ref('weekly')  // or 'monthly'

// Chart data
const chartData = ref({ labels: [], datasets: [{ label: 'Expense (KSh)', data: [], backgroundColor: '#facc15' }] })
const chartOptions = ref({
  responsive: true,
  maintainAspectRatio: false,
  plugins: {
    legend: { display: false },
    title: { display: true, text: 'Farm Expenses Overview' }
  },
  scales: {
    y: { beginAtZero: true, title: { display: true, text: 'Amount (KSh)' } },
    x: { title: { display: true, text: groupBy.value === 'weekly' ? 'Week' : 'Month' } }
  }
})

// Load farmers list
async function loadFarmers() {
  const res = await api.get('farmers/')
  farmers.value = res.data
}

// Load farms when farmer changes
async function onFarmerChange() {
  selectedFarm.value = ''
  if (selectedFarmer.value) {
    const res = await api.get(`farms/?farmer=${selectedFarmer.value}`)
    farms.value = res.data
  } else farms.value = []
  await loadExpenses()
}

// Load expenses data
async function loadExpenses() {
  const params = {}
  if (selectedFarm.value) params.farm = selectedFarm.value
  const res = await api.get('expenses/', { params })
  expenses.value = res.data.map(e => ({
    ...e,
    farm_name: farms.value.find(f => f.id === e.farm)?.name || 'All'
  }))
  updateChart()
}

// Process chart data based on groupBy
function updateChart() {
  const grouped = {}
  expenses.value.forEach(e => {
    const dt = new Date(e.date)
    let label
    if (groupBy.value === 'weekly') {
      const week = `${dt.getFullYear()}-W${Math.ceil((dt.getDate())/7)}`
      label = week
    } else {
      label = dt.toLocaleDateString('en-GB', { year: 'numeric', month: 'short' })
    }
    grouped[label] = (grouped[label] || 0) + e.amount
  })

  const labels = Object.keys(grouped).sort()
  chartData.value = {
    labels,
    datasets: [{ label: 'Expense (KSh)', data: labels.map(l => grouped[l]), backgroundColor: '#facc15' }]
  }
  chartOptions.value.scales.x.title.text = groupBy.value === 'weekly' ? 'Week' : 'Month'
}

onMounted(async () => {
  await loadFarmers()
  await loadExpenses()
})

watch([selectedFarmer, selectedFarm, groupBy], loadExpenses)
</script>

<style scoped>
/* Optional custom styles */
</style>
