<template>
  <b-form @submit="onSubmit" @reset="onReset" class="w-100">
      <div class="container">
        <div class="row">
          <div class="col">
            <form-template :itemForm="listOfNewItems[0]"
                           :employeeInitials="employeeInitials">

            </form-template>
          </div>
          <div class="col">
            <component-list ref="componentList"/>
          </div>
        </div>
      </div>
      <div class="submit-reset-buttons">
        <b-button type="submit" variant="primary">Добавить записи</b-button>
        <b-button type="reset" variant="danger" @click="initForms">Отмена</b-button>
      </div>
    </b-form>
</template>

<script>
/* eslint-disable */
  import FormTemplate from "../../FormTemplate";
  import ComponentList from "../ComponentList";
  import {bus} from "../../../../main";

  export default {
    name: "GroupAddForm",
    components:{
      FormTemplate,
      ComponentList
    },
    props:['employeeInitials'],
    data(){
      return{
        itemForm: {
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
        },
        show: false,
        listOfNewItems: [],
        shows: [],
      }
    },
    methods:{
      init(){
        this.listOfNewItems.push(this.itemForm)
      },
      initForms() {
        for (let item in this.listOfNewItems) {
          item = {
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
        }
      },
      async createItem(payload) {
        const response = await fetch(`http://localhost:8000/api/v1/item/`, {
          method: 'POST',
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
        bus.$emit('updateList')
      },
      onReset(evt) {
        evt.preventDefault();
        this.initForms();
      },
      onSubmit(evt) {
        evt.preventDefault();
        for (let item in this.ListOfNewItems)
        this.itemForm.components = this.$refs.componentList.createComponentList()
        const payload = {
          name: this.itemForm.name,
          user: this.itemForm.user,
          responsible: this.itemForm.responsible,
          components: this.itemForm.components,
          inventory_n: this.itemForm.inventory_n,
          otss_category: this.itemForm.otss_category,
          condition: this.itemForm.condition,
          unit_from: this.itemForm.unit_from,
          in_operation: this.itemForm.in_operation,
          fault_document_requisites: this.itemForm.fault_document_requisites,
          date_of_receipt: this.itemForm.date_of_receipt,
          number_of_receipt: this.itemForm.number_of_receipt,
          requisites: this.itemForm.requisites,
          transfer_date: this.itemForm.transfer_date,
          otss_requisites: this.itemForm.otss_requisites,
          spsi_requisites: this.itemForm.spsi_requisites,
          transfer_requisites: this.itemForm.transfer_requisites,
          comment: this.itemForm.comment,
          last_check: this.itemForm.last_check,
        };
        this.createItem(payload);
        this.initForms();
      },
    },
    async created() {
      this.init()
    }
  }
</script>

<style>

</style>
