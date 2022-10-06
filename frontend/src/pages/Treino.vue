<template>
    <q-page>
         <audio id="chatAudio" >
            <source src=
                "../../public/sounds/beep.mp3" 
                type="audio/mpeg">
        </audio>
        <audio id="chatAudioTwo" >
            <source src=
                "../../public/sounds/beepTwo.mp3" 
                type="audio/mpeg">
        </audio>
   
        <div class="text-center text-h4 text-weight-bold q-ma-lg text-uppercase">Treino</div>
        <div class="flex flex-center text-h4">
            <div><span v-if="hour < 10">0</span>{{ hour }}:</div>
            <div><span v-if="minute < 10">0</span>{{ minute }}:</div>
            <div><span v-if="second < 10">0</span>{{ second }}</div>
        </div>
        
        <div class="row flex flex-center q-py-lg">
            <div class="col-2">
                <q-btn round icon="stop" class="btn-continuar q-mb-sm q-mx-sm" @click="stop" />
                <q-btn :disable="playDisabled" round icon="play_arrow" class="btn-continuar q-mb-sm q-mx-sm" @click="timer" />
                <q-btn round icon="pause" class="btn-continuar q-mb-sm q-mx-sm" @click="pause" />
            </div>
        </div>
        <div class="q-px-lg ">
            <!-- <div class="text-center text-h6 text-weight-medium q-mt-xl text-uppercase">Atividades</div> -->
            <div class="row flex q-py-md text-uppercase text-weight-bold bg-grey-6">
                <div class="col-1 flex-start text-center">Ordem</div>
                <div class="col-4 flex-center text-center">Nome</div>
                <div class="col-3 flex-center text-center">Tempo (em minutos)</div>
                <div class="col-4 flex-center text-center">Intensidade</div>
            </div>
            <div v-for="(exercicio, index) in treino.exercicios" :key="exercicio.idExercicio">
                <div class="row flex q-py-lg" :class="index%2 == 0 ? '' : 'bg-grey-3'">
                    <div class="col-1 flex-start text-center">{{ index +1 }}</div>
                    <div class="col-4 flex-center text-center text-capitalize">{{ exercicio.tipoTreino}}</div>
                    <div class="col-3 flex-center text-center">
                        {{tempoTotal * (exercicio.porcentagemTreino/100)}} ({{exercicio.porcentagemTreino}}%)
                        <!-- <span>
                            <span v-if="exercicio.porcentagemTreino < 10">0</span>{{exercicio.porcentagemTreino}}:
                        </span>
                        <span>
                            <span v-if="atividadeAtualSecond < 10">0</span>{{atividadeAtualSecond}}
                        </span> -->
                    </div>
                    <div class="col-4 flex-center text-center text-uppercase">{{exercicio.intensidade}}</div>
                </div>
                <q-separator :key="'sep' + exercicio.idExercicio" />
            </div>
        </div>
        <q-dialog v-model="feedbackDialog">
            <q-card style="width: 300px" class="q-px-sm q-pb-md">
                    <q-card-section>
                        <div class="text-h6">Feedback</div>
                    </q-card-section>
                    <!-- <div v-for="perguntaFeedback in perguntasFeedback" :key="perguntaFeedback.idPerguntaFeedback"> -->
                            <!-- {{perguntaFeedback}} -->
                        <div class="row flex flex-center q-mt-lg q-pt-lg">
                            <div v-for="(perguntaFeedback, i) in perguntasFeedback" :key="i" :class="perguntaFeedback.dependeDe !== null ? 'hidden' : '' + 'row flex-center col-12 questao q-py-lg'" :id="questionRefPrefix + perguntaFeedback.idPerguntaFeedback">
                                <div class="text-center text-weight-medium">{{i + 1}} - {{perguntaFeedback.texto}}</div>
                                <div v-if="clicouEmEnviar" class="row col-12 flex flex-center text-negative text-center text-caption q-mt-xs q-mb-sm">
                                    Campo obrigatório
                                </div> 
                                
                                <div class="q-mt-sm col-12">
                                    <q-option-group
                                        :ref="questionRefPrefix + perguntaFeedback.idPerguntaFeedback"
                                        v-model="respostas[perguntaFeedback.idPerguntaFeedback]"
                                        class="flex justify-center items-center"
                                        :options="perguntaFeedback.opcoesResposta" 
                                        @update:model-value="alterarRespostas(perguntaFeedback.idPerguntaFeedback, $event)"
                                    />
                                    
                                </div>
                            </div>
                        </div>
                    <!-- </div> -->
                    <!-- <q-item-label header>Tempo</q-item-label>
                    <q-item dense>
                        <q-item-section avatar>
                            <q-icon name="schedule" />
                        </q-item-section>
                        <q-item-section>
                                
                                <q-slider
                                    color="default"
                                   
                                    v-model="tempo"
                                    :step="5"
                                    :min="20"
                                    :max="90"
                                    label
                                    :label-value="tempo + ' minutos'"
                                />
                            
                        </q-item-section>
                    </q-item> -->

                    <!-- <q-item-label header>Clima</q-item-label> -->
                    <!-- <q-item dense class="q-pt-lg">
                        <q-item-section avatar>
                            <q-icon name="sunny" />
                        </q-item-section>
                        <q-item-section>
                           <q-select v-model="clima" :options="options" label="Clima" />
                        </q-item-section>
                    </q-item> -->
                    <q-card-actions class="q-pt-lg" align="center">
                        <q-btn label="Enviar" color="positive" v-close-popup @click="enviarResposta"/>
                    </q-card-actions>
                </q-card>
        </q-dialog>
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
import { TreinoController } from "src/services/controllers/TreinoController";
import { PerguntasFeedbackController } from "src/services/controllers/PerguntasFeedbackController";
import { FeedbackController } from "src/services/controllers/FeedbackController";

