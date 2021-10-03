import { createRouter, createWebHistory } from 'vue-router'
import Home from "../views/Home.vue"
import Mypage from "../components/Mypage.vue"
import WriteSonagi from "../views/WriteSonagi.vue"
import WriteFootprint from "../views/WriteFootprint.vue"
import WriteBook from "../views/WriteBook.vue"
import WriteMunhak from "../views/WriteMunhak.vue"


const routes = [
	{
		path: '/home', 
		name: 'Home', 
		component: Home
	},
	{	
		path: '/mypage', 
		name: 'Mypage', 
		component: Mypage
	},
	{
		path: '/writesonagi',
		name: 'WriteSonagi',
		component: WriteSonagi
	},
	{
		path: '/writefootprint',
		name: 'WriteFootprint',
		component: WriteFootprint
	},
	{
		path: '/writebook',
		name: 'WriteBook',
		component: WriteBook
	},
	{
		path: '/writemunhak',
		name: 'WriteMunhak',
		component: WriteMunhak
	}
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
