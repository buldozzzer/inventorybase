<template>
  <div>
    <b-container>
      <b-col class="mt-3">
        <h3>ОТСС категории</h3>
      </b-col>
      <b-col>
        <b-button variant="success" class="mt-3" v-b-modal.o-t-s-s-category-add-modal>
          Добавить категорию ОТСС
        </b-button>
      </b-col>
      <o-t-s-s-category-table :otss-categories="otssCategories"
                              :edit-o-t-s-s="editOTSS"
                              :select-to-remove-record="selectToRemoveOTSS"/>
    </b-container>
    <o-t-s-s-category-add-modal/>
    <confirm-form :payload="selected[0]"
                  :dynamic-id="otssConfirm"
                  :message="otssCategoryMessage"
                  :op="removeOTSS"/>
    <o-t-s-s-category-edit-modal ref="otssEdit"/>
  </div>
</template>

<script>
/* eslint-disable */
  import OTSSCategoryAddModal from "./OTSSCategoryAddModal";
  import OTSSCategoryTable from "./OTSSCategoryTable";
  import OTSSCategoryEditModal from "./OTSSCategoryEditModal";
  import ConfirmForm from "../../item/ConfirmForm";
  import {bus} from "../../../main";

  export default {
    name: "OTSSCategoryPage",
    components: {
      ConfirmForm,
      OTSSCategoryAddModal,
      OTSSCategoryTable,
      OTSSCategoryEditModal,
    },
    data(){
      return {
        otssCategoryMessage: 'Удалить категорию ОТСС из базы?',
        otssConfirm: 'otss-confirm',
        otssCategories: [],
        selected: []
      }
    },
    methods:{
      async selectToRemoveOTSS(data) {
        this.selected.push(data)
      },
      async removeOTSS(otss) {
        const _id = otss['_id']
        const response = await fetch(`http://localhost:8000/api/v1/otss/${_id}/`, {
          method: 'DELETE',
          headers: {
            'Accept': 'application/json',
            'Content-type': 'application/json'
          },
        });
        if (response.status !== 204) {
          alert(JSON.stringify(await response.json(), null, 2));
        }
        await this.fetchOTSS()
      },
      async fetchOTSS() {
        const response = await fetch('http://localhost:8000/api/v1/otss/')
        this.otssCategories = await response.json()
        this.otssCategories = this.otssCategories['otss']
        this.selected = []
      },
      editOTSS(item) {
        this.$refs.otssEdit.form = item
      },
    },
    async created() {
      await this.fetchOTSS()

      await bus.$on('newData', () => {
        this.fetchOTSS()
      })
    },
  }
</script>

<style scoped>

</style>
