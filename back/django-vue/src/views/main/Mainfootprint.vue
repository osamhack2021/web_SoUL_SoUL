<template>
	<div id="mainouter">
		<h2 id="question-box">{{ Question }}</h2> <!-- Question.vue에서 받은 num에 따라 question이 달라짐. 또한 밑에 content-box에 띄워야할 컨텐츠로 num따라 다르게 DB에서 가져옴 -->
		<button @click="openpost()" :key="i" v-for="(content, i) in contentList">
			<section id="content-box">
				<div class="nickname">{{ content.Nickname }}</div>
				<p class="maintext-box">{{ content.mainText }}</p>
				<div class="date-box">{{ content.contentDate }}</div>
			</section>
		</button>
	</div>
</template>

<script>
	
	export default {
		data() {
			return {
				Question: "",
				contentList: [
					{Nickname: "김동규", mainText: "이 청춘 굳세게 시들어 피에 하였으며, 뜨거운지라, 철환하였는가? 얼마나 이는 원질이 있는 곳이 피는 생의 힘차게 이것이다. 위하여, 무엇을 쓸쓸한 피에 이상의 방황하여도, 만천하의 이상의 있다.", 
					contentDate: "2021.10.05"},
					{Question: "", Nickname: "김동규", mainText: "이 청춘 굳세게 시들어 피에 하였으며, 뜨거운지라, 철환하였는가? 얼마나 이는 원질이 있는 곳이 피는 생의 힘차게 이것이다. 위하여, 무엇을 쓸쓸한 피에 이상의 방황하여도, 만천하의 이상의 있다.", 
					contentDate: "2021.10.05"},
					{Question: "", Nickname: "김동규", mainText: "이 청춘 굳세게 시들어 피에 하였으며, 뜨거운지라, 철환하였는가? 얼마나 이는 원질이 있는 곳이 피는 생의 힘차게 이것이다. 위하여, 무엇을 쓸쓸한 피에 이상의 방황하여도, 만천하의 이상의 있다.", 
					contentDate: "2021.10.05"}
				]};
		}, 
		methods: {
			openpost() {
				this.$router.push('postfootprint');
			},
			getQuestion(){
				this.Question = this.$store.getters.getQuestion;
			}
		},
		mounted() {
			this.getQuestion();
		}
	}
</script>

<style scoped>
	#question-box {
		margin: 0 auto 1rem;
		text-align: center;
	}
	#content-box {
		/* margin: 0 auto 16px; */
		padding: 0 1rem;
		width: 42.5rem;
		background: rgba(196,196,196,0.2);
		border: 1px solid rgba(196,196,196,0.4);
		border-radius: 4px; 
	}
	#content-box p { margin: 0; }
	#content-box .maintext-box {
		display: -webkit-box;
		-webkit-line-clamp: 7; /*줄 넘어가면 잘라주는 웹킷*/
		-webkit-box-orient: vertical; /*줄 넘어가면 잘라주는 웹킷*/
		overflow: hidden;
	}
	#content-box .nickname { margin: 0.5rem 0; font-size: 1.25rem; }
	#content-box .date-box {
		text-align: right;
		font-size: 0.875rem;
		padding-bottom: 0.5rem;
	}
</style>