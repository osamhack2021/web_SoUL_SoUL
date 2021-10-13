<template>
<div>
	<header id="header">
		<section class="inner">
			<button @click="toHome" id="logo"><img src="../assets/logo2.png" alt=""></button>
			<div id="right-icon">
				<router-link to="/sonagi"><img @click="selected = [1, 0, 0, 0]" :src="imgsrc[0][selected[0]]" alt="home" class="iconsize iconbox"></router-link>
				<a href="#"><img @click="selected = [0, 1, 0, 0]" :src="imgsrc[1][selected[1]]" alt="follower" class="iconsize iconbox"></a>
				<a href="#"><img @click="selected = [0, 0, 1, 0]" :src="imgsrc[2][selected[2]]" alt="bookmark" class="iconsize iconbox"></a>
				<router-link @click="selected = [0, 0, 0, 0]" to="/mypage/sonagi" id="profileIcon" class="iconbox">{{ userinitial }}</router-link>
				<div class="dropdown">
					<button @click="selected = [0, 0, 0, 0]" class="btn" type="button" id="writecontent" data-bs-toggle="dropdown" aria-expanded="false"></button>
					<ul class="dropdown-menu dropdown-menu-end" aria-labelledby="writecontent">
						<router-link class="dropdown-item" to="/writesonagi">소나기</router-link>
						<router-link class="dropdown-item" to="/writefootprint">발자국</router-link>
						<router-link class="dropdown-item" to="/writebook">독후감</router-link>
						<router-link class="dropdown-item" to="/writemunhak">문학</router-link>
						</ul>
				</div>
			</div>
		</section>
	</header>
</div>
</template>

<script>
	// import Home from '../views/Home.vue'
	// import Mypage from '../components/Mypage.vue'
	export default {
		// components: {Home, Mypage},
		name: 'header',
		data() {
			return {
				userinitial: '',
				selected : [1, 0, 0, 0],
				isshow: true,
				imgsrc : [
					[require("../assets/home1.png"), require("../assets/home2.png")],
						[require("../assets/follower1.png"), require("../assets/follower2.png")],
							[require("../assets/bookmark1.png"), require("../assets/bookmark2.png")],
							[require("../assets/write1.png"), require("../assets/write2.png")]
				]
			};
		},
		methods: {
			toHome() {
				let islogin = this.$store.state.islogin;
				if(islogin) {console.log("login O"); this.$router.replace('/sonagi'); this.selected = [1, 0, 0, 0];}
				else {console.log("login X"); this.$router.replace('home');}
			},
			getInitial() {
				this.userinitial = this.$store.getters.getInitial;
			},
		}, 
		created() {
			this.getInitial();
		}
	}
</script>	

<style>
	#main-contaniner {position: relative;	top: 7.5rem;}
	#main-contaniner textarea {margin-left: 0.5rem; margin-right: 0.5rem;}
	#writing-box {
		display: grid;
		top: 20px;
		width: 42.5rem;
		border: 2px solid #C4C4C4;
		margin: 0 auto;
	}
	input:focus, textarea:focus { outline:none;}
	#writing-box textarea.autosize { min-height: 50px; }
	#writing-box #maintext-box {
		border: none;
		resize: none;
		/* overflow-y: hidden; */
	}
	#main-contaniner #writing-box-footer {
		width: 42.5rem;
		margin: 0 auto;
	}
	#writing-box-footer #public-checkbox {
		margin: 5px 0 0;
	}
	#writing-box-footer #public-checkbox #public:focus, #public:active {outline: none !important; box-shadow: none !important; border-color: #C4C4C4; fill: #C4C4C4}
	#writing-box-footer #public-checkbox .form-check-input:checked{background-color: #C4C4C4; border-color: #C4C4C4;}
	#writing-box-footer #public-checkbox .form-check-input:focus{
		background-image: url("data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' viewBox='-4 -4 8 8'%3e%3ccircle r='3' fill='rgba%280, 0, 0, 0.25%29'/%3e%3c/svg%3e");
	}
	#writing-box-footer #button-submit {
		display: block;
		border: 0.125rem solid #C4C4C4;
		border-radius: 5px;
		background: #C4C4C4;
		color: #FFF;
		font-size: 1.5rem;
		margin: 5px auto;
		width: 9.375rem;
		height: 3.5rem;
	}
	#writing-box-footer #button-submit:disabled {
		background: #FFFFFF;
		color: #C4C4C4;
	}
	#writing-box-footer #button:active { opacity: 0.5; border: 0.0625rem solid #AFAFAF;}
	.form-switch .form-check-input {
		vertical-align: middle;
    width: 3em;
    height: 1.5em;
		margin-top: 1.5px;
	}
	.form-switch .form-check-label {
		font-size: 1.15rem;
		margin: 0 0 0 0.5rem;
	}
	#date-box {
		font-size: 0.875rem;
		width: auto;
		margin: 0;
		padding-right: 0.8rem;
		padding-bottom: 0.5rem;
		text-align: right;
		color: #C4C4C4;
	}
	.selectedbutton:active {
		background: #C4C4C4;
		color: #FFFFFF;
	}
	.selectedbutton:visited {
		background: #C4C4C4;
		color: #FFFFFF;
	}
</style>

<style scope>
	#header {
		position: fixed;
		width: 100%;
		left: 0;
		top: 0;
		z-index: 999;
		/* border-bottom: 1px solid; */
	}
	#header .inner {
		width: 42.1875rem;
		height: 6.25rem;
		margin: 0 auto;
		display: flex;
		justify-content: space-between;
		align-items: center;
	}
	#header .inner a:active {	opacity: 0.7;}
	#header .inner #logo{	border: none; background: none;}
	#header .inner #logo img{ width: 9.375rem;}
	/* #header .inner button{ outline: none;} */
	#header #right-icon {
		/* width: 11.875rem; */
		display: flex;
		justify-content: space-between;
		align-items: center;
	}
	#header #right-icon a:visited {color: black;}
	#header #right-icon #profileIcon{
		display: inline-block;
		border: 0.125rem solid black;
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
	#writecontent {
		background-image: url(../assets/write1.png);
		width: 30px;
		height: 32px;
		background-size: 29px 29px;
		background-repeat: no-repeat;
		margin: 6px;
	}
	#writecontent:focus {
		background-image: url(../assets/write2.png) !important;
	}
</style>