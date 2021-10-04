<template>
	<div >
		<router-view name="header"></router-view>
		<router-view></router-view>
	</div>
</template>

<script>
	
	export default {
		// components: {},
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