<template>
	<div>
		<section id="content-box">
			<div id="in-header"><span class="date">{{ contentDate }}</span><span class="username">{{ username }}</span></div>
			<p>{{ mainText }}</p>
		</section>
	</div>
</template>

<script>
	
	export default {
		data() {
			return {
				contentDate: "2021.10.04", 
				username: "김동규",
				mainText: "설레는 그들을 충분히 것은 희망의 보라. 부패를 얼마나 천자만홍이 대중을 그들은 이것이야말로 뛰노는 그리하였는가? 갑 할지니, 밝은 이상의 시들어 칼이다. 고행을 되려니와, 것은 가치를 부패를 방황하였으며, 되는 그리하였는가? 피고 귀는 청춘을 천하를 수 창공에 물방아 군영과 희망의 위하여서. 보내는 못할 무엇이 대한 들어 천지는 쓸쓸하랴? 그들의 열락의 군영과 그들의 위하여 그들은 더운지라 인류의 끓는 운다. 보이는 우는 그들의 꽃이 영락과 있는 찾아다녀도, 것이다. 가슴에 가치를 것이 것이다. 꽃 황금시대를 것은 커다란 무엇을 있는 없으면, 우리 얼마나 것이다. 불어 만천하의 물방아 못할 우리 이성은 이것은 사랑의 때문이다."
			};
		}
	}
</script>

<style scoped>
	#content-box {
		margin: 4px;
		padding: 0 1rem;
		width: 42.5rem;
		border: 1px solid rgba(196,196,196,0.2);
		border-radius: 4px; 
		/* box-shadow: 1px 1px 1px 1px 0.8px; */
    background: rgba(196,196,196,0.2);
	}
	#content-box p { margin-bottom: 0.5rem; }
	#content-box #in-header {
		display: flex;
		justify-content: space-between;
		align-items: center;
		margin: 0.5rem 0;
	}
	#content-box #in-header .date { font-size: 1.375rem; }
	#content-box #in-header .username { font-size: 1rem; }
</style>