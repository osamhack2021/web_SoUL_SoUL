<template>
<div>
	<Header />
	<div id="main-contaniner">
		<section id="writing-box">
			<input type="text" id="date-box" :value="Today"/>
			<textarea id="maintext-box" v-model="textValue" cols="88" rows="25" autofocus></textarea>
		</section>
		<section id="writing-box-footer">
			<div id="public-checkbox" class="form-check form-switch">
				<input class="form-check-input" type="checkbox" id="public">
				<label class="form-check-label" for="public">공개 여부</label>
			</div>
			<button class="button-submit" :disabled="textValue == ''">작성완료</button>
	</section>
	</div>
	</div>
</template>

<script>
	import Header from '../components/Header'
	import dayjs from "dayjs"
	
	export default {
		components: {Header, },
		data() {
			return {
				Today: dayjs().format("YYYY-MM-DD"),
				textValue: "",
			};
		}
		// computed: {
		// 	user() {
		// 		return this.$store.state.user;
		// 	}
		// }
	}
</script>

<style>
	#main-contaniner { display: grid; margin: 8.125rem 0 0;	grid-column-gap: 10px; }
	#writing-box {
		display: grid;
		top: 20px;
		width: 42.5rem;
		border: 2px solid #C4C4C4;
		margin: 0 auto;
	}
	#writing-box input:focus, textarea:focus { outline:none; }
	#writing-box #date-box {
		margin: 10px auto 10px;;
		border-bottom: 2px solid #C4C4C4; border-right: 0; border-left: 0; border-top: 0;
		text-align: center;
	}
	#writing-box #maintext-box {
		margin: 0 auto;
		border: none;
		resize: none;
	}
	#main-contaniner #public-checkbox {
		margin: 5px 0 0;
	}
	#main-contaniner #writing-box-footer {
		justify-content: space-between;
		width: 42.5rem;
		margin: 0 auto;
	}
	#public-checkbox-box #public:focus, #public:active {outline: none !important; box-shadow: none;}
	#writing-box-footer .button-submit {
		display: block;
		border: 0.0625rem solid #0D6EFD;
		border-radius: 5px;
		background: #0D6EFD;
		color: #FFF;
		font-size: 1.5rem;
		margin: 5px auto;
		width: 9.375rem;
		height: 3.5rem;
	}
	#writing-box-footer .button-submit:disabled {
		border-color: #C4C4C4;
		background: #C4C4C4;
	}
	#writing-box-footer button:active { opacity: 0.5; border: 0.0625rem solid #AFAFAF;}
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
</style>
