<template>
  <!--  // template 就相当于html-->
  <div class="home">
    深圳的天气是： {{msg}}
  </div>
</template>

<script>
    export default {
        name: "Home",
        data() {
            return {
                msg: '',
            }
        },
        created() {
            //this指的是vue对象
            this.$axios.get('http://wthrcdn.etouch.cn/weather_mini?city=深圳')
                .then((res) => {
                    this.msg = res.data.data.ganmao
                    //箭头函数 这里的this指的是当前对象的父级-vue对象
                })
        }
    }
</script>

<style scoped>

</style>
