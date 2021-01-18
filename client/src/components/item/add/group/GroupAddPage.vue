<template>
  <b-container class="mt-3">
    <b-row>
      <b-col cols="2">
        <b-navbar v-b-scrollspy:scrollspy-nested class="flex-column">
          <b-nav pills vertical>
            <b-nav-item v-for="item in listOfNewItems"
                        :key="item.index"
                        :href="'#item-' + item.index"
                        @click="scrollIntoView">
              {{ item.name ? item.name : 'Материальная ценность ' + (item.index + 1) }}
            </b-nav-item>
            <b-button variant="dark" @click="addForm">+</b-button>
          </b-nav>
        </b-navbar>
      </b-col>
      <b-col cols="10">
        <div id="scrollspy-nested"
             style="position:relative; height:600px; overflow-y:scroll"
             ref="content">
          <group-add-form v-for="item in listOfNewItems"
                          :key="item.index"
                          :item-form="item"
                          :employee-initials="employeeInitials"
                          :id="'item-' + item.index">
          </group-add-form>
        </div>
      </b-col>
    </b-row>
  </b-container>
</template>

<script>
/* eslint-disable */
  import GroupAddForm from "./GroupAddForm";
  import {bus} from "../../../../main";

  export default {
    name: "GroupAddPage",
    components: {
      GroupAddForm
    },
    data() {
      return {
        employeeList: [],
        employeeInitials: [],
        show: false,
        listOfNewItems: [],
        shows: [],
      }
    },
    methods: {
      init() {
        let itemForm = {
          index: 0,
          name: '',
          user: '',
          responsible: '',
          components: [],
          inventory_n: '',
          otss_category: '',
          condition: '',
          unit_from: '',
          in_operation: '',
          fault_document_requisites: '',
          date_of_receipt: null,
          number_of_receipt: '',
          requisites: '',
          transfer_date: null,
          otss_requisites: '',
          spsi_requisites: '',
          transfer_requisites: '',
          comment: '',
          last_check: null,
        }
        let list = []
        for (let i = 0; i < 1; i++) {
          itemForm.index = i
          list.push(itemForm)
          itemForm.index = null
        }
        this.listOfNewItems = list
      },
      addForm(){
        let itemForm = {
          index: null,
          name: '',
          user: '',
          responsible: '',
          components: [],
          inventory_n: '',
          otss_category: '',
          condition: '',
          unit_from: '',
          in_operation: '',
          fault_document_requisites: '',
          date_of_receipt: null,
          number_of_receipt: '',
          requisites: '',
          transfer_date: null,
          otss_requisites: '',
          spsi_requisites: '',
          transfer_requisites: '',
          comment: '',
          last_check: null,
        }
        itemForm.index = this.listOfNewItems.length
        this.listOfNewItems.push(itemForm)
      },
      scrollIntoView(evt) {
        evt.preventDefault()
        const href = evt.target.getAttribute('href')
        const el = href ? document.querySelector(href) : null
        if (el) {
          this.$refs.content.scrollTop = el.offsetTop
        }
      },
      employeeToString() {
        for (let i = 0; i < this.employeeList.length; i++) {
          this.employeeInitials.push(
            this.employeeList[i].surname + ' ' +
            this.employeeList[i].name[0] + '.' +
            this.employeeList[i].secname[0] + '.');
        }
      },
      async fetchEmployees() {
        const response = await fetch('http://localhost:8000/api/v1/employee/')
        this.employeeList = await response.json()
        this.employeeList = this.employeeList['employees']
        this.employeeToString()
      },
    },
    async created() {
      await this.fetchEmployees()
      this.init()
    },
  }
</script>

<style  >

</style>
