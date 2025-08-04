import { createRouter, createWebHistory } from 'vue-router'
import Login from '../components/Login.vue'
import Signup from '../components/Signup.vue'
// import Dashboard from '../components/Dashboard.vue'
import Expenses from '../components/Expenses.vue'
import Deliveries from '../components/Deliveries.vue'
import LandingPage from '../components/LandingPage.vue'
import CentersMap from '../components/CentersMap.vue'
import SoilData from '../components/SoilData.vue'
import TruckLocationsMap from '../components/TruckLocationsMap.vue'
import WeatherMap from '../components/WeatherMap.vue'

const routes = [
  { path: '/', component: LandingPage },
  { path: '/login', component: Login },
  { path: '/signup', component: Signup },
  { path: '/expenses', component: Expenses, meta: { requiresAuth: true } },
  { path: '/deliveries', component: Deliveries, meta: { requiresAuth: true } },
  { path: '/centers', component: CentersMap, meta: {requiresAuth: true} },
  { path: '/soil', component: SoilData, meta: {requiresAuth: true} },
  { path: '/loctruck', component: TruckLocationsMap, meta: {requiresAuth: true} },
   { path: '/weather', component: WeatherMap, meta: {requiresAuth: true} },
]

const router = createRouter({
  history: createWebHistory(),
  routes,
})

router.beforeEach((to, from, next) => {
  const token = localStorage.getItem('token')
  if (to.meta.requiresAuth && !token) {
    next('/login')
  } else {
    next()
  }
})

export default router
