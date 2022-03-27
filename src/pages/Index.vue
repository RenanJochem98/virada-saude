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
                        <input-email @changeEmail="email = $event"/>
                        <input-password @changePassword="password = $event" />
                        <q-btn label="Login" class="btn-login full-width q-mb-sm " :to="{ name: 'Questionario' }" />
                        <q-btn label="Esqueci minha senha" class="full-width" color="red" />
                     </q-form>
                </q-card-section>

                <q-separator inset />

                <q-card-section>
                    <div class="q-px-sm">
                        <q-btn label="Novo cadastro" class="q-px-sm full-width" color="positive" />
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
import InputEmail from 'components/Inputs/InputEmail.vue'
import InputPassword from 'components/Inputs/InputPassword.vue'
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
    
  }

});
</script>
