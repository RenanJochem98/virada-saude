<template>
    <q-input 
        ref="email"
        square 
        clearable 
        v-model="email" 
        type="email"
        label="Email"
        lazy-rules
        :rules="[this.required,this.isEmail,this.short]"
        @update:model-value="updateEmail">
        <template v-slot:prepend>
            <q-icon name="email" />
        </template>
    </q-input>
</template>

<script>
import { defineComponent } from "vue";

export default defineComponent({
  name: "InputEmail",
  data : function() {
    return {
        email: ''
    };
  },
  methods: {
    updateEmail () {
      this.$emit('changeEmail', this.email)
    },
    required (val) {
      return  (val && val.length > 0 || 'O campo email não pode estar vazio')
    },
    short(val) {
      return  (val && val.length > 3 || 'O campo email deve ter ao menos três caracteres')
    },
    isEmail (val) {
        const emailPattern = /^(?=[a-zA-Z0-9@._%+-]{6,254}$)[a-zA-Z0-9._%+-]{1,64}@(?:[a-zA-Z0-9-]{1,63}\.){1,8}[a-zA-Z]{2,63}$/
        return (emailPattern.test(val) || 'O email inserido não é válido')
    }
  }

});
</script>
