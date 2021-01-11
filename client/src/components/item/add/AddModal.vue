<!--eslint-disable-->
<template>
  <b-modal ref="addItemModal"
           id="add-item-modal"
           title="Добавить запись в базу мат. ценностей"
           size="xl"
           no-close-on-backdrop
           hide-footer
           hide-header-close>
    <!--no-close-on-backdrop или настроить очистку формы при нажатии на задний фон-->

    <b-form @submit="onSubmit" @reset="onReset" class="w-100">
      <div class="container">
        <div class="row">
          <div class="col">
            <form-template :itemForm="itemForm"
                           :employeeInitials="employeeInitials"></form-template>
          </div>
          <div class="col">
            <component-list ref="componentList"/>
          </div>
        </div>
      </div>
      <div class="submit-reset-buttons">
        <b-button type="submit" variant="primary">Добавить запись</b-button>
        <b-button type="reset" variant="danger" @click="initForm">Отмена</b-button>
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
        itemForm: {},
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
      initForm() {
        this.itemForm.name = '';
        this.itemForm.user = '';
        this.itemForm.responsible = '';
        this.itemForm.components = [];
        this.itemForm.inventory_n = '';
        this.itemForm.otss_category = '';
        this.itemForm.condition = '';
        this.itemForm.unit_from = '';
        this.itemForm.in_operation = '';
        this.itemForm.fault_document_requisites = '';
        this.itemForm.date_of_receipt = null;
        this.itemForm.number_of_receipt = '';
        this.itemForm.requisites = '';
        this.itemForm.transfer_date = null;
        this.itemForm.otss_requisites = '';
        this.itemForm.spsi_requisites = '';
        this.itemForm.transfer_requisites = '';
        this.itemForm.comment = '';
        this.itemForm.last_check = null;

        this.$refs.componentList.initComponentForm()
      },

      onReset(evt) {
        evt.preventDefault();
        this.$refs.addItemModal.hide();
        this.initForm();
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
        this.initForm();
      },
      isIntroduced: function (left, right) {
        return left !== right
      },
    },
    created() {
    }
  }
</script>

<style scoped>
</style>
