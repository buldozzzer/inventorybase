<template>
  <div>
    <b-container>
      <b-col class="mt-3">
        <h3>Типы состовляющих</h3>
      </b-col>
      <b-col>
        <b-button variant="success" class="mt-3" v-b-modal.type-add-modal>
          Добавить тип составляющей
        </b-button>
      </b-col>
      <type-table :types="types"
                  :edit-type="editType"
                  :select-to-remove-record="selectToRemoveType"/>
    </b-container>
    <type-add-modal/>
    <confirm-form :payload="selected[0]"
                  :dynamic-id="typeConfirm"
                  :message="typeMessage"
                  :op="removeType"/>
    <type-edit-modal ref="typeEdit"/>
  </div>
</template>

<script>
/* eslint-disable */
  import {bus} from "../../../main";
  import ConfirmForm from "../../item/ConfirmForm";
  import TypeTable from "../type/TypeTable";
  import TypeAddModal from "../type/TypeAddModal";
  import TypeEditModal from "../type/TypeEditModal";

  export default {
    name: 'TypePage',
    components: {
      ConfirmForm,
      TypeTable,
      TypeAddModal,
      TypeEditModal,
    },
    data() {
      return {
        typeMessage: 'Удалить тип из базы?',
        typeConfirm: 'type-confirm',
        types: [],
        selected: []
      };
    },
    methods: {
      async selectToRemoveType(data) {
        this.selected.push(data)
      },

      async fetchTypes() {
        const response = await fetch('http://localhost:8000/api/v1/type/')
        this.types = await response.json()
        this.types = this.types['types']
        this.selected = []
      },
      async removeType(unit) {
        const _id = unit['_id']
        const response = await fetch(`http://localhost:8000/api/v1/type/${_id}/`, {
          method: 'DELETE',
          headers: {
            'Accept': 'application/json',
            'Content-type': 'application/json'
          },
        });
        if (response.status !== 204) {
          alert(JSON.stringify(await response.json(), null, 2));
        }
        await this.fetchTypes()
      },
      editType(item) {
        this.$refs.typeEdit.form = item
      },
    },
    async created() {
      await this.fetchTypes()

      await bus.$on('newData', () => {
        this.fetchTypes()
      })
    },
  };
</script>

<style scoped>

</style>
