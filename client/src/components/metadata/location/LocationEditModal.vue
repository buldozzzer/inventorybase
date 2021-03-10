<template>
  <div>
    <b-modal ref="locationEditModal"
           id="location-edit-modal"
           title="Редактировать местоположение"
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
              <b-form-group id="form-location-group"
                            label="Местоположение:"
                            label-for="form-object-input">
                <b-form-input id="form-location-input"
                              type="text"
                              class="mt-3"
                              v-model="form.object"
                              :value="form.object"
                              required
                              placeholder="Введите название объекта"
                              :state="check(form.object, '')">
                </b-form-input>
                <b-form-input id="form-corpus-input"
                              type="text"
                              class="mt-3"
                              v-model="form.corpus"
                              :value="form.corpus"
                              required
                              placeholder="Введите номер корпуса"
                              :state="check(form.corpus, '')">
                </b-form-input>
                <b-form-input id="form-cabinet-input"
                              type="text"
                              class="mt-3"
                              v-model="form.cabinet"
                              :value="form.cabinet"
                              required
                              placeholder="Введите номер кабинета"
                              :state="check(form.cabinet, '')">
                </b-form-input>
                <b-form-input id="form-unit-input"
                              type="text"
                              class="mt-3"
                              v-model="form.unit"
                              :value="form.unit"
                              required
                              placeholder="Введите подразделение"
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
    name: "LocationEditModal",
    data() {
      return {
        form: {
          object: '',
          corpus: '',
          cabinet: '',
          unit: ''
        }
      }
    },
    methods:{
      async editLocation(payload) {
        const _id = payload['_id'];
        const response = await fetch(`http://localhost:8000/api/v1/location/${_id}/`, {
          method: 'PUT',
          mode: 'cors',
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
        this.$refs.locationEditModal.hide()
      },
      onSubmit(evt) {
        evt.preventDefault();
        this.$refs.locationEditModal.hide();
        const payload = this.form
        this.editLocation(payload)
      },
      check(left, right){
        return left !== right
      }
    },

  }
</script>

<style scoped>

</style>
