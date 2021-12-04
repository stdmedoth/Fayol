<template id="">
  <v-container>
    <v-row>
      <v-col
        cols="12"
        sm="12"
      >
        <v-textarea
          name="input-7-1"
          :label="$t('Observation')"
          hint="Hint text"
        ></v-textarea>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
export default {
  mounted(){

  },
  data(){
    return {
      tab: null,
      rules: []
    }
  },
  components: {

  }

}
</script>
