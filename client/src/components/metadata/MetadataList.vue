<template>
  <div>
    <b-container>
      <b-col>
        <b-button variant="success" class="mt-3" v-b-modal.employee-add-modal>
          Добавить сотрудника
        </b-button>
      </b-col>
      <employee-table :employee-list="employeeList"
                      :edit-employee="editEmployee"
                      :select-to-remove-record="selectToRemoveRecord"/>
      <b-col>
        <b-button variant="success" class="mt-3" v-b-modal.employee-add-modal>
          Добавить категорию ОТСС
        </b-button>
      </b-col>
    </b-container>
    <employee-add-modal/>
      <confirm-form ref="confirmModal"
                    :payload="selected[0]"
                    :message="employeeMessage"
                    :op="removeEmployee"
      ></confirm-form>
      <employee-edit-modal ref="employeeEdit"
      ></employee-edit-modal>
  </div>
</template>

<script>
/* eslint-disable */
import {bus} from "../../main";
import EmployeeAddModal from "./add/EmployeeAddModal";
import ConfirmForm from "../item/ConfirmForm";
import EmployeeEditModal from "./edit/EmployeeEditModal";
import EmployeeTable from "./tables/EmployeeTable";

export default {
    name: 'MetadataList',
  components: {EmployeeAddModal, ConfirmForm, EmployeeEditModal, EmployeeTable},
  data() {
      return {
        employeeMessage: 'Удалить сотрудника из базы?',
        otssCategoryMessage: 'Удалить категорию ОТСС из базы?',
        employeeList: [],
        otssCategories: [],
        selected: []
      };
    },
    methods: {
      async fetchEmployees() {
        const response = await fetch('http://localhost:8000/api/v1/employee/')
        this.employeeList = await response.json()
        this.employeeList = this.employeeList['employees']
        this.selected = []
      },
      async selectToRemoveRecord(employee) {
        this.selected.push(employee)
      },
      editEmployee(item){
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
    },
    async created() {
      await this.fetchEmployees()
      await bus.$on('newData', () => {
        this.fetchEmployees()
      })
    },
  };
</script>
