<template>
    <q-input filled v-model="time" mask="time" :rules="['time']" @update:model-value="onInput">
        <template v-slot:append>
            <q-icon name="access_time" class="cursor-pointer">
                <q-popup-proxy cover transition-show="scale" transition-hide="scale">
                    <q-time v-model="time" @update:model-value="onInput">
                        <div class="row items-center justify-end">
                            <q-btn v-close-popup label="Fechar" color="primary" flat />
                        </div>
                    </q-time>
                </q-popup-proxy>
            </q-icon>
        </template>
    </q-input>
</template>

<script>
import { defineComponent } from "vue";

export default defineComponent({
  name: "InputTime",
  data : function() {
    return {
        time: '00:00',
    };
  },
  methods: {
    onInput () {
      this.$emit('changeTime', this.time)
    }
  }

});
</script>