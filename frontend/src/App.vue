<template>
  <!-- <transition name="fade" mode="out-in"> -->
  <router-view></router-view>
  <!-- </transition> -->
</template>

<script>
  export default {
    name: "App",
  };
</script>

<style lang="scss">
  @import url("https://fonts.googleapis.com/css?family=Baloo+Da+2&display=swap");

  .v-application {
    font-family: "Baloo Da 2" !important;
  }

  // View Transition Animations
  .fade-enter-active,
  .fade-leave-active {
    transition-duration: 0.07s;
    transition-property: opacity;
    transition-timing-function: ease-in-out;
  }
  .fade-enter,
  .fade-leave-active {
    opacity: 0;
  }
</style>
