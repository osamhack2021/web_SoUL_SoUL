<template>
	<div id="main-container">
		<header>
			<img src="../assets/logo2.png" alt="" width="150">
			<div id="header-selectIcon">
				<a class="headerIcon" href="#"><img src="../assets/home1.png" alt="home" width="27"></a>
				<a class="headerIcon" href="#"><img src="../assets/follower1.png" alt="home" width="27"></a>
				<a class="headerIcon" href="#"><img src="../assets/bookmark1.png" alt="home" width="27"></a>
				<a id="profileIcon" href="#">H</a>
				<a class="headerIcon" href="#"><img src="../assets/edit1.png" alt="home" width="27"></a>
		</div>
		</header>
	</div>
</template>

<script>
	export default {
		name: 'header',
		data() {
			return {
				username: 'H'
			};
		}
	}
</script>	

<style>
	header {
		position: relative;
		height: 100px;
		left: 11%;
	}
	header > img {
		position: absolute;
		top: 18.455px;
	}
	#header-selectIcon {
		position: absolute;
		left: 750px;
		top: 34.5px;
		height: 40px;
	}
	#header-selectIcon a:not(#profileIcon) {
		display: inline-block;
		margin: 0 7.5px;
		width: 27px;
		height: 27px;
	}
	#profileIcon {
		display: inline-block;
		position: relative;
		color: black;
		text-decoration: none;
		top: 5px;
		
		box-sizing: border-box;
		border: 1.5px solid black;
		border-radius: 50%;
		
		font-size: 20px;
		font-weight: bold;
		text-align: center;
		/* line-height: 30px; */
		
		width: 30px;
		height: 30px;

	}
</style>
