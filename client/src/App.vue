<!--eslint-disable-->
<template>
  <div id="app">
    <div>
      <b-navbar toggleable="lg" type="dark" variant="dark">
        <b-navbar-brand href="#/items/"><b>База материальных ценностей</b></b-navbar-brand>
        <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>
        <b-collapse id="nav-collapse" is-nav>
          <b-navbar-nav>
            <b-nav-item-dropdown text="Таблицы">
              <b-dropdown-item href="#/items">Мат. ценности</b-dropdown-item>
              <b-dropdown-item href="#/employees">Сотрудники</b-dropdown-item>
              <b-dropdown-item href="#/categories">Категории</b-dropdown-item>
              <b-dropdown-item href="#/otss">Катеогрии ОТСС</b-dropdown-item>
              <b-dropdown-item href="#/locations">Местоположения</b-dropdown-item>
              <b-dropdown-item href="#/units">Подразделения</b-dropdown-item>
              <b-dropdown-item href="#/conditions">Состояния</b-dropdown-item>
              <b-dropdown-item href="#/types">Типы</b-dropdown-item>
            </b-nav-item-dropdown>
          </b-navbar-nav>

          <!-- Right aligned nav items -->
          <b-navbar-nav class="ml-auto">
            <b-nav-item-dropdown right>
              <!-- Using 'button-content' slot -->
              <template #button-content>
                <em>User</em>
              </template>
              <b-dropdown-item href="#">Profile</b-dropdown-item>
              <b-dropdown-item href="#">Sign Out</b-dropdown-item>
            </b-nav-item-dropdown>
          </b-navbar-nav>
        </b-collapse>
      </b-navbar>
    </div>
    <router-view/>
  </div>
</template>

<script>
/* eslint-disable */
  import { bus } from "@/main";
  export default {
    name: 'App',
    data() {
      return {
        dataForChildren: null
      }
    },
    async mounted() {
      await bus.$on('clearDataForChildren', () => {this.dataForChildren = null})
    }
  };
</script>

<style>

</style>
