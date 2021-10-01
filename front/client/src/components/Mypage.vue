<template>
	<div id="main-contaniner">
		<Header />
		<div id="in-contaniner">
			<section id="profile-box">
				<img class="iconsize" src="../assets/profile-tmp.png" />
				<div id="profile-information">
					<p class="name">{{ username }}</p>
					<p class="intro">{{ userintro }}</p>
				</div>
				<div id="edit-button" class="button-default"><a class="fontCenter" href="#">프로필 수정</a></div>
			</section>
			<div id="mycontents">
				<section id="content-box"></section>
			</div>
		</div>
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
	#in-contaniner {
		position: relative;
		top: 7.5rem;
	}
	#profile-box a:link, a:visited, a:hover { color: #AFAFAF; text-decoration: none;}
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
	#profile-box #edit-button {
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
		height: 33.125em;
		border: 1px solid;
		margin: 1.5em auto 0;
	}
	.button-default {
		position: relative;
		box-sizing: border-box;
		border: 0.0625rem solid #AFAFAF;
		background: #fff;
	}
	.fontCenter {
		display: block;
		text-align: center;
	}
</style>