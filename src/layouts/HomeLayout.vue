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

    <q-drawer v-model="leftDrawerOpen" show-if-above class="bg-grey-4">
      <q-scroll-area class="fit">
          <q-list>

            <template v-for="(menuItem, index) in menuList" :key="index">
              <q-item clickable v-ripple 
                :active="this.$route.name == menuItem.nameLink" 
                :disable="menuItem.nameLink == ''" 
                @click="showNotImplemented(menuItem.nameLink, menuItem.label)"
              >
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
import { Notify } from 'quasar'

const menuList = [
  {
    icon: 'calendar_month',
    label: 'Calendário',
    separator: false,
    nameLink: "Home",
    active: true
  },
  {
    icon: 'fitness_center',
    label: 'Próximo Treino',
    separator: true,
    nameLink: 'ProximoTreino',
    active: false
  },
  {
    icon: 'quiz',
    label: 'Sua avaliação sobre o último treino',
    separator: false,
    nameLink: '',
    active: false
  },
  {
    icon: 'analytics',
    label: 'Desempenho',
    separator: true,
    nameLink: '',
    active: false
  },
  {
    icon: 'account_circle',
    label: 'Dados Pessoais',
    separator: false,
    nameLink: '',
    active: false
  },
  {
    icon: 'settings',
    label: 'Alterar Dias de Treino',
    separator: false,
    nameLink: '',
    active: false
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
    },
    showNotImplemented (nameLink, label) {
      if (nameLink == '') {
         Notify.create({
          type: 'negative',
          message: 'A ação para "'+label+'" ainda não foi implementada.'
        })
      }else{
        this.$router.push( {name: nameLink})
      }
    }
  }
});
</script>
