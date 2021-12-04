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
          :items="contacts"
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
        {text: 'Nome', value: 'nome',},
        {text: 'Celular', value: 'celular',},
        {text: 'Telefone', value: 'telefone',},
        {text: 'E-mail', value: 'email', },
      ],
      contacts: [
        {
          nome: 'João Calisto',
          celular: '199202121',
          telefone: '192121212',
          email: 'dsadsadsa@dasdsa.com'
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
