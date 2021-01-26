<template>
  <div>
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
                    @click="edit(row.item)">
            Редактировать
          </b-button>
          <br>
          <b-button variant="danger"
                    class="mt-3"
                    v-b-modal.employee-confirm
                    @click="remove(row.item)">
            Удалить
          </b-button>
        </div>
      </template>
    </b-table>
  </div>
</template>

<script>
/* eslint-disable */
  export default {
    name: "EmployeeTable",
    props: ['employeeList', 'editEmployee', 'selectToRemoveRecord'],
    data() {
      return {
        employeeFields: [
          {
            key: "edit_remove", isRowHeader: true, class: 'text-center'
          },
          {
            key: "surname", label: "Фамилия", sortable: true
          },
          {
            key: "name", label: "Имя", sortable: true
          },
          {
            key: "secname", label: "Отчество", sortable: true,
          },
        ],
      }
    },
    methods: {
      edit(data){
        this.editEmployee(data)
      },
      remove(data){
        this.selectToRemoveRecord(data)
      }
    }
  }
</script>

<style scoped>

</style>
