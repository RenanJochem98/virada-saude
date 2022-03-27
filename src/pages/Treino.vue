<template>
    <q-page>
         <audio id="chatAudio" >
            <source src=
                "../../public/sounds/beep.mp3" 
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
                <q-btn label="Iniciar" class="btn-continuar q-mb-sm q-mx-sm" @click="timer" />
                <q-btn label="Pause" class="btn-continuar q-mb-sm" @click="pause" />
            </div>
        </div>
         <div class="row flex flex-center q-py-lg">
            
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


export default defineComponent({
  name: "Treino",
  data: () => {
      return {
        hour: 0,
        minute: 0,
        second: 0,
        millisecond: 0,
        cron: 0
      }
  },
  methods: {
      pause() {
          clearInterval(this.cron)
      },
      timer() {
        const audio = document.getElementById("chatAudio")
        this.cron = setInterval(() => {
            this.second += 1
            if(this.second % 10 == 0) {
                
                audio.play()
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
      }
  }
});
</script>
