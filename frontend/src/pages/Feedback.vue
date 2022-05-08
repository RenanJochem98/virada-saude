<template>
    <q-page padding>
        <div class="text-center text-h4 text-weight-bolder q-mt-lg">Feedback</div>
            <div class="flex flex-center text-center q-my-xl row">
                <div v-for="pergunta in perguntas" :key="pergunta.id" :id="pergunta.id" :class='pergunta.dependeDaResposta !== null? "hide": ""' class="col-12 q-mt-md" >
                <div class=" text-weight-bolder">{{pergunta.texto}}</div>
                <div>
                    <q-radio v-for="opcao in pergunta.opcoes" :key="opcao.id" :val="opcao.id" v-model="respostas[pergunta.id]" :label="opcao.texto"  class=""
                        @update:model-value="clickOption(pergunta.id, $event)"/>
                </div>
            </div>
        </div>
        <div class="row flex flex-center">
            <q-btn label="Enviar" class="btn-continuar q-mb-sm col-5" @click="sendAnswers"  />
        </div>
            
    </q-page>
</template>
<style lang="scss">
    .btn-continuar {
        background: $default;
        color: white
    }
    .hide {
        display: none;
    }
</style>
<script>
import { defineComponent } from "vue";

const perguntas = [
    {
        id: 1,
        texto: 'Pergunta numero 1',
        tipo: 'select',
        opcoes: [
            {
                id: 1,
                texto: 'Sim'
            },
            {
                id: 2,
                texto: 'Nao'
            }
        ],
        dependeDaResposta: null
    },
    {
        id: 2,
        texto: 'Pergunta numero 2 - Deve apacerecer no Sim da pergunta 1',
        tipo: 'select',
        opcoes: [
            {
                id: 3,
                texto: 'Opcao 1'
            },
            {
                id: 4,
                texto: 'Opcao 2'
            }
        ],
        dependeDaResposta: 1
    },
    {
        id: 3,
        texto: 'Pergunta numero 3 - Deve apacerecer no Nao da pergunta 1',
        tipo: 'select',
        opcoes: [
            {
                id: 5,
                texto: 'Opcao 1'
            },
            {
                id: 6,
                texto: 'Opcao 2'
            }
        ],
        dependeDaResposta: 2
    },
    {
        id: 4,
        texto: 'Pergunta numero 4 - Deve apacerecer no Nao da pergunta 1',
        tipo: 'select',
        opcoes: [
            {
                id: 7,
                texto: 'Opcao 1'
            },
            {
                id: 8,
                texto: 'Opcao 2'
            }
        ],
        dependeDaResposta: 2
    }
]


export default defineComponent({
  name: "Feedback",
  data () {
      return {
          perguntas,
          respostas: {},
          perguntasDependentes: {}
      }
  },
  methods: {
      clickOption (idPergunta, idResposta) {
          this.respostas[idPergunta] == idResposta

          if (!this.perguntasDependentes[idPergunta]) {
              this.perguntasDependentes[idPergunta] = {}
          }

          if (!this.perguntasDependentes[idPergunta][idResposta]) {
              this.perguntasDependentes[idPergunta][idResposta] = this.perguntas.filter(p => p.dependeDaResposta === idResposta)
          }

          //mostra as questões dependentes da pergunta atual
          this.perguntasDependentes[idPergunta][idResposta].forEach(perguntaDependente => {
              document.getElementById(perguntaDependente.id).classList.remove('hide')
          })

          // esconde perguntas dependentes das outras respostas da pergunta atual 
          Object.keys(this.perguntasDependentes[idPergunta]).forEach(idRespostaAtual => {
             if (idRespostaAtual != idResposta) {
                this.perguntasDependentes[idPergunta][idRespostaAtual].forEach(perguntaDependente => {
                    document.getElementById(perguntaDependente.id).classList.add('hide')
                })
            } 
          })   
      },
      sendAnswers () {

      }
  }
});
</script>