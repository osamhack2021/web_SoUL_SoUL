<template>
	<div id="footer">
		<p class="developer-intro">소개 | 블로그 | 도움말 | 개인정보처리방침 | 개발자소개</p>
		<div id="copyright-box">
			<div class="tmp"><span>아이콘 저작권</span><span><button @click="isShowCopyright = !isShowCopyright" class="dropdown-toggle"></button></span></div>
			<ul v-if="isShowCopyright">
				<li><div>Follows, Bookmark, Munhak Icons made by <a href="https://www.freepik.com(https://www.freepik.com/)" title="Freepik">Freepik</a> from <a href="[https://www.flaticon.com/](https://www.flaticon.com/)" title="Flaticon">[www.flaticon.com](http://www.flaticon.com/)</a></div></li>
				<li><div>Home Icons made by <a href="https://www.flaticon.com/authors/pixel-perfect" title="Pixel perfect">Pixel perfect</a> from <a href="https://www.flaticon.com/" title="Flaticon">www.flaticon.com</a></div></li>
				<li><div>Write Icons made by <a href="https://www.flaticon.com/authors/becris(https://www.flaticon.com/authors/becris)" title="Becris">Becris</a> from <a href="[https://www.flaticon.com/](https://www.flaticon.com/)" title="Flaticon">[www.flaticon.com](http://www.flaticon.com/)</a></div></li>
				<li><div>Sonagi Icons made by <a href="https://www.flaticon.com/authors/catalin-fertu" title="Catalin Fertu">Catalin Fertu</a> from <a href="https://www.flaticon.com/" title="Flaticon">www.flaticon.com</a></div></li>
				<li><div>Book Icons made by <a href="http://catalinfertu.com" title="Catalin Fertu">Catalin Fertu</a> from <a href="https://www.flaticon.com/" title="Flaticon">www.flaticon.com</a></div></li>
				<li><div>Footprint Icons made by <a href="https://www.flaticon.com/authors/vitaly-gorbachev" title="Vitaly Gorbachev">Vitaly Gorbachev</a> from <a href="https://www.flaticon.com/" title="Flaticon">www.flaticon.com</a></div></li>
			</ul>
		</div>
	</div>
</template>

<script>
	export default {
		data() {
			return {
				isShowCopyright: "false"
			};
		},
	}
</script>

<style scoped>
	#footer {
		display: grid;
		bottom: 0;
		text-align: center;
		width: 100%;
		margin-top: 150px;
	}
	#footer .developer-intro {
		margin: 0 auto;
		color: gray;
	}
	#footer #copyright-box{
		position: relative;
		margin: 0 auto;
		color: gray;
	}
	#footer ul li {
		list-style: none;
		font-size: 12px;
	}
	#copyright-box button {
		border: none;
		background: none;
		margin: .5rem;
		color: gray;
	}
	/* .tmp{
		position: relative;
		
	} */
</style>