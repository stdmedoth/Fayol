<template id="">
  <v-sheet
    elevation="24"
    :shaped="true"
    :rounded="true"
  >
    <v-parallax
      height="200"
      :src="image_url"
    >
      <v-row
        align="center"
        justify="center"
      >
        <v-col
          sm="6"
        >
          <h1 class="text-h1 font-weight-bold mb-4">
            {{AppName}}
          </h1>
          <h4 class="subheading">
            Your simple Integrated Management System (IMS)
          </h4>
        </v-col>
        <v-col
          sm="6"
        >
          <v-img src="@/assets/imgs/department.png" />
        </v-col>
      </v-row>
    </v-parallax>
  </v-sheet>
</template>

<script>
  export default {
    data(){
      return {
        AppName: 'Fayol',
        image_url: 'https://cdn.vuetifyjs.com/images/parallax/material2.jpg'

      }
    }
  }
</script>
