import axios from 'axios'

export default {
	methods: {
		async $api(url, data) {
			return (await axios({
				methods: 'post',
				url,
				data
			}).catch(e => {
				console.log(e);
			})).data;
		}
	}
}