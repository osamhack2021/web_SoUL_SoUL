<template>
	<div>
		<h2 id="question-box">{{ question }}</h2> <!-- Question.vue에서 받은 num에 따라 question이 달라짐. 또한 밑에 content-box에 띄워야할 컨텐츠로 num따라 다르게 DB에서 가져옴 -->
		<section id="content-box">
			<div class="nickname">{{ Nickname }}</div>
			<p>{{ mainText }}</p>
			<div class="date-box">{{ contentDate }}</div>
		</section>
	</div>
</template>

<script>
	
	export default {
		data() {
			return {
				question: "군생활 중 가장 아찔했던 순간은?",
				Nickname: "김동규",
				mainText: "이 청춘 굳세게 시들어 피에 하였으며, 뜨거운지라, 철환하였는가? 얼마나 이는 원질이 있는 곳이 피는 생의 힘차게 이것이다. 위하여, 무엇을 쓸쓸한 피에 이상의 방황하여도, 만천하의 이상의 있다.",
				contentDate: "2021.10.05"
			};
		}
	}
</script>

<style scoped>
	#question-box {
		margin: 0 auto 1rem;
		text-align: center;
	}
	#content-box {
		margin: 0 auto 26px;
		padding: 0 1rem;
		width: 42.5rem;
		background: rgba(196,196,196,0.2);
		border: 1px solid rgba(196,196,196,0.4);
		border-radius: 4px; 
	}
	#content-box p { margin: 0; }
	/* #content-box #in-header {
		display: grid;
		align-items: center;
		margin: 0.5rem 0;
	} */
	#content-box .nickname { margin: 0.5rem 0; font-size: 1.25rem; }
	#content-box .date-box {
		text-align: right;
		font-size: 0.875rem;
		padding-bottom: 0.5rem;
	}
</style>