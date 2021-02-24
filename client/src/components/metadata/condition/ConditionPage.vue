<template>
  <div>
    <b-container>
      <b-col class="mt-3">
        <h3>Состояния</h3>
      </b-col>
      <b-col>
        <b-button variant="success" class="mt-3" v-b-modal.condition-add-modal>
          Добавить состояние
        </b-button>
      </b-col>
      <condition-table :conditions="conditions"
                      :edit-condition="editConditions"
                      :select-to-remove-record="selectToRemoveCondition"/>
    </b-container>
    <condition-add-modal/>
    <confirm-form :payload="selected[0]"
                  :dynamic-id="conditionConfirm"
                  :message="conditionMessage"
                  :op="removeCondition"/>
    <condition-edit-modal ref="conditionEdit"/>
  </div>
</template>

<script>
/* eslint-disable */
  import {bus} from "../../../main";
  import ConfirmForm from "../../item/ConfirmForm";
  import ConditionTable from "../condition/ConditionTable";
  import ConditionAddModal from "../condition/ConditionAddModal";
  import ConditionEditModal from "../condition/ConditionEditModal";

  export default {
    name: 'ConditionPage',
    components: {
      ConfirmForm,
      ConditionTable,
      ConditionAddModal,
      ConditionEditModal,
    },
    data() {
      return {
        conditionMessage: 'Удалить состояние из базы?',
        conditionConfirm: 'condition-confirm',
        conditions: [],
        selected: []
      };
    },
    methods: {
      async selectToRemoveCondition(data) {
        this.selected.push(data)
      },

      async fetchConditions() {
        const response = await fetch('http://localhost:8000/api/v1/condition/')
        this.conditions = await response.json()
        this.conditions = this.conditions['conditions']
        this.selected = []
      },
      async removeCondition(unit) {
        const _id = unit['_id']
        const response = await fetch(`http://localhost:8000/api/v1/condition/${_id}/`, {
          method: 'DELETE',
          headers: {
            'Accept': 'application/json',
            'Content-type': 'application/json'
          },
        });
        if (response.status !== 204) {
          alert(JSON.stringify(await response.json(), null, 2));
        }
        await this.fetchConditions()
      },
      editConditions(item) {
        this.$refs.conditionEdit.form = item
      },
    },
    async created() {
      await this.fetchConditions()

      await bus.$on('newData', () => {
        this.fetchConditions()
      })
    },
  };
</script>

<style scoped>

</style>
