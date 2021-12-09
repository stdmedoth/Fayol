<template id="">
  <div class="products_registers">
    <v-card
      class="d-flex flex-column"
      height="500"
      elevation="24"
    >
      <v-card-text style="height: 400px; overflow: auto;">
        <v-form
          ref="products_registers_form"
          v-model="form_valid"
          lazy-validation
        >
          <v-toolbar
            dark
            flat
          >
            <v-card-title>{{$t('Person')}}</v-card-title>
            <template v-slot:extension>
              <v-tabs
                v-model="tab"
                align-with-title
              >
                <v-tabs-slider color="black"></v-tabs-slider>
                <v-tab  v-for="(_tab, i) in tablist" :key="i">
                  {{$t(i)}}
                </v-tab>
              </v-tabs>
            </template>
          </v-toolbar>
          <v-tabs-items v-model="tab">
            <v-tab-item v-for="(component, i) in tablist" :key="i">
              <component :is="i" />
            </v-tab-item>
          </v-tabs-items>
        </v-form>
      </v-card-text>
      <v-spacer></v-spacer>
      <v-card-actions>
        <v-btn
          outlined
          :disabled="disable_action.conclude"
        >
          {{$t('Conclude')}}
        </v-btn>
        <v-btn
          outlined
          :disabled="disable_action.change"
        >
          {{$t('Change')}}
        </v-btn>
        <v-btn
          outlined
          color="red"
          :disabled="disable_action.cancel"
        >
        {{$t('Cancel')}}
        </v-btn>
        <v-btn
          outlined
          color="red"
          :disabled="disable_action.exclude"
        >
          {{$t('Exclude')}}
        </v-btn>
      </v-card-actions>
    </v-card>
  </div>
</template>

<script>
import Basic from  '@/views/Registers/Person/Main';
import Contacts from  '@/views/Registers/Person/Contacts';
import Address from  '@/views/Registers/Person/Address';
import Financial from  '@/views/Registers/Person/Financial';
import Others from  '@/views/Registers/Person/Others';

export default {
  mounted(){

  },
  data(){
    return {
      form_valid: false,
      tab: null,
      disable_action:{
        change: false,
        conclude: true,
        cancel: true,
        exclude: true
      },
      tablist: {
        Basic,
        Address,
        Contacts,
        Financial,
        //Others,
      }
    }
  },
  components: {
    Basic,
    Address,
    Contacts,
    Financial,
    Others,
  }

}
</script>
