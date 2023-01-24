<template>
  <router-view />
</template>
<script>
import { defineComponent } from "vue";

export default defineComponent({
  name: "App",
  beforeMount(){
    this.teste()
  },
  methods: {
    teste() {
      console.log(process.env.URL_API)
      console.log(process.env.URLA_API)
      console.log(process.env)
    }
  }
});
</script>
