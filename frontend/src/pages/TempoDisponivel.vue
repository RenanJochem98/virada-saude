<template>
    <q-page padding>
        <div class="text-center text-h4 text-weight-bold q-ma-lg text-uppercase">Tempo Disponível</div>
        <div v-for="i in quantLinhas" :key="i">
            <div class="row flex flex-center">
                <div class="col-2 col-md-2 col-lg-2 q-px-lg q-mx-lg">
                    <q-select v-model="listaPeriodos[i].dia" :options="diasSemana" label="Dia" />
                </div>
                <div class="col-1 col-md-1 col-lg-1 q-mx-lg">
                    <InputTime @changeTime="listaPeriodos[i].horaInicio = $event"/>
                </div>
                <div class="col-1 col-md-1 col-lg-1 q-mx-lg">
                    <InputTime @changeTime="listaPeriodos[i].horaFim = $event"/>
                </div>
            </div>
        </div>
        <div class="row flex flex-center">
            <q-btn class="col-6 col-md-2 col-lg-6 q-px-lg q-mx-lg" color="green-9" icon-right="add_circle" label="Adicionar" @click="addLinha"/>
            <q-btn class="col-6 col-md-2 col-lg-6 q-px-lg q-mx-lg" color="red-9" icon-right="remove_circle" label="Remover" @click="removeLinha"/>
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
import InputTime  from 'src/components/Inputs/InputTime.vue'

export default defineComponent({
  name: "TempoDisponivel",
  components: { InputTime },
  data: () => {
      return {
        diasSemana: [],
        quantLinhas: 1,
        listaPeriodos: {
            1: {
                dia: "",
                horaInicio: "",
                horaFim: "",
            }
        }
      }
  },
  beforeMount(){
    this.buscarPerguntas()
  },
  methods: {
      addLinha () {
        this.quantLinhas++
        this.listaPeriodos[this.quantLinhas] = {
                dia: "",
                horaInicio: "",
                horaFim: "",
            }
      },
      removeLinha () {
        if(this.quantLinhas > 1) {
            delete this.listaPeriodos[this.quantLinhas]
            this.quantLinhas--
        } else {
            this.$q.notify({
                type: 'warning',
                message: "Você precisa adicionar pelo menos um período."
            })
        }
        
      },
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
      },
      async enviar(){
        console.log("id user logado", this.$store.getters['user/getIdUser'])
        console.log("listaperiodos: ", this.listaPeriodos)

        let teste = []
        const list = Object.values(this.listaPeriodos)
        console.log("list", list)
        list.forEach(e => {
            if(e.dia) {
                let item = {
                "id_dia_semana": e.dia.value,
                "id_usuario": this.$store.getters['user/getIdUser'],
                "hora_inicio": e.horaInicio,
                "hora_fim": e.horaFim
            }
            teste.push(item)
            }
            
        });
        console.log("teste", teste)

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
