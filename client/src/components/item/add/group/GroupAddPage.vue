<template>
  <div id="add-form">
    <b-row class="mt-3">
      <b-col cols="2">
        <div id="scrollspy-buttons"
             :style="{ height: scroll_form }"
             ref="buttons">
          <b-navbar v-b-scrollspy:scrollspy-nested
                    style="margin: auto"
                    class="flex-column">
            <b-nav pills vertical>
              <b-nav-item v-for="item in listOfNewItems"
                          :key="item.index"
                          :href="'#item-' + item.index"
                          @click="scrollIntoView">
                {{ item.name ? item.name : 'Материальная ценность ' + (item.index + 1) }}
              </b-nav-item>
              <b-button variant="light"
                        class="mt-3"
                        @click="addForm">+
              </b-button>
              <b-button variant="danger"
                        v-if="listOfNewItems.length > 1"
                        @click="deleteLastForm">-
              </b-button>
              <b-button variant="success"
                        @click="createItems">
                {{ listOfNewItems.length === 1 ? 'Добавить запись' : 'Добавить записи' }}
              </b-button>
            </b-nav>
          </b-navbar>
        </div>
      </b-col>
      <b-col cols="10">
        <div id="scrollspy-nested"
             :style="{ height: scroll_form }"
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
  </div>
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
        index: 0,
        show: false,
        scroll_form: '',
        employeeList: [],
        employeeInitials: [],
        listOfNewItems: [],
      }
    },
    methods: {
      init() {
        if(this.$parent.$data.dataForChildren == null) {
          let item = {
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
          this.listOfNewItems.push(item)
          this.index += 1
        } else {
          this.listOfNewItems.push(this.$parent.$data.dataForChildren)
          this.listOfNewItems[0]['index'] = this.index
          this.index += 1
          this.$parent.$data.dataForChildren = null
        }
      },
      addForm(){
        let item = {
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
        item.index = this.index
        this.listOfNewItems.push(item)
        this.index += 1
      },
      deleteLastForm(){
        this.listOfNewItems.splice( this.listOfNewItems.length-1, 1)
        this.index -= 1
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
        const response = await fetch(`${process.env.ROOT_API}/inventorybase/api/v1/employee/`,
        {
          mode: "cors",
        })
        this.employeeList = await response.json()
        this.employeeList = this.employeeList['employees']
        this.employeeToString()
      },
      async createItems() {
        bus.$emit('fetchComponents')
        for (let i = 0; i<this.listOfNewItems.length; i++) {
          const payload = {
            name: this.listOfNewItems[i].name,
            user: this.listOfNewItems[i].user,
            responsible: this.listOfNewItems[i].responsible,
            components: this.listOfNewItems[i].components,
            inventory_n: this.listOfNewItems[i].inventory_n,
            otss_category: this.listOfNewItems[i].otss_category,
            condition: this.listOfNewItems[i].condition,
            unit_from: this.listOfNewItems[i].unit_from,
            in_operation: this.listOfNewItems[i].in_operation,
            fault_document_requisites: this.listOfNewItems[i].fault_document_requisites,
            date_of_receipt: this.listOfNewItems[i].date_of_receipt,
            number_of_receipt: this.listOfNewItems[i].number_of_receipt,
            requisites: this.listOfNewItems[i].requisites,
            transfer_date: this.listOfNewItems[i].transfer_date,
            otss_requisites: this.listOfNewItems[i].otss_requisites,
            spsi_requisites: this.listOfNewItems[i].spsi_requisites,
            transfer_requisites: this.listOfNewItems[i].transfer_requisites,
            comment: this.listOfNewItems[i].comment,
            last_check: this.listOfNewItems[i].last_check,
          };
          const response = await fetch(`http://localhost:8000/inventorybase/api/v1/item/`, {
            method: 'POST',
            mode: 'cors',
            headers: {
              'Accept': 'application/json',
              'Content-type': 'application/json'
            },
            body: JSON.stringify(payload)
          });
          /* eslint-disable */
          if (response.status !== 201) {
            alert(JSON.stringify(await response.json(), null, 2));
          }
        }
        this.listOfNewItems = []
        this.index = 0
        this.init()
        bus.$emit('updateList')
        bus.$emit('clearComponentForm')
      },
    },
    async created() {
      await this.fetchEmployees()
      this.init()
    },
    mounted() {
      let _height = document.documentElement.clientHeight * 0.9
      this.scroll_form = _height.toString() + 'px'
    }
  }
</script>

<style scoped>
  #scrollspy-nested{
    position:relative;
    width: 98%;
    overflow-y:scroll
  }
  #add-form{
    width: 98%;
    margin: auto;
  }
  #scrollspy-buttons{
    position:relative;
    overflow-y:scroll;
    width: 105%;
    overflow-x: hidden;
  }
</style>
