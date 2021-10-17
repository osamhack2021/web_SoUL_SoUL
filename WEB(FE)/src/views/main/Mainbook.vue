<template>
	<div id="mainouter">
		<button @click="openpost()" :key="i" v-for="(content, i) in contentList">
			<section id="content-box">
				<div id="in-header"><span class="title">{{ content.bookTitle }}</span><span class="username">{{ content.bookAuthor }}</span></div>
				<p>{{ content.introText }}</p>
				<div class="date-box">{{ content.contentDate }}</div>
			</section>
		</button>
	</div>
</template>

<script>
	
	export default {
		data() {
			return {
				contentList: [
					{bookTitle: "노인과 바다", bookAuthor: "허밍웨이", introText: "설레는 그들을 충분히 것은 희망의 보라. 부패를 얼마나 천자만홍이 대중을 그들은 이것이야말로 뛰노는 그리하였는가? 갑 할지니, 밝은 이상의 시들어 칼이다. 고행을 되려니와, 것은 가치를 부패를 방황하였으며, 되는 그리하였는가? ",
					contentDate: "2021.10.05"},
					{bookTitle: "노인과 바다", bookAuthor: "허밍웨이", introText: "설레는 그들을 충분히 것은 희망의 보라. 부패를 얼마나 천자만홍이 대중을 그들은 이것이야말로 뛰노는 그리하였는가? 갑 할지니, 밝은 이상의 시들어 칼이다. 고행을 되려니와, 것은 가치를 부패를 방황하였으며, 되는 그리하였는가? ",
					contentDate: "2021.10.05"},
					{bookTitle: "노인과 바다", bookAuthor: "허밍웨이", introText: "설레는 그들을 충분히 것은 희망의 보라. 부패를 얼마나 천자만홍이 대중을 그들은 이것이야말로 뛰노는 그리하였는가? 갑 할지니, 밝은 이상의 시들어 칼이다. 고행을 되려니와, 것은 가치를 부패를 방황하였으며, 되는 그리하였는가? ",
					contentDate: "2021.10.05"},
				]};
		}, 
		methods: {
			openpost() {
				this.$router.push('postbook');
			}
		}
	}
</script>

<style scoped>
	#content-box {
		/* margin: 0 auto 26px; */
		padding: 0 1rem;
		width: 42.5rem;
		background: rgba(196,196,196,0.2);
		border: 1px solid rgba(196,196,196,0.4);
		border-radius: 4px; 
	}
	#content-box p { margin: 0; }
	#content-box #in-header {
		display: flex;
		justify-content: space-between;
		align-items: center;
		margin: 0.5rem 0;
	}
	#content-box #in-header .title { font-size: 1.25rem; }
	#content-box #in-header .username { font-size: 1rem; }
	#content-box .date-box {
		text-align: right;
		font-size: 0.875rem;
		padding: 0.5rem 0;
	}
</style>