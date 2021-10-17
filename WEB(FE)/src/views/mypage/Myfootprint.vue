<template>
	<section>
		<router-link to="/postfootprint" class="content" :key="i" v-for="(content, i) in contentList">
			{{ content.question }}
		</router-link>
	</section>
</template>

<script>
	export default {
		data() {
			return {
				contentList:[
					{question: "4. 군생활 중 가장 외로웠던 순간은?"},
					{question: "4. 군생활 중 가장 외로웠던 순간은?"},
					{question: "4. 군생활 중 가장 외로웠던 순간은?"}
				]};
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
		margin: 1rem auto;
		background-color: rgba(196, 196, 196, 0.3);
		color: black !important;
	}
	.content:active {
		opacity: 0.8;
	}
</style>