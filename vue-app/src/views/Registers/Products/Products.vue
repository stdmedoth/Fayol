<template id="">
  <div class="products_registers">
    <v-card>
      <v-card-title>{{$t('Products')}}</v-card-title>
      <v-card-text height="200">
        <v-form>
          <v-toolbar
            color="grey"
            dark
            flat
          >
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
      <v-card-actions class="ml-10">
        <v-btn outlined>
          {{$t('Conclude')}}
        </v-btn>
        <v-btn outlined>
          {{$t('Change')}}
        </v-btn>
        <v-btn
          outlined
          color="red"
        >
          {{$t('Cancel')}}
        </v-btn>
        <v-btn
          outlined
          color="red"
        >
          {{$t('Exclude')}}
        </v-btn>
      </v-card-actions>
    </v-card>
  </div>
</template>

<script>
import Information from './Information';
import Revenues from './Revenues';
import Complement from './Complement';

export default {
  mounted(){

  },
  data(){
    return {
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
