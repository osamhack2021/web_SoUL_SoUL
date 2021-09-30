<template>
	<div id="main-contaniner">
		<Header />
		<section id="profile-box">
			<img src="../assets/profile-tmp.png" />
			<div id="profile-information">
				<p class="name">{{ username }}</p>
				<p class="intro">{{ userintro }}</p>
	</div>
			<button id="profile-edit">프로필 수정</button>
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
	#profile-box {
		position: relative;
		width: 680px;
		display: flex;
		top: 120px;
		border: 1px solid;
		margin: 0 auto;
	}
	#profile-box #profile-information {
		margin-left: 50px;
	}
	#profile-box #profile-information .name {
		font-size: 2.25em;
		margin: 5px 0;
	}
	#profile-box #profile-information .intro {
		font-size: 1.25em;
		margin: 0;
	}
	#profile-box #profile-edit {
		border: 1px solid gray;
		width: 100px;
		height: 30px;
		background: #fff;
	}
</style>