<template>
	<section>
		<router-link to="/postmunhak" class="content">
			<div>
				<div id="title">{{ munhakTitle }}</div>
			<div class="maintext-box">{{ mainText }}</div></div>
			<div class="date-box">{{ contentDate }}</div>
	</router-link>
	</section>
</template>

<script>
	export default {
		data() {
			return {
				munhakTitle: "작은 것들을 위한 시",
				mainText: "불러 위하여 그들의 같이, 들어 따뜻한 유소년에게서 만물은 피가 것이다. 별과 청춘에서만 끓는 능히 간에 착목한는 구하기 피다. 피가 꾸며 커다란 몸이 있으며, 행복스럽고 때까지 교향악이다. 피어나기 예수는 인생에 미묘한 천자만홍이 때문이다. 따뜻한 별과 풍부하게 몸이 열락의 그러므로 이것이다. 행복스럽고 노년에게서 귀는 구하지 미인을 뛰노는 자신과 눈에 찬미를 운다. 청춘의 이상은 그들의 없으면, 물방아 대한 기쁘며, 간에 있다. 할지라도 투명하되 밝은 뛰노는 품으며, 풍부하게 약동하다. 가슴이 가슴에 주는 풀밭에 철환하였는가? 심장의 품에 투명하되 목숨이 말이다. 그들은 있는 새 있을 불러 이상 것이 교향악이다.",
				contentDate: "2021.10.06"
			};
		}
	}
</script>

<style scoped>
	.content {
		display: block;
		width: 42.5rem;
		border: 1px solid rgba(196, 196, 196, 0.8);
		border-radius: 5px;
		padding: 0.6rem 0.8rem 0.5rem;
		margin: 0 auto 0.5rem;
		background-color: rgba(196, 196, 196, 0.3);
		color: black !important;
	}
	.content:active {
		opacity: 0.8;
	}
	.content #title {
		font-size: 1.125rem;
		margin-bottom: 0.5rem;
	}
	.content .maintext-box {
		display: -webkit-box;
		-webkit-line-clamp: 7; /*줄 넘어가면 잘라주는 웹킷*/
		-webkit-box-orient: vertical; /*줄 넘어가면 잘라주는 웹킷*/
		overflow: hidden;
	}
	.content .date-box {
		text-align: right;
    font-size: 0.875rem;
		margin-top: 0.25rem;
	}
</style>