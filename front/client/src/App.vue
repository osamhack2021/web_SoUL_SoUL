<template>
	<Header />
	<div id="main_container">
		<div id="inner">
			<SideBar />
		</div>
		<router-view/>
	</div>
</template>

<script>
	import Header from './components/Header'
	import SideBar from './components/SideBar'
	export default {
		components: {Header, SideBar},
		// computed: {
		// 	user() {
		// 		return this.$store.state.user;
		// 	}
		// }
	}
</script>

<style>
	#main_container {
		padding-top: 100px;
		display: flex;
		justify-content: center;
		border: 1px solid;
	}
	#inner {
		position: relative;
		display: block;
		width: 1000px;
		height: 1000px; /*컨텐츠 들어오면 지울 것*/
		border: 1px solid red;
	}
</style>
