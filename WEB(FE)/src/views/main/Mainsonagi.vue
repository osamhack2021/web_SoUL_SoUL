<template>
	<div id="mainouter">
		<button @click="openpost(i)" :key="i" v-for="(post, i) in post_list" >
			<section id="content-box">
				<div id="in-header"><span class="date">{{ post.created_at }}</span><span class="nickname">{{ post.nickname }}</span></div>
				<p class="maintext-box">{{ post.content }}</p>
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
				post_list: []
			};
		},
		methods: {
			openpost(i) {
				this.$store.state.Content = this.post_list[i];
				this.$router.push('postsonagi');
			},
			modifyList() {
				let tmp = this.post_list;
				this.post_list = [];
                
				for(let i=0; i<tmp.length; i++){
					if(tmp[i].category == 1){
						this.post_list.push(tmp[i]);
					}
				}
				console.log(this.post_list);
			},
		},
		mounted() {    //DOM 객체가 생성된 후 DRF 서버에서 데이터를 (contentList) 가져와 저장
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
		}
	}

    
</script>

<style>
	#mainouter button {
		margin: 0 auto 16px;
		border: none;
		background: none;
		text-align: initial;
	}
	#mainouter button:active {
		opacity: 0.8;
		/* border: 1px solid rgba(196,196,196,0.4); */
		outline: none;
	}
	#mainouter button:focus {
		outline: none;
	}
</style>

<style scoped>
	#content-box {
		/* margin: 0 auto 26px; */
		padding: 0 1rem;
		width: 42.5rem;
		border: 1px solid rgba(196,196,196,0.2);
		border-radius: 4px; 
		/* box-shadow: 1px 1px 1px 1px 0.8px; */
    background: rgba(196,196,196,0.2);
	}
	#content-box p { margin-bottom: 0.7rem; }
	#content-box #in-header {
		display: flex;
		justify-content: space-between;
		align-items: center;
		margin: 0.5rem 0;
	}
	#content-box #in-header .date { font-size: 1.25rem; }
	#content-box #in-header .nickname { font-size: 1rem; }
	#content-box .maintext-box {
		display: -webkit-box;
		-webkit-line-clamp: 7; /*줄 넘어가면 잘라주는 웹킷*/
		-webkit-box-orient: vertical; /*줄 넘어가면 잘라주는 웹킷*/
		overflow: hidden;
	}
</style>
