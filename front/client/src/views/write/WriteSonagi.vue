<template>
	<div>
		<!-- <Header /> -->
		<div id="main-contaniner">
			<section id="writing-box">
				<input type="text" id="sonagi-date-box" :value="Today"/>
				<textarea id="maintext-box" v-model="textValue" cols="85" rows="25" autofocus placeholder="본문" />
			</section>
			<section id="writing-box-footer">
				<div id="public-checkbox" class="form-check form-switch">
					<input class="form-check-input" type="checkbox" id="public">
					<label class="form-check-label" for="public">공개 여부</label>
				</div>
				<button id="button-submit" :disabled="textValue == ''">업로드</button>
			</section>
		</div>
	</div>
</template>

<script>
	// import Header from '../components/Header'
	import dayjs from "dayjs"
	
	export default {
		// components: {Header, },
		data() {
			return {
				Today: dayjs().format("YYYY.MM.DD"),
				textValue: "",
			};
		}, 
		methods: {
			resize(obj) {
				obj.style.height = "1px";
				obj.style.height = (12 + obj.scrollHeight) + "px";
			}
	}
		// computed: {
		// 	user() {
		// 		return this.$store.state.user;
		// 	}
		// }
	}
</script>

<style>
	#button-submit {
		box-shadow: 0 1px 1px black;
	}
	#button-submit:active {
		outline: none;
		transform: translateY(2px);
		box-shadow: none;
	}
	#button-submit:focus {
		outline: none;
	}
</style>
<style scoped>	
	#writing-box #sonagi-date-box {
		margin: 10px auto 10px;
		border-bottom: 2px solid #C4C4C4; border-right: 0; border-left: 0; border-top: 0;
		text-align: center;
		font-size: 1.5rem !important;
		width: auto;
	}
</style>
