<template>
	<div id="main-contaniner">
		<Header />
		<section id="profile-box">
			<img class="iconsize" src="../assets/profile-tmp.png" />
			<div id="profile-information">
				<p class="name">{{ username }}</p>
				<p class="intro">{{ userintro }}</p>
			</div>
			<div id="edit-button" class="button-default"><a class="fontCenter" href="#">프로필 수정</a></div>
		</section>
		<section id="mycontents">
<!-- 	컨텐츠 버튼 구현하기		 -->
		</section>
	</div>
</template>

<script>

	import Header from './Header'

	export default {
		components: {Header, },
		data() {
			return {
				username: "Dongu", 
				userintro: "Nice to meet you!",
			};
		}
		// computed: {
		// 	user() {
		// 		return this.$store.state.user;
		// 	}
		// }
	}
</script>

<style>
	a:link, a:visited, a:hover { color: #AFAFAF; text-decoration: none;}
	a:active { text-decoration:none; opacity: 0.5;}
	#profile-box {
		position: relative;
		width: 42.5rem;
		display: flex;
		top: 7.5rem;
		border: 1px solid;
		margin: 0 auto;
	}
	#profile-box #profile-information {
		margin-left: 3.125rem;
	}
	#profile-box #profile-information .name {
		font-size: 2.25rem;
		margin: 0.3125rem 0;
	}
	#profile-box #profile-information .intro {
		font-size: 1.25rem;
		margin: 0;
	}
	#profile-box #edit-button {
		border-radius: 5px;
		width: 6.25rem;
		height: 1.875rem;
		margin-left: auto;
		top: 0.375rem;
		right: 0.375rem;
		line-height: 1.75rem;

	}
	#profile-box .iconsize{
		width: 8.75rem;
	}
	.button-default{
		position: relative;
		box-sizing: border-box;
		border: 0.0625rem solid #AFAFAF;
		background: #fff;
	}
	.fontCenter {
		display: block;
		text-align: center;
	}
/* 로고 박스 반응형으로 만들기 */
</style>