<template>
	<section>
		<a href="#" class="content">{{ question }}</a>
		<a href="#" class="content">{{ question }}</a>
		<a href="#" class="content">{{ question }}</a>
		<a href="#" class="content">{{ question }}</a>
	</section>
</template>

<script>
	export default {
		data() {
			return {
				question: "4. 군생활 중 가장 외로웠던 순간은?"
			};
		}
	}
</script>

<style scoped>
	.content {
		display: block;
		width: 42.5rem;
		border: 1px solid rgba(196, 196, 196, 0.8);
		border-radius: 5px;
		padding: 0.8rem;
		margin: 0 auto 0.5rem;
		background-color: rgba(196, 196, 196, 0.3);
		color: black !important;
	}
	.content:active {
		opacity: 0.8;
	}
</style>