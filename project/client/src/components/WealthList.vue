<template>
  <div>
    <b-table :items="wealth" :fields="fields" responsive="sm"></b-table>
    <table>
      <tbody>
      <!--        eslint-disable-->
      <tr v-for="w in wealth" :key="w.id">
        <td>{{ w.sirname }}</td>
        <td>{{ w.name }}</td>
        <td>{{ w.secname }}</td>
        <td>{{ w.position }}</td>
        <td>{{ w.rank }}</td>
        <td>{{ w.gender }}</td>
        <td>
          <b-button variant="danger" @click="removeWealth(w)">X</b-button>
        </td>
        <td>
          <b-button variant="warning" @click="editWealth(w)">edit</b-button>
        </td>
      </tr>
      </tbody>
    </table>

    <input placeholder="Фамилия" v-model="createdWealth.sirname">
    <input placeholder="Имя" v-model="createdWealth.name">
    <input placeholder="Отчество" v-model="createdWealth.secname">
    <input placeholder="Должность" v-model="createdWealth.position">
    <input placeholder="Звание" v-model="createdWealth.rank">
    <input placeholder="Пол" v-model="createdWealth.gender">
    <b-button variant="outline-primary" @click="createdWealth">Добавить</b-button>

    <table>
      <thead>
      <tr>
        <th>Фамилия</th>
        <th>Имя</th>
        <th>Отчество</th>
        <th>Должность</th>
        <th>Звание</th>
        <th>Пол</th>
      </tr>
      </thead>
      <tbody>
      <tr v-for="w in wealth" :key="w.id">
        <td>{{ w.sirname }}</td>
        <td>{{ w.name }}</td>
        <td>{{ w.secname }}</td>
        <td>{{ w.position }}</td>
        <td>{{ w.rank }}</td>
        <td>{{ w.gender }}</td>
        <td>
          <button type="button" class="btn btn-warning btn-sm">Update</button>
          <button type="button" class="btn btn-danger btn-sm">Delete</button>
        </td>
      </tr>
      </tbody>
    </table>

  </div>
</template>


<script>
export default {
  name: "WealthList",
  data() {
    return {
      /* eslint-disable */
      fields: [
        {
          key: "user",
          sortable: true
        },
        {
          key: "response",
          sortable: true
        },
        {
          key: "name",
          sortable: true,
        },
        {
          key: "inventory_n",
          sortable: true,
        },
        {
          key: "otss_category",
          sortable: true,
        },
        {
          key: "condition",
          sortable: true,
        },{
          key: "unit_from",
          sortable: true,
        },{
          key: "in_operation",
          sortable: true,
        },{
          key: "fault_document_requisites",
          sortable: true,
        },{
          key: "date_of_receipt",
          sortable: true,
        },{
          key: "number_of_receipt",
          sortable: true,
        },{
          key: "requisites",
          sortable: true,
        },{
          key: "transfer_date",
          sortable: true,
        },{
          key: "otss_requisites",
          sortable: true,
        },{
          key: "spsi_requisites",
          sortable: true,
        },{
          key: "trnasfer_requisites",
          sortable: true,
        },{
          key: "last_check",
          sortable: true,
        },{
          key: "comment",
          sortable: true,
        },
      ],
      wealth: [],
      createdWealth: {},
    };
  },
  methods: {
    async fetchWealth() {
      const response = await fetch('http://localhost:8000/api/v1/wealth/')
      this.wealth = await response.json()
    },
    async createWealth() {
      const response = await fetch('http://localhost:8000/api/v1/wealth/', {
        method: 'POST',
        headers: {
          'Accept': 'application/json',
          'Content-type': 'application/json'
        },
        body: JSON.stringify(this.createdWealth)
      });

      if (response.status !== 201) {
        alert(JSON.stringify(await response.json(), null, 2));
      }
      await this.fetchWealth()
    },
    /* eslint-disable */
    async removeWealth(wealth) {
      const {id} = wealth;
      const response = await fetch(`http://localhost:8000/api/v1/wealth/${id}/`, {
        method: 'DELETE',
        headers: {
          'Accept': 'application/json',
          'Content-type': 'application/json'
        },
      });
      if (response.status !== 204) {
        alert(JSON.stringify(await response.json(), null, 2));
      }
      await this.fetchWealth()
    },
    async editWealth(wealth) {
      const {id} = wealth;
      const response = await fetch(`http://localhost:8000/api/v1/wealth/${id}/`, {
        method: 'PUT',
        body: JSON.stringify(data),
        headers: {
          'Accept': 'application/json',
          'Content-type': 'application/json'
        },
      });
      const json = await response.json();
      console.log('Успех:', JSON.stringify(json));
      if (response.status !== 201) {
        alert(JSON.stringify(await response.json(), null, 2));
      }
      await this.fetchWealth()
    },
  },
  async created() {
    await this.fetchWealth()
  },
};
</script>

<style scoped>

</style>
