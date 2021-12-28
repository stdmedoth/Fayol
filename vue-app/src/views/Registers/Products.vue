<template id="">
  <div class="products_registers">
    <v-card
      class="d-flex flex-column"
      :height="$isMobile() ? 650 : 500"
      elevation="24"
    >
      <v-card-text :style="'overflow: auto;'">
        <v-form>
          <v-toolbar
            dark
            flat
          >
            <v-card-title>{{$t('Products')}}</v-card-title>
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
              <component :is="i" :tabName="i" />
            </v-tab-item>
          </v-tabs-items>
        </v-form>
      </v-card-text>
      <v-spacer></v-spacer>
      <v-card-actions>
        <v-btn
          class="ml-10"
          outlined
          @click="$root.$emit('products:submit')"
          v-if="disable_action.conclude"
        >
          {{$t('Conclude')}}
        </v-btn>
        <v-btn
          outlined
          v-if="disable_action.change"
        >
          {{$t('Change')}}
        </v-btn>
        <v-btn
          outlined
          color="red"
          v-if="disable_action.cancel"
        >
        {{$t('Cancel')}}
        </v-btn>
        <v-btn
          outlined
          color="red"
          v-if="disable_action.exclude"
        >
          {{$t('Exclude')}}
        </v-btn>
      </v-card-actions>
    </v-card>
  </div>
</template>

<script>
import Information from '@/views/Registers/Products/Information';
import Revenues from '@/views/Registers/Products/Revenues';
import Complement from '@/views/Registers/Products/Complement';

export default {
  mounted(){
    this.$root.$on('products:submit:tab_values_loaded', (tab_values)=>{
      let tab_length = Object.keys(this.tablist).length;

      let tab_submited = false;
      this.submit.tabs.forEach((tab) => {
        if(tab.name == tab_values.name){
          tab_submited = true;
        }
      });

      if(!tab_submited){
        this.submit.tabs.push({
          name: tab_values.name,
          values: tab_values.values,
          submited: true
        });
      }else{
        this.submit.tabs.forEach((tab) => {
          if(tab.name == tab_values.name){
            tab.submited = true;
          }else{
            tab.submited = false;
          }
        });
      }

      let tab_submited_length = this.submit.tabs.filter(t => t.submited ? true : false).length;
      if(tab_length == tab_submited_length ){
        this.$root.$emit('products:submit:alltabs_values_loaded');
      }
    });

    this.$root.$on('products:submit:alltabs_values_loaded', ()=>{
      console.log("Todas abas carregadas");
    })
  },
  data(){
    return{
      submit: {
        form_values: null,
        tabs: []
      },
      disable_action:{
        change: false,
        conclude: true,
        cancel: true,
        exclude: true
      },
      tab: null,
      tablist: {
        Information,
        Revenues,
        Complement
      }
    }
  },
  components: {
    Information,
    Revenues,
    Complement
  }

}
</script>
