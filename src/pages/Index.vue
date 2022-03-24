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
                        <q-input 
                            ref="email"
                            square 
                            clearable 
                            v-model="email" 
                            type="email"
                            label="Email">
                            <template v-slot:prepend>
                                <q-icon name="email" />
                            </template>
                        </q-input>
                        <q-input  
                            ref="password"
                            square 
                            clearable 
                            v-model="password"
                            :type="passwordFieldType"
                            class="q-mb-md"
                            label="Senha">
                
                            <template v-slot:prepend>
                                <q-icon name="lock" />
                            </template>
                            <template v-slot:append>
                                <q-icon 
                                :name="visibilityIcon"
                                @click="switchVisibility"
                                class="cursor-pointer" />
                            </template>
                        </q-input>
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

export default defineComponent({
  name: "Index",
  data : function() {
    return {
        email: '',
        username: '',
        password: '',
        repassword: '',
        register: false,
        passwordFieldType: 'password',
        visibility: false,
        visibilityIcon: 'visibility'
    };
  },
  methods: {
    switchVisibility() {
      this.visibility = !this.visibility
      this.passwordFieldType = this.visibility ? 'text' : 'password'
      this.visibilityIcon =  this.visibility ? 'visibility_off' : 'visibility'
    }
  }

});
</script>
