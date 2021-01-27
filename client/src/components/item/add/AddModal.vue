<!--eslint-disable-->
<template>
  <b-modal ref="addItemModal"
           id="add-item-modal"
           title="Добавить запись в базу мат. ценностей"
           size="xl"
           no-close-on-backdrop
           hide-footer
           hide-header-close>
    <b-form class="w-100">
      <div class="submit-reset-buttons mt-3 my">
        <b-button type="submit" variant="success" @click="onSubmit">
          Добавить запись
        </b-button>
        <b-button href="#/items/groupadd" variant="light" @click="sendForm">
          Добавить несколько записей
        </b-button>
        <b-button type="reset" variant="danger" @click="onReset">
          Отмена
        </b-button>
      </div>
      <div class="container mt-3">
        <div class="row">
          <div class="col">
            <form-template :itemForm="itemForm"
                           :employeeInitials="employeeInitials">
            </form-template>
          </div>
          <div class="col">
            <component-list ref="componentList"/>
          </div>
        </div>
      </div>
    </b-form>
  </b-modal>
</template>

<script>
/* eslint-disable */
  import ComponentList from "./ComponentList";
  import {bus} from '../../../main'
  import FormTemplate from "../FormTemplate";

  export default {
    /* eslint-disable */
    name: "AddModal",
    props: ['employeeInitials'],
    components: {
      ComponentList,
      FormTemplate
    },
    data() {
      return {
        otssCategories: [1, 2, 3, 'Не секретно'],
        conditions: ['Исправно', 'Неисправно'],
        operation: ['Используется', 'Не используется'],
        employeeList: [],
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
      }

    },
    methods: {
      /* eslint-disable */
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
        evt.preventDefault()
        this.$refs.addItemModal.hide()
        this.clearFrom()
      },
      onSubmit(evt) {
        evt.preventDefault();
        this.$refs.addItemModal.hide();
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
        this.clearFrom()
      },
      isIntroduced(left, right) {
        return left !== right
      },
      sendForm(){
        this.itemForm['components'] = this.$refs.componentList.createComponentList()
        this.$parent.$parent.$data.dataForChildren = this.itemForm
      },
      clearFrom(){
        this.itemForm = {
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
  }
</script>

<style>
  .submit-reset-buttons{
    display: -o-flex;
  }
</style>
