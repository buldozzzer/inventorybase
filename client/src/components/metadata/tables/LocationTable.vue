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
          <b-button variant="warning"
                    v-b-modal.location-edit-modal
                    @click="edit(row.item)">
            Редактировать
          </b-button>
          <br>
          <b-button variant="danger"
                    class="mt-3"
                    v-b-modal.location-confirm
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
