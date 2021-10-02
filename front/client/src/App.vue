<template>
	<div >
		<WriteSonagi />
	</div>
</template>

<script>
	import WriteSonagi from './views/WriteSonagi'


	export default {
		components: {WriteSonagi, },
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