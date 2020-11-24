<!--eslint-disable-->
<template>
  <div id="app">
    <div>
      <b-navbar toggleable="lg" type="dark" variant="info">
        <b-navbar-brand href=""><b>База материальных ценностей</b></b-navbar-brand>
        <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>
        <b-collapse id="nav-collapse" is-nav>
          <b-navbar-nav>
            <b-nav-item-dropdown text="Добавить">
              <b-dropdown-item v-b-modal.add-item-modal>Добавить запись в базу мат. ценностей</b-dropdown-item>
              <b-dropdown-item href="#">Добавить запись в базу сотрудиков</b-dropdown-item>
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
    <add-modal></add-modal>
  </div>
</template>

<script>
/* eslint-disable */
import AddModal from "./components/AddModal";

export default {
  name: 'App',

  components: {
    AddModal,
  },
  methods: {

  }
};

</script>

<style>
</style>
