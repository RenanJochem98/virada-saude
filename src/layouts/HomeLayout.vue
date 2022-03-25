<template>
  <q-layout view="hHh Lpr lFf">
    <q-header elevated class="custom-header">
      <q-toolbar>
        <q-btn
          flat
          dense
          round
          icon="menu"
          aria-label="Menu"
          @click="toggleLeftDrawer"
        />
        <q-toolbar-title> Virada Saúde </q-toolbar-title>
      </q-toolbar>
    </q-header>

    <q-drawer v-model="leftDrawerOpen" show-if-above>
      <q-scroll-area class="fit">
          <q-list>

            <template v-for="(menuItem, index) in menuList" :key="index">
              <q-item clickable :active="menuItem.label === 'Calendário'" v-ripple>
                <q-item-section avatar>
                  <q-icon :name="menuItem.icon" />
                </q-item-section>
                <q-item-section>
                  {{ menuItem.label }}
                </q-item-section>
              </q-item>
              <q-separator :key="'sep' + index"  v-if="menuItem.separator" />
            </template>

          </q-list>
      </q-scroll-area>
    </q-drawer>

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

const menuList = [
  {
    icon: 'calendar_month',
    label: 'Calendário',
    separator: true
  },
  {
    icon: 'fitness_center',
    label: 'Próximo Treino',
    separator: false
  },
  {
    icon: 'quiz',
    label: 'Sua avaliação sobre o último treino',
    separator: false
  },
  {
    icon: 'analytics',
    label: 'Desempenho',
    separator: true
  },
  {
    icon: 'account_circle',
    label: 'Dados Pessoais',
    separator: false
  },
  {
    icon: 'settings',
    label: 'Alterar Dias de Treino',
    separator: false
  }
]

export default defineComponent({
  name: "HomeLayout",
  data: () => {
    return {
      menuList,
      leftDrawerOpen: ref(false)
    }
    
  },
  methods: {
    toggleLeftDrawer() {
      this.leftDrawerOpen = !this.leftDrawerOpen;
    }
  }
});
</script>
