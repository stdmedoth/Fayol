<template id="">
  <v-container scrolled>
    <v-row class="mt-5">
      <v-col
        sm="3"
      >
        <v-select
          :label="$t('Payment Condition')"
          :items="paymentsConditions"
          v-model="form_values.payment_condition"
          item-text="text"
          item-value="value"
          :outlined="true"
          :clearable="true"
        >
        </v-select>
      </v-col>
      <v-col sm="7">
        <v-checkbox
          v-model="form_values.paid_shipping"
          :label="$t('Paid Shipping')"
        >
        </v-checkbox>
        <vuetify-money
          :disabled="!form_values.paid_shipping"
          :label="$t('Minimum value for paid shipping')"
          v-model="form_values.paid_freight"
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
  computed:{

  },
  mounted(){
    this.form_values.payment_condition = this.paymentsConditions[0];
  },
  data(){
    return {
      form_values: {
        payment_condition: '',
        paid_shipping: false,
      },
      paymentsConditions: [
        {text: 'Teste1', value: 1},
        {text: 'Teste2', value: 2},
      ],
      tab: null,
      rules: []
    }
  },
  methods: {

  },
  components: {

  }

}
</script>
