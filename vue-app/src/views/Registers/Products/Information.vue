<template id="">
  <v-container>
    <v-row>
      <v-col
        cols="12"
        md="12"
      >
        <v-text-field
          :label="$t('Product Name')"
          :rules="rules"
          hide-details="auto"
        ></v-text-field>
      </v-col>
    </v-row>
    <v-row>
      <v-col
        cols="12"
        md="6"
      >
        <v-text-field
          :label="$t('Weight')"
          :rules="rules"
          hide-details="auto"
        ></v-text-field>
      </v-col>
      <v-col
        cols="12"
        md="6"
      >
        <v-text-field
          :label="$t('Supplier')"
          :rules="rules"
          hide-details="auto"
        ></v-text-field>
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
