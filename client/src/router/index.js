import { createRouter, createWebHistory } from 'vue-router'
// import Vue from 'vue'
// import Router from 'vue-router'
import Home from "../views/Home.vue"
import Mypage from "../components/Mypage.vue"

// Vue.use(Router)

export const routes = [
	{
		path: '/home', 
		name: 'Home', 
		component: Home
	},
	{	
		path: '/mypage', 
		name: 'Mypage', 
		component: Mypage
	}
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
