<template>
  <div class="p-3 mb-2 bg-gradient-primary">
    <b-container>
      <b-row>
        <b-col>
          <b-form-select
            v-model="filters.responsible"
            :options="employeeInitials"
          ></b-form-select>
        </b-col>
      </b-row>
    </b-container>
  </div>
</template>

<script>
/* eslint-disable */
  export default {
    name: "Filters",
    props: ['employeeInitials'],
    data() {
      return {
        filters: {
          responsible: null
        },
        employees: []
      }
    },
    methods:{
      setEmployees(){
        this.employees = this.employeeInitials
        this.employees.push({text: '-', value: null})
      }
    },
    async created(){
      await this.setEmployees()
    }
  }
</script>

<style scoped>

</style>
