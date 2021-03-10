<template>
  <div>
    <b-modal ref="typeAddModal"
           id="type-add-modal"
           title="Добавить тип составляющей"
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
              <b-form-group id="form-type-group"
                            label="Тип составляющей:"
                            label-for="form-type-input">
                <b-form-input id="form-type-input"
                              type="text"
                              class="mt-3"
                              v-model="form.type"
                              :value="form.type"
                              required
                              autofocus
                              placeholder="Введите тип составляющей"
                              :state="check(form.type, '')">
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
    name: "TypeAddModal",
    data() {
      return {
        form:{
          type: ''
        }
      }
    },
    methods: {
      async createType() {
        const response = await fetch('http://localhost:8000/api/v1/type/', {
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
        this.$refs.typeAddModal.hide()
      },
      onSubmit(evt) {
        evt.preventDefault();
        this.$refs.typeAddModal.hide();
        this.createType();
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

<style scoped>

</style>
