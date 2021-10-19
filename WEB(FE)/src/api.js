import axios from 'axios'

export default {
	methods: {
		async $getAPI(url) {
			return (await axios({
				methods: 'GET',
				url,
			})
				.then(response => {
					return response.data;
				})
				.catch(e => {
				console.log("Failed", e);
			}))
		},
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