<template>
  <div id="vue_det">
    <h2>site : {{site}}</h2>
    <h1>url : {{url}}</h1>
    <h1>alexa : {{alexa}}</h1>
    <h1 style="color:#00FF00">{{details()}}</h1>
  </div>
</template>

<script type="text/javascript">
export default {
  // data: function () {
  //   return {
  //     site: '菜鸟教程',
  //     url: 'www.runoob.com',
  //     alexa: '10000'
  //   }
  // },
  data () {
    return {
      site: '菜鸟教程',
      url: 'www.runoob.com',
      alexa: '10001'
    }
  },
  methods: {
    details: function () {
      return this.site + ' - 学的不仅是技术，更是梦想！'
    }
  }
}
</script>
