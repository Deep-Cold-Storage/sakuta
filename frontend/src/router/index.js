import Vue from 'vue'
import VueRouter from 'vue-router'

import Dashboard from '../views/Dashboard.vue'

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
    component: () => import(/* webpackChunkName: "create-customer" */ '../views/Customer/CreateCustomer.vue')
  },
  {
    path: '/customers/:customerId',
    name: 'View Customer',
    component: () => import(/* webpackChunkName: "view-customer" */ '../views/Customer/ViewCustomer.vue')
  },
  {
    path: '/customers/:customerId/edit',
    name: 'Edit Customer',
    component: () => import(/* webpackChunkName: "edit-customer" */ '../views/Customer/EditCustomer.vue')
  },
  {
    path: '/customers/:customerId/contacts',
    name: 'Create Contact',
    component: () => import(/* webpackChunkName: "create-contact" */ '../views/Contact/CreateContact.vue')
  },
  {
    path: '/customers/:customerId/branches',
    name: 'Create Branch',
    component: () => import(/* webpackChunkName: "create-branch" */ '../views/Branch/CreateBranch.vue')
  },
  {
    path: '/contacts/:contactId',
    name: 'View Contact',
    component: () => import(/* webpackChunkName: "view-contact" */ '../views/Contact/ViewContact.vue')
  },
  {
    path: '/contacts/:contactId/edit',
    name: 'Edit Contact',
    component: () => import(/* webpackChunkName: "edit-contact" */ '../views/Contact/EditContact.vue')
  },
  {
    path: '/branches/:branchId/contacts',
    name: 'Assign Contact',
    component: () => import(/* webpackChunkName: "assign-contact" */ '../views/Branch/AssignContact.vue')
  },
  {
    path: '/branches/:branchId',
    name: 'View Branch',
    component: () => import(/* webpackChunkName: "view-branch" */ '../views/Branch/ViewBranch.vue')
  },
  {
    path: '/branches/:branchId/edit',
    name: 'Edit Branch',
    component: () => import(/* webpackChunkName: "edit-branch" */ '../views/Branch/EditBranch.vue')
  },
  {
    path: '*',
    name: 'Not Found',
    component: () => import(/* webpackChunkName: "not-found" */ '../views/NotFound.vue')
  },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
