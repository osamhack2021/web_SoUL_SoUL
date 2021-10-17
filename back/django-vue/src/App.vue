<template>
	<div>
		<router-view name="header"></router-view>
		<router-view class="maincontent"></router-view>
		<router-view name="footer"></router-view>
		<spinner :loading="$store.state.LoadingStatus"/>
	</div>
</template>

<script>
	import Spinner from './components/Spinner.vue'
	
	export default {
		components: {Spinner},
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