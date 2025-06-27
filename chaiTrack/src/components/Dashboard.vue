<template>
  <div class="flex flex-col min-h-screen bg-gray-50">
    <!-- Header -->
    <header class="bg-green-700 text-white py-4 px-6 shadow-md flex justify-between items-center">
      <h1 class="text-2xl font-bold">🍃 ChaiTrack Dashboard</h1>
      <div class="text-sm">Smart Tea Farming</div>
    </header>

    <!-- Main Content -->
    <div class="flex flex-1">
      <!-- Sidebar -->
      <aside class="hidden md:block w-64 bg-green-800 text-white">
        <div class="p-6 text-xl font-semibold border-b border-green-700">📊 Menu</div>
        <nav class="p-4 space-y-2">
          <div class="px-4 py-2 rounded bg-green-900">📈 Daily Deliveries</div>
          <div class="px-4 py-2 rounded hover:bg-green-700">👨‍🌾 Farmers</div>
          <div class="px-4 py-2 rounded hover:bg-green-700">🗺️ Farm Boundaries</div>
          <div class="px-4 py-2 rounded hover:bg-green-700">💰 Expenses</div>
          <div class="px-4 py-2 rounded hover:bg-green-700">🚛 Truck Locations</div>
          <div class="px-4 py-2 rounded hover:bg-green-700">🌦️ Weather</div>
          <div class="px-4 py-2 rounded hover:bg-green-700">🧪 Soil Data</div>
        </nav>
      </aside>

      <!-- Dashboard Content Area -->
      <main class="flex-1 p-6">
        <h2 class="text-2xl font-semibold text-green-700 mb-4">Welcome to ChaiTrack</h2>
        
        <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-4">
          <div class="bg-white rounded shadow p-4">
            <p class="text-gray-600">Today's Delivery</p>
            <h3 class="text-2xl font-bold text-green-600">138 Kg</h3>
          </div>
          <div class="bg-white rounded shadow p-4">
            <p class="text-gray-600">Active Farmers</p>
            <h3 class="text-2xl font-bold text-green-600">32</h3>
          </div>
          <div class="bg-white rounded shadow p-4">
            <p class="text-gray-600">Average Labour Cost</p>
            <h3 class="text-2xl font-bold text-green-600">KSh 540</h3>
          </div>
        </div>

        <div class="mt-6 bg-white rounded shadow p-6">
          <h3 class="text-xl font-semibold mb-2 text-gray-700">Summary</h3>
          <p class="text-gray-600">
            Monitor your tea collection, farm boundaries, truck movements, and environmental data in one place. Use the sidebar to navigate and get insights into your daily operations.
          </p>
        </div>
      </main>
    </div>

    <!-- Footer -->
    <footer class="bg-green-900 text-white text-center py-3">
      &copy; {{ new Date().getFullYear() }} ChaiTrack – Built for Smart Tea Farming 🍵
    </footer>
  </div>
</template>

<script setup>
// No imports needed yet – layout only
</script>

<style scoped>
/* Optional: smooth fade-ins */
</style>
