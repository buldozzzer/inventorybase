<template>
  <div class="p-3 mb-2 bg-gradient-primary" style="z-index: 1000">
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

      <b-row class="text-center">
        <b-col>
          <b-form-group label="Кому передано:">
            <b-form-select
              v-model="filters.user"
              :options="employees"/>
          </b-form-group>
        </b-col>
        <b-col>
          <b-form-group label="Объект:">
            <b-form-select
              v-model="filters.location_object"
              :options="points[0]"/>
          </b-form-group>
        </b-col>
        <b-col>
          <b-form-group label="Подразделение:">
            <b-form-select
              v-model="filters.location_unit"
              :options="points[3]"/>
          </b-form-group>
        </b-col>
        <b-col>
          <b-form-group label="Использование:">
            <b-form-select
              v-model="filters.location_corpus"
              :options="points[2]"/>
          </b-form-group>
        </b-col>
        <b-col>
          <b-form-group label="По контексту:">
            <b-form-select
              v-model="filters.location_cabinet"
              :options="points[1]">
            </b-form-select>
          </b-form-group>
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
    props: ['prep_employees', 'filters'],
    data() {
      return {
        otssCategories: [],
        conditions: [],
        operation: ['Используется', 'Не используется', {text: '-', value: null}],
        units: [],
        // filters: {
        //   responsible: null,
        //   otss_category: null,
        //   condition: null,
        //   in_operation: null,
        // },
        employees: [],
        fuseString: '',
        locations: []
      }
    },
    computed:{
      points: function () {
        let objects = []
        let cabinets = []
        let corpuses = []
        let units =[]

        for(let i = 0; i < this.locations.length; ++i){
          objects.push(this.locations[i]['object'])
          cabinets.push(this.locations[i]['cabinet'])
          corpuses.push(this.locations[i]['corpus'])
          units.push(this.locations[i]['unit'])
        }

        objects.push({value: null, text: '-'})
        cabinets.push({value: null, text: '-'})
        corpuses.push({value: null, text: '-'})
        units.push({value: null, text: '-'})

        return [objects, cabinets, corpuses, units]
      }
    },
    methods:{
      createEmployeeList() {
        this.employees = []
        this.prep_employees.forEach(element => this.employees.push(element))
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
        const response = await fetch(`${process.env.ROOT_API}/inventorybase/api/v1/otss/`,
        {
          mode: "cors",
        })
        categories = await response.json()
        categories = categories['otss']
        for(let key in categories){
          this.otssCategories.push(categories[key]['category'])
        }
        this.otssCategories.push({text: '-', value: null})
      },
      async fetchConditions() {
        let tempArr = []
        const response = await fetch(`${process.env.ROOT_API}/inventorybase/api/v1/condition/`,
        {
          mode: "cors",
        })
        tempArr = await response.json()
        tempArr = tempArr['conditions']
        for (let i = 0; i < tempArr.length; ++i){
          this.conditions.push(tempArr[i]['condition'])
        }
        this.conditions.push({text: '-', value: null})
      },
      resetFilters(){
        this.$parent.$data.fuseString = ''
        this.fuseString =''
        bus.$emit('resetFilters')
      },
      async fetchUnits() {
        let tempArr = []
        const response = await fetch(`${process.env.ROOT_API}/inventorybase/api/v1/unit/`,
        {
          mode: "cors",
        })
        tempArr = await response.json()
        tempArr = tempArr['units']
        for (let i = 0; i < tempArr.length; ++i){
          this.units.push(tempArr[i]['unit'])
        }
      },
      async fetchLocations() {
        const response = await fetch(`${process.env.ROOT_API}/inventorybase/api/v1/location/`,
        {
          mode: "cors",
        })
        this.locations = await response.json()
        this.locations = this.locations['locations']
      },
    },
    watch:{
      fuseString: function (){
        this.$parent.$data.fuseString = this.fuseString
        bus.$emit('changeFuseString', this.fuseString)
      },
    },
    async created(){
      await this.fetchOTSS()
      await this.fetchConditions()
      await this.fetchLocations()
      await bus.$on('fetchEmployees', () => {this.createEmployeeList()})
    },
  }
</script>

<style scoped>

</style>
