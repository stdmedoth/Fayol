import Vue from 'vue'
import VueRouter from 'vue-router'
import DashBoard from '@/views/DashBoard.vue';
import PeopleRegisters from '@/views/Registers/People.vue';
import ProductsRegisters from '@/views/Registers/Products/Products.vue';

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'Main',
    component: DashBoard
  },
  {
    path: '/dashboard',
    name: 'DashBoard',
    component: DashBoard
  },
  {
    path: '/registers/products',
    name: 'Products',
    component: ProductsRegisters
  },
  {
    path: '/registers/people',
    name: 'People',
    component: PeopleRegisters
  },

]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
