<template>
  <div>
    <b-modal ref="employeeAddModal"
           id="employee-add-modal"
           title="Добавить сотрудника в базу"
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
              <b-form-group id="form-surname-group"
                            label="ФИО:"
                            label-for="form-surname-input">
                <b-form-input id="form-surname-input"
                              type="text"
                              class="mt-3"
                              autofocus
                              v-model="form.surname"
                              :value="form.surname"
                              required
                              placeholder="Введите фамилию"
                              :state="check(form.surname, '')">
                </b-form-input>
                <b-form-input id="form-name-input"
                              type="text"
                              class="mt-3"
                              v-model="form.name"
                              :value="form.name"
                              required
                              placeholder="Введите имя"
                              :state="check(form.name, '')">
                </b-form-input>
                <b-form-input id="form-secname-input"
                              type="text"
                              class="mt-3"
                              v-model="form.secname"
                              :value="form.secname"
                              required
                              placeholder="Введите отчество"
                              :state="check(form.secname, '')">
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
    name: "EmployeeAddModal",
    data(){
      return{
        form: {
          surname: '',
          name: '',
          secname: '',
        }
      }
    },
    methods: {
      async createEmployee() {
        const response = await fetch(`${process.env.ROOT_API}/inventorybase/api/v1/employee/`, {
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
        this.$refs.employeeAddModal.hide()

      },
      onSubmit(evt) {
        evt.preventDefault();
        this.$refs.employeeAddModal.hide();
        this.createEmployee();
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
