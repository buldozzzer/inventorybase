<template>
  <div>
    <b-table class="mt-3"
             striped hover
             ref="selectableTable"
             fixed
             sort-by="surname"
             :items="units"
             :fields="unitFields"
             small>
      <template #head(edit_remove)="scope">
        <div class="text-nowrap">Изменить/Удалить</div>
      </template>
      <template #cell(edit_remove)="row">
        <div class="text-nowrap">
          <b-button variant="warning"
                    v-b-modal.unit-edit-modal
                    @click="edit(row.item)">
            Редактировать
          </b-button>
          <br>
          <b-button variant="danger"
                    class="mt-3"
                    v-b-modal.unit-confirm
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
    name: "UnitTable",
    props:['units', 'editUnit', 'selectToRemoveRecord'],
    data(){
      return {
        unitFields:[
          {
            key: "edit_remove", isRowHeader: true, class: 'text-center'
          },
          {
            key: 'unit', label: "Подразделние, откуда поступила мат. ценность", sortable: true, class: 'text-center'
          },
        ]
      }
    },
    methods:{
      edit(data){
        this.editUnit(data)
      },
      remove(data){
        this.selectToRemoveRecord(data)
      }
    }
  }
</script>

<style>

</style>
