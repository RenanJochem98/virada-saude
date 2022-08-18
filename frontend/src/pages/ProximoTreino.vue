<template>
    <q-page>
        <div class="text-center text-h4 text-weight-bold q-ma-lg text-uppercase">Próximo Treino</div>

        <div class="q-px-lg ">
            <!-- <div class="text-center text-h6 text-weight-medium q-mt-xl text-uppercase">Atividades</div> -->
            <div class="row flex q-py-md text-uppercase text-weight-bold bg-grey-6">
                <div class="col-1 flex-start text-center">ID</div>
                <div class="col-4 flex-center text-center">Nome</div>
                <div class="col-3 flex-center text-center">Tempo (em minutos)</div>
                <div class="col-4 flex-center text-center">Intensidade</div>
            </div>
            <div v-for="(atividade, index) in treino.atividades" :key="atividade.id">
                <div class="row flex q-py-lg" :class="index%2 == 0 ? '' : 'bg-grey-3'">
                    <div class="col-1 flex-start text-center">{{ atividade.id }}</div>
                    <div class="col-4 flex-center text-center">{{ atividade.nome}}</div>
                    <div class="col-3 flex-center text-center">{{atividade.tempoEmMinutos}} minutos</div>
                    <div class="col-4 flex-center text-center text-uppercase">{{atividade.intensidade }}</div>
                </div>
                <q-separator :key="'sep' + atividade.id" />
            </div>
            <div class="row flex flex-center q-py-lg">
                <!-- <q-btn label="Começar" class="btn-continuar q-mb-sm col-5" @click="comecar" /> -->
                <q-btn label="Começar" class="btn-continuar q-mb-sm col-5" @click="sliders = true" />
            </div>

            <q-dialog v-model="sliders">
                <q-card style="width: 300px" class="q-px-sm q-pb-md">
                    <q-card-section>
                        <div class="text-h6">Informações Pré-Treino</div>
                    </q-card-section>

                    <q-item-label header>Tempo</q-item-label>
                    <q-item dense>
                        <q-item-section avatar>
                            <q-icon name="schedule" />
                        </q-item-section>
                        <q-item-section>
                            <!-- <div class="row q-gutter-md"> -->
                                <!-- <q-btn
                                    round
                                    class="col-xs-2 col-sm-2 flex flex-start"
                                    icon="remove"
                                    color="default" 
                                    size="xs"
                                    @click="tempo--"/> 
                                     class="col-xs-4 col-sm-4 flex flex-center"-->
                                <q-slider
                                    color="default"
                                   
                                    v-model="tempo"
                                    :step="5"
                                    :min="20"
                                    :max="90"
                                    label
                                    :label-value="tempo + ' minutos'"
                                />
                                <!-- <q-btn
                                    round
                                    class="col-xs-2 col-sm-2 flex flex-end"
                                    icon="add"
                                    color="default"
                                    size="xs"
                                    @click="tempo++" /> -->
                            <!-- </div> -->
                            
                        </q-item-section>
                    </q-item>

                    <!-- <q-item-label header>Clima</q-item-label> -->
                    <q-item dense class="q-pt-lg">
                        <q-item-section avatar>
                            <q-icon name="sunny" />
                        </q-item-section>
                        <q-item-section>
                           <q-select v-model="clima" :options="options" label="Clima" />
                        </q-item-section>
                    </q-item>
                    <q-card-actions class="q-pt-lg" align="center">
                        <q-btn label="Começar" color="positive" v-close-popup :to="{ name: 'Treino' }" />
                    </q-card-actions>
                </q-card>
            </q-dialog>
        </div>
    </q-page>
</template>
<style lang="scss">
    .btn-continuar {
        background: $default;
        color: white
    }

    .text-default {
        color: $default !important;
    }
    .bg-default {
        background: $default !important;
    }
    .heigth {
        height: 2px !important;
    }
</style>

<script>
import { defineComponent } from "vue";
import { Dialog } from 'quasar'

const treino = {
    dataReferencia: '2022-03-28',
    tempoTotalEmMinutos: 60,
    atividades: [
        {
            id: 1,
            nome: 'Caminhada',
            descricao: 'A caminhada é um movimento onde o ser humando se desloca mantendo sempre um pé no chão.',
            tempoEmMinutos: 10,
            intensidade: 'leve'
        },
        {
            id: 2,
            nome: 'Corrida',
            descricao: 'A corrida é um movimento onde o ser humando se desloca de maneira acelerada.',
            tempoEmMinutos: 10,
            intensidade: 'pesado'
        }
    ]
}
export default defineComponent({
  name: "ProximoTreino",
  data: () => {
      return {
        treino,
        sliders: false,
        tempo: 20,
        options: ['Ensolarado', 'Nublado', 'Chuvoso'],
        clima: 'Ensolarado'
      }
  },
  methods: {
    comecar () {
        Dialog.create({ 
        title: 'Opções de treino',
        message: 'Choose an option:',
        options: {
          type: 'radio',
          model: 'opt1',
          // inline: true
          items: [
            { label: 'Option 1', value: 'opt1', color: 'secondary' },
            { label: 'Option 2', value: 'opt2' },
            { label: 'Option 3', value: 'opt3' }
          ]
        },
        cancel: {
          push: true,
          color: 'negative'
        },
        ok: {
          push: true,
          color: 'positive'
        },
        persistent: true
      })
    }
  }
});
</script>
