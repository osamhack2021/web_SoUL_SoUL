<template>
	<div id="main-container">
		<div id="inner">
			<img id="logo" src="../assets/logo.png" alt="logo">
			<button id="login">로그인</button> <!-- 로그인 버튼으로 대체  -->
			<section class="tmp">추천 컨텐츠 글</section>
		</div>
	</div>
</template>

<script>
	//카카오톡 서비스로 로그인 및 회원가입 기능 구현
</script>

<style>
	#main-container {
		display: flex;
		justify-content: center;
	}
	#main-container #inner {
		display: flex;
		width: 1200px;
		/* height: 2000px; */
		justify-content: flex-start;
		flex-direction: column;
		align-items: center;
		padding: 110px;
		
		/* border: 1px solid; */
	}
	#logo {
		position: relative;
		width: 353px;
		height: 176px;
	}
	#login {
		/* 임의로 지정한 텍스트("로그인") */
		position: relative;
		width: 143px;
		height: 46px;
		border: 1px solid #F9E000;
		background: #F9E000;
		margin: 40px 0 245px 0;
		
		font-size: 25px;
		/* align-items: center;
		text-align: center; */

	}
	.tmp {
		position: relative;
		width: 831px;
		height: 237px;
		background: gray;
		color: white;
		text-align: center;
	}
</style>
