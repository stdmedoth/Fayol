<template id="">
  <v-container>
    <v-row class="mt-5">
      <v-col
        cols="12"
        sm="12"
      >
        <v-text-field
          :label="$t('Product Name')"
          :rules="rules"
          type="text"
          :outlined="true"
          :clearable="true"
          hide-details="auto"
        ></v-text-field>
      </v-col>
    </v-row>
    <v-row>
      <v-col
        cols="12"
        sm="6"
      >
        <v-text-field
          :label="$t('Weight')"
          :rules="rules"
          type="number"
          :outlined="true"
          :clearable="true"
          hide-details="auto"
        ></v-text-field>
      </v-col>
      <v-col
        cols="12"
        sm="6"
      >
        <v-text-field
          :label="$t('Supplier')"
          :rules="rules"
          type="text"
          :outlined="true"
          :clearable="true"
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
