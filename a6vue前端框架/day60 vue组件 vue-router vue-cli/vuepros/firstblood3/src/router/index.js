import Vue from 'vue'

import Router from 'vue-router'
// 抛出了VueRouter对象，现在是引入VueRouter对象起名字为Router

import Home from '@/components/Home'
// @代指的是src路径
// 引入了Home.vue文件中通过export default 抛出的对象

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      component: Home
    },
  {
      path: '/home',
      component: Home
    }
  ]
})

