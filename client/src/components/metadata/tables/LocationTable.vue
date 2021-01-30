<template>
  <div>
    <b-table class="mt-3"
             striped hover
             ref="selectableTable"
             fixed
             :items="locations"
             :fields="locationFields"
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
                  v-b-modal.edit-item-modal
                  @click="edit(row.item)">
          </b-icon>
          <b-icon icon="trash"
                  variant="danger"
                  font-scale="2"
                  data-toggle="tooltip"
                  data-placement="top"
                  title="Удалить"
                  v-b-modal.confirm-modal
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
    name: "LocationTable",
    props:['locations', 'editLocation', 'selectToRemoveRecord'],
    data(){
      return {
        locationFields:[
          {
            key: "edit_remove", isRowHeader: true, class: 'text-center'
          },
          {
            key: 'object', label: "Объект", sortable: true, class: 'text-center'
          },
          {
            key: 'corpus', label: "Корпус", sortable: true, class: 'text-center'
          },
          {
            key: 'cabinet', label: "Кабинет", sortable: true, class: 'text-center'
          },
          {
            key: 'unit', label: "Подразделение", sortable: true, class: 'text-center'
          },
        ]
      }
    },
    methods:{
      edit(data){
        this.editLocation(data)
      },
      remove(data){
        this.selectToRemoveRecord(data)
      }
    }
  }
</script>

<style scoped>

</style>
