import { createRouter, createWebHistory } from 'vue-router'
import Home from "../views/Home.vue"
import Footer from "../components/Footer.vue"
import Header from "../components/Header.vue"
import Mypage from "../components/Mypage.vue"
import WriteSonagi from "../views/WriteSonagi.vue"
import WriteFootprint from "../views/WriteFootprint.vue"
import WriteBook from "../views/WriteBook.vue"
import WriteMunhak from "../views/WriteMunhak.vue"
import Main from "../components/Main.vue"
import Mysonagi from "../views/Mysonagi.vue"
import Myfootprint from "../views/Myfootprint.vue"
import Mybook from "../views/Mybook.vue"
import Mymunhak from "../views/Mymunhak.vue"
import Mainsonagi from "../views/Mainsonagi"
import Mainfootprint from "../views/Mainfootprint"
import Mainbook from "../views/Mainbook"
import Mainmunhak from "../views/Mainmunhak"

const routes = [
	{
		path: '/home', 
		name: 'Home', 
		components: {
			default: Home,
			footer: Footer
		}
	},
	{
		path: '/main',
		components: {
			default: Main, 
			header: Header
		},
		children: [
			{ path: 'sonagi', name: 'Mysonagi', component: Mainsonagi},
			{ path: 'footprint', name: 'Myfootprint', component: Mainfootprint},
			{ path: 'book', name: 'Mybook', component: Mainbook},
			{ path: 'munhak', name: 'Mymunhak', component: Mainmunhak}
		],
	},
	{	
		path: '/', //mypage 붙여주기
		name: 'Mypage', 
		components: {
			default: Mypage,
			header: Header
		},
		children: [
			{ path: 'sonagi', component: Mysonagi },
			{ path: 'footprint', component: Myfootprint },
			{ path: 'book', component: Mybook },
			{ path: 'munhak', component: Mymunhak }
		],
	},
	{
		path: '/writesonagi',
		name: 'WriteSonagi',
		components: {
			default: WriteSonagi, 
			header: Header
		}
	},
	{
		path: '/writefootprint',
		name: 'WriteFootprint',
		components: {
			default: WriteFootprint,
			header: Header
		}
	},
	{
		path: '/writebook',
		name: 'WriteBook',
		components: {
			default: WriteBook,
			header: Header
		}
	},
	{
		path: '/writemunhak',
		name: 'WriteMunhak',
		components: {
			default: WriteMunhak,
			header: Header
		}
	},
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
