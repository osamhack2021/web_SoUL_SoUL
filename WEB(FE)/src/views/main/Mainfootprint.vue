<template>
	<div id="mainouter">
		<h2 id="question-box">{{ Question }}</h2> <!-- Question.vue에서 받은 num에 따라 question이 달라짐. 또한 밑에 content-box에 띄워야할 컨텐츠로 num따라 다르게 DB에서 가져옴 -->
		<button @click="openpost()" :key="i" v-for="(post, i) in post_list">
			<section id="content-box">
				<div class="nickname">{{ post.Nickname }}</div>
				<p class="maintext-box">{{ post.mainText }}</p>
				<div class="date-box">{{ post.contentDate }}</div>
			</section>
		</button>
	</div>
</template>

<script>
	import axios from "axios"
	let url = "http://soul-bojmb.run.goorm.io/post/post/";    // Django DRF 서버 주소
	
	export default {
		data() {
			return {
				Question: "",
				post_list: []
			};
		}, 
		methods: {
			openpost() {
				this.$router.push('postfootprint');
			},
			getQuestion(){
				this.Question = this.$store.getters.getQuestion;
			},
			modifyList() {
				let tmp = this.post_list;
				this.post_list = [];
                
				for(let i=0; i<tmp.length; i++){
					if(tmp[i].category == 2){
						this.post_list.push(tmp[i]);
					}
				}
				console.log(this.post_list);
			},
		},
		mounted() {
			axios({
				moethod: "GET",
				url: url
			})
				.then(response => {
				this.post_list = response.data;
				this.modifyList();
			})
				.catch(response => {
				console.log("Failed", response);
			});
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