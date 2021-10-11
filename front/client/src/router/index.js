import { createRouter, createWebHistory } from 'vue-router'
import Home from "../views/Home.vue"
import Login from "../views/Login.vue"
import Footer from "../components/Footer.vue"
import Header from "../components/Header.vue"
import Main from "../views/main/Main.vue"
import Mainsonagi from "../views/main/Mainsonagi"
import Questions from "../views/main/Questions"
import Mainfootprint from "../views/main/Mainfootprint"
import Mainbook from "../views/main/Mainbook"
import Mainmunhak from "../views/main/Mainmunhak"
import Mypage from "../views/mypage/Mypage.vue"
import Mysonagi from "../views/mypage/Mysonagi.vue"
import Myfootprint from "../views/mypage/Myfootprint.vue"
import Mybook from "../views/mypage/Mybook.vue"
import Mymunhak from "../views/mypage/Mymunhak.vue"
import EditProfile from '../views/mypage/EditProfile.vue'
import WriteSonagi from "../views/write/WriteSonagi.vue"
import WriteQues from "../views/write/WriteQues.vue"
import WriteFootprint from "../views/write/WriteFootprint.vue"
import WriteBook from "../views/write/WriteBook.vue"
import WriteMunhak from "../views/write/WriteMunhak.vue"
import PostSonagi from "../views/post/PostSonagi.vue"
import PostFootprint from "../views/post/PostFootprint.vue"
import PostBook from "../views/post/PostBook.vue"
import PostMunhak from "../views/post/PostMunhak.vue"

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
		path: '/login', 
		name: 'login', 
		component: Login
	},
	{
		path: '/',
		components: {
			default: Main, 
			header: Header
		},
		children: [
			{ path: 'sonagi', name: 'Mysonagi', component: Mainsonagi},
			{ path: 'questions', name: 'Questions', component: Questions},
			{ path: 'footprint', name: 'Myfootprint', component: Mainfootprint},
			{ path: 'book', name: 'Mybook', component: Mainbook},
			{ path: 'munhak', name: 'Mymunhak', component: Mainmunhak}
		],
	},
	{	
		path: '/mypage', //mypage 붙여주기
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
		path: '/editprofile',
		name: 'EditProfile',
		components: {
			default: EditProfile,
			header: Header
		}
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
		path: '/writeques', 
		components: {
			default: WriteQues,
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
	{
		path: '/postsonagi',
		name: 'PostSonagi',
		components: {
			default: PostSonagi,
			header: Header
		}
	},
	{
		path: '/postfootprint',
		name: 'PostFootprint',
		components: {
			default: PostFootprint,
			header: Header
		}
	},
	{
		path: '/postbook',
		name: 'PostBook',
		components: {
			default: PostBook,
			header: Header
		}
	},
	{
		path: '/postmunhak',
		name: 'PostMunhak',
		components: {
			default: PostMunhak,
			header: Header
		}
	},
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
