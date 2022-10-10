import { createRouter, createWebHistory } from 'vue-router'
import Home from '@/components/Home'
import Login from '@/components/Login_front'
import Vuex from '@/components/Vuex'

const routes = [
  {
    path: '/',
    name: 'home',
    component: Home
  },
  {
    path: '/login',
    name: 'login',
    component: Login
  },

  {
    path: '/vuex',
    name: 'vuex',
    component: Vuex
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
