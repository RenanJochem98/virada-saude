<template>
    <q-page padding>
        <div class="text-center text-h4 text-weight-bold q-ma-lg text-uppercase">Tempo Disponível</div>
        <div v-for="dia in diasSemana" :key="dia.value">
            <div class="row flex flex-center">
                <div class="col-xs-12 col-sm-12 col-1 col-md-1 col-lg-1 text-bold flex flex-center">
                    {{dia.label}}
                </div>
                <q-radio v-for="(periodo, index) in [30, 45, 60]" :key="index" 
                    class="col-xs-12 col-sm-12 col-1 col-md-1 col-lg-1 flex flex-center" v-model="listaPeriodos[dia.value]" 
                    :val="periodo" 
                    :label="periodo + ' min'" />
            </div>
        </div>
        <div class="row flex flex-center q-pt-lg q-mt-lg">
            <q-btn label="Continuar" class="btn-continuar q-mb-sm col-5" @click="enviar"  />
        </div>
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
import { TempoDisponivelController } from '../services/controllers/TempoDisponivelController'

export default defineComponent({
  name: "TempoDisponivel",
//   components: { InputTime },
  data: () => {
      return {
        diasSemana: [],
        listaPeriodos: []
      }
  },
  beforeMount(){
    this.buscarDiasSemana()
  },
  methods: {
      
      async buscarDiasSemana(){
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
      },
      async enviar(){
        console.log("id user logado", this.$store.getters['user/getIdUser'])
        console.log("listaperiodos: ", this.listaPeriodos)
        let teste = []
        this.diasSemana.forEach(dia => {
            if(this.listaPeriodos[dia.value]){
                let item = {
                    "id_dia_semana": dia.value,
                    "id_usuario": this.$store.getters['user/getIdUser'],
                    "periodo_disponivel": this.listaPeriodos[dia.value],
                }
                teste.push(item)
            }
        })

        // Deve ser alterado para um bulk create, quando a api aceitar
        await teste.forEach(e => {
            let result =  TempoDisponivelController.CriarTempoDisponivel(e)
            console.log(result)
        })

        this.$q.notify({
                type: 'positive',
                message: 'Os períodos disponíveis foram cadastrados com sucesso!'
            })
        this.$router.push({name: "Home"})
      }
    }
});
</script>
