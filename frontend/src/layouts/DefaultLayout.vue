<template>
  <q-layout view="lHh Lpr lFf">
    <q-header elevated class="custom-header">
      <q-toolbar>
        <q-toolbar-title> Virada Saúde </q-toolbar-title>
        <BtnLogout />
      </q-toolbar>
    </q-header>

    <q-page-container>
      <router-view />
    </q-page-container>
  </q-layout>
</template>
<style lang="scss">
  .custom-header {
    background-color: $default
  }
</style>

<script>

import { defineComponent, ref } from "vue";
import BtnLogout from 'src/components/Buttons/BtnLogout.vue'
export default defineComponent({
  name: "DefaultLayout",
  components: { BtnLogout }
});
</script>
