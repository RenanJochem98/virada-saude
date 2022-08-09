<template>
    <q-page padding>
        <div class="text-center text-h4 text-weight-bold q-ma-lg text-uppercase">Tempo Disponível</div>
        <!-- <q-radio :options="this.diasSemana"/> -->
        <q-select v-model="model" :options="diasSemana" label="Dia" />

        <q-input filled v-model="horaInicio" mask="time" :rules="['time']">
            <template v-slot:append>
            <q-icon name="access_time" class="cursor-pointer">
                <q-popup-proxy cover transition-show="scale" transition-hide="scale">
                <q-time v-model="horaInicio">
                    <div class="row items-center justify-end">
                    <q-btn v-close-popup label="Fechar" color="primary" flat />
                    </div>
                </q-time>
                </q-popup-proxy>
            </q-icon>
            </template>
        </q-input>

        <q-input filled v-model="horaFim" mask="time" :rules="['time']">
            <template v-slot:append>
            <q-icon name="access_time" class="cursor-pointer">
                <q-popup-proxy cover transition-show="scale" transition-hide="scale">
                <q-time v-model="horaFim">
                    <div class="row items-center justify-end">
                    <q-btn v-close-popup label="Close" color="primary" flat />
                    </div>
                </q-time>
                </q-popup-proxy>
            </q-icon>
            </template>
        </q-input>
    </q-page>
</template>
<style lang="scss">
    .btn-continuar {
        background: $default;
        color: white
    }
</style>

<script>
import { defineComponent } from "vue";
import { DiaSemanaController } from '../services/controllers/DiaSemanaController'
export default defineComponent({
  name: "TempoDisponivel",
  data: () => {
      return {
        diasSemana: [],
        model: "",
        horaInicio: "00:00",
        horaFim: "00:00"
      }
  },
  beforeMount(){
    this.buscarPerguntas()
  },
  methods: {
      async buscarPerguntas(){
        const diasSemana = await DiaSemanaController.BuscarDiasSemana()
        console.log("diasSemana", diasSemana)
        if(diasSemana.status) {
            if(diasSemana.status == 401) {
                this.$q.notify({
                    type: 'negative',
                    message: diasSemana.mensagem
                })
            }
        } else {
            this.diasSemana = diasSemana
        }
      }
    }
});
</script>
