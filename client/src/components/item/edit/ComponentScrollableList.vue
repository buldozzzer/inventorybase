<template>
<div>
          <h4 id="component-1">1 компонент</h4>
          <b-container id="comp-1">
            <b-row>
              <b-col cols="12">
                <b-form-group id="form-comp-1_name-group"
                              label="Название составляющей:"
                              label-for="form-comp-1_name-input">
                  <b-form-input id="form-comp-1_name-input"
                                type="text"
                                required
                                :state="check(component1.name, '')"
                                v-model="component1.name"
                                placeholder="Введите название составляющей">
                  </b-form-input>
                </b-form-group>
              </b-col>
            </b-row>

            <b-row>
              <b-col cols="12">
                <b-form-group id="form-comp-1_serial_n-group"
                              label="Заводской номер составляющей:"
                              label-for="form-comp-1_serial_n-input">
                  <b-form-input id="form-comp-1_serial_n-input"
                                type="text"
                                v-model="component1.serial_n"

                                required
                                :state="check(component1.serial_n, '')"
                                placeholder="Введите заводской номер">
                  </b-form-input>
                </b-form-group>
              </b-col>
            </b-row>

            <b-row>
              <b-col cols="6">
                <b-form-group id="form-comp-1_type-group"
                              label="Тип составляющей:"
                              label-for="form-comp-1_type-input">
                  <b-form-input id="form-comp-1_type-input"
                                type="text"
                                v-model="component1.type"

                                required
                                :state="check(component1.type, '')"
                  >
                  </b-form-input>
                </b-form-group>
              </b-col>

              <b-col cols="6">
                <b-form-group id="form-comp-1_view-group"
                              label="Вид составляющей:"
                              label-for="form-comp-1_view-input">
                  <b-form-input id="form-comp-1_view-input"
                                type="text"
                                v-model="component1.view"

                                required
                                :state="check(component1.view, '')"
                  >
                  </b-form-input>
                </b-form-group>
              </b-col>
            </b-row>

            <b-row>
              <b-col cols="6">
                <b-form-group id="form-comp-1_category-group"
                              label="Категория:"
                              label-for="form-comp-1_category-input">
                  <b-form-input id="form-comp-1_category-input"
                                type="text"
                                v-model="component1.category"

                                required
                                :state="check(component1.category, '')"
                  >
                  </b-form-input>
                </b-form-group>
              </b-col>

              <b-col cols="6">
                <b-form-group id="form-comp-1_year-group"
                              label="Год выпуска:"
                              label-for="form-comp-1_year-input">
                  <b-form-input id="form-comp-1_year-input"
                                type="text"
                                v-model="component1.year"

                                required
                                :state="check(component1.year, '')"
                  >
                  </b-form-input>
                </b-form-group>
              </b-col>
            </b-row>

            <b-row>
              <b-col cols="6">
                <b-form-group id="form-comp-1_cost-group"
                              label="Цена:"
                              label-for="form-comp-1_cost-input">
                  <b-form-input id="form-comp-1_cost-input"
                                type="text"
                                v-model="component1.cost"

                                required
                                :state="check(component1.cost, '')"
                  >
                  </b-form-input>
                </b-form-group>
              </b-col>
            </b-row>

            <b-row>
              <b-col cols="6">
                <b-form-group id="form-comp-1_object-group"
                              label="Объект:"
                              label-for="form-comp-1_object-input">
                  <b-form-input id="form-comp-1_object-input"
                                type="text"
                                v-model="component1.location.object"

                                required
                                :state="check(component1.location.object, '')"
                  >
                  </b-form-input>
                </b-form-group>
              </b-col>

              <b-col cols="6">
                <b-form-group id="form-comp-1_corpus-group"
                              label="Корпус:"
                              label-for="form-comp-1_corpus-input">
                  <b-form-input id="form-comp-1_corpus-input"
                                type="text"
                                v-model="component1.location.corpus"

                                required
                                :state="check(component1.location.corpus, '')"
                  >
                  </b-form-input>
                </b-form-group>
              </b-col>
            </b-row>

            <b-row>
              <b-col cols="6">
                <b-form-group id="form-comp-1_unit-group"
                              label="Подразделение:"
                              label-for="form-comp-1_unit-input">
                  <b-form-input id="form-comp-1_unit-input"
                                type="text"
                                v-model="component1.location.unit"
                                required
                                :state="check(component1.location.unit, '')"
                  >
                  </b-form-input>
                </b-form-group>
              </b-col>

              <b-col cols="6">
                <b-form-group id="form-comp-1_cabinet-group"
                              label="Кабинет:"
                              label-for="form-comp-1_cabinet-input">
                  <b-form-input id="form-comp-1_cabinet-input"
                                type="text"
                                v-model="component1.location.cabinet"

                                required
                                :state="check(component1.location.cabinet, '')"
                  >
                  </b-form-input>
                </b-form-group>
              </b-col>
            </b-row>

            <b-row v-if="!show2">
              <b-col cols="4">
                <b-button @click="show2=addComponent(component1)">Добавить компонент</b-button>
              </b-col>
            </b-row>
          </b-container>
        </div>
</template>

<script>
export default {
name: "ComponentScrollableList"
}
</script>

<style scoped>

</style>
