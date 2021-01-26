<template>
  <div>
    <b-modal ref="unitEditModal"
             id="unit-edit-modal"
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
              <b-form-group id="form-unit-group"
                            label="Подразделние, откуда поступила мат. ценность:"
                            label-for="form-unit-input">
                <b-form-input id="form-unit-input"
                              type="text"
                              class="mt-3"
                              v-model="form.unit"
                              :value="form.unit"
                              required
                              placeholder="Введите название подразделния"
                              :state="check(form.unit, '')">
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
    name: "UnitEditModal",
    data() {
      return {
        form:{
          unit: ''
        }
      }
    },
    methods:{
      async editUnit(payload) {
        const _id = payload['_id'];
        const response = await fetch(`http://localhost:8000/api/v1/unit/${_id}/`, {
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
        this.$refs.unitEditModal.hide()
      },
      onSubmit(evt) {
        evt.preventDefault();
        this.$refs.unitEditModal.hide();
        const payload = this.form
        this.editUnit(payload)
      },
      check(left, right){
        return left !== right
      }
    },

  }
</script>

<style>

</style>
