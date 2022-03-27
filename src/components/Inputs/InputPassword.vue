<template>
    <q-input  
        ref="password"
        square 
        clearable 
        v-model="password"
        :type="passwordFieldType"
        class="q-mb-md"
        label="Senha"
        @update:model-value="updatePassword" >

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
</template>

<script>
import { defineComponent } from "vue";

export default defineComponent({
  name: "InputEmail",
  data : function() {
    return {
        password: '',
        passwordFieldType: 'password',
        visibility: false,
        visibilityIcon: 'visibility'
    };
  },
  methods: {
    updatePassword () {
      this.$emit('changePassword', this.password)
    },
    switchVisibility() {
      this.visibility = !this.visibility
      this.passwordFieldType = this.visibility ? 'text' : 'password'
      this.visibilityIcon =  this.visibility ? 'visibility_off' : 'visibility'
    }
  }

});
</script>
