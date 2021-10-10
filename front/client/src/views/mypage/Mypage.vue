<template>
	<div id="main-contaniner">
		<section id="profile-box">
			<img class="iconsize" src="../../assets/profile-tmp.png" />
			<div id="profile-information">
				<p class="name">{{ username }}</p>
				<p class="intro">{{ userintro }}</p>
			</div>
			<div id="button-edit" class="button-default"><a class="fontCenter" href="#" style="font-size: 14px; line-height: 26px">프로필 수정</a></div>
		</section>
		<div id="mycontents">
			<div id="box-button-content">
				<router-link class="fontCenter" to="/mypage/sonagi" @click="changeBtn(1)"><span :class="{ gray: btn == 1}" class="button-default button-content">소나기</span></router-link>
				<router-link class="fontCenter" to="/mypage/footprint" @click="changeBtn(2)"><span :class="{ gray: btn == 2}" class="button-default button-content">발자국</span></router-link>
				<router-link class="fontCenter" to="/mypage/book" @click="changeBtn(3)"><span :class="{ gray: btn == 3}" class="button-default button-content">독후감</span></router-link>
				<router-link class="fontCenter" to="/mypage/munhak" @click="changeBtn(4)"><span :class="{ gray: btn == 4}" class="button-default button-content">문학</span></router-link>
			</div>
			<section id="content-header"></section>
			<section><!-- 안에 컨텐츠별 글 상자 나오게 구성-->
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
				btn: 1
			};
		},
		methods: {
			// selectedButton(n){
			// 	if(n == 1) {
			// 		console.log(n);
			// 		this.$refs.bt1.style.backgroundColor = "#C4C4C4";
			// 	}
			// 	else if(n == 2) {
			// 		console.log(n);
			// 		this.$refs.bt2.style.backgroundColor = "#C4C4C4";
			// 	}
			// }
			changeBtn(n){
				this.btn = n;
			}
		},
		// computed: {

		// }
	}
</script>

<style scope>
	#main-contaniner a:link, a:visited, a:hover { color: gray; text-decoration: none;}
	#profile-box a:active { text-decoration:none; opacity: 0.8;}
	#profile-box {
		position: relative;
		width: 42.5rem;
		height: 8.75rem;
		display: flex;
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
		/* line-height: 1.75rem; */
	}
	#mycontents {
		position: relative;
		width: 42.5rem;
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
	.button-default {
		position: relative;
		box-sizing: border-box;
		border: 0.125rem solid #C4C4C4;
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
	.gray {
		background-color: #C4C4C4;
		color: white;
	}
</style>