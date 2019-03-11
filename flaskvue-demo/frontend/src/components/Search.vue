<template>
  <div class="search">
    <div class="mainer">
      <!-- <logo-select :logoList="logoData" @logoSelect="logoSelect"></logo-select> -->
      <div class="loading"
           v-if="isShow"
           v-text="loading">
      </div>
      <div class="img">
        <img :src=img
             alt="">
      </div>
      <div class="bar">
        <select name="select"
                id="select"
                value=""
                v-model="select">
          <option value="0">百度</option>
          <option value="1">搜狗</option>
          <option value="2">360</option>
        </select>
        <input type="text"
               v-model="keyWork"
               @keydown.enter="searchFun()" />
        <button @click="searchFun">搜一下</button>
        <br>

      </div>
      <!-- <div>
      <transition-group tag="ul">
        <li v-for="(value,index) in myData">
          {{item}}
        </li>
      </transition-group>
    </div> -->
    </div>
  </div>
</template>
<script>
import logoSelect from './logo-select'
export default {
  components: {
    logoSelect
  },
  data () {
    return {
      loadText: '正在努力加载中....',
      now: -1,
      loading: 'aloading...',
      keyWork: '',
      select: '0',
      isShow: true,
      searchIndex: 0,
      logoData: [{
        name: '百度搜索',
        imgSrc: require('../assets/baidu_logo.png'), // 引入图片，如果是在js中，必须require进来
        searchSrc: 'https://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=0&rsv_idx=1&tn=baidu&wd='
      }, {
        name: '搜狗搜索',
        imgSrc: require('../assets/sougou_logo.png'),
        searchSrc: 'https://www.sogou.com/web?query='
      }, {
        name: '360搜索',
        imgSrc: require('../assets/360_logo.png'),
        searchSrc: 'https://www.so.com/s?ie=utf-8&shb=1&src=360sou_newhome&q='
      }],
      logoIdex: 0,
      img: require('../assets/baidu_logo.png'),
      myData: []
    }
  },
  watch: {
    keyWork (val, old) {
      this.keyWork = val
      console.log('val:' + val + ';old:' + old)
    },
    select (val, old) {
      console.log('val:' + val + ';old:' + old)
      this.img = this.logoData[val].imgSrc
    }
  },
  beforeCreate () {
    this.isShow = true
  },
  methods: {
    searchFun () {
      // console.log(this.keyWork)
      window.open(this.logoData[this.select].searchSrc + this.keyWork)
    }
  },
  mounted () {
    this.isShow = false
  }
}
</script>

<style scoped>
.search {
  width: 100%;
  height: 100%;
  background: url("../assets/background01.png") no-repeat center top;
  background-size: 100%;
  padding-top: 200px;
}
/* .img img {
  width: 560px;
  height: 100px;
} */
.img {
  position: relative;
  width: 560px;
  height: 60px;
  margin: 0 auto;
  /* border: 1px solid; */
}
.img img {
  position: absolute;
  /* transform: translate(-50%, -50%); */
  transform: translate(50%, -70%);
  top: 50%;
  text-align: center;
}
.search .mainer {
  width: 610px;
  margin: auto;
}
.search .mainer input {
  width: 500px;
  height: 50px;
  display: block;
  float: left;
}
.bar {
  width: 700px;
}
.bar * {
  font-size: 16px;
}
.search .mainer button {
  width: 100px;
  height: 55px;
  border: 1px solid green;
  background-color: green;
  color: #fff;
  display: inline-block;
  float: left;
}
.loading {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: rgba(255, 255, 255, 8);
}
.bar select {
  width: 60px;
  height: 56px;
  float: left;
  appearance: none;
  -moz-appearance: none;
  -webkit-appearance: none;
  /* float: right; */
  /* border: 1px solid #3988fb; */
  color: #3988fb;
  font-weight: bold;
  padding: 0 0 0 14px; /* 填充*/
  border-radius: 0; /* 去除圆角*/
  outline: 0 none !important;
  blr: expression(this.onFocus=this.blur());
}
</style>
