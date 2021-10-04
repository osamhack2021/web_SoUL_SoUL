<template>
	<div id="main-contaniner">
		<section id="profile-box">
			<img class="iconsize" src="../assets/profile-tmp.png" />
			<div id="profile-information">
				<p class="name">{{ username }}</p>
				<p class="intro">{{ userintro }}</p>
			</div>
			<div id="button-edit" class="button-default"><a class="fontCenter" href="#">프로필 수정</a></div>
		</section>
		<div id="mycontents">
			<div id="box-button-content">
				<!-- <a class="fontCenter" href="#" v-on:click="selectedButton(this)"></a>
				<a class="fontCenter" href="#"><span class="button-default button-content selectedbutton">발자국</span></a>
				<a class="fontCenter" href="#"><span class="button-default button-content selectedbutton">독후감</span></a>
				<a class="fontCenter" href="#"><span class="button-default button-content selectedbutton">문학</span></a> -->
				<router-link class="fontCenter" to="/mypage/sonagi"><span class="button-default button-content selectedbutton">소나기</span></router-link>
				<router-link class="fontCenter" to="/mypage/footprint"><span class="button-default button-content selectedbutton">발자국</span></router-link>
				<router-link class="fontCenter" to="/mypage/book"><span class="button-default button-content selectedbutton">독후감</span></router-link>
				<router-link class="fontCenter" to="/mypage/munhak"><span class="button-default button-content selectedbutton">문학</span></router-link>
			</div>
			<section id="content-header"></section>
			<section id="content-box"><!-- 안에 컨텐츠별 글 상자 나오게 구성-->
					<router-view></router-view>
			</section>
		</div>
	</div>
</template>

<script>

	export default {
		// components: { },
		data() {
			return {
				username: "Dongu", 
				userintro: "Nice to meet you!",
			};
		},
		methods: {
			selectedButton(obj){
				obj.style.background = "#C4C4C4";
			}
		}
		// computed: {
		// 	user() {
		// 		return this.$store.state.user;
		// 	}
		// }
	}
</script>

<style scope>
	#main-contaniner a:link, a:visited, a:hover { color: #AFAFAF; text-decoration: none;}
	#profile-box a:active { text-decoration:none; opacity: 0.5;}
	#profile-box {
		position: relative;
		width: 42.5rem;
		height: 8.75rem;
		display: flex;
		border: 1px solid;
		margin: 0 auto;
	}
	#profile-box #profile-information {
		margin-left: 3.125rem;
	}
	#profile-box .iconsize {
		width: 8.75rem;
	}
	#profile-box #profile-information .name {
		font-size: 2.25rem;
		margin: 0.3125rem 0;
	}
	#profile-box #profile-information .intro {
		font-size: 1.25rem;
		margin: 0;
	}
	#profile-box #button-edit {
		border-radius: 5px;
		width: 6.25rem;
		height: 1.875rem;
		margin-left: auto;
		top: 0.375rem;
		right: 0.375rem;
		line-height: 1.75rem;
	}
	#mycontents {
		position: relative;
		width: 42.5rem;
		border: 1px solid;
		margin: 1.5rem auto 0;
	}
	#mycontents #box-button-content {
		display: flex;
		justify-content: space-between;
	}
	#mycontents #content-header {
		position: relative;
		width: 42.5rem;
		height: 2.5rem;
		margin: 0.5rem 0;
		
		border: 1px solid;
	}
	#mycontents #content-box {
		display: flex;
		position: relative;
		width: 42.5rem;
		height: 28.125rem; /*나중에 없애기*/
		border: 1px solid;
	}
	.button-default {
		position: relative;
		box-sizing: border-box;
		border: 0.125rem solid #AFAFAF;
		background: #fff;
	}
	.fontCenter {
		display: block;
		text-align: center;
	}
	.button-content {
		display: flex;
		justify-content: center;
		align-items: center;
		width: 8.125rem;
		height: 2.5rem;
		border-radius: 10px;
		top: 0;
		right: 0;
		line-height: 2.375rem;
	}
</style>