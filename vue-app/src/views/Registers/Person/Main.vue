<template id="">
  <v-container scrolled>
    <v-row>
      <v-col sm="2">
        <v-btn>{{$t('Extern Search Person')}}</v-btn>
      </v-col>
    </v-row>
    <v-row class="mt-5">
      <v-col
        sm="4"
      >
        <v-select
          :items="documentTypes"
          v-model="doc_type"
          item-text="text"
          item-value="value"
          :outlined="true"
          :clearable="true"
          @change='doc_type_changed'
        >
        </v-select>
      </v-col>
      <v-col sm="8">
        <v-text-field
          :label="$t('Document ID 1')"
          v-model="form_values.doc_id1"
          return-masked-value
          v-mask="doc1_mask"
          :disabled="!doc_type"
          :outlined="true"
          :clearable="true"
        ></v-text-field>
      </v-col>
    </v-row>
    <v-row>
      <v-col sm="6">
        <v-text-field
          :label="$t('Document ID 2')"
          v-model="form_values.doc_id2"
          return-masked-value
          v-mask="doc2_mask"
          :outlined="true"
          :clearable="true"
        ></v-text-field>
      </v-col>
      <v-col sm="6">
        <v-select
          :label="$t('Person Type')"
          v-model="form_values.person_type"
          :items="personTypes"
          :outlined="true"
          :clearable="true"
        >
      </v-select>
      </v-col>
    </v-row>
    <v-row>
      <v-col sm="6">
        <v-text-field
          :label="$t('Extern Code')"
          v-model="form_values.extern_code"
          :outlined="true"
          :clearable="true"
        ></v-text-field>
      </v-col>
      <v-col sm="6">
        <v-text-field
          :label="$t('Since')"
          v-model="form_values.since"
          v-mask="$t('date_format')"
          :outlined="true"
          :clearable="true"
        ></v-text-field>
      </v-col>
    </v-row>
    <v-row>
      <v-col sm="12">
      <v-text-field
        :label="$t('Person Name 1')"
        v-model="form_values.name1"
        :outlined="true"
        :clearable="true"
      ></v-text-field>
      </v-col>
    </v-row>
    <v-row>
      <v-col sm="12">
      <v-text-field
        :label="$t('Person Name 2')"
        v-model="form_values.name2"
        :outlined="true"
        :clearable="true"
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
          return doc.doc1_mask;
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

  },
  data(){
    return {
      form_values: {
        name1: '',
        name2: '',
        person_type: '',
        doc_id1: '',
        doc_id2: '',
        extern_code: '',
        since: '',
      },
      doc_type: false,
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
      if(this.doc_type == null){
        this.form_values.doc_id1 = '';
      }
    }
  },
  components: {

  }

}
</script>
