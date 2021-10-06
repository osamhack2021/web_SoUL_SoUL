<template>
	<div>
		<div id="main-contaniner">
			<h2>{{ Question }}</h2>
			<section id="writing-box">
				<textarea id="maintext-box" v-model="textValue" cols="85" rows="15" autofocus placeholder="본문" />
				<div id="date-box">{{Today}}</div>
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
	import dayjs from "dayjs"
	
	export default {
		// components: {Header, },
		data() {
			return {
				Today: dayjs().format("YYYY-MM-DD"),
				textValue: "",
				Question: "가장 기억에 남는 순간은?"
			};
		}
		// computed: {
		// 	user() {
		// 		return this.$store.state.user;
		// 	}
		// }
	}
</script>

<style scoped>
	#main-contaniner > h2 {
		text-align: center;
		border-bottom: 2px solid #C4C4C4;
		margin: 20px auto 56px;
		width: 40rem;
		padding-bottom: 10px;
	}
</style>
 