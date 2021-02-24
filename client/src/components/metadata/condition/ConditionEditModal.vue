<template>
  <div>
    <b-modal ref="conditionEditModal"
             id="condition-edit-modal"
             title="Редактировать запись"
             no-close-on-backdrop
             hide-footer
             hide-header-close>
      <b-form class="w-100">
      <div class="submit-reset-buttons mt-3 my">
        <b-button type="submit" variant="success" @click="onSubmit">
          Редактировать
        </b-button>
        <b-button type="reset" variant="danger" @click="onReset">
          Отмена
        </b-button>
      </div>
        <div class="container mt-3">
          <div class="row">
            <div class="col">
              <b-form-group id="form-condition-group"
                            label="Категория:"
                            label-for="form-condition-input">
                <b-form-input id="form-condition-input"
                              type="text"
                              class="mt-3"
                              v-model="form.condition"
                              :value="form.condition"
                              required
                              placeholder="Введите название состояния"
                              :state="check(form.condition, '')">
                </b-form-input>
              </b-form-group>
            </div>
          </div>
        </div>
      </b-form>
    </b-modal>
  </div>
</template>

<script>
/* eslint-disable */
  import {bus} from "../../../main";

  export default {
    name: "ConditionEditModal",
    data() {
      return {
        form:{
          condition: ''
        }
      }
    },
    methods:{
      async editCondition(payload) {
        const _id = payload['_id'];
        const response = await fetch(`http://localhost:8000/api/v1/condition/${_id}/`, {
          method: 'PUT',
          body: JSON.stringify(payload),
          headers: {
            'Accept': 'application/json',
            'Content-type': 'application/json'
          },
        });
        const json = await response.json();
        console.log('Успех:', JSON.stringify(json));
        if (response.status !== 202) {
          alert(JSON.stringify(await response.json(), null, 2));
        }
        bus.$emit('newData')
      },
      onReset(evt) {
        evt.preventDefault()
        this.$refs.conditionEditModal.hide()
      },
      onSubmit(evt) {
        evt.preventDefault();
        this.$refs.conditionEditModal.hide();
        const payload = this.form
        this.editCondition(payload)
      },
      check(left, right){
        return left !== right
      }
    },

  }
</script>

<style>

</style>
