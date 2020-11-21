<template>
  <div>
    <b-table  :items="employees" :fields="fields" responsive="sm"></b-table>
    <table>
      <thead>
      <th>Фамилия</th>
      <th>Имя</th>
      <th>Отчество</th>
      <th>Должность</th>
      <th>Звание</th>
      <th>Пол</th>
      </thead>
      <tbody>
      <!--        eslint-disable-->
      <tr v-for="employee in employees" :key="employee.id">
        <td>{{ employee.sirname }}</td>
        <td>{{ employee.name }}</td>
        <td>{{ employee.secname }}</td>
        <td>{{ employee.position }}</td>
        <td>{{ employee.rank }}</td>
        <td>{{ employee.gender }}</td>
        <td>
          <b-button variant="danger" @click="removeEmployee(employee)">X</b-button>
        </td>
        <td>
          <b-button variant="warning" @click="editEmployee(employee)">edit</b-button>
        </td>
      </tr>
      </tbody>
    </table>

    <input placeholder="Фамилия" v-model="createdEmployee.sirname">
    <input placeholder="Имя" v-model="createdEmployee.name">
    <input placeholder="Отчество" v-model="createdEmployee.secname">
    <input placeholder="Должность" v-model="createdEmployee.position">
    <input placeholder="Звание" v-model="createdEmployee.rank">
    <input placeholder="Пол" v-model="createdEmployee.gender">
    <b-button variant="outline-primary" @click="createEmployee">Добавить</b-button>

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
      <tr v-for="employee in employees" :key="employee.id">
        <td>{{ employee.sirname }}</td>
        <td>{{ employee.name }}</td>
        <td>{{ employee.secname }}</td>
        <td>{{ employee.position }}</td>
        <td>{{ employee.rank }}</td>
        <td>{{ employee.gender }}</td>
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
  name: 'EmployeesList',

  data() {
    return {
      /* eslint-disable */
      fields: [
        {
          key: "sirname",
          sortable: true
        },
        {
          key: "name",
          sortable: true
        },
        {
          key: "secname",
          sortable: true,
        },
        {
          key: "position",
          sortable: true,
        },
        {
          key: "rank",
          sortable: true,
        },
        {
          key: "gender",
          sortable: true,
        },
      ],
      employees: [],
      createdEmployee: {},
    };
  },
  methods: {
    async fetchEmployees() {
      const response = await fetch('http://localhost:8000/api/v1/employee/')
      this.employees = await response.json()
    },
    async createEmployee() {
      const response = await fetch('http://localhost:8000/api/v1/employee/', {
        method: 'POST',
        headers: {
          'Accept': 'application/json',
          'Content-type': 'application/json'
        },
        body: JSON.stringify(this.createdEmployee)
      });

      if (response.status !== 201) {
        alert(JSON.stringify(await response.json(), null, 2));
      }
      await this.fetchEmployees()
    },
    /* eslint-disable */
    async removeEmployee(employee) {
      const {id} = employee;
      const response = await fetch(`http://localhost:8000/api/v1/employee/${id}/`, {
        method: 'DELETE',
        headers: {
          'Accept': 'application/json',
          'Content-type': 'application/json'
        },
      });
      if (response.status !== 204) {
        alert(JSON.stringify(await response.json(), null, 2));
      }
      await this.fetchEmployees()
    },
    async editEmployee(employee) {
      const {id} = employee;
      const response = await fetch(`http://localhost:8000/api/v1/employee/${id}/`, {
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
      await this.fetchEmployees()
    },
  },
  async created() {
    await this.fetchEmployees()
  },
};
</script>
