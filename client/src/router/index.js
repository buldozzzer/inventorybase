import Vue from 'vue';
import Router from 'vue-router';
/* eslint-disable */
import EmployeePage from "@/components/metadata/employee/EmployeePage";
import ItemList from "@/components/item/ItemList";
import GroupAddPage from "@/components/item/add/group/GroupAddPage";
import GroupEditPage from "@/components/item/edit/group/GroupEditPage";
import OTSSCategoryPage from "@/components/metadata/OTSS/OTSSCategoryPage";
import UnitPage from "../components/metadata/unit/UnitPage";
import CategoryPage from "../components/metadata/category/CategoryPage";
import LocationPage from "../components/metadata/location/LocationPage";
import TypePage from "../components/metadata/type/TypePage";
import ConditionPage from "../components/metadata/condition/ConditionPage";
import Test from "../components/item/recognize/RecognizeModal";

Vue.use(Router);

export default new Router({
  routes: [
    { path: '/', redirect: '/items/' },
    {
      path: '/items/groupadd/',
      name: 'GroupAddPage',
      component: GroupAddPage,
    },
    {
      path: '/items/groupedit/',
      name: 'GroupEditPage',
      component: GroupEditPage,
    },
    {
      path: '/items/',
      name: 'ItemList',
      component: ItemList,
    },
    {
      path: '/employees/',
      name: 'EmployeeList',
      component: EmployeePage,
    },
    {
      path: '/otss/',
      name: 'OTSSList',
      component: OTSSCategoryPage,
    },
    {
      path: '/units/',
      name: 'UnitList',
      component: UnitPage,
    },
    {
      path: '/categories/',
      name: 'CategoryList',
      component: CategoryPage,
    },
    {
      path: '/locations/',
      name: 'LocationList',
      component: LocationPage,
    },
    {
      path: '/types/',
      name: 'TypeList',
      component: TypePage,
    },
    {
      path: '/conditions/',
      name: 'ConditionList',
      component: ConditionPage,
    },
    {
      path: '/test2/',
      name: 'Test',
      component: Test
    }
  ],
});
