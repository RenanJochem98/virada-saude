<template>
    <q-page>
        <div class="text-center text-h4 text-weight-bold q-ma-lg text-uppercase">
            Sua agenda
        </div>
        <!-- <div style="max-width: 800px; width: 100%;"> -->
        <div class="q-mx-xl q-px-xl q-mt-md">            
            <q-calendar-month
            v-model="selectedDate"
            :day-height="60"
            :day-min-height="60"
            animated
            bordered
            date-header="stacked"
            locale="pt-BR"
            >
            <template #day="{ scope: { timestamp } }">
            <template
              v-for="event in eventsMap[timestamp.date]"
              :key="event.id"
            >
              <div
                :class="badgeClasses(event, 'day')"
                :style="badgeStyles(event, 'day')"
                class="my-event"
              >
                <div class="title q-calendar__ellipsis">
                  {{ event.title + (event.time ? ' - ' + event.time : '') }}
                  <q-tooltip>{{ event.details }}</q-tooltip>
                </div>
              </div>
            </template>
          </template>
            </q-calendar-month>
        </div>
    </q-page>
</template>
<script>
import { defineComponent } from "vue";
import {QCalendarMonth, parseDate, parseTimestamp, addToDate} from '@quasar/quasar-ui-qcalendar';


const CURRENT_DAY = new Date();

CURRENT_DAY.setMilliseconds(0)
CURRENT_DAY.setSeconds(0)
CURRENT_DAY.setMinutes(0)
CURRENT_DAY.setHours(0)

function getCurrentDay (day) {
  const newDay = new Date(CURRENT_DAY)
  newDay.setDate(day)
  const tm = parseDate(newDay)
  return tm.date
}

export default defineComponent({
  name: "Home",
  components: {QCalendarMonth}, 
  beforeMount () {
    this.montaEventosTeste()
  },
  data: () => {
    return {
        selectedDate: "",
        events: []
    };
  }
  ,computed: {
    eventsMap () {
      const map = {}
      if (this.events.length > 0) {
        this.events.forEach(event => {
          (map[ event.date ] = (map[ event.date ] || [])).push(event)
          if (event.days !== undefined) {
            let timestamp = parseTimestamp(event.date)
            let days = event.days
            // add a new event for each day
            // skip 1st one which would have been done above
            do {
              timestamp = addToDate(timestamp, { day: 1 })
              if (!map[ timestamp.date ]) {
                map[ timestamp.date ] = []
              }
              map[ timestamp.date ].push(event)
              // already accounted for 1st day
            } while (--days > 1)
          }
        })
      }
      //console.log(map)
      return map
    }
  },
  methods: {
      montaEventosTeste () {
        let dataBase = new Date()
        dataBase.setMilliseconds(0)
        dataBase.setSeconds(0)
        dataBase.setMinutes(0)
        dataBase.setHours(0)

        for(let i = 1; i < 33; i+=2){
          
          let date = getCurrentDay(i)
          dataBase.setFullYear(parseInt(date.substring(0,4), 10))
          dataBase.setMonth(parseInt(date.substring(5,7), 10) - 1)
          dataBase.setDate(parseInt(date.substring(8,10), 10))
          
          
          this.events.push({
                id: i,
                title: 'Treino teste: '+i,
                details: 'Dia de treino',
                date: date,
                bgcolor: dataBase < CURRENT_DAY ? "red" : 
                    dataBase.toDateString() == CURRENT_DAY.toDateString() ? "green" : "blue"
            })
        }
      },
       badgeClasses (event, type) {
      return {
        [ `text-white bg-${ event.bgcolor }` ]: true,
        'rounded-border': true
      }
    },

    badgeStyles (day, event) {
      const s = {}
      // s.left = day.weekday === 0 ? 0 : (day.weekday * this.parsedCellWidth) + '%'
      // s.top = 0
      // s.bottom = 0
      // s.width = (event.days * this.parsedCellWidth) + '%'
      return s
    },

    onToday () {
      this.$refs.calendar.moveToToday()
    },
    onPrev () {
      this.$refs.calendar.prev()
    },
    onNext () {
      this.$refs.calendar.next()
    },
    onMoved (data) {
      console.log('onMoved', data)
    },
    onChange (data) {
      console.log('onChange', data)
    },
    onClickDate (data) {
      console.log('onClickDate', data)
    },
    onClickDay (data) {
      console.log('onClickDay', data)
    },
    onClickWorkweek (data) {
      console.log('onClickWorkweek', data)
    },
    onClickHeadDay (data) {
      console.log('onClickHeadDay', data)
    },
    onClickHeadWorkweek (data) {
      console.log('onClickHeadWorkweek', data)
    }
  }
});
</script>
