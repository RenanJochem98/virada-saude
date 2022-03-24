<template>
    <!-- <q-page class="flex row justify-around"> -->
    <q-page class="">
        <div class="text-center text-h4 text-weight-bolder q-mt-lg">Questionario inicial</div>
        <div class="text-center text-weight-bolder q-mt-sm">Breve descrição sobre o questionario</div>
        <div class="row flex flex-center q-mt-lg q-pt-lg">
            <div v-for="(index, i) in [6,5,4,3,2,1]" :key="i" class="col-12 text-center q-py-lg">
                <div class="text-weight-medium">{{i + 1}} - Enunciado da questão</div>
                <div v-for="(jIndex, j) in [6,5,4,3,2,1]" :key="j">
                    <q-radio v-model="shape" :val="j" :label="'Opção: ' + jIndex" />
                </div>
            </div>
        </div>
        <div class="row flex flex-center">
            <q-btn label="Continuar" class="btn-continuar q-mb-sm col-5" :to="{ name: 'Questionario' }" />
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
  name: "Questionario",
  data: function() {
    return {
        shape: ""
    };
}
});
</script>