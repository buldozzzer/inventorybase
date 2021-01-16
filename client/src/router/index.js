import Vue from 'vue';
import Router from 'vue-router';
/* eslint-disable */
import EmployeeList from "@/components/employee/EmployeeList";
import ItemList from "@/components/item/ItemList";

Vue.use(Router);

export default new Router({
  routes: [
    {
      path: '/items',
      name: 'ItemList',
      component: ItemList,
    },
    {
      path: '/employees',
      name: 'EmployeeList',
      component: EmployeeList,
    },
  ],
});
