<template>
  <div class="p-6 bg-white rounded shadow w-full">
    <h2 class="text-xl font-semibold text-green-700 mb-4">Farm Expenses Overview</h2>

    <div class="mb-4">
      <label for="farmer" class="block mb-1 text-gray-700 font-medium">Select Farmer</label>
      <select v-model="selectedFarmer" @change="filterByFarmer" class="w-full p-2 border rounded">
        <option value="">All Farmers</option>
        <option v-for="farmer in uniqueFarmers" :key="farmer" :value="farmer">{{ farmer }}</option>
      </select>
    </div>

    <div v-if="selectedFarmer" class="mb-4">
      <label for="farm" class="block mb-1 text-gray-700 font-medium">Select Farm</label>
      <select v-model="selectedFarm" @change="filterByFarm" class="w-full p-2 border rounded">
        <option value="">All Farms</option>
        <option v-for="farm in uniqueFarmsForSelectedFarmer" :key="farm" :value="farm">{{ farm }}</option>
      </select>
    </div>

    <div class="grid grid-cols-1 md:grid-cols-2 gap-6 mb-6">
      <div v-if="dailyChart?.labels?.length" class="bg-gray-50 p-4 rounded shadow">
        <h3 class="text-sm font-medium text-gray-600 mb-2">📅 Daily Expenses</h3>
        <Bar :data="dailyChart" :options="chartOptions('Daily')" style="height:200px" />
        <p class="mt-2 text-xs text-gray-500">Top Day: {{ topDayExpense }}</p>
      </div>
      <div v-if="weeklyChart?.labels?.length" class="bg-gray-50 p-4 rounded shadow">
        <h3 class="text-sm font-medium text-gray-600 mb-2">📈 Weekly Expenses</h3>
        <Bar :data="weeklyChart" :options="chartOptions('Weekly')" style="height:200px" />
        <p class="mt-2 text-xs text-gray-500">Top Week: {{ topWeekExpense }}</p>
      </div>
      <div v-if="monthlyChart?.labels?.length" class="bg-gray-50 p-4 rounded shadow">
        <h3 class="text-sm font-medium text-gray-600 mb-2">📆 Monthly Expenses</h3>
        <Bar :data="monthlyChart" :options="chartOptions('Monthly')" style="height:200px" />
        <p class="mt-2 text-xs text-gray-500">Top Month: {{ topMonthExpense }}</p>
      </div>
      <div v-if="yearlyChart?.labels?.length" class="bg-gray-50 p-4 rounded shadow">
        <h3 class="text-sm font-medium text-gray-600 mb-2">📊 Yearly Expenses</h3>
        <Bar :data="yearlyChart" :options="chartOptions('Yearly')" style="height:200px" />
        <p class="mt-2 text-xs text-gray-500">Top Year: {{ topYearExpense }}</p>
      </div>
    </div>

    <div v-if="selectedFarmer" class="bg-green-50 p-4 rounded border border-green-200">
      <h3 class="text-lg font-semibold text-green-700 mb-2">🏆 Expense Leaderboard - {{ selectedFarmer }}</h3>
      <ul class="list-disc ml-4 text-sm">
        <li v-for="(expense, farm) in rankedFarms" :key="farm">
          {{ farm }} - {{ expense.toLocaleString() }} KSh
        </li>
      </ul>
    </div>

    <h3 class="text-lg font-semibold text-green-700 mt-8 mb-2">📋 Raw Expense Data</h3>
    <table class="min-w-full table-auto text-sm border">
      <thead class="bg-green-100">
        <tr>
          <th class="px-2 py-1 border">ID</th>
          <th class="px-2 py-1 border">Farmer</th>
          <th class="px-2 py-1 border">Farm</th>
          <th class="px-2 py-1 border">Date</th>
          <th class="px-2 py-1 border">Type</th>
          <th class="px-2 py-1 border">Amount (KSh)</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="exp in filteredExpenses" :key="exp.id">
          <td class="px-2 py-1 border">{{ exp.id }}</td>
          <td class="px-2 py-1 border">{{ exp.farmer.first_name}}</td>
          <td class="px-2 py-1 border">{{ exp.farm_name }}</td>
          <td class="px-2 py-1 border">{{ exp.date }}</td>
          <td class="px-2 py-1 border">{{ exp.expense_type }}</td>
          <td class="px-2 py-1 border">{{ exp.amount.toLocaleString() }}</td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script setup>
