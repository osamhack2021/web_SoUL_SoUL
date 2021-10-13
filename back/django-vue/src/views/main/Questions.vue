<template>
	<div>
		<!-- DB 안에는 각 질문이 번호가 매겨져있음. 이 링크(버튼)을 클릭하면 num이 해당 질문에 대한 숫자로 바뀌고 num을 Mainfootprint.vue로 넘겨서 
Mainfootprint.vue에서는 num을 가지고 question을 띄워줌. 그리고 num에 따라서 DB에서 가져오는 contents도 달라짐
-->
		<button class="questionbox" @click="openquestion()">1. 군생활 중 가장 아찔했던 순간은?</button>
		<button class="questionbox">2. 군생활 중 가장 행복했던 순간은?</button>
		<button class="questionbox">3. 군생활 중 가장 힘들었던 순간은?</button>
		<button class="questionbox">4. 군생활 중 가장 외로웠던 순간은?</button>
		<button class="questionbox">5. 군생활 중 가장 위기였던 순간은?</button>
	</div>
</template>

<script>
	export default {
		data() {
			return {
				num: 0
			};
		},
		methods: {
			openquestion() {
				// this.$router.push('footprint'); //history에 스택이 쌓여서 나중에 뒤로갈 수 있음
				this.$router.replace('footprint'); //history에 스택이 쌓이지 않아서 뒤로갈 수 없음
			}
		}
		// computed: {
			// chageNum() {
		// 		this.num = 
		// 	}
		//}
	}
</script>

<style scoped>
	.questionbox {
		display: grid;
		margin: 0 auto 26px;
		padding: 1rem 1rem;
		width: 31.25rem;
		background: rgba(196,196,196,0.2);
		border: 1px solid rgba(196,196,196,0.4);
		border-radius: 4px;
		font-size: 1.2rem;
	}
	.questionbox:active {
		opacity: 0.8;
		border: 1px solid rgba(196,196,196,0.4);
		outline: none;
	}
	.questionbox:focus {
		outline: none;
	}
</style>