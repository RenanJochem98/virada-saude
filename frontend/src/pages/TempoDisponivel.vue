<template>
    <q-page>
        <div class="text-center text-h4 text-weight-bold q-ma-lg text-uppercase">Tempo Disponível</div>

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
                <q-btn label="Começar" class="btn-continuar q-mb-sm col-5" :to="{ name: 'Treino' }" />
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
        treino
      }
  }
});
</script>
