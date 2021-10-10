import { createStore } from 'vuex'

const store = createStore({
	state() {
		return {
			Mypagebtn: 1
		}
	}, 
	mutations: {
		changeBtn(state, n) {
			state.Mypagebtn = n;
		}
	}
})

export default store;