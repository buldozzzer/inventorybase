<template>
  <div class="p-3 mb-2 bg-gradient-primary">
    <b-container>
      <b-row>
        <b-col>
          <b-form-group label="Ответственный:">
            <b-form-select
              v-model="filters.responsible"
              :options="employees"/>
          </b-form-group>
        </b-col>
        <b-col>
          <b-form-group label="Категория ОТСС:">
            <b-form-select
              v-model="filters.otss_category"
              :options="otssCategories"/>
          </b-form-group>
        </b-col>
        <b-col>
          <b-form-group label="Состояние:">
            <b-form-select
              v-model="filters.condition"
              :options="conditions"/>
          </b-form-group>
        </b-col>
        <b-col>
          <b-form-group label="Использование:">
            <b-form-select
              v-model="filters.in_operation"
              :options="operation"/>
          </b-form-group>
        </b-col>
        <b-col>
          <b-form-group label="По контексту:">
            <b-form-input
              v-model="fuseString"
            ></b-form-input>
          </b-form-group>
        </b-col>
<!--        <b-col>-->
<!--          <b-button variant="dark" @click="changeString">-->
<!--            Применить фильтры-->
<!--          </b-button>-->
<!--        </b-col>-->
        <b-col>
          <b-button variant="dark" @click="resetFilters">
            Сбросить фильтры
          </b-button>
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
          in_operation: null,
        },
        employees: [],
        fuseString: null
      }
    },
    methods:{
      async createEmployeeList() {
        const response = await fetch('http://localhost:8000/api/v1/employee/')
        let payload = await response.json()
        payload = payload['employees']
        this.employeeToString(payload)
        this.employees.push({value: null, text: '-'})
      },
      employeeToString(payload) {
        for (let i = 0; i < payload.length; i++) {
          this.employees.push(
            payload[i].surname + ' ' +
            payload[i].name[0] + '.' +
            payload[i].secname[0] + '.');
        }
      },
      resetFilters(){
        this.filters = {
          responsible: null,
          otss_category: null,
          condition: null,
          in_operation: null
        }
        this.$parent.$data.fuseString = null
        bus.$emit('resetFilters', this.filters)
      },

    },
    watch:{
      fuseString: function (){
        this.$parent.$data.fuseString = this.fuseString
        bus.$emit('changeFuseString', this.fuseString)
      }
    },
    async created(){
      await this.createEmployeeList()
    }
  }
</script>

<style scoped>

</style>
