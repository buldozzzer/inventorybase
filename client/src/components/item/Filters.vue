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
        <b-col>
          <b-form-select
            v-model="filters.otss_category"
            :options="otssCategories"
          ></b-form-select>
        </b-col>
        <b-col>
          <b-form-select
            v-model="filters.condition"
            :options="conditions"
          ></b-form-select>
        </b-col>
        <b-col>
          <b-form-select
            v-model="filters.in_operation"
            :options="operation"
          ></b-form-select>
        </b-col>
        <b-col>
          <b-button variant="dark" @click="resetFilters">Сбросить фильтры</b-button>
        </b-col>
      </b-row>
    </b-container>
  </div>
</template>

<script>
/* eslint-disable */
  import {bus} from '../../main'

  export default {
    name: "Filters",
    props: ['employeeInitials'],
    data() {
      return {
        otssCategories: [1, 2, 3, 'Не секретно', {text: '-', value: null}],
        conditions: ['Исправно', 'Неисправно', {text: '-', value: null}],
        operation: ['Используется', 'Не используется', {text: '-', value: null}],
        filters: {
          responsible: null,
          otss_category: null,
          condition: null,
          in_operation: null
        },
        employees: []
      }
    },
    methods:{
      setEmployees(){
        this.employees = this.employeeInitials
        this.employees.push({text: '-', value: null})
      },
      resetFilters(){
        this.filters = {
          responsible: null,
          otss_category: null,
          condition: null,
          in_operation: null
        }
        bus.$emit('resetFilters', this.filters)
      }
    },
    async created(){
      await this.setEmployees()
    }
  }
</script>

<style scoped>

</style>
