<template>
    <q-page>
        <div class="text-center text-h4 text-weight-bold q-ma-lg text-uppercase">
            Sua agenda
        </div>
        <!-- <div style="max-width: 800px; width: 100%;"> -->
        <div class="q-mx-xl q-mt-md shadow-5">
            <!-- <MonthCalendar :events="eventos"/> -->
            <div>
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
                    <!-- <div>{{timestamp.date}}</div> -->
                      <template
                          v-for="event in eventosMapeados[timestamp.date]"
                          :key="event.id"
                          >
                          <div :class="badgeClasses(event, 'day')"
                              :style="badgeStyles(event, 'day')"
                              class="my-event">
                              <div class="title q-calendar__ellipsis">
                                  {{ event.title + (event.time ? ' - ' + event.time : '') }}
                                  <q-tooltip>{{ event.details }}</q-tooltip>
                              </div>
                          </div>
                      </template>
                  </template>
              </q-calendar-month>
          </div>
        </div> 
    </q-page>
</template>
<script>
import { defineComponent } from "vue";
// import MonthCalendar from 'components/MonthCalendar.vue'
// import { TempoDisponivelController } from '../services/controllers/TempoDisponivelController'
import { TreinoController } from '../services/controllers/TreinoController'
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
  components: { QCalendarMonth/*MonthCalendar*/}, 
  beforeMount () {
    this.BuscarTreinos()
  },
  data: () => {
    return {
      selectedDate: "",
      events: [],
      eventosMapeados: []
    };
  },
  
  methods: {
    async BuscarTreinos() {
      const idUsuario = this.$store.getters['user/getIdUser']
      // const tempos = await TempoDisponivelController.BuscarTempoDisponivel({id_usuario: idUsuario})
      const proximoTreino = await TreinoController.BuscarProximoTreino(idUsuario)
      
      if(proximoTreino.status) {
            this.$q.notify({
                type: 'negative',
                message: proximoTreino.mensagem
            })
      }
      else {
        const [year,month, day] = proximoTreino.dataExecucaoPrevista.split('-')
        const dataPrevista = new Date(year, month-1, day)
        const hoje = new Date()
        let resultado = {
              id: proximoTreino.idTreino,
              title: 'Treino: '+proximoTreino.idTreino,
              details: dataPrevista < hoje ? 'Próximo Treino (Atrasado)' :'Próximo Treino',
              date: dataPrevista,
              time: '06:00',
              bgcolor: dataPrevista < hoje ? 'orange' : 'blue'
              // duration: proximoTreino.periodoDisponivel
          }
        this.events.push(resultado)
      }

      const treinosExecutados = await TreinoController.BuscarTreinosExecutados(idUsuario)

      if(treinosExecutados.status) {
            this.$q.notify({
                type: 'negative',
                message: treinosExecutados.mensagem
            })
      }
      else {
        
        treinosExecutados.forEach(element => {
          let [year,month, day] = [null, null, null]
          let detelhesTreino = ""
          let cor = ""
          if(element.dataExecucao != null){
            [year,month, day] = element.dataExecucao.split('-')
            detelhesTreino = "Treino já executado"
            cor = "green"
          }else{
            [year,month, day] = element.dataExecucaoPrevista.split('-')
            detelhesTreino = "Treino cancelado"
            cor = "red"
          }
          
          let dataExecucao = new Date(year, month-1, day)
          
          this.events.push({
              id: element.idTreino,
              title: 'Treino: '+element.idTreino,
              details: detelhesTreino,
              date: dataExecucao,
              time: '06:00',
              bgcolor: cor
              // duration: element.periodoDisponivel
          })
        })        
      }
      
      this.eventosMapeados = this.eventsMap()
    },
    eventsMap () {
      // this.definirCorBadge()
      const map = {}
      let eventKey = ''
      if (this.events.length > 0) {
        this.events.forEach(event => {
          let month = event.date.getMonth()+1;
          let day = event.date.getDate();
          eventKey = event.date.getFullYear() + '-'+(month < 10 ? '0' : '') + month+'-'+ (day < 10 ? '0' : '') + day;
          // console.log(event.date.toString())
          (map[ eventKey ] = (map[ eventKey ] || [])).push(event);
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
      return map
    },
    definirCorBadge() {
      this.events.forEach(element => {
        element.bgcolor = element.date < CURRENT_DAY ? "red" : 
          element.date.toDateString() == CURRENT_DAY.toDateString() ? "green" : "blue"
      })
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
    //#region Calendar events
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
    },
    //#endregion
  }
});
</script>
