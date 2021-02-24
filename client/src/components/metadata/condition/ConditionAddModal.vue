<template>
  <div>
    <b-modal ref="conditionAddModal"
           id="condition-add-modal"
           title="Добавить состояние"
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
              <b-form-group id="form-condition-group"
                            label="Категория:"
                            label-for="form-condition-input">
                <b-form-input id="form-condition-input"
                              type="text"
                              class="mt-3"
                              v-model="form.condition"
                              :value="form.condition"
                              required
                              placeholder="Введите название категории"
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
    name: "ConditionAddModal",
    data() {
      return {
        form:{
          condition: ''
        }
      }
    },
    methods: {
      async createCondition() {
        const response = await fetch('http://localhost:8000/api/v1/condition/', {
          method: 'POST',
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
        this.$refs.conditionAddModal.hide()
      },
      onSubmit(evt) {
        evt.preventDefault();
        this.$refs.conditionAddModal.hide();
        this.createCondition();
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
