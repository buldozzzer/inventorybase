import Vue from 'vue';
import Router from 'vue-router';
/* eslint-disable */
import EmployeeList from "@/components/EmployeeList";
import ItemList from "@/components/ItemList";

Vue.use(Router);

export default new Router({
  routes: [
    {
      path: '/',
      name: 'ItemList',
      component: ItemList,
    },
    {
      path: '/employees',
      name: 'EmployeesList',
      component: EmployeeList,
    },
  ],
});
