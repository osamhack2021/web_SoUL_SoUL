import { createStore } from "vuex";

export default createStore({
	state() {
		return{
			_user: {
				id: 'admin',
				pw: 1234,
				nickname: "Hampeyong",
			},
			islogin: 0,
			mypageBtn: 1, 
			Question: ''
		}
	},
	getters: {
		getUser(state) {
			return state._user;
		},
		getInitial(state) {
			return state._user.nickname[0];
		},
		getNickname(state) {
			return state._user.nickname;
		}, 
		getQuestion(state) {
			return state.Question;
		}
	},
	mutations: {
		selectedMyBtn(state, btn) {
			state.mypageBtn = btn;
		},
		dologin(state) {
			state.islogin = 1;
		}
	}
});