import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
// import axios from 'axios';

// Vue.prototype.$http = axios;
// Vue.config.productionTip = false;

createApp(App).use(router).mount('#app')
// new Vue({
//   el: '#app',
//   render : h => h (App),
//   router
// });
