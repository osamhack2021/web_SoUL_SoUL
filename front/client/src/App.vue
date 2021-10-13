<template>
	<div>
		<router-view name="header"></router-view>
		<router-view class="maincontent"></router-view>
		<router-view name="footer"></router-view>
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

<style scoped>
	html {
		font-size: 16px;
	}
	.maincontent {
		min-height: 700px;
	}
</style>