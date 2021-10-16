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
			questions: [
					"0",
					"1. 군생활 중 가장 아찔했던 순간은?",
					"2. 군생활 중 가장 행복했던 순간은?",
					"3. 군생활 중 가장 힘들었던 순간은?",
					"4. 군생활 중 가장 외로웠던 순간은?",
					"5. 군생활 중 가장 위기였던 순간은?",
			],
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
		getQuestions(state) {
			return state.questions;
		},
		getQuestion(state) {
			return state.Question.substring(3,);
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