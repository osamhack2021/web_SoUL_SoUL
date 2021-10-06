<template>
	<div id="main-container">
		<div id="inner">
			<img id="logo" src="../assets/logo.png" alt="logo">
			<router-link to="/login" id="login-button">로그인</router-link>
			<section class="tmp">추천 컨텐츠 글</section>
		</div>
	</div>
</template>

<script>
	//카카오톡 서비스로 로그인 및 회원가입 기능 구현
</script>

<style scoped>
	/* #main-container {
		display: flex;
		justify-content: center;
	} */
	#main-contaniner {		
		position: relative;
		top: 7.5rem;
	}
	#main-container #inner {
		display: flex;
		width: 1200px;
		/* height: 2000px; */
		justify-content: flex-start;
		flex-direction: column;
		align-items: center;
		padding: 110px;
		margin: 0 auto;
		/* border: 1px solid; */
	}
	#inner #logo {
		width: 353px;
		height: 176px;
	}
	#inner #login-button {
		width: 8.75rem;
		height: 2.75rem;
		box-sizing: content;
		border: 1px solid #F9E000;
		border-radius: 0.25rem;
		background: #F9E000;
		margin: 2.5rem 0 15rem 0;
		
		font-size: 1.5rem;
		color: black;
		text-decoration: none;
		text-align: center;
		line-height: 2.75rem;
	}
	#inner #login-button:visited {
		color: black;
	}
	#inner #login-button:active {
		opacity: 0.8;
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
