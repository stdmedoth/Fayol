<template id="">
  <div class="products_registers">
    <v-card
      class="d-flex flex-column"
      height="500"
      elevation="24"
    >
      <v-card-text style="height: 400px; overflow: auto;">
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
import Information from '@/views/Registers/Products/Information';
import Revenues from '@/views/Registers/Products/Revenues';
import Complement from '@/views/Registers/Products/Complement';

export default {
  mounted(){

  },
  data(){
    return {
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
