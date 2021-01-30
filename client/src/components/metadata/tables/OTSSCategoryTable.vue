<template>
  <div>
    <b-table class="mt-3"
             striped hover
             ref="selectableTable"
             fixed
             sort-by="surname"
             :items="otssCategories"
             :fields="otssFields"
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
    name: "OTSSCategoryTable",
    props:['otssCategories', 'editOTSS', 'selectToRemoveRecord'],
    data(){
      return {
        otssFields:[
          {
            key: "edit_remove", isRowHeader: true, class: 'text-center'
          },
          {
            key: 'category', label: "ОТСС категория", sortable: true, class: 'text-center'
          },
        ]
      }
    },
    methods:{
      edit(data){
        this.editOTSS(data)
      },
      remove(data){
        this.selectToRemoveRecord(data)
      }
    }
  }
</script>

<style scoped>

</style>
