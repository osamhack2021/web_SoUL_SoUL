<template>
<div>
	<Header />
	<div id="main-contaniner">
		<section id="writing-box">
			<textarea id="maintext-box" cols="88" rows="28" autofocus></textarea>
			<p>{{Today}}</p>
		</section>
		<section id="writing-box-footer">
			<div id="public-checkbox-box" class="form-check form-switch">
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
	#writing-box #maintext-box {
		margin: 0 auto;
		border: none;
		resize: none;
	}
	#writing-box p {
		font-size: 0.5rem;
		}
		#main-contaniner #public-checkbox {
		/* width: 100px; */
		height: 1.25rem;
		margin: 5px 0 0;
	}
	#main-contaniner #writing-box-footer {
		display: flex;
		justify-content: space-between;
		width: 42.5rem;
		margin: 0 auto;
	}
	#public-checkbox-box #public:focus, #public:active {outline: none !important; box-shadow: none;}
	.button-submit {
		border: 0.0625rem solid #AFAFAF;
		border-radius: 5px;
		background: #AFAFAF;
		color: #FFF;
		margin: 5px 0 0;
	}
	#writing-box-footer button:active { opacity: 0.5; border: 0.0625rem solid #AFAFAF;
	}
</style>
