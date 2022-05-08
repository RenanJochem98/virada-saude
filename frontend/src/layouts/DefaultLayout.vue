<template>
  <q-layout view="lHh Lpr lFf">
    <q-header elevated class="custom-header">
      <q-toolbar>
        <q-toolbar-title> Virada Saúde </q-toolbar-title>
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

export default defineComponent({
  name: "DefaultLayout"
});
</script>
