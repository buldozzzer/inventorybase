<template>
  <div>
    <b-container>
      <b-col>
        <b-button variant="success" class="mt-3" v-b-modal.employee-add-modal>
          Добавить сотрудника
        </b-button>
      </b-col>
      <b-table class="mt-3"
               striped hover
               ref="selectableTable"
               fixed
               sort-by="surname"
               :items="employeeList"
               :fields="employeeFields"
               small>
        <template #head(edit_remove)="scope">
          <div class="text-nowrap">Изменить/Удалить</div>
        </template>
        <template #cell(edit_remove)="row">
          <div class="text-nowrap">
            <b-button variant="warning"
                      v-b-modal.employee-edit-modal
                      @click="editEmployee(row.item)">
              Редактировать
            </b-button>
            <br>
            <b-button variant="danger"
                      class="mt-3"
                      v-b-modal.confirm-modal
                      @click="selectToRemoveRecord(row.item)">
              Удалить
            </b-button>
          </div>
        </template>
      </b-table>
      <employee-add-modal>
      </employee-add-modal>
      <confirm-form ref="confirmModal"
                    :payload="selected[0]"
                    :message="employeeMessage"
                    :op="removeEmployee"
      ></confirm-form>
      <employee-edit-modal ref="employeeEdit"
      ></employee-edit-modal>
    </b-container>
  </div>
</template>

<script>
/* eslint-disable */
  import {bus} from "../../main";
import EmployeeAddModal from "./add/EmployeeAddModal";
import ConfirmForm from "../item/ConfirmForm";
import EmployeeEditModal from "./edit/EmployeeEditModal";

export default {
    name: 'MetadataList',
  components: {EmployeeAddModal, ConfirmForm, EmployeeEditModal},
  data() {
      return {
        employeeMessage: 'Удалить сотрудника из базы?',
        employeeFields: [
          {
            key: "edit_remove",
            isRowHeader: true,
            class: 'text-center'
          },
          {
            key: "surname",
            label: "Фамилия",
            sortable: true
          },
          {
            key: "name",
            label: "Имя",
            sortable: true
          },
          {
            key: "secname",
            label: "Отчество",
            sortable: true,
          },
        ],
        employeeList: [],
        selected: []
      };
    },
    methods: {
      async fetchEmployees() {
        const response = await fetch('http://localhost:8000/api/v1/employee/')
        this.employeeList = await response.json()
        this.employeeList = this.employeeList['employees']
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
        this.selected =[]
      })
    },
  };
</script>
