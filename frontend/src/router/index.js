import Vue from 'vue'
import VueRouter from 'vue-router'

import Dashboard from '../views/Dashboard.vue'
import CreateCustomer from '../views/CreateCustomer.vue'
import ViewCustomer from '../views/ViewCustomer.vue'
import EditCustomer from '../views/EditCustomer.vue'

import ViewContact from '../views/ViewContact.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'Dashboard',
    component: Dashboard
  },
  {
    path: '/customers/create',
    name: 'Create Customers',
    component: CreateCustomer
  },
  {
    path: '/customers/:customerId',
    name: 'View Customer',
    component: ViewCustomer
  },
  {
    path: '/customers/:customerId/edit',
    name: 'Edit Customer',
    component: EditCustomer
  },
  {
    path: '/contacts/:contactId',
    name: 'View Contact',
    component: ViewContact
  },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
