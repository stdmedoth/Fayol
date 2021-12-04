<template>
  <div id="dashboard_page">
    <v-row>
      <v-col sm="12">
        <Banner />
      </v-col>
    </v-row>
    <v-row>
      <v-col
        sm="6"
      >
        <Calendar />
      </v-col>
      <v-col
        sm="6"
      >
        <Notes />
      </v-col>
    </v-row>
  </div>
</template>

<script>
import Banner from '@/components/widgets/Banner';
import Calendar from '@/components/widgets/Calendar';
import Notes from '@/components/widgets/Notes';
export default {
  name: 'DashBoard',
  data(){
    return {

    }
  },
  components: {
    Calendar,
    Banner,
    Notes
  }
}
</script>
