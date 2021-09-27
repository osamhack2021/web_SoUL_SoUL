module.exports = {
	publicPath: '',
	devServer: {
		// host: '0.0.0.0',
		// hot: true,
		disableHostCheck: true
	},
	chainWebpack: config => {
		config.plugins.delete('prefetch'); //prefetch 삭제
	}
}