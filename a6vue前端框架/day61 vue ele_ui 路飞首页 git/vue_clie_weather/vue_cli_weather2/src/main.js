// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import router from './router'

// import axios from "axios"
import axios from 'axios'
// 在node-models引入进来的直接写包名，不用加路径
Vue.prototype.$axios = axios //原型链
//将axios封装到Vue对象中，
// 只要封装到这个对象中的方法和属性，
// 其他组件中都可以直接通过组件对象来调用

Vue.config.productionTip = false

/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  components: { App },
  template: '<App/>'
})
