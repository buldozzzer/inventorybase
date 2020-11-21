import Vue from 'vue';
import Router from 'vue-router';
/* eslint-disable */
import EmployeeList from "@/components/EmployeeList";
import WealthList from "@/components/WealthList";

Vue.use(Router);

export default new Router({
  routes: [
    {
      path: '/',
      name: 'WealthList',
      component: WealthList,
    },
    {
      path: '/employees',
      name: 'EmployeesList',
      component: EmployeeList,
    },
  ],
});
