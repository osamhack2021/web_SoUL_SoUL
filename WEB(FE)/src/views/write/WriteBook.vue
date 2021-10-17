<template>
	<div>
		<div id="main-contaniner">
			<section id="writing-box-header">
				<input type="text" id="Title-box" :value="bookTitle" placeholder="제목"/>
				<input type="text" id="Author-box" :value="bookAuthor" placeholder="저자"/>
			</section>
			<section id="writing-box">
				<textarea id="maintext-box" v-model="textValue" cols="85" rows="24" autofocus placeholder="본문" />
				<div id="date-box">{{Today}}</div>
			</section>
			<section id="bookintro-box">
				<textarea id="bookintro" cols="85" row="4" placeholder="소개글" />
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
				bookTitle: "",
				bookAuthor: "",
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
	#main-contaniner #writing-box-header {display: grid;}
	#main-contaniner > h2 {
		text-align: center;
		border-bottom: 2px solid #C4C4C4;
		margin: 1.25rem auto 3.5rem;
		width: 40rem;
		padding-bottom: 0.625rem;
	}
	#main-contaniner #writing-box-header {
		width: 42.5rem;
		margin: 0 auto;
	}
	#main-contaniner #writing-box-header #Title-box {
		width: 42.5rem;
		margin: 0 auto;
		border: 0;
		/* border-bottom: 2px solid #C4C4C4; border-right: 0; border-left: 0; border-top: 0;/ */
		text-align: center;
		font-size: 1.75rem;
	}
	#main-contaniner #writing-box-header #Author-box {
		display: block;
		margin: 0.25rem 0.5rem;
		border: 0;
		/* border-bottom: 2px solid #C4C4C4; border-right: 0; border-left: 0; border-top: 0; */
		text-align: right;
	}
	#main-contaniner #bookintro-box {
		/* display: grid;
		top: 20px; */
		width: 42.5rem;
		border: 2px solid #C4C4C4;
		margin: 4px auto 0;
	}
	#main-contaniner #bookintro-box #bookintro {
		border: none;
		resize: none;
		/* overflow-y: hidden; */
	}
</style>
 