<template id="">
  <v-container>
    <v-row class="mt-5">
      <v-col
        cols="12"
        sm="6"
      >
        <vuetify-money
          :label="$t('Unitary Quantity')"
          :rules="rules"
          type="number"
          hide-details="auto"
          :outlined="true"
          :clearable="true"
          :options="currencyOptions"
        ></vuetify-money>
      </v-col>
      <v-col
        cols="12"
        sm="6"
      >
        <vuetify-money
          :label="$t('Retail quantity')"
          :rules="rules"
          type="number"
          hide-details="auto"
          :outlined="true"
          :clearable="true"
          :options="currencyOptions"
        ></vuetify-money>
      </v-col>
    </v-row>
    <v-row>
      <v-col
        cols="12"
        sm="6"
      >
        <v-text-field
          :label="$t('Group')"
          :rules="rules"
          type="text"
          :outlined="true"
          :clearable="true"
          hide-details="auto"
        ></v-text-field>
      </v-col>
      <v-col
        cols="12"
        sm="6"
      >
        <vuetify-money
          :label="$t('Main Price')"
          :rules="rules"
          type="number"
          hide-details="auto"
          :outlined="true"
          :clearable="true"
          :options="currencyOptions"
        ></vuetify-money>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
export default {
  props: {
    tabName: String
  },
  mounted(){
    this.$root.$on('products:submit', ()=>{
      let data = {name: this.tabName, values: this.form_fields};
      this.$root.$emit('products:submit:tab_values_loaded', data);
    })
  },
  data(){
    return {
      tab: null,
      rules: [],
      currencyOptions: {
        locale: "pt-BR",
        prefix: "R$",
        suffix: "",
        length: 11,
        precision: 2
      },
    }
  },
  components: {

  }

}
</script>
