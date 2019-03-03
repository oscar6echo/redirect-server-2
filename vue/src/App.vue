<template>
  <div id="my-app">
    <Home />
  </div>
</template>

<script>
import Home from './components/Home.vue';

export default {
  name: 'app',
  components: {
    Home
  }
};
</script>

<style>
@import url('https://fonts.googleapis.com/css?family=Roboto');

html,
body {
  font-family: 'Roboto', sans-serif;
}

#my-app {
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  font-family: 'Roboto', sans-serif;
  /* text-align: center; */
}
</style>
