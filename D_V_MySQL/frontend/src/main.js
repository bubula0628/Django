//import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'

//import axios
import * as Vue from 'vue' // in Vue 3
import axios from 'axios'
import VueAxios from 'vue-axios'
//axios.defaults.baseURL='http://localhost:8000'


//import elementplus
import ElementPlus from 'element-plus'
import 'element-plus/lib/theme-chalk/index.css'

const app = Vue.createApp(App)
app.config.globalProperties.$axios = axios
app.use(VueAxios, axios).use(store).use(router).use(ElementPlus).mount('#app')