import { ref, watch, computed, onMounted } from 'vue';
import { Bar } from 'vue-chartjs';
import { Chart as ChartJS, Title, Tooltip, Legend, BarElement, CategoryScale, LinearScale } from 'chart.js';
ChartJS.register(Title, Tooltip, Legend, BarElement, CategoryScale, LinearScale);

const expenses = ref([]);
const selectedFarmer = ref('');
const selectedFarm = ref('');
const filteredExpenses = ref([]);

const fetchExpenses = async () => {
  try {
    const res = await fetch('http://127.0.0.1:8000/api/expenses/');
    const data = await res.json();
    console.log(data); 
    expenses.value = data;
    filterByFarmer();
  } catch (err) {
    console.error('Error fetching expenses:', err);
  }
};

const filterByFarmer = () => {
  selectedFarm.value = '';
  if (!selectedFarmer.value) {
    filteredExpenses.value = expenses.value;
  } else {
    filteredExpenses.value = expenses.value.filter(e => {
      // Handle both direct farmer string and nested farmer object
      const farmer = e.farmer?.first_name || e.farmer;
      return farmer === selectedFarmer.value;
    });
  }
};

const filterByFarm = () => {
  if (!selectedFarm.value) {
    filterByFarmer();
  } else {
    filteredExpenses.value = expenses.value.filter(e => e.farmer === selectedFarmer.value && e.farm === selectedFarm.value);
  }
};

const uniqueFarmers = computed(() => {
  return [...new Set(expenses.value.map(e => {
    // Handle both direct farmer string and nested farmer object
    return e.farmer?.first_name || e.farmer;
  }))].filter(Boolean); // Remove null/undefined
});
const uniqueFarmsForSelectedFarmer = computed(() => {
  return [...new Set(expenses.value.filter(e => e.farmer === selectedFarmer.value).map(e => e.farm))];
});

const chartOptions = (title) => ({
  responsive: true,
  plugins: {
    legend: { display: false },
    title: { display: true, text: title + ' Expenses' }
  },
  scales: {
    y: {
      beginAtZero: true,
      ticks: { stepSize: 100 },
      title: { display: true, text: 'Amount (KSh)' }
    },
    x: {
      title: { display: true, text: 'Period' }
    }
  }
});

const prepareChartData = (expensesList, interval) => {
  const format = interval === 'daily' ? 10 : interval === 'weekly' ? 8 : interval === 'monthly' ? 7 : 4;
  const map = {};
  expensesList.forEach(e => {
    const key = new Date(e.date).toISOString().slice(0, format);
    map[key] = (map[key] || 0) + e.amount;
  });
  const labels = Object.keys(map);
  const data = Object.values(map);
  return { labels, datasets: [{ label: 'Expenses', data, backgroundColor: '#4caf50' }] };
};

const dailyChart = ref({ labels: [], datasets: [] });
const weeklyChart = ref({ labels: [], datasets: [] });
const monthlyChart = ref({ labels: [], datasets: [] });
const yearlyChart = ref({ labels: [], datasets: [] });

watch(filteredExpenses, () => {
  dailyChart.value = prepareChartData(filteredExpenses.value, 'daily');
  weeklyChart.value = prepareChartData(filteredExpenses.value, 'weekly');
  monthlyChart.value = prepareChartData(filteredExpenses.value, 'monthly');
  yearlyChart.value = prepareChartData(filteredExpenses.value, 'yearly');
});

const rankedFarms = computed(() => {
  const totals = {};
  filteredExpenses.value.forEach(e => {
    totals[e.farm] = (totals[e.farm] || 0) + e.amount;
  });
  return Object.fromEntries(Object.entries(totals).sort(([, a], [, b]) => b - a));
});

const topDayExpense = computed(() => dailyChart.value.labels?.[0] || '-');
const topWeekExpense = computed(() => weeklyChart.value.labels?.[0] || '-');
const topMonthExpense = computed(() => monthlyChart.value.labels?.[0] || '-');
const topYearExpense = computed(() => yearlyChart.value.labels?.[0] || '-');

onMounted(fetchExpenses);
</script>

<style scoped>
select:focus {
  outline: none;
  box-shadow: 0 0 0 2px rgba(72, 187, 120, 0.5);
}
</style>
