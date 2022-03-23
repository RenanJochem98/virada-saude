<template>
  <q-layout view="lHh Lpr lFf">
    <!-- <q-header elevated>
      <q-toolbar>
        <q-toolbar-title> Virada Saúde </q-toolbar-title>
      </q-toolbar>
    </q-header> -->


    <q-page-container class="default-background">
      <router-view />
    </q-page-container>
  </q-layout>
</template>

<style lang="scss">
    .default-background {
        background-color: $default;
        // background: linear-gradient(160deg, rgba(2,0,36,1) 12%, rgba(1,41,95,1) 84%, rgba(29,72,106,1) 100%);
    }
</style>

<script>
import { defineComponent, ref } from "vue";

export default defineComponent({
  name: "IndexLayout"
});
</script>
