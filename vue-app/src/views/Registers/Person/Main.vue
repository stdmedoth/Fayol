<template id="">
  <v-container>
    <v-row>
      <v-col md="2">
        <v-btn>{{$t('Extern Search Person')}}</v-btn>
      </v-col>
    </v-row>
    <v-row class="mt-5">
      <v-col
        cols="12"
        md="4"
      >
        <v-select
          :items="personTypes"
          v-model="form_values.doc_type.value"
          name="doc_type"
          item-text="text"
          item-value="value"
          :outlined="true"
          :clearable="true"
          :label="$t('Person Type')"
          @change='doc_type_changed'
          min-width="20"
        >
        </v-select>
      </v-col>
      <v-col
        cols="12"
        md="8"
      >
        <v-text-field
          :label="doc_name ? $t(doc_name) : $t('Choose the Person Type')"
          v-model="form_values.doc_id1.value"
          :rules="form_values.doc_id1.rules"
          name="doc_id1"
          return-masked-value
          v-mask="doc1_mask"
          :disabled="!form_values.doc_type.value"
          :outlined="true"
          @keydown.enter.prevent="inputEnter"
          :clearable="true"
        ></v-text-field>
      </v-col>
    </v-row>
    <v-row>
      <v-col
        cols="12"
        md="6"
      >
        <v-text-field
          :label="$t('Document ID 2')"
          v-model="form_values.doc_id2.value"
          :rules="form_values.doc_id2.rules"
          name="doc_id2"
          return-masked-value
          v-mask="doc2_mask"
          :outlined="true"
          :clearable="true"
        ></v-text-field>
      </v-col>
      <v-col md="6">
        <v-select
          :label="$t('Register Type')"
          v-model="form_values.register_type.value"
          :rules="form_values.register_type.rules"
          name="register_type"
          :items="registerTypes"
          :outlined="true"
          :clearable="true"
        >
      </v-select>
      </v-col>
    </v-row>
    <v-row>
      <v-col
        cols="12"
        md="6"
      >
        <v-text-field
          :label="$t('Extern Code')"
          v-model="form_values.extern_code.value"
          :rules="form_values.extern_code.rules"
          name="extern_code"
          :outlined="true"
          :clearable="true"
        ></v-text-field>
      </v-col>
      <v-col
        cols="12"
        md="6"
      >
        <v-text-field
          :label="$t('Since')"
          v-model="form_values.since.value"
          :rules="form_values.since.rules"
          v-mask="$t('date_format')"
          :outlined="true"
          :clearable="true"
        ></v-text-field>
      </v-col>
    </v-row>
    <v-row>
      <v-col
        cols="12"
        md="12"
      >
      <v-text-field
        :label="$t('Person Name 1')"
        v-model="form_values.name1.value"
        :rules="form_values.name1.rules"
        :outlined="true"
        :clearable="true"
      ></v-text-field>
      </v-col>
    </v-row>
    <v-row>
      <v-col
        cols="12"
        md="12"
      >
      <v-text-field
        :label="$t('Person Name 2')"
        v-model="form_values.name2.value"
        :rules="form_values.name2.rules"
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
    doc_name: {
      get(){
        let doc =  this.personTypes.find(e => e.value == this.form_values.doc_type.value);
        if(doc){
          return doc.doc1_name;
        }

        return '';
      },
      set(){

      }
    },
    doc1_mask: {
      get(){
        let doc =  this.personTypes.find(e => e.value == this.form_values.doc_type.value);
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
        name1: {value: '', rules: [v => v.length >= 1 || this.$t('Name field must be filled')], },
        name2: {value: '', /*rules: [v => v.length >= 1 || this.$t('Name 2 should be input')],*/ },
        person_type: {value: '', rules: [v => v.length >= 1 || this.$t('Person Type field must be filled')], },
        doc_id1: {value: '', /*rules: [v => v.length >= 1 || this.$t('Document 1 field must be filled')],*/ },
        doc_id2: {value: '', /*rules: [v => v.length >= 1 || this.$t('Document 2 field must be filled')],*/ },
        register_type: {value: '', rules: [v => v.length >= 1 || this.$t('Register Type must be filled')] },
        extern_code: {value: '', /*rules: [v => v.length >= 1 || this.$t('Extern Code field must be filled')],*/ },
        since: {value: '', /*rules: [v => v.length >= 1 || this.$t('Since field must be filled')],*/ },
        doc_type: {value: false, },
      },
      personTypes: [
        {text: this.$t('Legal'), value: 1, doc1_name: this.$t('Legal Person Doc'), doc1_mask: '##.###.###/####-##'},
        {text: this.$t('Physical'), value: 2, doc1_name: this.$t('Physical Person Doc'), doc1_mask: '###.###.###-##'},
      ],
      registerTypes: [
        {text: 'Cliente', value: 1,},
        {text: 'Fornecedor', value: 2,},
      ],
      tab: null,
      rules: []
    }
  },
  methods: {
    inputEnter(e){
      let element = e.target;
      let form_element = this.form_values[element.name];
      console.log(form_element);
    },
    doc_type_changed(){
      if(this.form_values.doc_type.value == null){
        this.form_values.doc_id1 = '';
      }
    }
  },
  components: {

  }

}
</script>
