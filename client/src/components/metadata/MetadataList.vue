<template>
  <div>
    <b-table class="mt-3"
             striped hover
             ref="selectableTable"
             selectable
             :items="employeeList"
             :fields="fields"
             small>
    </b-table>
  </div>
</template>

<script>
/* eslint-disable */
  export default {
    name: 'MetadataList',

    data() {
      return {
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
        employeeList: [],
      };
    },
    methods: {
      async fetchEmployees() {
        const response = await fetch('http://localhost:8000/api/v1/employee/')
        this.employeeList = await response.json()
        this.employeeList = this.employeeList['employees']
      },
      // async createEmployee() {
      //   const response = await fetch('http://localhost:8000/api/v1/employee/', {
      //     method: 'POST',
      //     headers: {
      //       'Accept': 'application/json',
      //       'Content-type': 'application/json'
      //     },
      //     body: JSON.stringify(this.createdEmployee)
      //   });
      //   if (response.status !== 201) {
      //     alert(JSON.stringify(await response.json(), null, 2));
      //   }
      //   await this.fetchEmployees()
      // },
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
