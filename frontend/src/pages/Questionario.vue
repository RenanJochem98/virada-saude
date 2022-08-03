<template>
    <!-- <q-page class="flex row justify-around"> -->
    <q-page class="">
        <div class="text-center text-h4 text-weight-bolder q-mt-lg">Questionario inicial</div>
        <div class="text-center text-weight-bolder q-mt-sm">Breve descrição sobre o questionario</div>
        
        <div class="row flex flex-center q-mt-lg q-pt-lg">
            <div v-for="(pergunta, i) in perguntas" :key="i" class="col-12 q-mt-lg">
                <div v-if="pergunta.dependeDe == null">
                    <div class="text-center text-weight-medium">{{i + 1}} - {{pergunta.texto}}</div>
                
                    <div v-if="clicouEmEnviar && (respostas[pergunta.idPerguntaAnamnese] == null || respostas[pergunta.idPerguntaAnamnese] === undefined)" class="text-negative text-center text-caption q-mt-xs q-mb-sm">Campo obrigatório</div>

                    <div class="q-mt-sm col-12">
                        <q-option-group :ref="questionRefPrefix + pergunta.idPerguntaAnamnese" v-model="respostas[pergunta.idPerguntaAnamnese]" :options="pergunta.opcoesResposta"  class="flex justify-center items-center"
                        @update:model-value="respostas[pergunta.idPerguntaAnamnese] == $event"/>
                    </div>
                </div>
            </div>
        </div>
        <div class="row flex flex-center">
            <q-btn label="Continuar" class="btn-continuar q-mb-sm col-5" @click="sendAnswers"  />
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
import { PerguntaAnamnseController } from '../services/controllers/PerguntasAnamneseController'
const options = [
    {
        label: 'Option 1',
        value: 'op1'
    },
    {
        label: 'Option 2',
        value: 'op2'
    },
    {
        label: 'Option 3',
        value: 'op3'
    },
]

export default defineComponent({
  name: "Questionario",
  data: function() {
    return {
        options,
        shape: "",
        respostas: {},
        questions: [6,5,4],
        clicouEmEnviar: false,
        questionRefPrefix: "questionRef",
        perguntas: []
    };
  },
  beforeMount(){
    this.buscarPerguntas()
  },
  methods: {
      async buscarPerguntas(){
        const perguntas = await PerguntaAnamnseController.BuscarTodasPerguntasParaSelectField()
        if(perguntas.status) {
            if(perguntas.status == 401) {
                this.$q.notify({
                    type: 'negative',
                    message: perguntas.mensagem
                })
            }
        } else {
            this.perguntas = perguntas
        }
        console.log('questionario options', this.perguntas)
      },
      sendAnswers () {
        this.clicouEmEnviar = true
        let temErro = false
        
        temErro = this.questions.length !== Object.values(this.respostas).filter(i =>  i !== null && i !== undefined && i !== '').length

        //   this.$refs.fieldRef1[0].validate()
        if(!temErro){
            console.log('passou') 
            this.$router.push( { name: 'Home' })
        }else {
            console.log('nao passou')
        }
        //   
      }
  }
});
</script>