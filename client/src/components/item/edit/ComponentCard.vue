<template>
  <div>
    <h4 :id="'component'+component.id">
      {{ 'Компонент ' + (component.id) }}
    </h4>
    <b-container>
      <b-row>
        <b-col cols="12">
          <b-form-group id="form-comp_name-group"
                        label="Название составляющей:"
                        label-for="form-comp_name-input">
            <b-form-input id="form-comp_name-input"
                          type="text"
                          required
                          :state="check(component.name, '')"
                          v-model="component.name"
                          placeholder="Введите название составляющей">
            </b-form-input>
          </b-form-group>
        </b-col>
      </b-row>

      <b-row>
        <b-col cols="12">
          <b-form-group id="form-comp_serial_n-group"
                        label="Заводской номер составляющей:"
                        label-for="form-comp_serial_n-input">
            <b-form-input id="form-comp_serial_n-input"
                          type="text"
                          v-model="component.serial_n"
                          placeholder="Введите заводской номер">
<!--              required-->
<!--              :state="check(component.serial_n, '')"-->
            </b-form-input>
          </b-form-group>
        </b-col>
      </b-row>

      <b-row>
        <b-col cols="6">
          <b-form-group id="form-comp_type-group"
                        label="Тип составляющей:"
                        label-for="form-comp_type-input">
            <b-form-input id="form-comp_type-input"
                          type="text"
                          v-model="component.type">
<!--                          required-->
<!--                          :state="check(component.type, '')"-->
            </b-form-input>
          </b-form-group>
        </b-col>

        <b-col cols="6">
          <b-form-group id="form-comp_cost-group"
                        label="Цена:"
                        label-for="form-comp_cost-input">
            <b-form-input id="form-comp_cost-input"
                          type="number"
                          min="0"
                          v-model="component.cost">
              <!--                                required-->
              <!--                                :state="check(component.cost, '')"-->
            </b-form-input>
          </b-form-group>
        </b-col>
      </b-row>

      <b-row>
        <b-col cols="6">
          <b-form-group id="form-comp_category-group"
                        label="Категория:"
                        label-for="form-comp_category-input">
            <b-form-input id="form-comp_category-input"
                          type="text"
                          v-model="component.category">
<!--                          required-->
<!--                          :state="check(component.category, '')"-->
            </b-form-input>
          </b-form-group>
        </b-col>

        <b-col cols="6">
          <b-form-group id="form-comp_year-group"
                        label="Год выпуска:"
                        label-for="form-comp_year-input">
            <b-form-input id="form-comp_year-input"
                          type="text"
                          v-model="component.year">
<!--                          required-->
<!--                          :state="check(component.year, '')"-->
            </b-form-input>
          </b-form-group>
        </b-col>
      </b-row>

      <b-row>
        <b-col cols="6">
          <b-form-group id="form-comp_object-group"
                        label="Объект:"
                        label-for="form-comp_object-input">
            <b-form-input id="form-comp_object-input"
                          type="text"
                          v-model="component.location.object">
<!--                          required-->
<!--                          :state="check(component.location.object, '')"-->
            </b-form-input>
          </b-form-group>
        </b-col>

        <b-col cols="6">
          <b-form-group id="form-comp_corpus-group"
                        label="Корпус:"
                        label-for="form-comp_corpus-input">
            <b-form-input id="form-comp_corpus-input"
                          type="text"
                          v-model="component.location.corpus">
<!--                          required-->
<!--                          :state="check(component.location.corpus, '')"-->
            </b-form-input>
          </b-form-group>
        </b-col>
      </b-row>

      <b-row>
        <b-col cols="6">
          <b-form-group id="form-comp_unit-group"
                        label="Подразделение:"
                        label-for="form-comp_unit-input">
            <b-form-input id="form-comp_unit-input"
                          type="text"
                          v-model="component.location.unit">
<!--                          required-->
<!--                          :state="check(component.location.unit, '')"-->
            </b-form-input>
          </b-form-group>
        </b-col>

        <b-col cols="6">
          <b-form-group id="form-comp_cabinet-group"
                        label="Кабинет:"
                        label-for="form-comp_cabinet-input">
            <b-form-input id="form-comp_cabinet-input"
                          type="text"
                          v-model="component.location.cabinet">
<!--                          required-->
<!--                          :state="check(component.location.cabinet, '')"-->
            </b-form-input>
          </b-form-group>
        </b-col>
      </b-row>
      <b-row>
        <b-col>
          <b-form-group id="form-user-group"
                        label="Лицо,которому передано в пользование:"
                        label-for="form-user-input">
            <!--              :state="isIntroduced(itemForm.user, '')"-->
            <b-form-input id="form-user-input"
                          v-model="component.user"
                          list="employee-list"
                          placeholder="Иванов И.И.">
            </b-form-input>
            <datalist id="employee-list">
              <option>---------</option>
              <option v-for="employee in employeeInitials">{{ employee }}</option>
            </datalist>
          </b-form-group>
        </b-col>
      </b-row>
    </b-container>
  </div>
</template>

<script>
/* eslint-disable */
  export default {
    name: "ComponentCard",
    props:['component', 'employeeInitials'],
    data(){
      return{
      }
    },
    methods:{
      check(left, right){
        return left !== right
      },
    },
  }
</script>

<style scoped>

</style>
