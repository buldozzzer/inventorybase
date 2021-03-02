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
          <b-iconstack :title="message" @click="getConnection">
            <b-icon icon="diagram2-fill"
                    scale="1"
                    variant="success">
            </b-icon>
            <b-icon icon="slash-circle"
                    v-if="!connection"
                    scale="1.25"
                    variant="danger">
            </b-icon>
          </b-iconstack>
        </b-navbar-nav>
      </b-collapse>
    </b-navbar>
  </div>
</template>

<script>
/* eslint-disable */
export default {
  name: 'Nav',
  data(){
    return{
      connection: false,
      message: 'Соединение с сервером отсутствует'
    }
  },
  methods:{
    async getConnection(){
      const response = await fetch(`http://localhost:8000/api/v1/test/`)
      if(response.status === 200) {
        this.connection = true
        this.message = 'Соединение с сервером установлено'
      }
    }
  },
  async created() {
    await this.getConnection()
  }
};
</script>

<style scoped>

</style>
