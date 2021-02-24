<template>
  <div>
    <b-container>
      <b-col class="mt-3">
        <h3>Категории</h3>
      </b-col>
      <b-col>
        <b-button variant="success" class="mt-3" v-b-modal.category-add-modal>
          Добавить категорию
        </b-button>
      </b-col>
      <category-table :categories="categories"
                      :edit-category="editCategories"
                      :select-to-remove-record="selectToRemoveCategory"/>
    </b-container>
    <category-add-modal/>
    <confirm-form :payload="selected[0]"
                  :dynamic-id="categoryConfirm"
                  :message="categoryMessage"
                  :op="removeCategory"/>
    <category-edit-modal ref="categoryEdit"/>
  </div>
</template>

<script>
/* eslint-disable */
  import {bus} from "../../../main";
  import ConfirmForm from "../../item/ConfirmForm";
  import CategoryTable from "../category/CategoryTable";
  import CategoryAddModal from "../category/CategoryAddModal";
  import CategoryEditModal from "../category/CategoryEditModal";

  export default {
    name: 'CategoryPage',
    components: {
      ConfirmForm,
      CategoryTable,
      CategoryAddModal,
      CategoryEditModal,
    },
    data() {
      return {
        categoryMessage: 'Удалить категорию из базы?',
        categoryConfirm: 'category-confirm',
        categories: [],
        selected: []
      };
    },
    methods: {
      async selectToRemoveCategory(data) {
        this.selected.push(data)
      },

      async fetchCategories() {
        const response = await fetch('http://localhost:8000/api/v1/category/')
        this.categories = await response.json()
        this.categories = this.categories['categories']
        this.selected = []
      },
      async removeCategory(unit) {
        const _id = unit['_id']
        const response = await fetch(`http://localhost:8000/api/v1/category/${_id}/`, {
          method: 'DELETE',
          headers: {
            'Accept': 'application/json',
            'Content-type': 'application/json'
          },
        });
        if (response.status !== 204) {
          alert(JSON.stringify(await response.json(), null, 2));
        }
        await this.fetchCategories()
      },
      editCategories(item) {
        this.$refs.categoryEdit.form = item
      },
    },
    async created() {
      await this.fetchCategories()

      await bus.$on('newData', () => {
        this.fetchCategories()
      })
    },
  };
</script>

<style scoped>

</style>
