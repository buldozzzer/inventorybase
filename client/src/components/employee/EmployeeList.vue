<template>
  <div>
  </div>
</template>

<script>
export default {
  name: 'EmployeeList',

  data() {
    return {
      /* eslint-disable */
      fields: [
        {
          key: "surname",
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
