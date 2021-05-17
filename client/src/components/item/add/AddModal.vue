<!--eslint-disable-->
<template>
<!--  test-branch-->
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
        <b-button id="add-component-button"
                  @click="showComponents = !showComponents">
          {{!showComponents ? 'Добавить компоненты' : 'Убрать компоненты'}}
        </b-button>
      </div>
      <b-container class="mt-3">
        <b-row>
          <b-col :cols="colsize">
            <form-template ref="itemForm"
                           :itemForm="itemForm"
                           :categories="categories"
                           :show-components="showComponents"
                           :location_units="location_units"
                           :location_objects="location_objects"
                           :location_corpuses="location_corpuses"
                           :location_cabinets="location_cabinets"
                           :employeeInitials="employeeInitials">
            </form-template>
          </b-col>
          <b-col>
            <component-list v-show="showComponents"
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
    props: ['employeeInitials',
      'categories',
      'location_units',
      'location_objects',
      'location_corpuses',
      'location_cabinets'],
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
          serial_n: '',
          category: '',
          year: '',
          cost: '',
          location_object: '',
          location_unit: '',
          location_corpus: '',
          location_cabinet: ''
        },
        showComponents: false,
      }
    },
    computed:{
      colsize: function(){
        if(this.showComponents)
          return 6
        else
          return 12
      }
    },
    methods: {
      /* eslint-disable */
      async createItem(payload) {
        const response = await fetch(`${process.env.ROOT_API}/inventorybase/api/v1/item/`, {
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
          serial_n: this.itemForm.serial_n,
          category: this.itemForm.category,
          year: this.itemForm.year,
          cost: this.itemForm.cost,
          location_object: this.itemForm.location_object,
          location_unit: this.itemForm.location_unit,
          location_corpus: this.itemForm.location_corpus,
          location_cabinet: this.itemForm.location_cabinet
        };
        this.createItem(payload);
        this.clearForm()
      },
      isIntroduced(left, right) {
        return left !== right
      },
      sendForm() {
        if (this.$refs.componentList != null) {
          this.itemForm['components'] = this.$refs.componentList.createComponentList()
        }
        bus.$emit('fetchDataForChildren', this.itemForm)
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
          serial_n: '',
          category: '',
          year: '',
          cost: '',
          location_object: '',
          location_unit: '',
          location_corpus: '',
          location_cabinet: ''
        }
      },
    }
  }
</script>

<style>
  .submit-reset-buttons{
    display: -o-flex;
  }
  #add-component-button{
    position: absolute;
    right: 1.5%;
  }
</style>
