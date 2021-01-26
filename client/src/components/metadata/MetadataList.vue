<template>
  <div>
    <b-container>
      <b-col class="mt-3" >
        <h3>Сотрудники</h3>
      </b-col>
      <b-col>
        <b-button variant="success" class="mt-3" v-b-modal.employee-add-modal>
          Добавить сотрудника
        </b-button>
      </b-col>
      <employee-table :employee-list="employeeList"
                      :edit-employee="editEmployee"
                      :select-to-remove-record="selectToRemoveRecord"/>
      <b-col class="mt-3">
        <h3>ОТСС категории</h3>
      </b-col>
      <b-col>
        <b-button variant="success" class="mt-3" v-b-modal.o-t-s-s-category-add-modal>
          Добавить категорию ОТСС
        </b-button>
      </b-col>
      <o-t-s-s-category-table :otss-categories="otssCategories"
                              :edit-o-t-s-s="editOTSS"
                              :select-to-remove-record="selectToRemoveRecord"/>
      <b-col class="mt-3">
        <h3>Подразделение, откуда поступила мат. ценность</h3>
      </b-col>
      <b-col>
        <b-button variant="success" class="mt-3" v-b-modal.unit-add-modal>
          Добавить подразделение
        </b-button>
      </b-col>
      <unit-table :units="units"
                  :edit-unit="editUnit"
                  :select-to-remove-record="selectToRemoveRecord"/>
    </b-container>
    <employee-add-modal/>
    <confirm-form :payload="selected[0]"
                  :dynamic-id="employeeConfirm"
                  :message="employeeMessage"
                  :op="removeEmployee"/>
    <employee-edit-modal ref="employeeEdit"/>

    <o-t-s-s-category-add-modal/>
    <employee-edit-modal ref="employeeEdit"/>

    <confirm-form :payload="selected[0]"
                  :dynamic-id="otssConfirm"
                  :message="otssCategoryMessage"
                  :op="removeOTSS"/>
    <o-t-s-s-category-edit-modal ref="otssEdit"/>

    <unit-add-modal/>
    <confirm-form :payload="selected[0]"
                  :dynamic-id="unitConfirm"
                  :message="unitMessage"
                  :op="removeUnit"/>
    <unit-edit-modal ref="unitEdit"/>
  </div>
</template>

<script>
/* eslint-disable */
  import {bus} from "../../main";
  import EmployeeAddModal from "./add/EmployeeAddModal";
  import ConfirmForm from "../item/ConfirmForm";
  import EmployeeEditModal from "./edit/EmployeeEditModal";
  import EmployeeTable from "./tables/EmployeeTable";
  import OTSSCategoryAddModal from "./add/OTSSCategoryAddModal";
  import OTSSCategoryTable from "./tables/OTSSCategoryTable";
  import OTSSCategoryEditModal from "./edit/OTSSCategoryEditModal";
  import UnitTable from "./tables/UnitTable";
  import UnitAddModal from "./add/UnitAddModal";
  import UnitEditModal from "./edit/UnitEditModal";

  export default {
    name: 'MetadataList',
    components: {
      EmployeeAddModal,
      ConfirmForm,
      EmployeeEditModal,
      EmployeeTable,
      OTSSCategoryAddModal,
      OTSSCategoryTable,
      OTSSCategoryEditModal,
      UnitTable,
      UnitAddModal,
      UnitEditModal
    },
    data() {
      return {
        unitMessage: 'Удалить подразделение из базы?',
        unitConfirm: 'unit-confirm',
        employeeConfirm: 'employee-confirm',
        otssConfirm: 'otss-confirm',
        employeeMessage: 'Удалить сотрудника из базы?',
        otssCategoryMessage: 'Удалить категорию ОТСС из базы?',
        employeeList: [],
        otssCategories: [],
        units: [],
        selected: []
      };
    },
    methods: {
      async selectToRemoveRecord(data) {
        this.selected.push(data)
      },

      async fetchEmployees() {
        const response = await fetch('http://localhost:8000/api/v1/employee/')
        this.employeeList = await response.json()
        this.employeeList = this.employeeList['employees']
        this.selected = []
      },
      editEmployee(item) {
        this.$refs.employeeEdit.employeeForm = item
      },
      async removeEmployee(employee) {
        const _id = employee['_id']
        const response = await fetch(`http://localhost:8000/api/v1/employee/${_id}/`, {
          method: 'DELETE',
          headers: {
            'Accept': 'application/json',
            'Content-type': 'application/json'
          },
        });
        if (response.status !== 204) {
          alert(JSON.stringify(await response.json(), null, 2));
        }
        await this.fetchEmployees()
      },

      async removeOTSS(otss) {
        const _id = otss['_id']
        const response = await fetch(`http://localhost:8000/api/v1/otss/${_id}/`, {
          method: 'DELETE',
          headers: {
            'Accept': 'application/json',
            'Content-type': 'application/json'
          },
        });
        if (response.status !== 204) {
          alert(JSON.stringify(await response.json(), null, 2));
        }
        await this.fetchOTSS()
      },
      async fetchOTSS() {
        const response = await fetch('http://localhost:8000/api/v1/otss/')
        this.otssCategories = await response.json()
        this.otssCategories = this.otssCategories['otss']
        this.selected = []
      },
      editOTSS(item) {
        this.$refs.otssEdit.form = item
      },

      async fetchUnits() {
        const response = await fetch('http://localhost:8000/api/v1/unit/')
        this.units = await response.json()
        this.units = this.units['units']
        this.selected = []
      },
      async removeUnit(unit) {
        const _id = unit['_id']
        const response = await fetch(`http://localhost:8000/api/v1/unit/${_id}/`, {
          method: 'DELETE',
          headers: {
            'Accept': 'application/json',
            'Content-type': 'application/json'
          },
        });
        if (response.status !== 204) {
          alert(JSON.stringify(await response.json(), null, 2));
        }
        await this.fetchUnits()
      },
      editUnit(item) {
        this.$refs.unitEdit.form = item
      },

      async fetchTyps() {
        const response = await fetch('http://localhost:8000/api/v1/type/')
        this.types = await response.json()
        this.types = this.types['types']
        this.selected = []
      },
      async removeType(unit) {
        const _id = unit['_id']
        const response = await fetch(`http://localhost:8000/api/v1/type/${_id}/`, {
          method: 'DELETE',
          headers: {
            'Accept': 'application/json',
            'Content-type': 'application/json'
          },
        });
        if (response.status !== 204) {
          alert(JSON.stringify(await response.json(), null, 2));
        }
        await this.fetchUnits()
      },
      editType(item) {
        this.$refs.typeEdit.form = item
      },
    },
    async created() {
      await this.fetchEmployees()
      await this.fetchOTSS()
      await this.fetchUnits()
      await bus.$on('newData', () => {
        this.fetchEmployees()
        this.fetchUnits()
        this.fetchOTSS()
      })
    },
  };
</script>
