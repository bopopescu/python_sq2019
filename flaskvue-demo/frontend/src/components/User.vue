<template>
  <div class="user">
    <p>User page</p>
    <p>Users: {{ userList }}</p>
    <button @click="getIdcsList">Get Users</button>
  </div>

</template>

<script>
// import axios from 'axios'

export default {
  data () {
    return {
      userList: 0
    }
  },
  methods: {
    getIdcsList () {
      const path = '/user/users'
      // this.$axios.get(this.BASE_API + path)
      this.$axios.get(this.BaseUrl + path)
        .then(response => {
          this.userList = response.data
        })
        .catch(error => {
          console.log(error)
        })
    }
  }
}
</script>