export default defineComponent({
  name: "Treino",
  data: () => {
      return {
        perguntasFeedback: {},
        respostas: {},
        perguntasObrigatorias: [],
        perguntasNaoObrigatorias: [],
        treino:{},
        tempoTotal: 30,
        hour: 0,
        minute: 0,
        second: 0,
        atividadeAtualSecond: 0,
        cron: null,
        playDisabled: false,
        feedbackDialog: false,
        questionRefPrefix: "feedbackRef",
        clicouEmEnviar: false
      }
  },
  beforeMount(){
    this.BuscarTreino()
    this.BuscarPerguntasFeedback()
  },
  methods: {
        async BuscarPerguntasFeedback(){
            const result = await PerguntasFeedbackController.BuscarTodasPerguntasParaSelectField()
            console.log(result)
            if(result.status) {
                if(result.status == 401) {
                    this.$q.notify({
                        type: 'negative',
                        message: result.mensagem
                    })
                }
            } else {
                this.perguntasFeedback = result

                this.perguntasFeedback.forEach(p => {
                    if(p.dependeDe) {
                        this.perguntasNaoObrigatorias.push(p)
                    } else {
                        this.perguntasObrigatorias.push(p)
                    }
                })
                console.log(this.perguntasFeedback)
            }
        },
        async BuscarTreino() {
            const idUsuario = this.$store.getters['user/getIdUser']
            const result = await TreinoController.BuscarTreino(idUsuario, '2022-09-21')
            console.log(result)
            if(result.status) {
                if(result.status == 401) {
                    this.$q.notify({
                        type: 'negative',
                        message: result.mensagem
                    })
                }
            } else {
                this.treino = result
            }
        },
        alterarRespostas (idQuestao, idResposta) {

            this.respostas[idQuestao] == idResposta
            let dependentesRespostas = this.perguntasFeedback.filter(p => {
                return p.dependeDe && p.dependeDe.idOpcaoRespostaFeedback == idResposta
            })


            dependentesRespostas.forEach(d => {
                document.getElementById(this.questionRefPrefix + d.idPerguntaFeedback).classList.remove('hidden')
                this.perguntasObrigatorias.push(d)
                this.perguntasNaoObrigatorias = this.perguntasNaoObrigatorias.filter(p => {
                        return p.idPerguntaFeedback !== d.idPerguntaFeedback
                    })
            })

            //Esconde questoes dependentes que ja foram exibidas, mas com tiveram respostas alteradas
            let dependentesPerguntas = this.perguntasFeedback.filter(p => {
                return p.dependeDe && p.dependeDe.idPerguntaFeedback == idQuestao
            })
            dependentesPerguntas.forEach(d => {
                if(this.respostas[idQuestao] && d.dependeDe.idOpcaoRespostaFeedback != this.respostas[idQuestao]) {
                    this.perguntasNaoObrigatorias.push(d)
                    this.removePerguntaNaoObrigatoria(d)
                    this.perguntasObrigatorias = this.perguntasObrigatorias.filter(p => {
                        return p.idPerguntaFeedback !== d.idPerguntaFeedback
                    })
                }
            })
        },
        removePerguntaNaoObrigatoria(pergunta) {
            document.getElementById(this.questionRefPrefix + pergunta.idPerguntaFeedback).classList.add('hidden')
            delete this.respostas[pergunta.idPerguntaFeedback] // se pergunta for escondida, resposta nao deve ser enviada
            
            if(pergunta.dependeDe !== null) {
                let dependentes = this.perguntasFeedback.filter(d => {
                    return d.dependeDe && d.dependeDe.idPerguntaFeedback == pergunta.idPerguntaFeedback
                })
                dependentes.forEach(p => {
                    this.removePerguntaNaoObrigatoria(p)
                    this.perguntasObrigatorias = this.perguntasObrigatorias.filter(d => {
                        return p.idPerguntaFeedback !== d.idPerguntaFeedback
                    })
                })
            }
        },
      pause() {
        this.playDisabled = false
        clearInterval(this.cron)
      },
      stop() {
        this.pause()
        this.cron = null
        this.hour = 0
        this.minute = 0
        this.second = 0,
        this.feedbackDialog = true
      },
      timer() {
        this.playDisabled = true
        const audio = document.getElementById("chatAudio")
        const audioTwo = document.getElementById("chatAudioTwo")
        this.cron = setInterval(() => {
            this.second += 1
            if(this.second % 10 == 0) {
                audio.play()
            }
            if(this.second % 15 == 0) {
                audioTwo.play()
            }
            if(this.second >= 60) {
                this.second = 0
                this.minute += 1
            }
            if(this.minute >= 60) {
                this.minute = 0
                this.hour += 1
            }
            
            
        }, 1000)
      },
      playCurrentActivity () {
          
      },
      montaEnvio () {

        let resposta = {
                usuario: this.$store.getters['user/getIdUser'],
                clima: "Ensolarado",
                treino: this.treino.idTreino,
                resultado_feedback: []
            }
        // console.log(this.respostas)
        this.perguntasObrigatorias.forEach(e => {
            // console.log(e)
            let item = {}
            item["id_pergunta_feedback"] = e.idPerguntaFeedback
            item["id_opcao_resposta_feedback"] =this.respostas[e.idPerguntaFeedback]
            resposta.resultado_feedback.push(item)
        })

        return resposta
      },
      enviarResposta(){
        // console.log(this.montaEnvio())
        const result = FeedbackController.CriarFeedback(this.montaEnvio())
            if(result.status) {
                this.$q.notify({
                    type: 'negative',
                    message: "Problema ao enviar feedback. Status retorno: " + result.status
                })
            } else {
                this.$q.notify({
                    type: 'positive',
                    message: "Feedback enviado com sucesso!"
                })
                // this.$router.push({ name: 'TempoDisponivel' })
            }
      }
  }
});
</script>
