import Vue from 'vue'
//引入vue核心模块

import Router from 'vue-router'
// 抛出了VueRouter对象，
// 现在是引入VueRouter对象,给对象起名字为Router

import Home from '@/components/Home'
// @代指的是src文件夹的路径
// 引入了Home.vue文件中通过export default 抛出的对象
//,给对象起名字为Home

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
    },
  ]
})

// C:\Users\Administrator\Desktop\ubuntu_gx\python32\a6vue前端框架\day60 vue组件 vue-router vue-cli\vue03\07 vuerouter简单使用2.html
//这个vue-cli是将上述一个html文件中的内容分成5个文件来存放
