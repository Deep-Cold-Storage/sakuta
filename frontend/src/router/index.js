import Vue from 'vue'
import VueRouter from 'vue-router'

import Dashboard from '../views/Dashboard.vue'
import CreateCustomer from '../views/CreateCustomer.vue'
import ViewCustomer from '../views/ViewCustomer.vue'
import EditCustomer from '../views/EditCustomer.vue'

import ViewContact from '../views/ViewContact.vue'
import CreateContact from '../views/CreateContact.vue'
import EditContact from '../views/EditContact.vue'

import ViewBranch from '../views/ViewBranch.vue'
import CreateBranch from '../views/CreateBranch.vue'
import EditBranch from '../views/EditBranch.vue'
import AssignContact from '../views/AssignContact.vue'



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
    path: '/customers/:customerId/contacts',
    name: 'Create Contact',
    component: CreateContact
  },
  {
    path: '/contacts/:contactId',
    name: 'View Contact',
    component: ViewContact
  },
  {
    path: '/contacts/:contactId/edit',
    name: 'Edit Contact',
    component: EditContact
  },
  {
    path: '/branches/:branchId',
    name: 'View Branch',
    component: ViewBranch
  },
  {
    path: '/customers/:customerId/branches',
    name: 'Create Branch',
    component: CreateBranch
  },
  {
    path: '/branches/:branchId/edit',
    name: 'Edit Branch',
    component: EditBranch
  },
  {
    path: '/branches/:branchId/contacts',
    name: 'Assign Contact',
    component: AssignContact
  },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
