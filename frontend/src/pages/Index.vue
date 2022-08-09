<template>
    <q-page class="flex flex-center row justify-around">
        <div class="titulo column text-h1 text-weight-bolder text-left">
            Virada Saúde
        </div>
        <div class="column">
            <q-card square class="shadow-24 custom-login-card">
                <!-- <q-card-section class="bg-deep-purple-7">
                    Login
                </q-card-section> -->

                <q-card-section class="q-pb-xl">
                     <q-form class="q-px-sm q-pt-md">
                        <input-email v-model="email" @changeEmail="email = $event" ref="email"/>
                        <input-password v-model="password" @changePassword="password = $event" ref="password"/>
                        <q-btn label="Login" class="btn-login full-width q-mb-sm " @click="Login" />
                        <q-btn label="Esqueci minha senha" class="full-width" color="red" />
                     </q-form>
                </q-card-section>

                <q-separator inset />

                <q-card-section>
                    <div class="q-px-sm">
                        <q-btn label="Novo cadastro" class="q-px-sm full-width" color="positive" :to="{ name: 'Cadastro' }" />
                    </div>
                </q-card-section>
            </q-card>
        </div>
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
//import { Store } from 'src/store'
import InputEmail from 'components/Inputs/InputEmail.vue'
import InputPassword from 'components/Inputs/InputPassword.vue'
import { UserController } from '../services/controllers/UserController'
import jwt_decode from "jwt-decode"
export default defineComponent({
  name: "Index",
  components: {InputEmail, InputPassword},
  data : function() {
    return {
        email: '',
        username: '',
        password: ''
    };
  },
  methods: {
    async Login(){
        const hasEmailError = this.$refs.email.hasError()
        const hasPasswordError = this.$refs.password.hasError()
        if(!hasEmailError && !hasPasswordError){
            const result = await UserController.Login(this.email, this.password)
            if(!result.status) {
                const decoded = jwt_decode(result.accessToken);
                await this.$store.dispatch('login/ActionSetAccessToken', result.accessToken)
                await this.$store.dispatch('login/ActionSetRefreshToken', result.refreshToken)
                await this.$store.dispatch('user/ActionSetIdUser', decoded.user_id)
                //await this.$store.dispatch('login/ActionSetIdUser', result.decoded.user_id)
                this.$q.notify({
                    type: 'positive',
                    message: "Login realizado com sucesso!"
                })
                if(!decoded.possui_anamnese){
                    this.$router.push({ name: 'Questionario' })
                } else if(!decoded.possui_tempo_disponivel_cadastrado) {
                    this.$router.push({ name: 'TempoDisponivel' })
                }else {
                    this.$router.push({ name: 'Home' })
                }
                
            } else {
                this.$q.notify({
                    type: 'negative',
                    message: result.mensagem
                })
            }
        }
    }
  }

});
</script>
