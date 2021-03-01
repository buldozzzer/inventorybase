<template>
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
        <b-navbar-nav class="ml-auto">
        </b-navbar-nav>
      </b-collapse>
    </b-navbar>
  </div>
</template>

<script>
export default {
  name: 'Nav',
};
</script>

<style scoped>

</style>
