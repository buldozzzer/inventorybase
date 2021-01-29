<template>
  <div>
    <b-table class="mt-3"
             striped hover
             ref="selectableTable"
             fixed
             sort-by="category"
             :items="categories"
             :fields="categoryFields"
             small>
      <template #head(edit_remove)="scope">
        <div class="text-nowrap">Изменить/Удалить</div>
      </template>
      <template #cell(edit_remove)="row">
        <div class="text-nowrap">
          <b-button variant="warning"
                    v-b-modal.category-edit-modal
                    @click="edit(row.item)">
            Редактировать
          </b-button>
          <br>
          <b-button variant="danger"
                    class="mt-3"
                    v-b-modal.category-confirm
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
    name: "CategoryTable",
    props:['categories', 'editCategory', 'selectToRemoveRecord'],
    data(){
      return {
        categoryFields:[
          {
            key: "edit_remove", isRowHeader: true, class: 'text-center'
          },
          {
            key: 'category', label: "Категория", sortable: true, class: 'text-center'
          },
        ]
      }
    },
    methods:{
      edit(data){
        this.editCategory(data)
      },
      remove(data){
        this.selectToRemoveRecord(data)
      }
    }
  }
</script>

<style>

</style>
