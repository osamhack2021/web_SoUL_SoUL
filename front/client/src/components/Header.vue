<template>
	<section id="main-container">
		<header id="header">
			<section class="inner">
			<a href="#"><img src="../assets/logo2.png" alt="" width="150"></a>
			<div id="right-icon">
				<a href="#"><img src="../assets/home1.png" alt="home" width="27"></a>
				<a href="#"><img src="../assets/follower1.png" alt="home" width="27"></a>
				<a href="#"><img src="../assets/bookmark1.png" alt="home" width="27"></a>
				<a id="profileIcon" href="#">H</a>
				<a href="#"><img src="../assets/edit1.png" alt="home" width="27"></a>
	</div>
	</section>
	</header>
	</section>
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
	#header {
		position: absolute;
		width: 100%;
		left: 0;
		top: 0;
		z-index: 999;
		border-bottom: 1px solid;
	}
	#header .inner {
		width: 675px;
		height: 100px;
		margin: 0 auto;
		display: flex;
		justify-content: space-between;
		align-items: center;
	}
	#header #right-icon {
		width: 190px;
		display: flex;
		justify-content: space-between;
		align-items: center;
	}
	#header #right-icon #profileIcon{
		display: inline-block;
		border: 1.5px solid;
		border-radius: 50%;
		color: black;
		text-decoration: none;
		width: 33px;
		height: 33px;
		text-align: center;
		font-size: 19px;
	}
</style>
