<template>
	<section>
		<a href="#" class="content">
			<div id="head">
				<div style="font-size: 1.25rem;">{{ bookTitle }}</div>
			<div>{{ bookAuthor }}</div></div>
			<div class="date-box">{{ contentDate }}</div>
	</a>
	</section>
</template>

<script>
	export default {
		data() {
			return {
				bookTitle: "노인과 바다",
				bookAuthor: "허밍웨이",
				contentDate: "2021.10.06"
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
		padding: 0.6rem 0.8rem 0.5rem;
		margin: 0 auto 0.5rem;
		background-color: rgba(196, 196, 196, 0.3);
		color: black !important;
	}
	.content #head {
		display: flex;
		justify-content: space-between;
		align-items: center;
	}
	.content:active {
		opacity: 0.8;
	}
	.content .date-box {
		text-align: right;
    font-size: 0.875rem;
		margin-top: 0.25rem;
	}
</style>