/* eslint-disable */
import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'
import Vue from 'vue';
import App from './App';
import router from './router';
import { BootstrapVue, IconsPlugin } from 'bootstrap-vue'
import VueFuse from 'vue-fuse'

Vue.use(VueFuse)

Vue.use(BootstrapVue)

Vue.use(IconsPlugin)

Vue.config.productionTip = false;

export const bus = new Vue();

/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  components: { App },
  template: '<App/>',
});
