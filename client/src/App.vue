<template>
  <div id="app">
    <nav class="navbar navbar-light navbar-expand">
      <router-link to="/" class="navbar-brand">Chef Daddy</router-link>
      <ul class="navbar-nav ml-auto">
        <li class="nav-item" v-if="$route.name=='Register'">
          <router-link to="Login" class="nav-link">Login</router-link>
        </li>
        <li class="nav-item" v-if="$route.name=='Login'">
          <router-link to="Register" class="nav-link">Register</router-link>
        </li>
        <li class="nav-item" v-if="isLoggedIn">
          <a href="#" class="nav-link" @click="logout">Logout</a>
        </li>
      </ul>
    </nav>
    <div class="container-fluid">
      <router-view></router-view>
    </div>
  </div>
</template>

<script>
export default {
  name: 'app',
  computed: {
    isLoggedIn() {
      return this.$store.getters.isLoggedIn
    }
  },
  methods: {
    logout() {
      this.$store.dispatch('logout')
      .then(response => {
        this.$router.push('/login')
      })
      .catch(error => {
        console.log(error)
      })
    }
  }
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
}
</style>
