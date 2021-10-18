const target = 'https://soul-bojmb.run.goorm.io'
// const cors = require('cors');

// let corsOption = {
//     origin: 'https://front-back.run.goorm.io/',    //허락하는 요청 주소
//     credentials: true    //true로 하면 설정한 내용을 response 헤더에 추가 해줍니다.
// }
// app.use(cors(corsOption));

module.exports = {
	publicPath: '',
	devServer: {
		port: 8080,
		disableHostCheck: true,
        proxy: {
            '^/': {
                target,
                changeOrigin: true
            }
        }
	},
	chainWebpack: config => {
		config.plugins.delete('prefetch'); //prefetch 삭제
	},
	// dev: {
	// 	proxyTable: {
	// 		'/api': {
	// 			target: 'http://0.0.0.0:3000/api',
	// 			changeOrigin: true,
	// 			pathRewrite: {
	// 				'^/api': ''
	// 			}
	// 		}
	// 	}
	// },
}