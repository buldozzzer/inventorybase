<template>
  <div>
    <b-modal ref="categoryAddModal"
           id="category-add-modal"
           title="Добавить категорию"
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
              <b-form-group id="form-category-group"
                            label="Категория:"
                            label-for="form-category-input">
                <b-form-input id="form-category-input"
                              type="text"
                              autofocus
                              class="mt-3"
                              v-model="form.category"
                              :value="form.category"
                              required
                              placeholder="Введите название категории"
                              :state="check(form.category, '')">
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
    name: "CategoryAddModal",
    data() {
      return {
        form:{
          category: ''
        }
      }
    },
    methods: {
      async createCategory() {
        const response = await fetch('http://localhost:8000/api/v1/category/', {
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
        this.$refs.categoryAddModal.hide()
      },
      onSubmit(evt) {
        evt.preventDefault();
        this.$refs.categoryAddModal.hide();
        this.createCategory();
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
