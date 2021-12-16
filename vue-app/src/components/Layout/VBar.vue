<template>
  <div>
    <v-app-bar
      app
      dense
      clipped-left
      dark
    >
      <v-app-bar-nav-icon v-if="$isMobile()" @click="$root.$emit('navigation_drawer:change_mini')"></v-app-bar-nav-icon>

      <v-toolbar-title>{{AppName}}</v-toolbar-title>

      <v-spacer></v-spacer>

      <v-btn icon>
        <v-icon>mdi-bell</v-icon>
      </v-btn>

      <v-btn icon>
        <v-icon>mdi-magnify</v-icon>
      </v-btn>

      <v-menu
        left
        bottom
      >
        <template v-slot:activator="{ on, attrs }">
          <v-btn
            icon
            v-bind="attrs"
            v-on="on"
          >
            <v-icon>mdi-dots-vertical</v-icon>
          </v-btn>
        </template>
        <!-- add options menu -->

        <!-- add options menu -->
      </v-menu>
    </v-app-bar>
  </div>
</template>

<script>
  export default{
    data(){
      return {
        AppName: 'Fayol'
      }
    }
  }
</script>
