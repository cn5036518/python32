// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'  //引入vue核心模块
import App from './App'  //导入App.vue组件
import router from './router' //导入路由router下的index.js

Vue.config.productionTip = false

/* eslint-disable no-new */
new Vue({
  el: '#app',  //圈地
  router,   //加载路由
  components: { App },  //加载父组件App.vue
  template: '<App/>'    //加载模板
})

// C:\Users\Administrator\Desktop\ubuntu_gx\python32\a6vue前端框架\day60 vue组件 vue-router vue-cli\vue03\07 vuerouter简单使用2.html
//这个vue-cli是将上述一个html文件中的内容分成5个文件来存放
