<template>
  <div>
    <b-modal id="employee-edit-modal"
             ref="employeeEditModal"
             title="Редактровать запись о сотруднике"
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
              <b-form-group id="form-surname-group"
                            label="ФИО:"
                            label-for="form-surname-input">
                <b-form-input id="form-surname-input"
                              type="text"
                              class="mt-3"
                              v-model="employeeForm.surname"
                              :value="employeeForm.surname"
                              required
                              placeholder="Введите фамилию"
                              :state="check(employeeForm.surname, '')">
                </b-form-input>
                <b-form-input id="form-name-input"
                              type="text"
                              class="mt-3"
                              v-model="employeeForm.name"
                              :value="employeeForm.name"
                              required
                              placeholder="Введите имя"
                              :state="check(employeeForm.name, '')">
                </b-form-input>
                <b-form-input id="form-secname-input"
                              type="text"
                              class="mt-3"
                              v-model="employeeForm.secname"
                              :value="employeeForm.secname"
                              required
                              placeholder="Введите отчество"
                              :state="check(employeeForm.secname, '')">
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
    name: "EmployeeEditModal",
    data(){
      return{
        employeeForm: {}
      }
    },
    methods:{
      async editEmployee(payload) {
        const _id = payload['_id'];
        const response = await fetch(`http://localhost:8000/api/v1/employee/${_id}/`, {
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
        this.$refs.employeeEditModal.hide()
      },
      onSubmit(evt) {
        evt.preventDefault();
        this.$refs.employeeEditModal.hide();
        const payload = this.employeeForm
        this.editEmployee(payload)
      },
      check(left, right){
        return left !== right
      }
    },
  }
</script>

<style scoped>

</style>
