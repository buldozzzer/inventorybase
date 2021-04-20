<template>
  <div>
    <b-container>
      <b-col class="mt-3">
        <h3>Подразделение, откуда поступила мат. ценность</h3>
      </b-col>
      <b-col>
        <b-button variant="success" class="mt-3" v-b-modal.unit-add-modal>
          Добавить подразделение
        </b-button>
      </b-col>
      <unit-table :units="units"
                  :edit-unit="editUnit"
                  :select-to-remove-record="selectToRemoveUnit"/>
    </b-container>
    <unit-add-modal/>
    <confirm-form :payload="selected[0]"
                  :dynamic-id="unitConfirm"
                  :message="unitMessage"
                  :op="removeUnit"/>
    <unit-edit-modal ref="unitEdit"/>
  </div>
</template>

<script>
/* eslint-disable */
  import {bus} from "../../../main";
  import ConfirmForm from "../../item/ConfirmForm";
  import UnitTable from "../unit/UnitTable";
  import UnitAddModal from "../unit/UnitAddModal";
  import UnitEditModal from "../unit/UnitEditModal";

  export default {
    name: 'UnitPage',
    components: {
      ConfirmForm,
      UnitTable,
      UnitAddModal,
      UnitEditModal,
    },
    data() {
      return {
        unitMessage: 'Удалить подразделение из базы?',
        unitConfirm: 'unit-confirm',
        units: [],
        selected: []
      };
    },
    methods: {
      async selectToRemoveUnit(data) {
        this.selected.push(data)
      },
      async fetchUnits() {
        const response = await fetch('http://localhost:8000/inventorybase/api/v1/unit/',
        {
          mode: "cors",
        })
        this.units = await response.json()
        this.units = this.units['units']
        this.selected = []
      },
      async removeUnit(unit) {
        const _id = unit['_id']
        const response = await fetch(`http://localhost:8000/inventorybase/api/v1/unit/${_id}/`, {
          method: 'DELETE',
          mode:'cors',
          headers: {
            'Accept': 'application/json',
            'Content-type': 'application/json'
          },
        });
        if (response.status !== 204) {
          alert(JSON.stringify(await response.json(), null, 2));
        }
        await this.fetchUnits()
      },
      editUnit(item) {
        this.$refs.unitEdit.form = item
      },
    },
    async created() {
      await this.fetchUnits()

      await bus.$on('newData', () => {
        this.fetchUnits()
      })
    },
  };
</script>

<style scoped>

</style>
