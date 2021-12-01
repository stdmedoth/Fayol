<template>
  <div id="dashboard_page">
    <v-parallax
      height="200"
      src="https://cdn.vuetifyjs.com/images/parallax/material2.jpg"
    >
      <v-row
        align="center"
        justify="center"
      >
        <v-col
          class="text-center"
          cols="12"
        >
          <h1 class="text-h4 font-weight-thin mb-4">
            {{AppName}}
          </h1>
          <h4 class="subheading">
            Your simple Integrated Management System (IMS)
          </h4>
        </v-col>
      </v-row>
    </v-parallax>
  </div>
</template>

<script>


export default {
  name: 'DashBoard',
  data(){
    return {
      AppName: 'Fayol'
    }
  },
  components: {

  }
}
</script>
