<!--eslint-disable-->
<template>
  <div id="app">
    <nav/>
    <router-view/>
  </div>
</template>

<script>
/* eslint-disable */
  import { bus } from "@/main";
  import Nav from "./components/Nav";
  export default {
    name: 'App',
    components: {Nav},
    data() {
      return {
        dataForChildren: null
      }
    },
    async mounted() {
      await bus.$on('clearDataForChildren', () => {this.dataForChildren = null})
    }
  };
</script>

<style>

</style>
