<!--eslint-disable-->
<template>
  <b-modal ref="addItemModal"
           id="add-item-modal"
           title="Добавить запись в базу мат. ценностей"
           size="xl"
           @hidden="clearForm"
           @show="clearForm"
           hide-footer>
<!--    hide-header-close no-close-on-backdrop-->
    <b-form class="w-100">
      <div class="submit-reset-buttons mt-3">
        <b-button type="submit"
                  variant="success"
                  :disabled="itemForm.name === ''"
                  @click="onSubmit">
          Добавить запись
        </b-button>
        <b-button href="#/items/groupadd" variant="light" @click="sendForm">
          Добавить несколько записей
        </b-button>
        <b-button type="reset" variant="danger" @click="onReset">
          Отмена
        </b-button>
      </div>
      <b-container class="mt-3">
        <b-row>
          <b-col :cols="colsize">
            <form-template :itemForm="itemForm"
                           ref="itemForm"
                           :employeeInitials="employeeInitials">
            </form-template>
          </b-col>
          <b-col>
            <b-button @click="showComponents = !showComponents">
              {{!showComponents ? 'Добавить компоненты' : 'Убрать компоненты'}}
            </b-button>
            <component-list v-if="showComponents"
                            ref="componentList"/>
          </b-col>
        </b-row>
      </b-container>
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
        showComponents: false
      }
    },
    computed:{
      colsize: function(){
        if(this.showComponents)
          return 6
        else
          return 10
      }
    },
    methods: {
      /* eslint-disable */
      async createItem(payload) {
        const response = await fetch(`http://localhost:8000/inventorybase/api/v1/item/`, {
          method: 'POST',
          mode: 'cors',
          headers: {
            'Content-type': 'application/json'
          },
          body: JSON.stringify(payload)
        });
        /* eslint-disable */
        if (response.status !== 201) {
          alert(JSON.stringify(await response.json(), null, 2));
          this.$parent.showErrorAlert()
        }
        bus.$emit('updateList')
        this.$parent.showAlert()
      },

      onReset(evt) {
        evt.preventDefault()
        this.$refs.addItemModal.hide()
        this.clearForm()
      },
      onSubmit(evt) {
        evt.preventDefault();
        this.$refs.addItemModal.hide();
        if (this.showComponents) {
          this.itemForm.components = this.$refs.componentList.createComponentList()
        }
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
        this.clearForm()
      },
      isIntroduced(left, right) {
        return left !== right
      },
      sendForm() {
        this.itemForm['components'] = this.$refs.componentList.createComponentList()
        this.$parent.$parent.$data.dataForChildren = this.itemForm
      },
      clearForm() {
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
    }
  }
</script>

<style>
  .submit-reset-buttons{
    display: -o-flex;
  }
</style>
