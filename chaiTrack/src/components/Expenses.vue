<template>
  <div class="p-6">
    <h1 class="text-2xl mb-4 font-bold text-green-700">Manage Farm Expenses</h1>

    <!-- Add Expense Form -->
    <form @submit.prevent="addExpense" class="bg-white shadow p-4 rounded mb-6 max-w-md">
      <label class="block mb-2">Select Farm</label>
      <select v-model="farm" class="input" required>
        <option disabled value="">-- Choose a Farm --</option>
        <option
          v-for="f in farms"
          :key="f.properties.id"
          :value="f.properties.id"
        >
          {{ f.properties.name }}
        </option>
      </select>

      <label class="block mt-4 mb-2">Date</label>
      <input v-model="date" type="date" class="input" required />

      <label class="block mt-4 mb-2">Expense Type</label>
      <input v-model="type" type="text" placeholder="e.g. Fertilizer" class="input" required />

      <label class="block mt-4 mb-2">Amount (KES)</label>
      <input v-model="amount" type="number" step="0.01" class="input" required />

      <button class="btn-green mt-4">Add Expense</button>
    </form>

    <!-- Expense Table -->
    <div class="overflow-x-auto">
      <table class="table-auto w-full bg-white shadow rounded">
        <thead class="bg-green-700 text-white">
          <tr>
            <th class="px-4 py-2 text-left">Farm</th>
            <th class="px-4 py-2">Date</th>
            <th class="px-4 py-2">Type</th>
            <th class="px-4 py-2">Amount</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="e in expenses" :key="e.id" class="border-t">
            <td class="px-4 py-2">{{ getFarmName(e.farm) }}</td>
            <td class="px-4 py-2">{{ e.date }}</td>
            <td class="px-4 py-2">{{ e.expense_type }}</td>
            <td class="px-4 py-2">{{ e.amount }}</td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useRouter } from 'vue-router'
import api from '@/axios'

const router = useRouter()

const farm = ref('')
const date = ref('')
const type = ref('')
const amount = ref('')

const expenses = ref([])
const farms = ref([])

// Get farm name from ID using GeoJSON properties
const getFarmName = (farmId) => {
  const match = farms.value.find(f => f.properties.id === farmId)
  return match ? match.properties.name : 'Unknown'
}

const fetchData = async () => {
  try {
    const [farmsRes, expensesRes] = await Promise.all([
      api.get('farms/'),
      api.get('expenses/')
    ])

    farms.value = Array.isArray(farmsRes.data)
      ? farmsRes.data
      : farmsRes.data.features || farmsRes.data.results || []

    expenses.value = Array.isArray(expensesRes.data)
      ? expensesRes.data
      : expensesRes.data.results || []

  } catch (err) {
    console.error('Error fetching data:', err)
    if (err.response?.status === 401) {
      alert('Session expired. Please log in again.')
      router.push('/login')
    }
  }
}

const addExpense = async () => {
  try {
    await api.post('expenses/', {
      farm: farm.value,
      date: date.value,
      expense_type: type.value,
      amount: amount.value
    })

    farm.value = ''
    date.value = ''
    type.value = ''
    amount.value = ''

    await fetchData()
  } catch (err) {
    console.error('Failed to add expense:', err)
    alert('Failed to add expense. Ensure you are logged in and fields are valid.')
  }
}

onMounted(fetchData)
</script>

<style scoped>
.input {
  @apply block w-full border border-gray-300 rounded px-4 py-2 mt-1;
}
.btn-green {
  @apply bg-green-600 text-white px-4 py-2 rounded hover:bg-green-700 w-full;
}
</style>
