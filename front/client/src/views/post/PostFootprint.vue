<template>
	<div>
		<div id="main-contaniner">
			<section id="post-box">
				<div class="question-box">{{ Question }}</div>
				<div class="maintext-box">{{ mainText }}</div>
				<div class="nickname">{{ nickName }}</div>
				<div class="date-box">{{ postDate }}</div>
			</section>
			<section id="post-box-footer">
				<button class="button-submit" @click="back()">◀</button>
			</section>
		</div>
	</div>
</template>

<script>	
	export default {
		// components: {Header, },
		data() {
			return {
				Question: "군생활 중 가장 아찔했던 순간은?",
				mainText: "설레는 그들을 충분히 것은 희망의 보라. 부패를 얼마나 천자만홍이 대중을 그들은 이것이야말로 뛰노는 그리하였는가? 갑 할지니, 밝은 이상의 시들어 칼이다. 고행을 되려니와, 것은 가치를 부패를 방황하였으며, 되는 그리하였는가? 피고 귀는 청춘을 천하를 수 창공에 물방아 군영과 희망의 위하여서.",
				nickName: "김동규",
				postDate: "2021.10.08",
			};
		},
		methods: {
			back() {
				this.$router.go(-1);
			}
		}
		// computed: {
		// 	user() {
		// 		return this.$store.state.user;
		// 	}
		// }
	}
</script>

<style>
	#post-box-footer { margin-top: 1rem;}
	#post-box-footer .button-submit {
		width: 7.5rem;
		height: 2.25rem;
		border: 2px solid #C4C4C4;
		border-radius: 5px;
		color: #C4C4C4;
	}
	#post-box-footer .button-submit:active {
		outline: none;
		opacity: 0.8;
	}
	#post-box-footer .button-submit:focus {
		outline: none;
	}
</style>
<style scoped>	
	#main-contaniner {
		width: 42.5rem;
		margin: 0 auto;
	}
	#post-box {
		display: block;
		padding: 1rem 1rem 0.5rem;
		border: 2px solid #C4C4C4;
	}
	#post-box .question-box {
		margin: 0 auto 10px;
		text-align: center;
		font-size: 1.5rem !important;
		width: auto;
	}
	#post-box .maintext-box {
		padding-top: 0.5rem;
		padding-bottom: 0.5rem;
	}
	#post-box .date-box {
		font-size: 0.875rem;
		color: #C4C4C4;
	}
	#post-box .nickname {
		float: right;
		font-size: 0.875rem;
		color: #C4C4C4;
	}
</style>
