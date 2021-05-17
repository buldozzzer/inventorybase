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
          <b-icon icon="pencil-square"
                  variant="primary"
                  data-toggle="tooltip"
                  data-placement="top"
                  title="Редактировать"
                  font-scale="1.2"
                  v-b-modal.unit-edit-modal
                  @click="edit(row.item)">
          </b-icon>
          <b-icon icon="trash"
                  variant="danger"
                  font-scale="1.2"
                  data-toggle="tooltip"
                  data-placement="top"
                  title="Удалить"
                  v-b-modal.unit-confirm
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
