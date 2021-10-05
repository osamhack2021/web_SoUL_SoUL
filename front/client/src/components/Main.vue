<template>
	<div>
		<section id="main-inner">
			<div id="sidebar-box">
				<router-link to="/sonagi">소나기</router-link>
				<router-link to="/footprint">발자국</router-link>
				<router-link to="/book">독후감</router-link>
				<router-link to="/munhak">문학</router-link>
			</div>
			<div id="contents-box">
				<router-view></router-view>
			</div>
		</section>
	</div>
</template>

<script>
	// import Header from "../components/Header.vue"
	
	export default {
		// components: {Header },
		// computed: {
		// 	user() {
		// 		return this.$store.state.user;
		// 	}
		// }
	}
</script>

<style scoped>
	a:active {
		opacity: 0.5;
	}
	#main-inner {
		position: relative;
		display: flex;
		top: 7.5rem;
		width: 900px;
		margin: 0 auto;
	}
	#main-inner #sidebar-box {
		position: absolute;
		display: flex;
		margin: 1rem 0 0;
		/* width: 50px; */
		/* height:100px; */
		flex-direction: column;
		/* width: 48.75rem;
		margin: 0 auto;
		border: 1px solid red; */
	}
	#sidebar-box a:first-child {
		margin-top: 0.25rem;
	}
	#sidebar-box a {
		color: black;
		text-decoration: none;
		margin-bottom: 1.5rem;
		/* border: 2px solid #C4C4C4;
		border-radius: 10px; */
		font-size: 20px;
		font-weight: bold;
		text-align: center;
	}
	#sidebar-box a:visited{
		color: black;
	}
	#main-inner #contents-box {
		/* position: absolute; */
		/* border: 1px solid; */
		width: 43.75rem;
		height: 1700px;
		
		margin: 0 auto;
		justify-content: center;
		align-items: center;
	}
</style>
 