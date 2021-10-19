<template>
	<div>
		<div id="main-contaniner">
			<section id="post-box">
				<div class="sonagi-date-box">{{ post.created_at }}</div>
				<div class="nickname">{{ post.nickName }}</div>
				<div class="maintext-box">{{ post.content }}</div>
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
				post: {}
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
		color: gray;
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
		display: grid;
		padding: 1rem;
		border: 2px solid #C4C4C4;
		border-radius: 4px;
	}
	#post-box .sonagi-date-box {
		margin: 0 auto;
		border-bottom: 2px solid #C4C4C4; border-right: 0; border-left: 0; border-top: 0;
		text-align: center;
		font-size: 1.5rem !important;
		width: auto;
	}
	#post-box .nickname {
		text-align: right;
	}
	#post-box .maintext-box {
		padding-top: 0.5rem;
		padding-bottom: 0.5rem;
	}
</style>
