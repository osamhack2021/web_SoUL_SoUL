<template>
	<div>
		<section id="content-box">
			<div id="in-header"><div class="title">{{ Title }}</div><div class="nickname">{{ Nickname }}</div></div>
			<p>{{ mainText }}</p>
			<div class="date-box">{{ contentDate }}</div>
		</section>
	</div>
</template>

<script>
	
	export default {
		data() {
			return {
				Title: "노인과 바다", 
				Nickname: "김동규",
				mainText: "이 청춘 굳세게 시들어 피에 하였으며, 뜨거운지라, 철환하였는가? 얼마나 이는 원질이 있는 곳이 피는 생의 힘차게 이것이다. 위하여, 무엇을 쓸쓸한 피에 이상의 방황하여도, 만천하의 이상의 있다. 무엇을 평화스러운 인생을 아니한 꽃 열매를 힘차게 있으랴? 보내는 얼음과 것은 구하지 품에 길을 살았으며, 봄바람이다.<br><br>청춘은 기관과 날카로우나 평화스러운 수 우는 봄바람이다. 풀밭에 사람은 날카로우나 긴지라 방황하여도, 청춘의 천하를 이상이 운다. 우리의 이것이야말로 청춘 이성은 밝은 전인 낙원을 없으면, 할지니, 이것이다. 우리 인간은 그들은 얼음에 것이다. 뛰노는 불러 찾아다녀도, 더운지라 뼈 피고 봄날의 아름다우냐?<br><br>황금시대를 내려온 끝에 위하여서 같은 가는 교향악이다. 바로 평화스러운 싶이 긴지라 가는 별과 수 주며, 아름다우냐? 가진 속에서 현저하게 발휘하기 끓는다. 설레는 이상의 같이, 품었기 뜨고, 위하여서, 충분히 약동하다. 그것은 사라지지 바로 방황하였으며, 듣는다. 봄바람을 붙잡아 것이 날카로우나 불어 열락의 품고 사랑의 것이다.",
				contentDate: "2021.10.05"
			};
		}
	}
</script>

<style scoped>
	#content-box {
		margin: 0 auto 26px;
		padding: 0 1rem;
		width: 42.5rem;
		background: rgba(196,196,196,0.2);
		border: 1px solid rgba(196,196,196,0.4);
		border-radius: 4px; 
	}
	#content-box p { margin: 0; }
	#content-box #in-header {
		display: grid;
		align-items: center;
		margin: 0.5rem 0;
	}
	#content-box #in-header .title { font-size: 1.25rem; margin: 0 auto; }
	#content-box #in-header .nickname { font-size: 1rem; text-align: right;}
	#content-box .date-box {
		text-align: right;
		font-size: 0.875rem;
		padding-bottom: 0.5rem;
	}
</style>