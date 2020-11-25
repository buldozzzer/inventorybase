<template>
  <b-card no-body>
    <b-card no-body>
      <b-nav pills card-header slot="header" v-b-scrollspy:nav-scroller>
        <b-nav-item href="#component-1" @click="scrollIntoView">1 компонент</b-nav-item>
        <!--        eslint-disable-next-line-->
        <b-nav-item href="#component-2" @click="scrollIntoView" v-if="show2">2 компонент</b-nav-item>
        <!--        eslint-disable-next-line-->
        <b-nav-item href="#component-3" @click="scrollIntoView" v-if="show3">3 компонент</b-nav-item>
        <!--        eslint-disable-next-line-->
        <b-nav-item href="#component-4" @click="scrollIntoView" v-if="show4">4 компонент</b-nav-item>
        <!--        eslint-disable-next-line-->
        <b-nav-item href="#component-5" @click="scrollIntoView" v-if="show5">5 компонент</b-nav-item>
      </b-nav>

      <b-card-body
        id="nav-scroller"
        ref="content"
        style="position:relative; height:650px; overflow-y:scroll;">
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
        <div v-if="show2">
          <h4 id="component-2">2 компонент</h4>
          <b-container id="comp-2">
            <b-row>
              <b-col cols="12">
                <b-form-group id="form-comp-2_name-group"
                              label="Название составляющей:"
                              label-for="form-comp-2_name-input">
                  <b-form-input id="form-comp-2_name-input"
                                type="text"
                                required
                                :state="check(component2.name, '')"
                                v-model="component2.name"
                                placeholder="Введите название составляющей">
                  </b-form-input>
                </b-form-group>
              </b-col>
            </b-row>

            <b-row>
              <b-col cols="12">
                <b-form-group id="form-comp-2_serial_n-group"
                              label="Заводской номер составляющей:"
                              label-for="form-comp-2_serial_n-input">
                  <b-form-input id="form-comp-2_serial_n-input"
                                type="text"
                                v-model="component2.serial_n"
                                required
                                :state="check(component2.serial_n, '')"
                                placeholder="Введите заводской номер">
                  </b-form-input>
                </b-form-group>
              </b-col>
            </b-row>

            <b-row>
              <b-col cols="6">
                <b-form-group id="form-comp-2_type-group"
                              label="Тип составляющей:"
                              label-for="form-item_type-input">
                  <b-form-input id="form-item_type-input"
                                type="text"
                                v-model="component2.type"
                                required
                                :state="check(component2.type, '')"
                  >
                  </b-form-input>
                </b-form-group>
              </b-col>

              <b-col cols="6">
                <b-form-group id="form-comp-2_view-group"
                              label="Вид составляющей:"
                              label-for="form-comp-2_view-input">
                  <b-form-input id="form-comp-2_view-input"
                                type="text"
                                v-model="component2.view"
                                required
                                :state="check(component2.view, '')"
                  >
                  </b-form-input>
                </b-form-group>
              </b-col>
            </b-row>

            <b-row>
              <b-col cols="6">
                <b-form-group id="form-comp-2_category-group"
                              label="Категория:"
                              label-for="form-comp-2_category-input">
                  <b-form-input id="form-comp-2_category-input"
                                type="text"
                                v-model="component2.category"
                                required
                                :state="check(component2.category, '')"
                  >
                  </b-form-input>
                </b-form-group>
              </b-col>

              <b-col cols="6">
                <b-form-group id="form-comp-2_year-group"
                              label="Год выпуска:"
                              label-for="form-comp-2_year-input">
                  <b-form-input id="form-comp-2_year-input"
                                type="text"
                                v-model="component2.year"
                                required
                                :state="check(component2.year, '')"
                  >
                  </b-form-input>
                </b-form-group>
              </b-col>
            </b-row>

            <b-row>
              <b-col cols="6">
                <b-form-group id="form-comp-2_object-group"
                              label="Объект:"
                              label-for="form-comp-2_object-input">
                  <b-form-input id="form-comp-2_object-input"
                                type="text"
                                v-model="component2.location.object"
                                required
                                :state="check(component2.location.object, '')"
                  >
                  </b-form-input>
                </b-form-group>
              </b-col>

              <b-col cols="6">
                <b-form-group id="form-comp-2_corpus-group"
                              label="Корпус:"
                              label-for="form-comp-2_corpus-input">
                  <b-form-input id="form-comp-2_corpus-input"
                                type="text"
                                v-model="component2.location.corpus"
                                required
                                :state="check(component2.location.corpus, '')"
                  >
                  </b-form-input>
                </b-form-group>
              </b-col>
            </b-row>

            <b-row>
              <b-col cols="6">
                <b-form-group id="form-comp-2_unit-group"
                              label="Подразделение:"
                              label-for="form-comp-2_unit-input">
                  <b-form-input id="form-comp-2_unit-input"
                                type="text"
                                v-model="component2.location.unit"
                                required
                                :state="check(component2.location.unit, '')"
                  >
                  </b-form-input>
                </b-form-group>
              </b-col>

              <b-col cols="6">
                <b-form-group id="form-comp-2_cabinet-group"
                              label="Кабинет:"
                              label-for="form-comp-2_cabinet-input">
                  <b-form-input id="form-comp-2_cabinet-input"
                                type="text"
                                v-model="component2.location.cabinet"
                                required
                                :state="check(component2.location.cabinet, '')"
                  >
                  </b-form-input>
                </b-form-group>
              </b-col>
            </b-row>
            <b-row v-if="!show3">
              <b-col cols="4">
                <b-button @click="show3 = addComponent(component2)">Добавить компонент</b-button>
              </b-col>
            </b-row>
          </b-container>
        </div>
        <div v-if="show3">
          <h4 id="component-3">3 компонент</h4>
          <b-container id="comp-3">
            <b-row>
              <b-col cols="12">
                <b-form-group id="form-comp-3_name-group"
                              label="Название составляющей:"
                              label-for="form-comp-3_name-input">
                  <b-form-input id="form-comp-3_name-input"
                                type="text"
                                required
                                :state="check(component3.name, '')"
                                v-model="component3.name"
                                placeholder="Введите название составляющей">
                  </b-form-input>
                </b-form-group>
              </b-col>
            </b-row>

            <b-row>
              <b-col cols="12">
                <b-form-group id="form-comp-3_serial_n-group"
                              label="Заводской номер составляющей:"
                              label-for="form-comp-3_serial_n-input">
                  <b-form-input id="form-comp-3_serial_n-input"
                                type="text"
                                v-model="component3.serial_n"
                                required
                                :state="check(component3.serial_n, '')"
                                placeholder="Введите заводской номер">
                  </b-form-input>
                </b-form-group>
              </b-col>
            </b-row>

            <b-row>
              <b-col cols="6">
                <b-form-group id="form-comp-3_type-group"
                              label="Тип составляющей:"
                              label-for="form-comp-3_type-input">
                  <b-form-input id="form-comp-3_type-input"
                                type="text"
                                v-model="component3.type"
                                required
                                :state="check(component3.type, '')"
                  >
                  </b-form-input>
                </b-form-group>
              </b-col>

              <b-col cols="6">
                <b-form-group id="form-comp-3_view-group"
                              label="Вид составляющей:"
                              label-for="form-comp-3_view-input">
                  <b-form-input id="form-comp-3_view-input"
                                type="text"
                                v-model="component3.view"
                                required
                                :state="check(component3.view, '')"
                  >
                  </b-form-input>
                </b-form-group>
              </b-col>
            </b-row>

            <b-row>
              <b-col cols="6">
                <b-form-group id="form-comp-3_category-group"
                              label="Категория:"
                              label-for="form-comp-3_category-input">
                  <b-form-input id="form-comp-3_category-input"
                                type="text"
                                v-model="component3.category"
                                required
                                :state="check(component3.category, '')"
                  >
                  </b-form-input>
                </b-form-group>
              </b-col>

              <b-col cols="6">
                <b-form-group id="form-comp-3_year-group"
                              label="Год выпуска:"
                              label-for="form-comp-3_year-input">
                  <b-form-input id="form-comp-3_year-input"
                                type="text"
                                v-model="component3.year"
                                required
                                :state="check(component3.year, '')"
                  >
                  </b-form-input>
                </b-form-group>
              </b-col>
            </b-row>

            <b-row>
              <b-col cols="6">
                <b-form-group id="form-comp-3_object-group"
                              label="Объект:"
                              label-for="form-comp-3_object-input">
                  <b-form-input id="form-comp-3_object-input"
                                type="text"
                                v-model="component3.location.object"
                                required
                                :state="check(component3.location.object, '')"
                  >
                  </b-form-input>
                </b-form-group>
              </b-col>

              <b-col cols="6">
                <b-form-group id="form-comp-3_corpus-group"
                              label="Корпус:"
                              label-for="form-comp-3_corpus-input">
                  <b-form-input id="form-comp-3_corpus-input"
                                type="text"
                                v-model="component3.location.corpus"
                                required
                                :state="check(component3.location.corpus, '')"
                  >
                  </b-form-input>
                </b-form-group>
              </b-col>
            </b-row>

            <b-row>
              <b-col cols="6">
                <b-form-group id="form-comp-3_unit-group"
                              label="Подразделение:"
                              label-for="form-comp-3_unit-input">
                  <b-form-input id="form-comp-3_unit-input"
                                type="text"
                                v-model="component3.location.unit"
                                required
                                :state="check(component3.location.unit, '')"
                  >
                  </b-form-input>
                </b-form-group>
              </b-col>

              <b-col cols="6">
                <b-form-group id="form-comp-3_cabinet-group"
                              label="Кабинет:"
                              label-for="form-comp-3_cabinet-input">
                  <b-form-input id="form-comp-3_cabinet-input"
                                type="text"
                                v-model="component3.location.cabinet"
                                required
                                :state="check(component3.location.cabinet, '')"
                  >
                  </b-form-input>
                </b-form-group>
              </b-col>
            </b-row>

            <b-row v-if="!show4">
              <b-col cols="4">
                <b-button @click="show4 = addComponent(component3)">Добавить компонент</b-button>
              </b-col>
            </b-row>
          </b-container>
        </div>
        <div v-if="show4">
          <h4 id="component-4">4 компонент</h4>
          <b-container id="comp-4">
            <b-row>
              <b-col cols="12">
                <b-form-group id="form-comp-4_name-group"
                              label="Название составляющей:"
                              label-for="form-comp-4_name-input">
                  <b-form-input id="form-comp-4_name-input"
                                type="text"
                                required
                                :state="check(component4.name, '')"
                                v-model="component4.name"
                                placeholder="Введите название составляющей">
                  </b-form-input>
                </b-form-group>
              </b-col>
            </b-row>

            <b-row>
              <b-col cols="12">
                <b-form-group id="form-comp-4_serial_n-group"
                              label="Заводской номер составляющей:"
                              label-for="form-comp-4_serial_n-input">
                  <b-form-input id="form-comp-4_serial_n-input"
                                type="text"
                                v-model="component4.serial_n"
                                required
                                :state="check(component4.serial_n, '')"
                                placeholder="Введите заводской номер">
                  </b-form-input>
                </b-form-group>
              </b-col>
            </b-row>

            <b-row>
              <b-col cols="6">
                <b-form-group id="form-comp-4_type-group"
                              label="Тип составляющей:"
                              label-for="form-comp-4_type-input">
                  <b-form-input id="form-comp-4_type-input"
                                type="text"
                                v-model="component4.type"
                                required
                                :state="check(component4.type, '')"
                  >
                  </b-form-input>
                </b-form-group>
              </b-col>

              <b-col cols="6">
                <b-form-group id="form-comp-4_view-group"
                              label="Вид составляющей:"
                              label-for="form-comp-4_view-input">
                  <b-form-input id="form-comp-4_view-input"
                                type="text"
                                v-model="component4.view"
                                required
                                :state="check(component4.view, '')"
                  >
                  </b-form-input>
                </b-form-group>
              </b-col>
            </b-row>

            <b-row>
              <b-col cols="6">
                <b-form-group id="form-comp-4_category-group"
                              label="Категория:"
                              label-for="form-comp-4_category-input">
                  <b-form-input id="form-comp-4_category-input"
                                type="text"
                                v-model="component4.category"
                                required
                                :state="check(component4.category, '')"
                  >
                  </b-form-input>
                </b-form-group>
              </b-col>

              <b-col cols="6">
                <b-form-group id="form-comp-4_year-group"
                              label="Год выпуска:"
                              label-for="form-comp-4_year-input">
                  <b-form-input id="form-comp-4_year-input"
                                type="text"
                                v-model="component4.year"
                                required
                                :state="check(component4.year, '')"
                  >
                  </b-form-input>
                </b-form-group>
              </b-col>
            </b-row>

            <b-row>
              <b-col cols="6">
                <b-form-group id="form-comp-4_object-group"
                              label="Объект:"
                              label-for="form-comp-4_object-input">
                  <b-form-input id="form-comp-4_object-input"
                                type="text"
                                v-model="component4.location.object"
                                required
                                :state="check(component4.location.object, '')"
                  >
                  </b-form-input>
                </b-form-group>
              </b-col>

              <b-col cols="6">
                <b-form-group id="form-comp-4_corpus-group"
                              label="Корпус:"
                              label-for="form-comp-4_corpus-input">
                  <b-form-input id="form-comp-4_corpus-input"
                                type="text"
                                v-model="component4.location.corpus"
                                required
                                :state="check(component4.location.corpus, '')"
                  >
                  </b-form-input>
                </b-form-group>
              </b-col>
            </b-row>

            <b-row>
              <b-col cols="6">
                <b-form-group id="form-comp-4_unit-group"
                              label="Подразделение:"
                              label-for="form-comp-4_unit-input">
                  <b-form-input id="form-comp-4_unit-input"
                                type="text"
                                v-model="component4.location.unit"
                                required
                                :state="check(component4.location.unit, '')"
                  >
                  </b-form-input>
                </b-form-group>
              </b-col>

              <b-col cols="6">
                <b-form-group id="form-comp-4_cabinet-group"
                              label="Кабинет:"
                              label-for="form-comp-4_cabinet-input">
                  <b-form-input id="form-comp-4_cabinet-input"
                                type="text"
                                v-model="component4.location.cabinet"
                                required
                                :state="check(component4.location.cabinet, '')"
                  >
                  </b-form-input>
                </b-form-group>
              </b-col>
            </b-row>

            <b-row v-if="!show5">
              <b-col cols="4">
                <b-button @click="show5 = addComponent(component4)">Добавить компонент</b-button>
              </b-col>
            </b-row>
          </b-container>
        </div>
        <div v-if="show5">
          <h4 id="component-5">5 компонент</h4>
          <b-container id="comp-5">
            <b-row>
              <b-col cols="12">
                <b-form-group id="form-comp-5_name-group"
                              label="Название составляющей:"
                              label-for="form-comp-5_name-input">
                  <b-form-input id="form-comp-5_name-input"
                                type="text"
                                required
                                :state="check(component5.name, '')"
                                v-model="component5.name"
                                placeholder="Введите название составляющей">
                  </b-form-input>
                </b-form-group>
              </b-col>
            </b-row>

            <b-row>
              <b-col cols="12">
                <b-form-group id="form-comp-5_serial_n-group"
                              label="Заводской номер составляющей:"
                              label-for="form-comp-5_serial_n-input">
                  <b-form-input id="form-comp-5_serial_n-input"
                                type="text"
                                v-model="component5.serial_n"
                                required
                                :state="check(component5.serial_n, '')"
                                placeholder="Введите заводской номер">
                  </b-form-input>
                </b-form-group>
              </b-col>
            </b-row>

            <b-row>
              <b-col cols="6">
                <b-form-group id="form-comp-5_type-group"
                              label="Тип составляющей:"
                              label-for="form-comp-5_type-input">
                  <b-form-input id="form-comp-5_type-input"
                                type="text"
                                v-model="component5.type"
                                required
                                :state="check(component5.type, '')"
                  >
                  </b-form-input>
                </b-form-group>
              </b-col>

              <b-col cols="6">
                <b-form-group id="form-comp-5_view-group"
                              label="Вид составляющей:"
                              label-for="form-comp-5_view-input">
                  <b-form-input id="form-comp-5_view-input"
                                type="text"
                                v-model="component5.view"
                                required
                                :state="check(component5.view, '')"
                  >
                  </b-form-input>
                </b-form-group>
              </b-col>
            </b-row>

            <b-row>
              <b-col cols="6">
                <b-form-group id="form-comp-5_category-group"
                              label="Категория:"
                              label-for="form-comp-5_category-input">
                  <b-form-input id="form-comp-5_category-input"
                                type="text"
                                v-model="component5.category"
                                required
                                :state="check(component5.category, '')"
                  >
                  </b-form-input>
                </b-form-group>
              </b-col>

              <b-col cols="6">
                <b-form-group id="form-comp-5_year-group"
                              label="Год выпуска:"
                              label-for="form-comp-5_year-input">
                  <b-form-input id="form-comp-5_year-input"
                                type="text"
                                v-model="component5.year"
                                required
                                :state="check(component5.year, '')"
                  >
                  </b-form-input>
                </b-form-group>
              </b-col>
            </b-row>

            <b-row>
              <b-col cols="6">
                <b-form-group id="form-comp-5_object-group"
                              label="Объект:"
                              label-for="form-comp-5_object-input">
                  <b-form-input id="form-comp-5_object-input"
                                type="text"
                                v-model="component5.location.object"
                                required
                                :state="check(component5.location.object, '')"
                  >
                  </b-form-input>
                </b-form-group>
              </b-col>

              <b-col cols="6">
                <b-form-group id="form-comp-5_corpus-group"
                              label="Корпус:"
                              label-for="form-comp-5_corpus-input">
                  <b-form-input id="form-comp-5_corpus-input"
                                type="text"
                                v-model="component5.location.corpus"
                                required
                                :state="check(component5.location.corpus, '')"
                  >
                  </b-form-input>
                </b-form-group>
              </b-col>
            </b-row>

            <b-row>
              <b-col cols="6">
                <b-form-group id="form-comp-5_unit-group"
                              label="Подразделение:"
                              label-for="form-comp-5_unit-input">
                  <b-form-input id="form-comp-5_unit-input"
                                type="text"
                                v-model="component5.location.unit"
                                required
                                :state="check(component5.location.unit, '')"
                  >
                  </b-form-input>
                </b-form-group>
              </b-col>

              <b-col cols="6">
                <b-form-group id="form-comp-5_cabinet-group"
                              label="Кабинет:"
                              label-for="form-comp-5_cabinet-input">
                  <b-form-input id="form-comp-5_cabinet-input"
                                type="text"
                                v-model="component5.location.cabinet"
                                required
                                :state="check(component5.location.cabinet, '')"
                  >
                  </b-form-input>
                </b-form-group>
              </b-col>
            </b-row>
          </b-container>
        </div>
      </b-card-body>
    </b-card>
  </b-card>
