<template>
	<div id="mainouter">
		<button @click="openpost()" :key="i" v-for="(content, i) in contentList">
			<section id="content-box">
				<div id="in-header"><span class="date">{{ content.created_at }}</span><span class="nickname">{{ content.author }}</span></div>
				<p class="maintext-box">{{ content.content }}</p>
			</section>
		</button>
	</div>
</template>

<script>
	import axios from "axios";
    // axios.defaults.baseURL = 'http://soul-bojmb.run.goorm.io/'; //서버주소
    // axios.defaults.headers.post['Content-Type'] = 'application/json;charset=utf-8';
    // axios.defaults.headers.post['Access-Control-Allow-Origin'] = '*';
    
    let url = "https://soul-bojmb.run.goorm.io"
    
	export default {
		data() {
			return {
				contentList: []
            };
		},
        mounted() {
            axios({
                method: "GET", 
                url: url
            })
            .then(response => {
                this.contentList = response.data;
            })
            .catch(response => {
                console.log("Failed", response);
            });
        },
		methods: {
			openpost() {
				this.$router.push('postsonagi');
			},
            getContentList: function() {},
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