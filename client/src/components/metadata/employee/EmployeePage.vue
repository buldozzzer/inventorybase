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
                      :select-to-remove-record="selectToRemoveEmployee"/>
    </b-container>
    <employee-add-modal/>
    <confirm-form :payload="selected[0]"
                  :dynamic-id="employeeConfirm"
                  :message="employeeMessage"
                  :op="removeEmployee"/>
    <employee-edit-modal ref="employeeEdit"/>
  </div>
</template>

<script>
/* eslint-disable */
  import {bus} from "../../../main";
  import EmployeeAddModal from "./EmployeeAddModal";
  import ConfirmForm from "../../item/ConfirmForm";
  import EmployeeEditModal from "./EmployeeEditModal";
  import EmployeeTable from "./EmployeeTable";

  export default {
    name: 'EmployeePage',
    components: {
      EmployeeAddModal,
      ConfirmForm,
      EmployeeEditModal,
      EmployeeTable,
    },
    data() {
      return {
        employeeMessage: 'Удалить сотрудника из базы?',
        employeeConfirm: 'employee-confirm',
        employeeList: [],
        selected: []
      };
    },
    methods: {
      async selectToRemoveEmployee(data) {
        this.selected.push(data)
      },

      async fetchEmployees() {
        const response = await fetch('http://localhost:8000/api/v1/employee/',
        {
          mode: "cors",
        })
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
          mode: 'cors',
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

<style scoped>

</style>
