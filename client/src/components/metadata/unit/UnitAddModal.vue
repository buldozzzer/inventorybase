<template>
  <div>
    <b-modal ref="unitAddModal"
           id="unit-add-modal"
           title="Добавить подразделние, откуда поступила мат. ценность в базу"
           no-close-on-backdrop
           hide-footer
           hide-header-close>
      <b-form class="w-100">
      <div class="submit-reset-buttons mt-3 my">
        <b-button type="submit" variant="success" @click="onSubmit">
          Добавить
        </b-button>
        <b-button type="reset" variant="danger" @click="onReset">
          Отмена
        </b-button>
      </div>
        <div class="container mt-3">
          <div class="row">
            <div class="col">
              <b-form-group id="form-unit-group"
                            label="Подразделение, откуда поступила мат. ценность:"
                            label-for="form-unit-input">
                <b-form-input id="form-unit-input"
                              type="text"
                              class="mt-3"
                              v-model="form.unit"
                              :value="form.unit"
                              required
                              autofocus
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
    name: "UnitAddModal",
    data() {
      return {
        form:{
          unit: ''
        }
      }
    },
    methods: {
      async createUnit() {
        const response = await fetch('http://localhost:8000/api/v1/unit/', {
          method: 'POST',
          mode: 'cors',
          headers: {
            'Accept': 'application/json',
            'Content-type': 'application/json'
          },
          body: JSON.stringify(this.form)
        });
        if (response.status !== 201) {
          alert(JSON.stringify(await response.json(), null, 2));
        }
        bus.$emit('newData')
      },
      onReset(evt) {
        evt.preventDefault()
        this.initForm()
        this.$refs.unitAddModal.hide()
      },
      onSubmit(evt) {
        evt.preventDefault();
        this.$refs.unitAddModal.hide();
        this.createUnit();
        this.initForm()
      },
      check(left, right){
        return left !== right
      },
      initForm(){
        for(let key in this.form){
          this.form[key] = ''
        }
      }
    }
  }
</script>

<style>

</style>
