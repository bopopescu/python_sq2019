<template>
  <div class="user">
    <p>Msp Interface Page</p>
    <p>getAppVersionConfig: </p>
    <p>{{ AppVersionConfig }}</p>
    <button @click="getAppVersionConfig">Get AppVersionConfig</button>
    <p>getdcs_msp-web: </p>
    <p>{{ getdcs_mspweb }}</p>
    <button @click="getdcsWeb">Get dcs_mspweb</button>
    <p>getdcs_mspserver: </p>
    <p>{{ getdcs_mspserver }}</p>
    <button @click="getdcsMspserver">Get dcs_mspserver</button>
  </div>

</template>

<script>
// import axios from 'axios'

export default {
  data () {
    return {
      AppVersionConfig: '',
      getdcs_mspweb: '',
      getdcs_mspserver: ''
    }
  },
  methods: {
    getAppVersionConfig () {
      const path = '/msp_interface/newWechat/apply/getAppVersionConfig'
      // this.$axios.get(this.BASE_API + path)
      this.$axios.get(this.BaseUrl + path)
        .then(response => {
          this.AppVersionConfig = response.data
        })
        .catch(error => {
          console.log(error)
        })
    },
    getdcsWeb () {
      const path = '/msp_interface/dcs/msp-web'
      // this.$axios.get(this.BASE_API + path)
      this.$axios.get(this.BaseUrl + path)
        .then(response => {
          this.getdcs_mspweb = response.data
        })
        .catch(error => {
          console.log(error)
        })
    },
    getdcsMspserver () {
      const path = '/msp_interface/dcs/mspserver'
      // this.$axios.get(this.BASE_API + path)
      this.$axios.get(this.BaseUrl + path)
        .then(response => {
          this.getdcs_mspserver = response.data
        })
        .catch(error => {
          console.log(error)
        })
    }
  }
}
</script>
