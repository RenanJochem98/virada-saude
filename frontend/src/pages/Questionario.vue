<template>
    <!-- <q-page class="flex row justify-around"> -->
    <q-page class="">
        <div class="text-center text-h4 text-weight-bolder q-mt-lg">Questionario inicial</div>
        <div class="text-center text-weight-bolder q-mt-sm">Breve descrição sobre o questionario</div>
        
        <div class="row flex flex-center q-mt-lg q-pt-lg">
            <div v-for="(pergunta, i) in perguntas" :key="i" :class="pergunta.dependeDe !== null ? 'hidden' : '' + 'row flex-center col-12 questao q-py-lg'" :id="questionRefPrefix + pergunta.idPerguntaAnamnese">
                <div class="text-center text-weight-medium">{{i + 1}} - {{pergunta.texto}}</div>
            
                <!-- <div v-if="clicouEmEnviar && (respostas[pergunta.idPerguntaAnamnese] == null || respostas[pergunta.idPerguntaAnamnese] === undefined)" class="text-negative text-center text-caption q-mt-xs q-mb-sm">Campo obrigatório</div> -->
                <div v-if="clicouEmEnviar" class="row col-12 flex flex-center text-negative text-center text-caption q-mt-xs q-mb-sm">
                    Campo obrigatório
                </div> 
                
                <div class="q-mt-sm col-12">
                    <q-option-group
                        :ref="questionRefPrefix + pergunta.idPerguntaAnamnese"
                        v-model="respostas[pergunta.idPerguntaAnamnese]"
                        class="flex justify-center items-center"
                        :options="pergunta.opcoesResposta" 
                        @update:model-value="alterarRespostas(pergunta.idPerguntaAnamnese, $event)"
                    />
                    
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
import { AnamneseController } from '../services/controllers/AnamneseController'
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
        perguntas: [],
        perguntasObrigatorias: [],
        perguntasNaoObrigatorias: [],
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
        this.perguntas.forEach(p => {
            if(p.dependeDe) {
                this.perguntasNaoObrigatorias.push(p)
            } else {
                this.perguntasObrigatorias.push(p)
            }
        })
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
            return p.dependeDe && p.dependeDe.idOpcaoRespostaAnamnese == idResposta
        })
        dependentesRespostas.forEach(d => {
           document.getElementById(this.questionRefPrefix + d.idPerguntaAnamnese).classList.remove('hidden')
           this.perguntasObrigatorias.push(d)
           this.perguntasNaoObrigatorias = this.perguntasNaoObrigatorias.filter(p => {
                    return p.idPerguntaAnamnese !== d.idPerguntaAnamnese
                })
        })

        //Esconde questoes dependentes que ja foram exibidas, mas com tiveram respostas alteradas
        let dependentesPerguntas = this.perguntas.filter(p => {
            return p.dependeDe && p.dependeDe.idPerguntaAnamnese == idQuestao
        })

        dependentesPerguntas.forEach(d => {
            if(this.respostas[idQuestao] && d.dependeDe.idOpcaoRespostaAnamnese != this.respostas[idQuestao]) {
                this.perguntasNaoObrigatorias.push(d)
                this.removePerguntaNaoObrigatoria(d)
                this.perguntasObrigatorias = this.perguntasObrigatorias.filter(p => {
                    return p.idPerguntaAnamnese !== d.idPerguntaAnamnese
                })
            }
        })
      },
      removePerguntaNaoObrigatoria(pergunta) {
        document.getElementById(this.questionRefPrefix + pergunta.idPerguntaAnamnese).classList.add('hidden')
        delete this.respostas[pergunta.idPerguntaAnamnese] // se pergunta for escondida, resposta nao deve ser enviada
        
        if(pergunta.dependeDe !== null) {
            let dependentes = this.perguntas.filter(d => {
                return d.dependeDe && d.dependeDe.idPerguntaAnamnese == pergunta.idPerguntaAnamnese
            })
            dependentes.forEach(p => {
                this.removePerguntaNaoObrigatoria(p)
                this.perguntasObrigatorias = this.perguntasObrigatorias.filter(d => {
                    return p.idPerguntaAnamnese !== d.idPerguntaAnamnese
                })
            })
        }
      },
      validaEnvio (){
        let result = true
        result = this.perguntasObrigatorias.length == Object.values(this.respostas).length
        // console.log("perguntasObrigatorias.length", this.perguntasObrigatorias.length)
        // console.log("respostas.length", Object.values(this.respostas).length)
        if(!result) {
            return result
        }

        this.perguntasObrigatorias.forEach(p => {
            // console.log("Id Pergunta Obrigatoria", p.idPerguntaAnamnese)
            // console.log("Resposta Pergunta Obrigatoria", this.respostas[p.idPerguntaAnamnese])
            if(!this.respostas[p.idPerguntaAnamnese]){
                result = false
            }
        })

        if(!result) {
            return result
        }

        this.perguntasNaoObrigatorias.forEach(p => {
            // console.log("Id Nao Pergunta Obrigatoria", p.idPerguntaAnamnese)
            // console.log("Resposta Pergunta Nao Obrigatoria", this.respostas[p.idPerguntaAnamnese])
            if(this.respostas[p.idPerguntaAnamnese]){
                //  console.log("Entrou aqui", p.idPerguntaAnamnese)
                result = false
            }
        })

        return result
      },
      montaEnvio () {
        let resposta = {
                usuario: this.$store.getters['user/getIdUser']
            }
        this.perguntasObrigatorias.forEach(e => {
            resposta[e.campoAnamneseCorrespondente] = this.respostas[e.idPerguntaAnamnese]
        })

        return resposta
      },
      sendAnswers () {
        console.log("perguntas: ", this.perguntas)
        console.log("perguntasObrigatorias: ", this.perguntasObrigatorias)
        // console.log("perguntasNaoObrigatorias: ", this.perguntasNaoObrigatorias)
        console.log("Respostas: ", this.respostas)
        console.log("Respostas Monstadas: ", this.montaEnvio())
        // console.log("Refs: ", this.$refs)
        // console.log("questionRef1: ", this.$refs['questionRef1'])
        // console.log("question1: ", this.$refs['question1'])

        this.clicouEmEnviar = !this.clicouEmEnviar
        let temErro = false
        const validacao = this.validaEnvio()
        // console.log("Validacao", validacao)
        if(validacao){
            const result = AnamneseController.CriarAnamnese(this.montaEnvio())
            if(result.status) {
                this.$q.notify({
                    type: 'negative',
                    message: "Problema ao enviar status. Status retorno: " + result.status
                })
            } else {
                this.$q.notify({
                    type: 'positive',
                    message: "Anamnese criada com sucesso!"
                })
                this.$router.push({ name: 'TempoDisponivel' })
            }
             
        } else {
             this.$q.notify({
                    type: 'negative',
                    message: "Formulario inválido"
                })
        }
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