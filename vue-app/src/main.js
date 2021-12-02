import Vue from 'vue'
import App from './App.vue'
import './registerServiceWorker'
import router from './router'
import store from './store'
import i18n from './i18n'

import vuetify from '@/plugins/vuetify';
import "@/plugins/vuetify-money.js";

import { VueMaskDirective } from 'v-mask'
Vue.directive('mask', VueMaskDirective);


Vue.config.productionTip = false;

new Vue({
  router,
  store,
  vuetify,
  i18n,
  render: h => h(App)
}).$mount('#app')
