<template>
  <v-app>
    <VBar />
    <VNavigationDrawer />
    <v-main app>
      <v-container fluid>
        <router-view></router-view>
      </v-container>
    </v-main>
    <v-footer app>
    </v-footer>
  </v-app>
</template>

<script>
import VBar from '@/components/Layout/VBar'
import VNavigationDrawer from '@/components/Layout/VNavigationDrawer'
  export default{
    data(){
      return {

      }
    },
    components: {
      VBar,
      VNavigationDrawer
    }
  }
</script>

<style>

</style>
