<template>
	<div>		
		<!-- <Home /> -->
		<Header />
		<SideBar />
	</div>
</template>

<script>
	// import Home from './views/Home'
	import Header from './components/Header'
	import SideBar from './components/SideBar'

	export default {
		components: {Header, SideBar, /*Home*/},
		// computed: {
		// 	user() {
		// 		return this.$store.state.user;
		// 	}
		// }
	}
</script>