</template>

<script>
/* eslint-disable */
export default {
  name: "ComponentScrollableList",
  data() {
    return {

      show2: false,
      show3: false,
      show4: false,
      show5: false,

      component1: {
        name: '',
        serial_n: '',
        category: '',
        type: '',
        view: '',
        year: '',
        location: {
          object: '',
          corpus: '',
          cabinet: '',
          unit: ''
        }
      },
      component2: {
        name: '',
        serial_n: '',
        category: '',
        type: '',
        view: '',
        year: '',
        location: {
          object: '',
          corpus: '',
          cabinet: '',
          unit: ''
        }
      },
      component3: {
        name: '',
        serial_n: '',
        category: '',
        type: '',
        view: '',
        year: '',
        location: {
          object: '',
          corpus: '',
          cabinet: '',
          unit: ''
        }
      },
      component4: {
        name: '',
        serial_n: '',
        category: '',
        type: '',
        view: '',
        year: '',
        location: {
          object: '',
          corpus: '',
          cabinet: '',
          unit: ''
        }
      },
      component5: {
        name: '',
        serial_n: '',
        category: '',
        type: '',
        view: '',
        year: '',
        location: {
          object: '',
          corpus: '',
          cabinet: '',
          unit: ''
        }
      },
    }
  },
  methods: {
    scrollIntoView(evt) {
      evt.preventDefault()
      const href = evt.target.getAttribute('href')
      const el = href ? document.querySelector(href) : null
      if (el) {
        this.$refs.content.scrollTop = el.offsetTop
      }
    },
    check(left, right) {
      return left !== right
    },
    initComponentForm() {
      let emptyComponent = {
        name: '',
        serial_n: '',
        category: '',
        type: '',
        view: '',
        year: '',
        location: {
          object: '',
          corpus: '',
          cabinet: '',
          unit: ''
        }
      }
      this.component1 = emptyComponent
      this.component2 = emptyComponent
      this.component3 = emptyComponent
      this.component4 = emptyComponent
      this.component5 = emptyComponent
    },
    addComponent(component) {
      let show = true
      for (let key in component) {
        if (component[key] === '' || component[key] === {
          object: '',
          corpus: '',
          cabinet: '',
          unit: ''
        }) {
          show = false
          break
        }
        return show
      }
    },
    createComponentList() {
      let components = []
      let check = true
      for (let key in this.component1) {
        if (this.component1[key] === '' || this.component1[key] === {
          object: '',
          corpus: '',
          cabinet: '',
          unit: ''
        }) {
          check = false
        }
      }
      if(check){
        components.push(this.component1)
      }
      for (let key in this.component2) {
        if (this.component2[key] === '' || this.component2[key] === {
          object: '',
          corpus: '',
          cabinet: '',
          unit: ''
        }) {
          check = false
        }
      }
      if(check){
        components.push(this.component2)
      }
      for (let key in this.component3) {
        if (this.component3[key] === '' || this.component3[key] === {
          object: '',
          corpus: '',
          cabinet: '',
          unit: ''
        }) {
          check = false
        }
      }
      if(check){
        components.push(this.component3)
      }
      for (let key in this.component4) {
        if (this.component4[key] === '' || this.component4[key] === {
          object: '',
          corpus: '',
          cabinet: '',
          unit: ''
        }) {
          check = false
        }
      }
      if(check){
        components.push(this.component4)
      }
      for (let key in this.component5) {
        if (this.component5[key] === '' || this.component5[key] === {
          object: '',
          corpus: '',
          cabinet: '',
          unit: ''
        }) {
          check = false
        }
      }
      if(check){
        components.push(this.component5)
      }
      return components
    }
  },
}
</script>

<style scoped>

</style>
