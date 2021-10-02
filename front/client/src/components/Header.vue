<template>
	<header id="header">
		<section class="inner">
			<a href="#"><img id="logosize" src="../assets/logo2.png" alt=""></a>
			<div id="right-icon">
				<a href="#"><img src="../assets/home1.png" alt="home" class="iconsize iconbox"></a>
				<a href="#"><img src="../assets/follower1.png" alt="follower" class="iconsize iconbox"></a>
				<a href="#"><img src="../assets/bookmark1.png" alt="bookmark" class="iconsize iconbox"></a>
				<a id="profileIcon" href="#" class="iconbox">H</a>
				<!-- <a href="#"><img src="../assets/write1.png"	alt="home" class="iconsize"></a> -->
				<div class="dropdown">
					<a class="btn" href="#" role="button" id="writecontent" data-bs-toggle="dropdown" aria-expanded="false">
						<img src="../assets/write1.png"	alt="write" class="iconsize"></a>
					<ul class="dropdown-menu dropdown-menu-end" aria-labelledby="writecontent">
						<li><a class="dropdown-item" href="#">소나기</a></li>
						<li><a class="dropdown-item" href="#">발자국</a></li>
						<li><a class="dropdown-item" href="#">독후감</a></li>
						<li><a class="dropdown-item" href="#">문학</a></li>
						</ul>
				</div>
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
	#header .inner a:active {	opacity: 0.5;}
	#header .inner #logosize{	width: 9.375em;	}
	#header #right-icon {
		/* width: 11.875rem; */
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
		margin: 6px;
	}
	#header #right-icon .iconsize{ width: 1.75em;	}
	#header #right-icon .iconbox{	margin: 6px; }
	#header #right-icon #writecontent{ padding: 6px; }
	.dropdown-item:active {	background-color: #C4C4C4; }
	.btn:focus,.btn:active {outline: none !important; box-shadow: none;}
	.dropdown-menu {min-width: fit-content;}
	.dropdown-item {text-align: center;}
</style>