import { createRouter, createWebHistory } from 'vue-router'
import store from '../store.js'

import Home from "../views/Home.vue"
import Login from "../views/Login.vue"
import Footer from "../components/Footer.vue"
import Header from "../components/Header.vue"

// import Main from "../views/main/Main.vue"
// import Mainsonagi from "../views/main/Mainsonagi.vue"
// import Questions from "../views/main/Questions.vue"
// import Mainfootprint from "../views/main/Mainfootprint.vue"
// import Mainbook from "../views/main/Mainbook.vue"
// import Mainmunhak from "../views/main/Mainmunhak.vue"

// import Mypage from "../views/mypage/Mypage.vue"
// import Mysonagi from "../views/mypage/Mysonagi.vue"
// import Myfootprint from "../views/mypage/Myfootprint.vue"
// import Mybook from "../views/mypage/Mybook.vue"
// import Mymunhak from "../views/mypage/Mymunhak.vue"

// import EditProfile from '../views/mypage/EditProfile.vue'

// import WriteSonagi from "../views/write/WriteSonagi.vue"
// import WriteQues from "../views/write/WriteQues.vue"
// import WriteFootprint from "../views/write/WriteFootprint.vue"
// import WriteBook from "../views/write/WriteBook.vue"
// import WriteMunhak from "../views/write/WriteMunhak.vue"

// import PostSonagi from "../views/post/PostSonagi.vue"
// import PostFootprint from "../views/post/PostFootprint.vue"
// import PostBook from "../views/post/PostBook.vue"
// import PostMunhak from "../views/post/PostMunhak.vue"

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
			default: () => import(/* webpackChunkName: "main" */ '../views/main/Main.vue'),
			header: Header,
			footer: Footer
		},
		children: [
			{ path: 'sonagi', name: 'Mysonagi', component: () => import(/* webpackChunkName: "main" */ '../views/main/Mainsonagi.vue')},
			{ path: 'questions', name: 'Questions', component: () => import(/* webpackChunkName: "main" */ '../views/main/Questions.vue')},
			{ path: 'footprint', name: 'Myfootprint', component: () => import(/* webpackChunkName: "main" */ '../views/main/Mainfootprint.vue')},
			{ path: 'book', name: 'Mybook', component: () => import(/* webpackChunkName: "main" */ '../views/main/Mainbook.vue')},
			{ path: 'munhak', name: 'Mymunhak', component: () => import(/* webpackChunkName: "main" */ '../views/main/Mainmunhak.vue')}
		],
	},
	{
		path: '/mypage', //mypage 붙여주기
		name: 'Mypage', 
		components: {
			default: () => import(/* webpackChunkName: "mypage" */ '../views/mypage/Mypage.vue'),
			header: Header,
			footer: Footer
		},
		children: [
			{ path: 'sonagi', component: () => import(/* webpackChunkName: "mypage" */ '../views/mypage/Mysonagi.vue') },
			{ path: 'footprint', component: () => import(/* webpackChunkName: "mypage" */ '../views/mypage/Myfootprint.vue') },
			{ path: 'book', component: () => import(/* webpackChunkName: "mypage" */ '../views/mypage/Mybook.vue') },
			{ path: 'munhak', component: () => import(/* webpackChunkName: "mypage" */ '../views/mypage/Mymunhak.vue') }
		],
	},
	{
		path: '/editprofile',
		name: 'EditProfile',
		components: {
			default: () => import(/* webpackChunkName: "mypage" */ '../views/mypage/EditProfile.vue'),
			header: Header,
			footer: Footer
		}
	},
	{
		path: '/writesonagi',
		name: 'WriteSonagi',
		components: {
			default: () => import('../views/write/WriteSonagi.vue'), 
			header: Header,
		}
	},
	{
		path: '/writeques',
		name: 'WriteQues',
		components: {
			default: () => import('../views/write/WriteQues.vue'),
			header: Header
		}
	},
	{
		path: '/writefootprint',
		name: 'WriteFootprint',
		components: {
			default: () => import('../views/write/WriteFootprint.vue'),
			header: Header
		}
	},
	{
		path: '/writebook',
		name: 'WriteBook',
		components: {
			default: () => import('../views/write/WriteBook.vue'),
			header: Header,
		}
	},
	{
		path: '/writemunhak',
		name: 'WriteMunhak',
		components: {
			default: () => import('../views/write/WriteMunhak.vue'),
			header: Header,
		}
	},
	{
		path: '/postsonagi',
		name: 'PostSonagi',
		components: {
			default: () => import('../views/post/PostSonagi.vue'),
			header: Header,
			footer: Footer
		}
	},
	{
		path: '/postfootprint',
		name: 'PostFootprint',
		components: {
			default: () => import('../views/post/PostFootprint.vue'),
			header: Header,
			footer: Footer
		}
	},
	{
		path: '/postbook',
		name: 'PostBook',
		components: {
			default: () => import('../views/post/PostBook.vue'),
			header: Header,
			footer: Footer
		}
	},
	{
		path: '/postmunhak',
		name: 'PostMunhak',
		components: {
			default: () => import('../views/post/PostMunhak.vue'),
			header: Header,
			footer: Footer
		}
	},
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
});

router.beforeEach((to, from, next) => { // eslint-disable-line no-unused-vars
	store.commit('startSpinner');
	setTimeout(() => {
		next();
	}, 1);
})

router.afterEach((to, from) => { // eslint-disable-line no-unused-vars
	store.commit('endSpinner');
})

export default router
