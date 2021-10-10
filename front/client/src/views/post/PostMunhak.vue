<template>
	<div>
		<div id="main-contaniner">
			<section id="post-box">
				<div class="title-box">{{ munhakTitle }}</div>
				<div class="nickname">{{ nickName }}</div>				
				<div class="maintext-box">{{ mainText }}</div>
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
				munhakTitle: "노인과 바다",
				nickName: "김동규",
				mainText: "설레는 그들을 충분히 것은 희망의 보라. 부패를 얼마나 천자만홍이 대중을 그들은 이것이야말로 뛰노는 그리하였는가? 갑 할지니, 밝은 이상의 시들어 칼이다. 고행을 되려니와, 것은 가치를 부패를 방황하였으며, 되는 그리하였는가? 피고 귀는 청춘을 천하를 수 창공에 물방아 군영과 희망의 위하여서. 보내는 못할 무엇이 대한 들어 천지는 쓸쓸하랴? 그들의 열락의 군영과 그들의 위하여 그들은 더운지라 인류의 끓는 운다. 보이는 우는 그들의 꽃이 영락과 있는 찾아다녀도, 것이다. 가슴에 가치를 것이 것이다. 꽃 황금시대를 것은 커다란 무엇을 있는 없으면, 우리 얼마나 것이다. 불어 만천하의 물방아 못할 우리 이성은 이것은 사랑의 때문이다.",
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
		border-radius: 4px;
	}
	#post-box .title-box {
		margin: 0 auto;
		text-align: center;
		font-size: 1.75rem !important;
		width: auto;
	}
	#post-box .nickname {
    margin: 0.25rem 0.5rem;
    text-align: right;
	}
	#post-box .maintext-box {
		padding-top: 0.5rem;
		padding-bottom: 0.5rem;
	}
	#post-box .date-box {
		font-size: 0.875rem;
		color: #C4C4C4;
	}
</style>
