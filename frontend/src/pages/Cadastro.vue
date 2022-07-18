<template>
    <q-page padding class="row justify-around q-mt-lg">
        <q-form class="col-6">
            <div class="text-center text-h4 text-weight-bold q-pb-lg  text-uppercase col-12">
                Novo Cadastro
            </div>
            <q-input ref="firstName" label="Qual seu primeiro nome?" v-model="first_name" @update:model-value="first_name = $event"  class="q-pb-md" lazy-rules :rules="[this.ValidarCampoNaoVazio]"/>
            <q-input ref="lastName" label="Qual seu sobrenome?" v-model="last_name" @update:model-value="last_name = $event" class="q-pb-md" lazy-rules :rules="[this.ValidarCampoNaoVazio]"/>
            <input-email ref="email" class="text-center" v-model="email"  @changeEmail="email = $event" lazy-rules :rules="[this.ValidarCampoNaoVazio]"/>
            <input-password ref="password" v-model="password" @changePassword="password = $event" lazy-rules :rules="[this.ValidarCampoNaoVazio]" />
            <q-select ref="empresa" v-model="empresa" :options="empresas" label="Empresa" lazy-rules :rules="[this.ValidarCampoEmpresaNaoVazio]" />
            <q-btn label="Cadastrar" class="btn-login full-width q-mb-sm " @click="CriarUsuario" />
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
import { UserController } from '../services/controllers/UserController'
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
    },
    ExisteErroNoFormulario () {
        this.$refs.firstName.validate()
        this.$refs.lastName.validate()
        const erroEmail = this.$refs.email.hasError()
        const erroSenha = this.$refs.password.hasError()
        this.$refs.empresa.validate()

        return this.$refs.firstName.hasError 
            || this.$refs.lastName.hasError
            || this.$refs.empresa.hasError
            || erroEmail
            || erroSenha
    },
    async CriarUsuario () {
        //console.log("Empresa", "")
        if(this.ExisteErroNoFormulario()){
            this.$q.notify({
                type: 'negative',
                message: 'Houve um erro ao realizar o cadastro.'
            })
        } else {
            const result = await UserController.CriarUsuario({
                firstName: this.first_name,
                lastName: this.last_name,
                email: this.email,
                password: this.password,
                empresa: this.empresa.value
            })
            console.log(result)
        }
       
    },
    ValidarCampoNaoVazio (val) {
        return  (val != null && val.length > 0 || 'Este campo não pode estar vazio')
    },
    ValidarCampoEmpresaNaoVazio (val) {
        console.log(val)
        return  (val != null && val != "" && typeof val != undefined || 'Este campo não pode estar vazio')
    }
  }

});
</script>