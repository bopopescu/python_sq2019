<template>
  <div class="logo-select">
    <img :src="logoList[selectedNow].imgSrc" />
    <transition name="logofade">
      <ul class="logoList"
          v-show="logoListFlag">
        <li vi-for="(item, index) in logoList"
            :key="index">
          <img :src="logoList[index].imgSrc" />
        </li>
      </ul>
    </transition>
  </div>
</template>

<script>
export default {
  props: {
    logoList: {
      type: Object,
      default: function () {
        return ''
      }
    }
  },
  methods: {
    selectLogo () {

    }
  },
  data () {
    return {
      selectedNow: 0,
      logoListFlag: false
    }
  }
}
</script>
