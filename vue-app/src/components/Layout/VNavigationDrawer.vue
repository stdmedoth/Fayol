<template>
  <v-navigation-drawer
    app
    dark
    permanent
    clipped
    v-if="($isMobile() && !mini) || (!$isMobile())"
    :mini-variant="mini"
    :expand-on-hover="hover"
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
                <v-icon :color="($route.name == 'Main') || ($route.name == 'DashBoard') ? 'blue' : ''">{{ item.icon }}</v-icon>
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
              <v-list-item>
                <v-list-item-icon :class="!mini && !hover ? 'ml-10' : 'ml-00'">
                  <v-icon color="blue">{{ children.icon }}</v-icon>
                </v-list-item-icon>
                <v-list-item-content>
                  <v-list-item-title right>{{ $t(children.title) }}</v-list-item-title>
                </v-list-item-content>
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
      this.$root.$on('navigation_drawer:change_lock', ()=>{
        this.hover = !this.hover;
      });
      this.$root.$on('navigation_drawer:change_mini', ()=>{
        this.hover = !this.mini;
        this.mini = !this.mini;
      });
      if(this.$isMobile()){
        this.$root.$emit('navigation_drawer:change_mini');
      }
    },
    data () {
      return {
        mini: false,
        hover: true,
        items: [
          { title: 'Dashboard', icon: 'mdi-view-dashboard', location: '/dashboard' },
          { title: 'Registers', icon: 'mdi-plus-circle-outline', childrens: [
            { title: 'Products', icon: 'mdi-package-variant-closed', location: '/registers/products' },
            { title: 'Person', icon: 'mdi-account-group', location: '/registers/Person' },
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
