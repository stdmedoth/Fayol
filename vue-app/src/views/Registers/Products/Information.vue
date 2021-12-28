<template id="">
  <v-container>
    <v-row class="mt-5">
      <v-col
        cols="12"
        sm="12"
      >
        <v-text-field
          :label="$t('Product Name')"
          type="text"
          :outlined="true"
          v-model="form_fields.product_name.value"
          :rules="form_fields.product_name.rules"
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
          type="number"
          :outlined="true"
          :clearable="true"
          hide-details="auto"
          v-model="form_fields.weight.value"
          :rules="form_fields.weight.rules"
        ></v-text-field>
      </v-col>
      <v-col
        cols="12"
        sm="6"
      >
        <v-autocomplete
          :items="suppliers"
          :filter="customFilter"
          color="white"
          item-value="id"
          item-text="name"
          :label="$t('Supplier')"
          :outlined="true"
          :clearable="true"
          :search-input.sync="searchSupplier"
          :loading="this.form_fields.supplier.isLoading"
          v-model="form_fields.supplier.value"
          :rules="form_fields.supplier.rules"
        ></v-autocomplete>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
export default {
  props: {
    tabName: String
  },
  watch: {
    searchSupplier () {
      this.form_fields.supplier.isLoading = true

      // Lazily load input items
      fetch('https://api.publicapis.org/entries')
      .then(res => res.json())
      .then(() => {
        this.suppliers = [
          { name: 'JOAO VICTOR CALISTO', id: 1 },
          { name: 'PEDRO ENRIQUE CALISTO', id: 2 },
          { name: 'MARCELENE BENJAMIN DE BRITO', id: 3 },
        ];

      })
      .catch(err => {
        console.log(err)
      })
      .finally(() => (this.form_fields.supplier.isLoading = false))
    },
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
      searchSupplier: null,
      suppliers: [

      ],
      form_fields: {
        product_name: {
          value: '',
          rules: [
            v => !!v || this.$t('Product Name is required'),
            v => (v && v.length <= 10) || 'Name must be less than 10 characters',
          ],
        },
        weight: {
          value: '',
          rules: [
            //v => !!v || 'Name is required',
            //v => (v && v.length <= 10) || 'Name must be less than 10 characters',
          ],
        },
        supplier: {
          isLoading: false,
          value: '',
          rules: [
            //v => !!v || 'Name is required',
            //v => (v && v.length <= 10) || 'Name must be less than 10 characters',
          ],
        },
      }
    }
  },
  methods: {
    customFilter (item, queryText) {
      const textOne = item.name.toLowerCase()
      const searchText = queryText.toLowerCase()

      return textOne.indexOf(searchText) > -1
    },
  },
  components: {

  }

}
</script>
