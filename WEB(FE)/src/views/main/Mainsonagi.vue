<template>
	<div id="mainouter">
		<button @click="openpost()" :key="i" v-for="(content, i) in contentList">
			<section id="content-box">
				<div id="in-header"><span class="date">{{ content.contentDate }}</span><span class="nickname">{{ content.Nickname }}</span></div>
				<p class="maintext-box">{{ content.mainText }}</p>
			</section>
		</button>
	</div>
</template>

<script>
	
	export default {
		data() {
			return {
				contentList: [
					{ contentDate: "2021.10.04", Nickname: "김동규",mainText: "설레는 그들을 충분히 것은 희망의 보라. 부패를 얼마나 천자만홍이 대중을 그들은 이것이야말로 뛰노는 그리하였는가? 갑 할지니, 밝은 이상의 시들어 칼이다. 고행을 되려니와, 것은 가치를 부패를 방황하였으며, 되는 그리하였는가? 피고 귀는 청춘을 천하를 수 창공에 물방아 군영과 희망의 위하여서. 보내는 못할 무엇이 대한 들어 천지는 쓸쓸하랴? 그들의 열락의 군영과 그들의 위하여 그들은 더운지라 인류의 끓는 운다. 보이는 우는 그들의 꽃이 영락과 있는 찾아다녀도, 것이다. 가슴에 가치를 것이 것이다. 꽃 황금시대를 것은 커다란 무엇을 있는 없으면, 우리 얼마나 것이다. 불어 만천하의 물방아 못할 우리 이성은 이것은 사랑의 때문이다." },
					{ contentDate: "2021.10.04", Nickname: "김동규",mainText: "설레는 그들을 충분히 것은 희망의 보라. 부패를 얼마나 천자만홍이 대중을 그들은 이것이야말로 뛰노는 그리하였는가? 갑 할지니, 밝은 이상의 시들어 칼이다. 고행을 되려니와, 것은 가치를 부패를 방황하였으며, 되는 그리하였는가? 피고 귀는 청춘을 천하를 수 창공에 물방아 군영과 희망의 위하여서. 보내는 못할 무엇이 대한 들어 천지는 쓸쓸하랴? 그들의 열락의 군영과 그들의 위하여 그들은 더운지라 인류의 끓는 운다. 보이는 우는 그들의 꽃이 영락과 있는 찾아다녀도, 것이다. 가슴에 가치를 것이 것이다. 꽃 황금시대를 것은 커다란 무엇을 있는 없으면, 우리 얼마나 것이다. 불어 만천하의 물방아 못할 우리 이성은 이것은 사랑의 때문이다." },
					{ contentDate: "2021.10.04", Nickname: "김동규",mainText: "설레는 그들을 충분히 것은 희망의 보라. 부패를 얼마나 천자만홍이 대중을 그들은 이것이야말로 뛰노는 그리하였는가? 갑 할지니, 밝은 이상의 시들어 칼이다. 고행을 되려니와, 것은 가치를 부패를 방황하였으며, 되는 그리하였는가? 피고 귀는 청춘을 천하를 수 창공에 물방아 군영과 희망의 위하여서. 보내는 못할 무엇이 대한 들어 천지는 쓸쓸하랴? 그들의 열락의 군영과 그들의 위하여 그들은 더운지라 인류의 끓는 운다. 보이는 우는 그들의 꽃이 영락과 있는 찾아다녀도, 것이다. 가슴에 가치를 것이 것이다. 꽃 황금시대를 것은 커다란 무엇을 있는 없으면, 우리 얼마나 것이다. 불어 만천하의 물방아 못할 우리 이성은 이것은 사랑의 때문이다." },
					{ contentDate: "2021.10.04", Nickname: "김동규",mainText: "설레는 그들을 충분히 것은 희망의 보라. 부패를 얼마나 천자만홍이 대중을 그들은 이것이야말로 뛰노는 그리하였는가? 갑 할지니, 밝은 이상의 시들어 칼이다. 고행을 되려니와, 것은 가치를 부패를 방황하였으며, 되는 그리하였는가? 피고 귀는 청춘을 천하를 수 창공에 물방아 군영과 희망의 위하여서. 보내는 못할 무엇이 대한 들어 천지는 쓸쓸하랴? 그들의 열락의 군영과 그들의 위하여 그들은 더운지라 인류의 끓는 운다. 보이는 우는 그들의 꽃이 영락과 있는 찾아다녀도, 것이다. 가슴에 가치를 것이 것이다. 꽃 황금시대를 것은 커다란 무엇을 있는 없으면, 우리 얼마나 것이다. 불어 만천하의 물방아 못할 우리 이성은 이것은 사랑의 때문이다." },
					
				]};
		},
		methods: {
			openpost() {
				this.$router.push('postsonagi');
			}
		}
	}
</script>

<style>
	#mainouter button {
		margin: 0 auto 16px;
		border: none;
		background: none;
		text-align: initial;
	}
	#mainouter button:active {
		opacity: 0.8;
		/* border: 1px solid rgba(196,196,196,0.4); */
		outline: none;
	}
	#mainouter button:focus {
		outline: none;
	}
</style>

<style scoped>
	#content-box {
		/* margin: 0 auto 26px; */
		padding: 0 1rem;
		width: 42.5rem;
		border: 1px solid rgba(196,196,196,0.2);
		border-radius: 4px; 
		/* box-shadow: 1px 1px 1px 1px 0.8px; */
    background: rgba(196,196,196,0.2);
	}
	#content-box p { margin-bottom: 0.7rem; }
	#content-box #in-header {
		display: flex;
		justify-content: space-between;
		align-items: center;
		margin: 0.5rem 0;
	}
	#content-box #in-header .date { font-size: 1.25rem; }
	#content-box #in-header .nickname { font-size: 1rem; }
	#content-box .maintext-box {
		display: -webkit-box;
		-webkit-line-clamp: 7; /*줄 넘어가면 잘라주는 웹킷*/
		-webkit-box-orient: vertical; /*줄 넘어가면 잘라주는 웹킷*/
		overflow: hidden;
	}
</style>