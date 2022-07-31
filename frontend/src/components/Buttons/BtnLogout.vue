<template>
  <q-btn
    flat
    dense
    icon="logout"
    @click="logout"
  />
</template>
<script>
export default {
  name: 'BtnLogout',
  methods: {
    logout () {
      this.$store.dispatch('login/ActionLogout')
      this.$router.push('/')
    }
  }
}
</script>
