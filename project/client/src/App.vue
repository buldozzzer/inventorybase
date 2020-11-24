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
            <b-nav-form>
              <vue-range-slider ref="slider"
                                v-model="SliderValue"
                                @change="stickyHeaderHeightToString"
                                min="300"
                                max="1000"
              ></vue-range-slider>
            </b-nav-form>

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
import ItemList from "./components/ItemList";
import AddModal from "./components/AddModal";
import VueRangeSlider from 'vue-range-slider'
import 'vue-range-slider/dist/vue-range-slider.css'

export default {
  name: 'App',
  components: {
    AddModal,
    VueRangeSlider
  },
  methods: {
    stickyHeaderHeightToString() {
      this.stickyHeaderHeight = this.SliderValue.toString() + 'px'
      return this.stickyHeaderHeight
    },
  }
};

</script>

<style>
</style>
