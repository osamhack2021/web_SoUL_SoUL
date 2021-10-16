<template>
	<div class="outline">
		<div class="login">
			<img class="comm__title" src="../assets/logo1.png" width="300"/>
			<div class="ipt__box">
					<input type="text" class="ipt" placeholder="ID" v-model="user.id">
			</div>
			<div class="ipt__box">
				<input type="password" class="ipt" placeholder="Password" v-model="user.pw" @keyup.enter="login()">
			</div>
			<div class="btn__box">
				<div class="ipt__btn">
					<a href="#" id="byn--signup" class="btn  btn--large button-submit" v-on:click="test()">SIGN UP</a>
				</div>
				<div class="ipt__btn">
					<a href="#" class="btn btn--confirm btn--large button-submit" v-on:click="login()">LOGIN</a>
				</div>
			</div>
		</div>
	</div>
</template>
<script>
	export default  {
		data() {
			return {
				user : {
					id : '',
					pw : ''
				}
			}
		},
		methods : {
			login: function() {
				let _user = this.$store.getters.getUser;
				// console.log(_user.id);
				// console.log(_user.pw);
				// console.log(this.user.id);
				// console.log(this.user.pw);
				if (this.user.id == '') {alert('아이디를 입력해주세요.');return;}
				if (this.user.pw == '') {alert('비밀번호를 입력해주세요.');return;}
				if (this.user.id == _user.id && this.user.pw == _user.pw) {
					this.$store.commit('dologin');
					console.log(this.$store.state.islogin);
					this.$router.push('/sonagi');
				} else {
					alert("아이디 또는 비밀번호가 일치하지 않습니다.");
				}
			},
			test: function() {
				return 0;
			}
		},
	}
</script>

<style scoped>
	.login {
		display: grid;
		position: absolute;
		top: 50%;
		left: 50%;
		transform: translate(-50%,-95%);
		justify-items: center;
	}
	.login .comm__title {
		margin-bottom: 3rem;
	}
	.login .ipt__box {
		margin: 0.25rem;
	}
	.login .ipt {
		width: 300px;
		height: 40px;
	}
	.login .btn__box {
		display: flex;
		justify-content: space-between;
		width: 300px;
	}
	.btn {
		background-color: #C4C4C4;
		color: white;
		margin-top: 10px;
	}
	.btn :active {
		opacity: 0.8;
	}
	.btn--large {
		width: 145px;
	}
	#btn--signup {
		background-color: #C4C4C4;
	}
</style>