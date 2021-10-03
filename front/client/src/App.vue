<template>
	<div >
		<Header />
	</div>
</template>

<script>
	import Header from "./components/Header.vue"
	export default {
		components: {Header,},
		// computed: {
		// 	user() {
		// 		return this.$store.state.user;
		// 	}
		// }
	}
</script>

<style>
	html {
		font-size: 16px;
	}
</style>