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

export default defineComponent({
  name: "Treino",
  data: () => {
      return {
        treino:{},
        tempoTotal: 30,
        hour: 0,
        minute: 0,
        second: 0,
        atividadeAtualSecond: 0,
        cron: null,
        playDisabled: false
      }
  },
  beforeMount(){
    this.BuscarTreino()
  },
  methods: {
        async BuscarTreino(){
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
      pause() {
        this.playDisabled = false
        clearInterval(this.cron)
      },
      stop() {
        this.pause()
        this.cron = null
        this.hour = 0
        this.minute = 0
        this.second = 0
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
          
      }
  }
});
</script>
