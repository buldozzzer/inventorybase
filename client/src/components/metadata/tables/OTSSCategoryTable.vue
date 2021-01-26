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
          <b-button variant="warning"
                    v-b-modal.otss-edit-modal
                    @click="edit(row.item)">
            Редактировать
          </b-button>
          <br>
          <b-button variant="danger"
                    class="mt-3"
                    v-b-modal.otss-confirm
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
    name: "OTSSCategoryTable",
    props:['otssCategories', 'editOTSS', 'selectToRemoveRecord'],
    data(){
      return {
        otssFields:[
          {
            key: "edit_remove", isRowHeader: true, class: 'text-center'
          },
          {
            key: 'category', label: "ОТСС категория", sortable: true
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
