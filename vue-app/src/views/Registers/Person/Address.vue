<template id="">
  <v-container>
    <v-row class="mt-5">
      <v-col
        sm="9"
      >
      </v-col>
      <v-col
        sm="3"
      >
        <v-spacer></v-spacer>
        <v-btn dark>Adicionar Novo</v-btn>
      </v-col>
    </v-row>
    <v-row class="mt-5">
      <v-col
        cols="12"
        sm="12"
      >
        <v-data-table
          :headers="headers"
          :items="address"
          :items-per-page="5"
          class="elevation-1"
        >
        </v-data-table>
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
      headers: [
        {text: 'Logradouro', value: 'logradouro',},
        {text: 'Número', value: 'numero',},
        {text: 'Cidade', value: 'cidade', },
        {text: 'Estado', value: 'estado',},
      ],
      address: [
        {
          logradouro: 'Rua dsadasdsa dadsadas',
          numero: '10',
          cidade: 'Campinas',
          estado: 'SP'
        }
      ],

      tab: null,
      rules: []
    }
  },
  components: {

  }

}
</script>
