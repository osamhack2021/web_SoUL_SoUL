<template>
	<div id="mainouter">
		<button @click="openpost()" :key="i" v-for="(post, i) in post_list">
			<section id="content-box">
				<div id="in-header"><span class="title">{{ post.bookTitle }}</span><span class="username">{{ post.bookAuthor }}</span></div>
				<p>{{ post.introText }}</p>
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
				post_list: []
			};
		}, 
		methods: {
			openpost() {
				this.$router.push('postbook');
			},
			modifyList() {
				let tmp = this.post_list;
				this.post_list = [];
                
				for(let i=0; i<tmp.length; i++){
					if(tmp[i].category == 3){
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