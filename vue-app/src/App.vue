<template>
  <v-app>
    <VBar />
    <VNavigationDrawer />
    <VMain />
  </v-app>
</template>

<script>
import VMain from '@/components/Layout/VMain';
import VBar from '@/components/Layout/VBar'
import VNavigationDrawer from '@/components/Layout/VNavigationDrawer'
  export default{
    data(){
      return {

      }
    },
    components: {
      VMain,
      VBar,
      VNavigationDrawer
    }
  }
</script>

<style>

</style>
