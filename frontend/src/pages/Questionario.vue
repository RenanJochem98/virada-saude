<template>
    <!-- <q-page class="flex row justify-around"> -->
    <q-page class="">
        <div class="text-center text-h4 text-weight-bolder q-mt-lg">Questionario inicial</div>
        <div class="text-center text-weight-bolder q-mt-sm">Breve descrição sobre o questionario</div>
        
        <div class="row flex flex-center q-mt-lg q-pt-lg">
            <div v-for="(pergunta, i) in perguntas" :key="i" :class="pergunta.dependeDe !== null ? 'hidden' : '' + 'row flex-center col-12 questao q-py-lg'" :id="questionRefPrefix + pergunta.idPerguntaAnamnese">
                <div class="text-center text-weight-medium">{{i + 1}} - {{pergunta.texto}}</div>
            
                <div v-if="clicouEmEnviar && (respostas[pergunta.idPerguntaAnamnese] == null || respostas[pergunta.idPerguntaAnamnese] === undefined)" class="text-negative text-center text-caption q-mt-xs q-mb-sm">Campo obrigatório</div>

                <div class="q-mt-sm col-12">
                    <q-option-group :ref="questionRefPrefix + pergunta.idPerguntaAnamnese" v-model="respostas[pergunta.idPerguntaAnamnese]" :options="pergunta.opcoesResposta"  class="flex justify-center items-center"
                    @update:model-value="alterarRespostas(pergunta.idPerguntaAnamnese, $event)"/>
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
        // console.log('questionario options', this.perguntas)
      },
      alterarRespostas (idQuestao, idResposta) {
        this.respostas[idQuestao] == idResposta
        // console.log("Perguntas: ", this.perguntas)
        // console.log("Respostas: ", this.respostas)
        // console.log("Refs: ", this.$refs)
        // console.log("Ref Quest 1: ",this.$refs.questionRef1)
        //document.getElementById(this.questionRefPrefix + "1").classList.remove('hidden')

        // Mostra questoes dependentes escondidas
        let dependentesRespostas = this.perguntas.filter(p => {
            return p.dependeDe && p.dependeDe.id_opcao_resposta_anamnese == idResposta
        })
        dependentesRespostas.forEach(d => {
           document.getElementById(this.questionRefPrefix + d.idPerguntaAnamnese).classList.remove('hidden')
        })

        //Esconde questoes dependentes que ja foram exibidas, mas com tiveram respostas alteradas
        let dependentesPerguntas = this.perguntas.filter(p => {
            return p.dependeDe && p.dependeDe.id_pergunta_anamnese == idQuestao
        })

        dependentesPerguntas.forEach(d => {
            if(this.respostas[idQuestao] && d.dependeDe.id_opcao_resposta_anamnese != this.respostas[idQuestao]) {
                document.getElementById(this.questionRefPrefix + d.idPerguntaAnamnese).classList.add('hidden')
            }
           
        })
      },
      sendAnswers () {
        console.log("Respostas: ", this.respostas)
        console.log("Refs: ", this.$refs)
        this.clicouEmEnviar = true
        let temErro = false
        
        // temErro = this.questions.length !== Object.values(this.respostas).filter(i =>  i !== null && i !== undefined && i !== '').length

        //   this.$refs.fieldRef1[0].validate()
        // if(!temErro){
        //     console.log('passou') 
        //     this.$router.push( { name: 'Home' })
        // }else {
        //     console.log('nao passou')
        // }
        //   
      }
  }
});
</script>