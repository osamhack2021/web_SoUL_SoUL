<template>
	<div class="outline">
		<div class="login">
			<img class="comm__title" src="../assets/logo.png" width="360"/>
			<div class="ipt__box">
					<input type="text" class="ipt" placeholder="ID" v-model="user.id">
			</div>
			<div class="ipt__box">
				<input type="password" class="ipt" placeholder="Password" v-model="user.password" @keyup.enter="login()">
			</div>
			<div class="btn__box">
				<div class="ipt__btn">
					<a href="#" class="btn btn--confirm btn--large" v-on:click="false">SIGN UP</a>
				</div>
				<div class="ipt__btn">
					<a href="#" class="btn btn--confirm btn--large" v-on:click="login()">LOGIN</a>
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
                    password : ''
                }
            }
        },
        methods : {
            login : function () {
                if (this.user.id == '') {alert('아이디를 입력해주세요.');return;}
                if (this.user.password == '') {alert('비밀번호를 입력해주세요.');return;}
                this.$http.post('/api/login', {user:this.user}).then((response) => {
                    if (response.data.success == true) {
                        alert(response.data.message);
                        this.$router.push('/list'); //로그인 성공시 list 페이지로 이동
                    } else {
                        alert(response.data.message);
                    }
                });
            }
        },
        created () {
        }
    }
</script>

<style scoped>
	.login {
		display: grid;
		position: absolute;
		top: 50%;
		left: 50%;
		transform: translate(-50%,-105%);
		justify-items: center;
	}
	.login .comm__title {
		margin-bottom: 2rem;
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
	}
	.btn--large {
		width: 130px;
	}
</style>