<template>
  <div class="search">
    <div class="img"><img :src=imgsrc></div>

    <br>
    <div class="bar">
      <input type="text"
             v-model="keyWord" />
      <div class="sel-btn">
        <button class="btn"
                @click="searchFun">{{msg}}
        </button>
        <select v-model="selected">
          <option v-for="search in search_data"
                  :value="search.index">{{search.name}}</option>
        </select>
      </div>
    </div>
  </div>
</template>
<script>
export default {
  data () {
    return {
      imgsrc: require('../assets/baidu_logo.png'),
      keyWord: '',
      selected: '0',
      msg: '百度一下',
      search_data: [
        {
          'index': 0,
          'name': 'daibu',
          'msg': '百度一下',
          'url': 'https://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=0&rsv_idx=1&tn=baidu&wd=',
          'img': require('../assets/baidu_logo.png') // 引入图片，如果是在js中，必须require进来
        },
        {
          'index': 1,
          'name': 'sogou',
          'msg': '搜狗搜索',
          'url': 'https://www.sogou.com/web?query=',
          'img': require('../assets/sougou_logo.png')
        },
        {
          'index': 2,
          'name': '360',
          'msg': '360搜索',
          'url': 'https://www.so.com/s?ie=utf-8&shb=1&src=360sou_newhome&q=',
          'img': require('../assets/360_logo.png')
        }
      ]
    }
  },
  watch: {
    selected (val, old) {
      console.log(val, old)
      this.imgsrc = this.search_data[val]['img']
      this.msg = this.search_data[val]['msg']
    },
    keyWord (val) {
      this.keyWord = val
    }
  },
  beforeCreate () {
  },
  methods: {
    searchFun () {
      // window.open('https://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=0&rsv_idx=1&tn=baidu&wd=' + '123')
      window.open(this.search_data[this.selected]['url'] + this.keyWord)
    },
    select () {
      console.log(this)
    }
  }
}
</script>
<style scoped>
.img {
  width: 970px;
  height: 300px;
  margin: 0 auto;
  position: relative;
  /* border: 1px solid; */
}

.img img {
  position: absolute;
  top: 50%;
  /* transform: translate(-50%, -50%); */
  transform: translate(120%, 100%);
  /* -webkit-transform: translate(100%, 100%); */
  text-align: center;
  /* border: 1px solid; */
}

.bar {
  width: 660px;
  height: 35px;
  /*border: 1px solid;*/
  margin: 0 auto;
}

.bar input {
  width: 490px;
  height: 31px;
  float: left;
  border: 1px solid #b8b8b8;
  border-right: 0;
  font-size: 14px;
}

.sel-btn {
  width: 160px;
  height: 35px;
  float: left;
}

.bar select {
  appearance: none;
  -moz-appearance: none;
  -webkit-appearance: none;
  width: 60px;
  height: 35px;
  float: right;
  border: 1px solid #3988fb;
  background: url("/static/img/select.png") no-repeat scroll right center #fff;
  background-size: 20px 20px;
  color: #3988fb;
  padding: 0 0 0 5px;
  border-radius: 0;
  outline: 0 none !important;
  blr: expression(this.onFocus=this.blur());
}

.bar button {
  width: 100px;
  height: 35px;
  float: right;
  border: 0;
  background: #3988fb;
  color: #fff;
  font-weight: bold;
  font-size: 14px;
  outline: 0 none !important;
  blr: expression(this.onFocus=this.blur());
}
</style>
