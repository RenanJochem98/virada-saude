<template>
    <q-page padding class="row justify-around q-mt-lg">
        <q-form class="col-6">
            <div class="text-center text-h4 text-weight-bold q-pb-lg  text-uppercase col-12">
                Novo Cadastro
            </div>
            <q-input label="Qual seu primeiro nome?" @update:model-value="first_name = $event"  class="q-pb-md"/>
            <q-input label="Qual seu sobrenome?" @update:model-value="last_name = $event" class="q-pb-md"/>
            <input-email class="text-center" @changeEmail="email = $event" ref="email"/>
            <input-password @changePassword="password = $event" ref="password"/>
            <q-select v-model="empresa" :options="empresas" label="Empresa" />
            <q-btn label="Login" class="btn-login full-width q-mb-sm " @click="login" />
            <q-btn label="Esqueci minha senha" class="full-width" color="red" />
        </q-form>
    </q-page>
</template>

<style lang="scss">
    .titulo {
        color: $blue-1;
    }
    .btn-login {
        background: $default;
        color: white
    }
    .custom-login-card {
        width:400px;
        // height:440px;
        height:30em;
    }
</style>

<script>
import { defineComponent } from "vue";
import { EmpresaController } from '../services/controllers/EmpresaController'
import InputEmail from 'components/Inputs/InputEmail.vue'
import InputPassword from 'components/Inputs/InputPassword.vue'
export default defineComponent({
  name: "Cadastro",
  components: {InputEmail, InputPassword},
  async beforeMount () {
      this.empresas = await this.BuscarEmpresas()
  },
  data : function() {
    return {
        email: '',
        username: '',
        password: '',
        first_name: '',
        last_name: '',
        empresa: '',
        empresas: []
    };
  },
  methods: {
    async BuscarEmpresas () {
        const result = await EmpresaController.BuscarEmpresas()
        //  = result
        console.log(result)
        return result
    }
  }

});
</script>