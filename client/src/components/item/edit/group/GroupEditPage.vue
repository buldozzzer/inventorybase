<template>
  <div>
    <b-container class="mt-3">
      <b-row>
        <b-col cols="2">
          <b-button variant="dark"
                    v-b-modal.confirm-modal>
            Внести изменения
          </b-button>
          <b-navbar v-b-scrollspy:scrollspy-nested class="flex-column">
            <b-nav pills vertical>
              <b-nav-item v-for="item in itemsForEdit"
                          :key="item['_id']"
                          :href="'#item-' + item['_id']"
                          @click="scrollIntoView">
                {{ item.name ? item.name : 'Материальная ценность ' + (item.index + 1) }}
              </b-nav-item>
            </b-nav>
          </b-navbar>
        </b-col>
        <b-col cols="10">
          <div id="scrollspy-nested"
               style="position:relative; height:550px; overflow-y:scroll"
               ref="items">
            <group-edit-form v-for="item in itemsForEdit"
                             :key="item['_id']"
                             :itemForm="item"
                             :id="'item-' + item['_id']"
                             :employeeInitials="employeeInitials"/>
          </div>
        </b-col>
      </b-row>
    </b-container>
    <confirm-form :title="title"
                  :message="message"
                  :op="editItems"/>
  </div>
</template>

<script>
/* eslint-disable */
  import GroupEditForm from "./GroupEditForm";
  import {bus} from "../../../../main";
  import ConfirmForm from "../../ConfirmForm";

  export default {
    name: "GroupEditPage",
    components: {
      GroupEditForm,
      ConfirmForm
    },
    data() {
      return {
        employeeInitials: [],
        employeeList: [],
        itemsForEdit: [],
        title: 'Подтвердите операцию',
        m: ''
      }
    },
    methods: {
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
      scrollIntoView(evt) {
        evt.preventDefault()
        const href = evt.target.getAttribute('href')
        const el = href ? document.querySelector(href) : null
        if (el) {
          this.$refs.items.scrollTop = el.offsetTop
        }
      },
      async editItems() {
        for (let i = 0; i < this.itemsForEdit.length; i++) {
          const _id = this.itemsForEdit[i]['_id']
          const response = await fetch(`http://localhost:8000/api/v1/item/${_id}/`,
            {
              method: 'PUT',
              body: JSON.stringify(this.itemsForEdit[i]),
              headers: {
                'Accept': 'application/json',
                'Content-type': 'application/json'
              },
            });
          const json = await response.json();
          console.log(JSON.stringify(json));
          if (response.status !== 202) {
            alert(JSON.stringify(await response.json(), null, 2));
          }
        }
      },
    },
    computed:{
      message: function () {
        if(this.itemsForEdit) {
          if (this.itemsForEdit.length === 1) {
            this.m = 'Вы уверены, что хотите внести изменения в запись?'
          } else {
            this.m = 'Вы уверены, что хотите внести изменения в записи?'
          }
        }
        return this.m
      }
    },
    async created() {
      await this.fetchEmployees()
      this.itemsForEdit = this.$parent.$data.dataForChildren
      bus.$emit('clearDataForChildren')
    },
  }
</script>

<style scoped>

</style>
