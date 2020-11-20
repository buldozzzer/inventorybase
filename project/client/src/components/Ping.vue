<template>
  <div>
    <b-table striped hover :items="items" :fields="fields"></b-table>
  </div>
</template>

<script>

import axios from 'axios';

export default {
  name: 'EmployeesView',
  data() {
    return {
      /* eslint-disable */
      fields: [
        {
          key: 'sirname',
          sortable: true
        },
        {
          key: 'name',
          sortable: false
        },
        {
          key: 'secname',
          sortable: true,
        },
        {
          key: 'position',
          sortable: true,
        },
        {
          key: 'rank',
          sortable: true,
        },
        {
          key: 'gender',
          sortable: true,
        },
      ],
      employees: [],
      employee: null
    };
  },
  methods: {
    getEmployees() {
      const path = 'http://localhost:8000/api/v1/employee/';
      axios.get(path)
        .then((res) => {
          this.employees = res.data;
        })
        .catch((error) => {
          /* eslint-disable */
          console.error(error);
        });
    },
  },
  async created() {
    await this.getEmployees();
  },
  mounted() {
    this.employee = this.employees.length
  }
};
</script>
