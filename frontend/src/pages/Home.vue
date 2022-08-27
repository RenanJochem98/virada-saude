<template>
    <q-page>
        <div class="text-center text-h4 text-weight-bold q-ma-lg text-uppercase">
            Sua agenda
        </div>
        <!-- <div style="max-width: 800px; width: 100%;"> -->
        <div class="q-mx-xl q-mt-md shadow-5">
            <MonthCalendar />
        </div> 
    </q-page>
</template>
<script>
import { defineComponent } from "vue";
import MonthCalendar from 'components/MonthCalendar.vue'

export default defineComponent({
  name: "Home",
  components: { MonthCalendar}, 
  beforeMount () {
  },
  data: () => {
    return {
    };
  },
  computed: {
  },
  methods: {
    async BuscarTreinos() {
      
    }
  }
});
</script>
