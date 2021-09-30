<template>
	<header id="header">
		<section class="inner">
			<a href="#"><img src="../assets/logo2.png" alt="" width="150"></a>
			<div id="right-icon">
				<a href="#"><img src="../assets/home1.png" alt="home" class="iconsize"></a>
				<a href="#"><img src="../assets/follower1.png" alt="home" class="iconsize"></a>
				<a href="#"><img src="../assets/bookmark1.png" alt="home" class="iconsize"></a>
				<a id="profileIcon" href="#">H</a>
				<a href="#"><img src="../assets/edit1.png"	alt="home" class="iconsize"></a>
			</div>
		</section>
	</header>
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
		width: 42.1875rem;
		height: 6.25rem;
		margin: 0 auto;
		display: flex;
		justify-content: space-between;
		align-items: center;
	}
	#header #right-icon {
		width: 11.875rem;
		display: flex;
		justify-content: space-between;
		align-items: center;
	}
	#header #right-icon #profileIcon{
		display: inline-block;
		border: 0.1rem solid black;
		border-radius: 50%;
		color: black;
		text-decoration: none;
		width: 1.8125rem;
		height: 1.8125rem;
		text-align: center;
		font-size: 1rem;
		font-weight: bold;
	}
	#header #right-icon .iconsize{
		width: 1.75em;
	}
</style>
