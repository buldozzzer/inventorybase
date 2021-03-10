<template>
  <div>
    <b-modal ref="categoryEditModal"
             id="category-edit-modal"
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
              <b-form-group id="form-category-group"
                            label="Категория:"
                            label-for="form-category-input">
                <b-form-input id="form-category-input"
                              type="text"
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
    name: "CategoryEditModal",
    data() {
      return {
        form:{
          category: ''
        }
      }
    },
    methods:{
      async editCategory(payload) {
        const _id = payload['_id'];
        const response = await fetch(`http://localhost:8000/api/v1/category/${_id}/`, {
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
        this.$refs.categoryEditModal.hide()
      },
      onSubmit(evt) {
        evt.preventDefault();
        this.$refs.categoryEditModal.hide();
        const payload = this.form
        this.editCategory(payload)
      },
      check(left, right){
        return left !== right
      }
    },

  }
</script>

<style>

</style>
