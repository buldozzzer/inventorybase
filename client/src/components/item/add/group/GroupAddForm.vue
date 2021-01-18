<template>
  <div >
    <h5>
      {{itemForm.name ? itemForm.name : 'Материальная ценность ' + (itemForm.index + 1) }}
    </h5>
    <b-form @submit="onSubmit" @reset="onReset" class="w-100">
      <b-container>
        <b-row>
          <b-col>
            <form-template :itemForm="itemForm"
                           :employeeInitials="employeeInitials">

            </form-template>
          </b-col>
          <b-col>
            <component-list v-if="itemForm">
            </component-list>
          </b-col>
        </b-row>
      </b-container>
    </b-form>
  </div>
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
    props:['employeeInitials', 'itemForm'],
    data(){
      return {
        item: {}
      }
    },
    methods:{
      initForms() {
          // item = {
          //   name: '',
          //   user: '',
          //   responsible: '',
          //   components: [],
          //   inventory_n: '',
          //   otss_category: '',
          //   condition: '',
          //   unit_from: '',
          //   in_operation: '',
          //   fault_document_requisites: '',
          //   date_of_receipt: null,
          //   number_of_receipt: '',
          //   requisites: '',
          //   transfer_date: null,
          //   otss_requisites: '',
          //   spsi_requisites: '',
          //   transfer_requisites: '',
          //   comment: '',
          //   last_check: null,
          // }
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
  }
</script>

<style>

</style>
