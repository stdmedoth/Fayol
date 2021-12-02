<template id="">
  <v-container scrolled>
    <v-row class="mt-5">
      <v-col
        md="3"
      >
        <v-select :items="documentTypes" v-model="doc_type" item-text="text" item-value="value">
        </v-select>
      </v-col>
      <v-col md="7">
        <v-text-field
          :label="$t('Document ID 1')"
          v-model="form_values.doc1_id"
          return-masked-value
          v-mask="doc1_mask"
        ></v-text-field>
      </v-col>
      <v-col md="2">
        <v-btn>{{$t('Extern Search People')}}</v-btn>
      </v-col>
    </v-row>
    <v-row>
      <v-col md="3">
        <v-text-field
          :label="$t('Document ID 2')"
          v-model="form_values.doc2_id"
          return-masked-value
          v-mask="doc2_mask"
        ></v-text-field>
      </v-col>
      <v-col md="3">
        <v-select
          :label="$t('Person Type')"
          v-model="form_values.person_type"
          :items="personTypes"
        >
      </v-select>
      </v-col>
      <v-col md="3">
        <v-text-field
          :label="$t('Extern Code')"
          v-model="form_values.extern_code"
        ></v-text-field>
      </v-col>
      <v-col md="3">
        <v-text-field
          :label="$t('Since')"
          v-model="form_values.since"
          v-mask="$t('date_format')"
        ></v-text-field>
      </v-col>
    </v-row>
    <v-row>
      <v-col md="12">
      <v-text-field
        :label="$t('Person Name 1')"
        v-model="form_values.name1"
      ></v-text-field>
      </v-col>
    </v-row>
    <v-row>
      <v-col md="12">
      <v-text-field
        :label="$t('Person Name 2')"
        v-model="form_values.name2"
      ></v-text-field>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
export default {
  computed:{
    doc1_mask: {
      get(){
        let doc =  this.documentTypes.find(e => e.value == this.doc_type);
        if(doc){
          return doc.doc1_mask
        }

        return '';
      },
      set(){

      }
    },
    doc2_mask: {
      get(){
        return '';
      },
      set(){
        return '';
      }
    }
  },
  mounted(){
    console.log(this.$i18n.messages.pt);
    this.doc_type = this.documentTypes[0];
  },
  data(){
    return {
      form_values: {
        name1: '',
        name2: '',
        person_type: '',
        doc1_id: '',
        doc2_id: '',
        extern_code: '',
        since: '',
      },
      doc_type: '',
      documentTypes: [
        {text: 'Juridica', value: 1, doc1_mask: '##.###.###/####-##'},
        {text: 'Física', value: 2, doc1_mask: '###.###.###-##'},
      ],
      personTypes: [
        {text: 'Cliente', value: 1,},
        {text: 'Fornecedor', value: 2,},
      ],
      tab: null,
      rules: []
    }
  },
  methods: {
    doc_type_changed(){
        console.log(this.doc_type)
    }
  },
  components: {

  }

}
</script>
