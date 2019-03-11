<!-- 展示模板 -->
<template>
  <div id="app">
    <!-- <img src="./assets/logo.png"> -->
    <!-- <img src="./assets/jklogo.jpeg"> -->
    <!-- <hello></hello> -->
    <!-- 路由匹配到的组件将显示在这里 -->
    <router-view />
  </div>
</template>

<script>
// 导入组件
import Hello from './components/Hello'

export default {
  name: 'App',
  components: {
    Hello
  }
}
</script>

<!-- 样式代码 -->
<style>
/* #app {
  font-family: "Avenir", Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
} */
html,
body,
#app {
  height: 100%;
  width: 100%;
  margin: 0;
  padding: 0;
  /* font-family: "Avenir", Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px; */
}
</style>
