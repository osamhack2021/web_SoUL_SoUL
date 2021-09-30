<template>
	<div >
		<Mypage />
	</div>
</template>

<script>
	// import Home from './views/Home'
	import Mypage from './components/Mypage'

	export default {
		components: {Mypage, /*Home*/},
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