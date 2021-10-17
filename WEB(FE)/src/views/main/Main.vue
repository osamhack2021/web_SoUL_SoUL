<template>
	<div>
		<section id="main-inner">
			<div id="sidebar-box">
				<router-link to="/sonagi"><img class="iconsize" @click="selected = [1, 0, 0, 0]" :src="imgsrc[0][selected[0]]" alt="sonagi"/></router-link>
				<router-link to="/questions"><img class="iconsize" @click="selected = [0, 1, 0, 0]" :src="imgsrc[1][selected[1]]" alt="footprint" /></router-link>
				<router-link to="/book"><img class="iconsize" @click="selected = [0, 0, 1, 0]" :src="imgsrc[2][selected[2]]" alt="book"/></router-link>
				<router-link to="/munhak"><img class="iconsize" @click="selected = [0, 0, 0, 1]" :src="imgsrc[3][selected[3]]" alt="munhak"/></router-link>
			</div>
			<div id="contents-box">
				<router-view></router-view>
			</div>
		</section>
	</div>
</template>

<script>
	export default {
		data() {
			return {
				selected : [],
				imgsrc : [
				[require("../../assets/rain1.png"), require("../../assets/rain2.png")],
					[require("../../assets/footprint1.png"), require("../../assets/footprint2.png")],
						[require("../../assets/book1.png"), require("../../assets/book2.png")],
						[require("../../assets/munhak1.png"), require("../../assets/munhak2.png")]
				]
			};
		},
		methods: {
			getMainbtn() {
				this.selected = this.$store.getters.getMainbtn;
			},
			storeMainbtn() {
				this.$store.commit('storeMainbtn', this.selected);
			}
		},
		created() {
			this.getMainbtn();
		}, 
		beforeUnmount() {
			this.storeMainbtn();
		}
	}
</script>

<style scoped>
	#main-inner {
		position: relative;
		display: flex;
		top: 8rem;
		width: 900px;
		margin: 0 auto;
	}
	#main-inner #sidebar-box .iconsize {
		width: 45px;
		height: 45px;
	}
	a:active {
		opacity: 0.5;
	}
	#main-inner #sidebar-box {
		position: fixed;
		display: flex;
		margin: -10px 24px 0;
		flex-direction: column;
	}
	#sidebar-box a:first-child {
		margin-top: 0.25rem;
	}
	#sidebar-box a {
		color: black;
		text-decoration: none;
		margin-bottom: 1.5rem;
		font-size: 20px;
		font-weight: bold;
		text-align: center;
	}
	#sidebar-box a:visited{
		color: black;
	}
	#main-inner #contents-box {
		width: 43.75rem;
		margin: 0 auto;
		justify-content: center;
		align-items: center;
	}
</style>
 