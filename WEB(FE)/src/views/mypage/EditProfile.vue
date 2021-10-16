<template>
	<div id="out-box">
		<section id="in-box">
			<img class="profileImg" src="../../assets/profile-tmp.png" />
			<div id="profile-information">
				<p>
					<label for="nickname">닉네임 </label><input type="text" id="nickname" v-model="nickname"/>
				</p>
				<p>
					<label for="intro" class="intro-label">소개글 </label><textarea id="intro" v-model="userintro" rows="4"/>
				</p>
				<p>
					<label for="pw">비밀번호 </label><input type="password" id="pw" />
				</p>
				<p>
					<label for="pw-confirm">비밀번호 확인 </label><input type="password" id="pw-confirm" />
				</p>
				<p>
					<label for="usernum">군번 </label><input type="text" id="usernum" v-model="usernum" readonly maxlength="50"/>
				</p>
				<div><button>수정</button></div>
			</div>
		</section>
	</div>
</template>

<script>

	export default {
		// components: { },
		data() {
			return {
				nickname: "", 
				userintro: "Nice to meet you!",
				password: '', 
				usernum: '20-76060000'
			};
		},
		mounted() {
			this.getNickname();
		},
		methods: {
			getNickname() {
				this.nickname = this.$store.getters.getNickname;
			}
		},
	}
</script>

<style scope>
	#out-box{ display: flex;}
	#in-box{
		display: flex;
		position: relative;
		top: 150px;
		/* width: 42.5rem;  */
		margin: 0 auto;
	}
	#in-box .profileImg{ width: 8.75rem; height: 8.75rem; margin-right: 10px;}
	#in-box #profile-information {
		display: grid;
		text-align: end;
	}
	#profile-information input, textarea {
		width: 300px;
		margin: 4px 0 4px 16px;
		border: 1px solid #C4C4C4;
		border-radius: 2px;
	}
	#profile-information #intro{
		resize: none;
	}
	#profile-information .intro-label{
		position: relative;
		top: -84px;
	}
	#profile-information button {
		border: 1px solid #A3A3A3;
		border-radius: 4px;
		color: gray;
	}
	#profile-information button:active {
		opacity: .8;
	}
	/* #in-box #profile-information {float: left;} */
</style>