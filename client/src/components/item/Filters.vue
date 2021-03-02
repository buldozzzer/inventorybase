<template>
  <div class="p-3 mb-2 bg-gradient-primary">
    <b-container>
      <b-row class="text-center">
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
        <b-col align="center">
          <b-icon icon="arrow-counterclockwise"
                  type="button"
                  data-toggle="tooltip"
                  class="mt-4"
                  data-placement="top"
                  title="Сбросить фильтры"
                  font-scale="2"
                  aria-hidden="false"
                  @click="resetFilters"></b-icon>
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
        otssCategories: [],
        conditions: [],
        operation: ['Используется', 'Не используется', {text: '-', value: null}],
        units: [],
        filters: {
          responsible: null,
          otss_category: null,
          condition: null,
          in_operation: null,
        },
        employees: [],
        fuseString: ''
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
      async fetchOTSS() {
        let categories = {}
        const response = await fetch('http://localhost:8000/api/v1/otss/')
        categories = await response.json()
        categories = categories['otss']
        for(let key in categories){
          this.otssCategories.push(categories[key]['category'])
        }
        this.otssCategories.push({text: '-', value: null})
      },
      async fetchConditions() {
        let tempArr = []
        const response = await fetch('http://localhost:8000/api/v1/condition/')
        tempArr = await response.json()
        tempArr = tempArr['conditions']
        for (let i = 0; i < tempArr.length; ++i){
          this.conditions.push(tempArr[i]['condition'])
        }
        this.conditions.push({text: '-', value: null})
      },
      resetFilters(){
        this.filters = {
          responsible: null,
          otss_category: null,
          condition: null,
          in_operation: null
        }
        this.$parent.$data.fuseString = ''
        this.fuseString =''
        bus.$emit('resetFilters', this.filters)
      },
      async fetchUnits() {
        let tempArr = []
        const response = await fetch('http://localhost:8000/api/v1/unit/')
        tempArr = await response.json()
        tempArr = tempArr['units']
        for (let i = 0; i < tempArr.length; ++i){
          this.units.push(tempArr[i]['unit'])
        }
      }
    },
    watch:{
      fuseString: function (){
        this.$parent.$data.fuseString = this.fuseString
        bus.$emit('changeFuseString', this.fuseString)
      }
    },
    async created(){
      await this.createEmployeeList()
      await this.fetchOTSS()
      await this.fetchConditions()
    }
  }
</script>

<style scoped>

</style>
