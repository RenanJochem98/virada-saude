<template>
    <q-page>
        <!-- <div style="max-width: 800px; width: 100%;"> -->
            <q-calendar-month
            v-model="selectedDate"
            :day-height="60"
            :day-min-height="60"
            animated
            bordered
            date-header="stacked"
            locale="pt-BR"
            />
        <!-- </div> -->
    </q-page>
</template>
<script>
import { defineComponent } from "vue";
import {QCalendarMonth} from '@quasar/quasar-ui-qcalendar';

export default defineComponent({
  name: "Home",
  components: {QCalendarMonth}, 
  data: () => {
    return {
        selectedDate: ""
    };
  }
});
</script>
