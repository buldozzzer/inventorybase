import Vue from 'vue';
import Router from 'vue-router';
/* eslint-disable */
import EmployeeList from "@/components/metadata/MetadataList";
import ItemList from "@/components/item/ItemList";
import GroupAddPage from "@/components/item/add/group/GroupAddPage";
import GroupEditPage from "@/components/item/edit/group/GroupEditPage";

Vue.use(Router);

export default new Router({
  routes: [
    {
      path: '/items',
      name: 'ItemList',
      component: ItemList,
    },
    {
      path: '/metadata',
      name: 'MetadataList',
      component: EmployeeList,
    },
    {
      path: '/items/groupadd',
      name: 'GroupAddPage',
      component: GroupAddPage,
    },
    {
      path: '/items/groupedit',
      name: 'GroupEditPage',
      component: GroupEditPage,
    },
  ],
});
