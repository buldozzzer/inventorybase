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
          <b-icon icon="pencil-square"
                  variant="warning"
                  data-toggle="tooltip"
                  data-placement="top"
                  title="Редактировать"
                  font-scale="2"
                  v-b-modal.employee-edit-modal
                  @click="edit(row.item)">
          </b-icon>
          <b-icon icon="trash"
                  variant="danger"
                  font-scale="2"
                  data-toggle="tooltip"
                  data-placement="top"
                  title="Удалить"
                  v-b-modal.employee-confirm
                  @click="remove(row.item)">
          </b-icon>
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
            key: "surname", label: "Фамилия", sortable: true, class: 'text-center'
          },
          {
            key: "name", label: "Имя", sortable: true, class: 'text-center'
          },
          {
            key: "secname", label: "Отчество", sortable: true, class: 'text-center'
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
