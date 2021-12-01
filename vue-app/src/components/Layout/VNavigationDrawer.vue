<template>
  <v-navigation-drawer
    app
    dark
    permanent
    :mini-variant="mini"
    clipped
  >

    <v-divider></v-divider>

    <v-list
      dense
      nav
    >
      <div
        v-for="(item, item_i) in items"
        :key="item_i"
      >
        <div v-if="!item.childrens">
          <router-link
            style="text-decoration: none"
            :to="item.location"
            custom
          >
            <v-list-item>
              <v-list-item-icon>
                <v-icon>{{ item.icon }}</v-icon>
              </v-list-item-icon>

              <v-list-item-content>
                <v-list-item-title>{{ $t(item.title) }}</v-list-item-title>
              </v-list-item-content>
            </v-list-item>
          </router-link>
        </div>
        <div v-else>
          <v-list-group
            :prepend-icon="item.icon"
          >
            <template v-slot:activator>
              <v-list-item-title>{{ $t(item.title) }}</v-list-item-title>
            </template>
            <router-link
              style="text-decoration: none"
              v-for="(children, children_i) in item.childrens"
              :key="children_i"
              :to="children.location"
              custom
            >
              <v-list-item >
                <v-list-item-content class="ml-10">
                  <v-list-item-title right>{{ $t(children.title) }}</v-list-item-title>
                </v-list-item-content>
                <v-list-item-icon>
                  <v-icon>{{ children.icon }}</v-icon>
                </v-list-item-icon>
              </v-list-item>
            </router-link>
          </v-list-group>
        </div>
      </div>
    </v-list>
  </v-navigation-drawer>
</template>

<script>
  export default {
    mounted(){
      this.$root.$on('navigation_drawer:change_mini', ()=>{
        this.mini = !this.mini;
      })
    },
    data () {
      return {
        mini: true,
        items: [
          { title: 'Dashboard', icon: 'mdi-view-dashboard', location: '/dashboard' },
          { title: 'Registers', icon: 'mdi-plus-circle-outline', childrens: [
            { title: 'Products', icon: 'mdi-archive-plus-outline', location: '/registers/products' },
            { title: 'People', icon: 'mdi-account-group', location: '/registers/people' },
          ] },
          { title: 'Financial', icon: 'mdi-wallet', childrens: [
            { title: 'Entradas', icon: 'mdi-cash-plus', location: '/financial/inflows' },
            { title: 'Saídas', icon: 'mdi-cash-minus', location: '/financial/outflows' },
          ]},
          { title: 'Inventory', icon: 'mdi-package-variant', childrens: [
            { title: 'Entradas', icon: 'mdi-store-plus', location: '/inventory/inflows' },
            { title: 'Saídas', icon: 'mdi-store-minus', location: '/inventory/outflows' },
          ] },
        ],
        right: null,
      }
    },
  }
</script>
