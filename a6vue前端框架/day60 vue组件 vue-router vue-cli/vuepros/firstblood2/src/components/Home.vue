<template>
  <div class="hello">
    <h1>xxx</h1>
    <h1>{{ msg }}</h1>
  </div>
</template>

<script>
export default {
  // name: 'Home', //组件名称
  data () {
    return {
      msg: '停车坐爱枫林晚'
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
  h1{
    color: red;
  }
</style>

<!--// C:\Users\Administrator\Desktop\ubuntu_gx\python32\a6vue前端框架\day60 vue组件 vue-router vue-cli\vue03\07 vuerouter简单使用2.html-->
<!--//这个vue-cli是将上述一个html文件中的内容分成5个文件来存放-->
