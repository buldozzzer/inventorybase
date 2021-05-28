<template>
<!--    eslint-disable-->
  <div>
    <div id="firstRow">
      <b-row class="text-center">
        <b-col cols="2" align-self="center">
          <b-button variant="danger"
                    class="mt-3"
                    v-if="selected.length !== 0" v-b-modal.confirm-modal>
            <b-icon icon="trash"
                    data-toggle="tooltip"
                    data-placement="top"
                    font-scale="1"
                    aria-hidden="false"></b-icon>
            Удалить
          </b-button>
        </b-col>
        <b-col cols="3" align-self="center">
          <b-button-group>
            <b-button variant="success"
                      class="mt-3"
                      v-b-modal.add-item-modal>
              <b-icon icon="download"
                      data-toggle="tooltip"
                      data-placement="top"
                      font-scale="1"
                      aria-hidden="false"></b-icon>
              Добавить
            </b-button>
            <b-dropdown right
                        variant="success"
                        class="mt-3">
              <b-dropdown-item href="#/items/recognize">
                <b-icon icon="card-image"
                        data-toggle="tooltip"
                        data-placement="top"
                        font-scale="1"
                        aria-hidden="false"></b-icon>
                Распознать текст
              </b-dropdown-item>
            </b-dropdown>
          </b-button-group>
        </b-col>
        <b-col cols="2" align-self="center">
          <b-button variant="light"
                    @click="showFilters = !showFilters"
                    class="mt-3">
            <b-icon :icon="filterIcon"
                    data-toggle="tooltip"
                    data-placement="top"
                    font-scale="1"
                    aria-hidden="false"></b-icon>
            Фильтры
          </b-button>
        </b-col>
        <b-col cols="2" align-self="center">
          <b-button class="mt-3"
                    variant="primary"
                    href="#/items/groupedit"
                    v-if="selected.length !== 0"
                    @click="sendToEditItems">
            <b-icon icon="pencil-square"
                    data-toggle="tooltip"
                    data-placement="top"
                    font-scale="1"
                    aria-hidden="false"></b-icon>
            Изменить
          </b-button>
        </b-col>
        <b-col cols="2" align-self="center">
          <b-button-group>
            <b-button variant="light"
                      :title="exportToExcelTitle"
                      v-b-modal.excel-exporter-modal
                      :disabled="selected.length === 0"
                      class="mt-3">
              Экспорт
            </b-button>
            <b-dropdown right
                        variant="light"
                        :title="exportToTemplateTitle"
                        class="mt-3">
              <b-dropdown-item v-b-modal.document-template-modal>
                <b-icon icon="file-earmark-code"
                        data-toggle="tooltip"
                        data-placement="top"
                        font-scale="1"
                        aria-hidden="false"></b-icon>
                Шаблоны
              </b-dropdown-item>
            </b-dropdown>
          </b-button-group>
        </b-col>
        <b-col cols="1">
          <div class="mt-3">
            {{ 'Всего: ' + items.length }}
            <br>
            {{ 'Показано: ' + filteredItems }}
            <br>
            {{ 'Выбрано: ' + selected.length }}
          </div>
        </b-col>
      </b-row>
    </div>
    <filters class="mt-3"
             v-show="showFilters === true"
             ref="filtersForList"
             :filters="filters"
             :employee-initials="employeeInitials">
    </filters>
    <div style="position: absolute; z-index: 999; width: 30%; bottom: 0; right: 0">
      <b-alert
        :show="dismissCountDown"
        dismissible
        @dismissed="dismissCountDown=0"
        @dismiss-count-down="countDownChanged">
        <p style="text-align: center;">
          <b-icon icon="check2"
                  variant="success"
                  font-scale="2"
                  data-toggle="tooltip"
                  data-placement="top">
          </b-icon>
          Успешно
        </p>
      </b-alert>
      <b-alert
        :show="dismissCountDownError"
        dismissible
        @dismissed="dismissCountDownError=0"
        @dismiss-count-down="countDownChangedError">
        <p style="text-align: center;">
          <b-icon icon="x"
                  variant="danger"
                  font-scale="2"
                  data-toggle="tooltip"
                  data-placement="top">
          </b-icon>
          Ошибка
        </p>
      </b-alert>
    </div>
    <!--    sticky-header="850px"-->
    <!--    v-bind:sticky-header="sliderValue+'px'"-->
    <b-table striped hover
             bordered
             small
             id="table"
             selected-variant="success"
             class="mt-3"
             ref="selectableTable"
             selectable
             :sort-by.sync="sortBy"
             :sticky-header="sliderValue"
             :items="items"
             :fields="fields"
             :filter-function="filterFunction"
             :filter="filters"
             @row-selected="onRowSelected">
      <template #table-colgroup="scope">
        <col
          v-for="field in scope.fields"
          :key="field.key"
          :id="'cell-' + field.key"
        >
      </template>
      <template #head()="scope">
        <div class="text-nowrap text-center" :title="scope.label">
          {{ scope.label }}
          <b-icon icon="x"
                  class="mt-1"
                  variant="dark"
                  data-toggle="tooltip"
                  data-placement="top"
                  title="Скрыть колонку"
                  font-scale="1.5"
                  @click="hideColumn(scope.label)">
          </b-icon>
        </div>
      </template>
      <template #head(unit_from)="scope">
        <div class="text-nowrap" title="Подразделение, откуда поступила мат. ценность">
          {{ scope.label }}
          <b-icon icon="x"
                  class="mt-1"
                  variant="dark"
                  data-toggle="tooltip"
                  data-placement="top"
                  title="Скрыть колонку"
                  font-scale="1.5"
                  @click="hideColumn(scope.label)">
          </b-icon>
        </div>
      </template>

      <template #head(transfer_requisites)="scope">
        <div class="text-nowrap" title="Реквизиты о передаче во временное пользование">
          {{ scope.label }}
          <b-icon icon="x"
                  class="mt-1"
                  variant="dark"
                  data-toggle="tooltip"
                  data-placement="top"
                  title="Скрыть колонку"
                  font-scale="1.5"
                  @click="hideColumn(scope.label)">
          </b-icon>
        </div>
      </template>

      <template #head(selected)="scope">
        <button :title="allRows"
                @click="selectAll"
                class="button-select-rows">
          ☑
        </button>
<!--        <b-icon icon="check-square"-->
<!--                :title="allRows"-->
<!--                type="btn"-->
<!--                data-toggle="tooltip"-->
<!--                @click="selectAll"-->
<!--                v-if="selected.length === 0"-->
<!--                data-placement="top"-->
<!--                font-scale="1"-->
<!--                aria-hidden="false"></b-icon>-->
<!--        <b-icon icon="check-square-fill"-->
<!--                v-else-->
<!--                data-toggle="tooltip"-->
<!--                type="btn"-->
<!--                @click="selectAll"-->
<!--                data-placement="top"-->
<!--                font-scale="1"-->
<!--                aria-hidden="false"></b-icon>-->
          <b-dropdown text="Поля"
                      variant="warning"
                      role="menu">
            <b-dropdown-text class="text-nowrap">
              <b-form-checkbox @change="showFullTable"
                               switch
                               style="text-align: left">
                {{ full ? 'Неполная таблица' : 'Полная таблица' }}
              </b-form-checkbox>
            </b-dropdown-text>
            <div class="dropdown-divider"></div>
            <div style="overflow-y: scroll; height: 500px">
              <b-dropdown-text class="text-nowrap">
                <b-form-checkbox v-for="title in titles"
                                 style="text-align: left"
                                 v-model="title['show']"
                                 @click="title['show'] = !title['show']"
                                 :key="title['key']">
                  {{ title['key'] }}
                </b-form-checkbox>
              </b-dropdown-text>
            </div>
          </b-dropdown>
      </template>
      <template #head(index)="scope">
        <div>Номер</div>
      </template>
      <template #cell(index)="data">
        <div class="text-center">
          {{ data.index + 1 }}
        </div>
      </template>
      <template #cell(name)="row">
        <div @dblclick="showFieldFromModal('name'), editableRow=row.item"
             class="text-center">
          {{ row.item.name ? row.item.name : '&nbsp' }}
        </div>
        <b-modal ref="name" centered
                 title="Измените значение поля"
                 size="xl"
                 hide-footer
                 hide-header-close>
          <b-form class="w-100">
            <div class="container mt-3">
              <b-form-textarea id="form-input"
                            type="text"
                            class="mt-3"
                            v-model="editableRow.name"
                            :value="editableRow.name">
              </b-form-textarea>
              <div class="mt-3">
                <b-button variant="success" @click="onSubmit('name', editableRow)">Изменить</b-button>
                <b-button variant="danger" @click="onReset('name')">Отмена</b-button>
              </div>
            </div>
          </b-form>
        </b-modal>
      </template>

      <template #cell(responsible)="row">
        <div @dblclick="showFieldFromModal('responsible'), editableRow=row.item"
             class="text-center">
          {{ row.item.responsible ? row.item.responsible : '&nbsp' }}
        </div>
        <b-modal ref="responsible"
                 centered
                 title="Измените значение поля"
                 hide-footer
                 hide-header-close>
          <b-form class="w-100">
            <div class="container mt-3">
              <b-form-group label-for="form-input">
                <b-form-input id="form-input"
                              type="text"
                              class="mt-3"
                              list="employee-list"
                              v-model="editableRow.responsible"
                              :value="editableRow.responsible">
                </b-form-input>
                <datalist id="employee-list">
                  <option v-for="employee in employeeInitials">{{ employee }}</option>
                </datalist>
              </b-form-group>
              <div class="mt-3">
                <b-button variant="success" @click="onSubmit('responsible', editableRow)">
                  Изменить
                </b-button>
                <b-button variant="danger" @click="onReset('responsible')">Отмена</b-button>
              </div>
            </div>
          </b-form>
        </b-modal>
      </template>

      <template #cell(user)="row">
        <div @dblclick="showFieldFromModal('user'), editableRow=row.item"
             class="text-center">
          {{ row.item.user ? row.item.user : '&nbsp' }}
        </div>
        <b-modal ref="user"
                 centered
                 title="Измените значение поля"
                 hide-footer
                 hide-header-close>
          <b-form class="w-100">
            <div class="container mt-3">
              <b-form-group label-for="form-input">
                <b-form-input id="form-input"
                              type="text"
                              class="mt-3"
                              list="user-list"
                              v-model="editableRow.user"
                              :value="editableRow.user">
                </b-form-input>
                <datalist id="user-list">
                  <option v-for="employee in employeeInitials">{{ employee }}</option>
                </datalist>
              </b-form-group>
              <div class="mt-3">
                <b-button variant="success" @click="onSubmit('user', editableRow)">
                  Изменить
                </b-button>
                <b-button variant="danger" @click="onReset('user')">Отмена</b-button>
              </div>
            </div>
          </b-form>
        </b-modal>
      </template>

      <template #cell(inventory_n)="row">
        <div @dblclick="showFieldFromModal('inventory_n'), editableRow=row.item"
             class="text-center">
          {{ row.item.inventory_n ? row.item.inventory_n : '&nbsp' }}
        </div>
        <b-modal ref="inventory_n"
                 centered
                 title="Измените значение поля"
                 hide-footer
                 hide-header-close>
          <b-form class="w-100">
            <div class="container mt-3">
              <b-form-group label-for="form-input">
                <b-form-input id="form-input"
                              type="text"
                              class="mt-3"
                              v-model="editableRow.inventory_n"
                              :value="editableRow.inventory_n">
                </b-form-input>
              </b-form-group>
              <div class="mt-3">
                <b-button variant="success" @click="onSubmit('inventory_n', editableRow)">
                  Изменить
                </b-button>
                <b-button variant="danger" @click="onReset('inventory_n')">Отмена</b-button>
              </div>
            </div>
          </b-form>
        </b-modal>
      </template>

      <template #cell(in_operation)="row">
        <div @dblclick="showFieldFromModal('in_operation'), editableRow=row.item"
             class="text-center">
          {{ row.item.in_operation ? row.item.in_operation : '&nbsp' }}
        </div>
        <b-modal ref="in_operation"
                 centered
                 title="Измените значение поля"
                 hide-footer
                 hide-header-close>
          <b-form class="w-100">
            <div class="container mt-3">
              <b-form-group label-for="form-select">
                <b-form-select id="form-select"
                               type="text"
                               class="mt-3"
                               :options="operation"
                               v-model="editableRow.in_operation"
                               :value="editableRow.in_operation">
                </b-form-select>
              </b-form-group>
              <div class="mt-3">
                <b-button variant="success" @click="onSubmit('in_operation', editableRow)">
                  Изменить
                </b-button>
                <b-button variant="danger" @click="onReset('in_operation')">Отмена</b-button>
              </div>
            </div>
          </b-form>
        </b-modal>
      </template>

      <template #cell(in_operation)="row">
        <div @dblclick="showFieldFromModal('in_operation'), editableRow=row.item"
             class="text-center">
          {{ row.item.in_operation ? row.item.in_operation : '&nbsp' }}
        </div>
        <b-modal ref="in_operation"
                 centered
                 title="Измените значение поля"
                 hide-footer
                 hide-header-close>
          <b-form class="w-100">
            <div class="container mt-3">
              <b-form-group label-for="form-select">
                <b-form-select id="form-select"
                               type="text"
                               class="mt-3"
                               :options="operation"
                               v-model="editableRow.in_operation"
                               :value="editableRow.in_operation">
                </b-form-select>
              </b-form-group>
              <div class="mt-3">
                <b-button variant="success" @click="onSubmit('in_operation', editableRow)">
                  Изменить
                </b-button>
                <b-button variant="danger" @click="onReset('in_operation')">Отмена</b-button>
              </div>
            </div>
          </b-form>
        </b-modal>
      </template>

      <template #cell(condition)="row">
        <div @dblclick="showFieldFromModal('condition'), editableRow=row.item"
             class="text-center">
          {{ row.item.condition ? row.item.condition : '&nbsp' }}
        </div>
        <b-modal ref="condition"
                 centered
                 title="Измените значение поля"
                 hide-footer
                 hide-header-close>
          <b-form class="w-100">
            <div class="container mt-3">
              <b-form-group label-for="form-select">
                <b-form-select id="form-select"
                               type="text"
                               class="mt-3"
                               :options="conditions"
                               v-model="editableRow.condition"
                               :value="editableRow.condition">
                </b-form-select>
              </b-form-group>
              <div class="mt-3">
                <b-button variant="success" @click="onSubmit('condition', editableRow)">
                  Изменить
                </b-button>
                <b-button variant="danger" @click="onReset('condition')">Отмена</b-button>
              </div>
            </div>
          </b-form>
        </b-modal>
      </template>

      <template #cell(unit_from)="row">
        <div @dblclick="showFieldFromModal('unit_from'), editableRow=row.item"
             class="text-center">
          {{ row.item.unit_from ? row.item.unit_from : '&nbsp' }}
        </div>
        <b-modal ref="unit_from" centered
                 title="Измените значение поля"
                 hide-footer
                 hide-header-close>
          <b-form class="w-100">
            <div class="container mt-3">
              <b-form-input id="form-input"
                            type="text"
                            class="mt-3"
                            list="unit_from-list"
                            v-model="editableRow.unit_from"
                            :value="editableRow.unit_from">
              </b-form-input>
              <datalist id="unit_from-list">
                <option v-for="unit in units">{{ unit }}</option>
              </datalist>
              <div class="mt-3">
                <b-button variant="success" @click="onSubmit('unit_from', editableRow)">Изменить</b-button>
                <b-button variant="danger" @click="onReset('unit_from')">Отмена</b-button>
              </div>
            </div>
          </b-form>
        </b-modal>
      </template>

      <template #cell(fault_document_requisites)="row">
        <div @dblclick="showFieldFromModal('fault_document_requisites'), editableRow=row.item"
             class="text-center">
          {{ row.item.fault_document_requisites ? row.item.fault_document_requisites : '&nbsp' }}
        </div>
        <b-modal ref="fault_document_requisites"
                 centered
                 title="Измените значение поля"
                 hide-footer
                 hide-header-close>
          <b-form class="w-100">
            <div class="container mt-3">
              <b-form-input id="form-input"
                            type="text"
                            class="mt-3"
                            v-model="editableRow.fault_document_requisites"
                            :value="editableRow.fault_document_requisites">
              </b-form-input>
              <div class="mt-3">
                <b-button variant="success"
                          @click="onSubmit('fault_document_requisites', editableRow)">
                  Изменить
                </b-button>
                <b-button variant="danger"
                          @click="onReset('fault_document_requisites')">
                  Отмена
                </b-button>
              </div>
            </div>
          </b-form>
        </b-modal>
      </template>

      <template #cell(number_of_receipt)="row">
        <div @dblclick="showFieldFromModal('number_of_receipt'), editableRow=row.item">
          {{ row.item.number_of_receipt ? row.item.number_of_receipt : '&nbsp' }}
        </div>
        <b-modal ref="number_of_receipt"
                 centered
                 title="Измените значение поля"
                 hide-footer
                 hide-header-close>
          <b-form class="w-100">
            <div class="container mt-3">
              <b-form-input id="form-input"
                            type="text"
                            class="mt-3"
                            v-model="editableRow.number_of_receipt"
                            :value="editableRow.number_of_receipt">
              </b-form-input>
              <div class="mt-3">
                <b-button variant="success"
                          @click="onSubmit('number_of_receipt', editableRow)">
                  Изменить
                </b-button>
                <b-button variant="danger"
                          @click="onReset('number_of_receipt')">
                  Отмена
                </b-button>
              </div>
            </div>
          </b-form>
        </b-modal>
      </template>

      <template #cell(requisites)="row">
        <div @dblclick="showFieldFromModal('requisites'), editableRow=row.item">
          <p>{{ row.item.requisites ? row.item.requisites : '&nbsp' }}</p>
        </div>
        <b-modal ref="requisites"
                 centered
                 title="Измените значение поля"
                 hide-footer
                 hide-header-close>
          <b-form class="w-100">
            <div class="container mt-3">
              <b-form-textarea id="form-input"
                               type="text"
                               class="mt-3"
                               v-model="editableRow.requisites"
                               :value="editableRow.requisites">
              </b-form-textarea>
              <div class="mt-3">
                <b-button variant="success"
                          @click="onSubmit('requisites', editableRow)">
                  Изменить
                </b-button>
                <b-button variant="danger"
                          @click="onReset('requisites')">
                  Отмена
                </b-button>
              </div>
            </div>
          </b-form>
        </b-modal>
      </template>

<!--      <template #cell(components)="row">-->
<!--        <b-icon v-if="row.detailsShowing"-->
<!--                icon="eye-slash"-->
<!--                font-scale="2"-->
<!--                @click="row.toggleDetails">-->
<!--        </b-icon>-->
<!--        <b-icon v-else-->
<!--                icon="eye"-->
<!--                font-scale="2"-->
<!--                @click="row.toggleDetails">-->
<!--        </b-icon>-->
<!--      </template>-->

      <template #row-details="row">
        <b-table :items="row.item.components" :fields="componentFields">
          <template #cell(index)="data">
            {{ data.index + 1 }}
          </template>

          <template #cell(location)="data">
            Объект: {{ data.item.location.object }}<br>
            Корпус: {{ data.item.location.corpus }}<br>
            Кабинет: {{ data.item.location.cabinet }}<br>
            Подразделение: {{ data.item.location.unit }}
          </template>
        </b-table>
      </template>

      <template #cell(selected)="row">
        <b-container>
          <b-row class="text-center">
            <b-col cols="3">
              <b-icon icon="check2"
                      v-show="row.rowSelected"
                      data-toggle="tooltip"
                      data-placement="top"
                      title="Выбрано"
                      font-scale="1.2">
              </b-icon>
            </b-col>
            <b-col v-if="row.item.components.length !== 0" cols="2">
              <b-icon v-if="row.detailsShowing"
                      icon="eye-slash"
                      font-scale="1"
                      @click="row.toggleDetails">
              </b-icon>
              <b-icon v-else
                      icon="eye"
                      font-scale="1"
                      @click="row.toggleDetails">
              </b-icon>
            </b-col>
            <b-col>

              <b-icon icon="pencil-square"
                      variant="primary"
                      data-toggle="tooltip"
                      data-placement="top"
                      title="Изменить"
                      font-scale="1"
                      v-b-modal.edit-item-modal
                      @click="selectToEditItem(row.item)">
              </b-icon>
              <b-icon icon="trash"
                      variant="danger"
                      font-scale="1"
                      data-toggle="tooltip"
                      data-placement="top"
                      title="Удалить"
                      v-b-modal.confirm-modal
                      @click="selectToRemoveItem(row.item)">
              </b-icon>
            </b-col>
          </b-row>
        </b-container>
      </template>

      <template #cell(otss_requisites)="row">
        <div @dblclick="showFieldFromModal('otss_requisites'), editableRow=row.item">
          {{ row.item.otss_requisites ? row.item.otss_requisites : '&nbsp' }}
        </div>
        <b-modal ref="otss_requisites"
                 centered
                 title="Измените значение поля"
                 hide-footer
                 hide-header-close>
          <b-form class="w-100">
            <div class="container mt-3">
              <b-form-textarea id="form-input"
                               type="text"
                               class="mt-3"
                               v-model="editableRow.otss_requisites"
                               :value="editableRow.otss_requisites">
              </b-form-textarea>
              <div class="mt-3">
                <b-button variant="success"
                          @click="onSubmit('otss_requisites', editableRow)">
                  Изменить
                </b-button>
                <b-button variant="danger"
                          @click="onReset('otss_requisites')">
                  Отмена
                </b-button>
              </div>
            </div>
          </b-form>
        </b-modal>
      </template>

      <template #cell(spsi_requisites)="row">
        <div @dblclick="showFieldFromModal('spsi_requisites'), editableRow=row.item">
          {{ row.item.spsi_requisites ? row.item.spsi_requisites : '&nbsp' }}
        </div>
        <b-modal ref="spsi_requisites"
                 centered
                 title="Измените значение поля"
                 hide-footer
                 hide-header-close>
          <b-form class="w-100">
            <div class="container mt-3">
              <b-form-textarea id="form-input"
                               type="text"
                               class="mt-3"
                               v-model="editableRow.spsi_requisites"
                               :value="editableRow.spsi_requisites">
              </b-form-textarea>
              <div class="mt-3">
                <b-button variant="success"
                          @click="onSubmit('spsi_requisites', editableRow)">
                  Изменить
                </b-button>
                <b-button variant="danger"
                          @click="onReset('spsi_requisites')">
                  Отмена
                </b-button>
              </div>
            </div>
          </b-form>
        </b-modal>
      </template>

      <template #cell(spsi_requisites)="row">
        <div @dblclick="showFieldFromModal('spsi_requisites'), editableRow=row.item">
          {{ row.item.spsi_requisites ? row.item.spsi_requisites : '&nbsp' }}
        </div>
        <b-modal ref="spsi_requisites"
                 centered
                 title="Измените значение поля"
                 hide-footer
                 hide-header-close>
          <b-form class="w-100">
            <div class="container mt-3">
              <b-form-textarea id="form-input"
                               type=""
                               class="mt-3"
                               v-model="editableRow.spsi_requisites"
                               :value="editableRow.spsi_requisites">
              </b-form-textarea>
              <div class="mt-3">
                <b-button variant="success"
                          @click="onSubmit('spsi_requisites', editableRow)">
                  Изменить
                </b-button>
                <b-button variant="danger"
                          @click="onReset('spsi_requisites')">
                  Отмена
                </b-button>
              </div>
            </div>
          </b-form>
        </b-modal>
      </template>

      <template #cell(transfer_requisites)="row">
        <div @dblclick="showFieldFromModal('transfer_requisites'), editableRow=row.item">
          {{ row.item.transfer_requisites ? row.item.transfer_requisites : '&nbsp' }}
        </div>
        <b-modal ref="transfer_requisites"
                 centered
                 title="Измените значение поля"
                 hide-footer
                 hide-header-close>
          <b-form class="w-100">
            <div class="container mt-3">
              <b-form-textarea id="form-input"
                               type="text"
                               class="mt-3"
                               v-model="editableRow.transfer_requisites"
                               :value="editableRow.transfer_requisites">
              </b-form-textarea>
              <div class="mt-3">
                <b-button variant="success"
                          @click="onSubmit('transfer_requisites', editableRow)">
                  Изменить
                </b-button>
                <b-button variant="danger"
                          @click="onReset('transfer_requisites')">
                  Отмена
                </b-button>
              </div>
            </div>
          </b-form>
        </b-modal>
      </template>

      <template #cell(comment)="row">
        <div @dblclick="showFieldFromModal('comment'), editableRow=row.item">
          {{ row.item['comment'] ? row.item['comment'] : '&nbsp' }}
        </div>
        <b-modal ref="comment"
                 centered
                 title="Измените значение поля"
                 hide-footer
                 hide-header-close>
          <b-form class="w-100">
            <div class="container mt-3">
              <b-form-textarea id="form-input"
                               type="text"
                               class="mt-3"
                               v-model="editableRow['comment']"
                               :value="editableRow['comment']">
              </b-form-textarea>
              <div class="mt-3">
                <b-button variant="success"
                          @click="onSubmit('comment', editableRow)">
                  Изменить
                </b-button>
                <b-button variant="danger"
                          @click="onReset('comment')">
                  Отмена
                </b-button>
              </div>
            </div>
          </b-form>
        </b-modal>
      </template>

      <template #cell(date_of_receipt)="row">
        <div @dblclick="showFieldFromModal('date_of_receipt'), editableRow=row.item">
          {{ row.item.date_of_receipt ? row.item.date_of_receipt : '&nbsp' }}
        </div>
        <b-modal ref="date_of_receipt"
                 centered
                 title="Измените значение поля"
                 hide-footer
                 hide-header-close>
          <b-form class="w-100">
            <div class="container mt-3">
              <b-form-datepicker
                v-model="editableRow.date_of_receipt"
                aria-controls="date_of_receipt-input"
                today-button
                reset-button
                close-button
                placeholder="Выберите дату"
                :date-format-options="{ day: '2-digit', month: 'short', year: 'numeric'}"
              ></b-form-datepicker>
              <div class="mt-3">
                <b-button variant="success"
                          @click="onSubmit('date_of_receipt', editableRow)">
                  Изменить
                </b-button>
                <b-button variant="danger"
                          @click="onReset('date_of_receipt')">
                  Отмена
                </b-button>
              </div>
            </div>
          </b-form>
        </b-modal>
      </template>

      <template #cell(transfer_date)="row">
        <div @dblclick="showFieldFromModal('transfer_date'), editableRow=row.item">
          {{ row.item.transfer_date ? row.item.transfer_date : '&nbsp' }}
        </div>
        <b-modal ref="transfer_date"
                 centered
                 title="Измените значение поля"
                 hide-footer
                 hide-header-close>
          <b-form class="w-100">
            <div class="container mt-3">
              <b-form-datepicker
                v-model="editableRow.transfer_date"
                aria-controls="transfer_date-input"
                today-button
                reset-button
                close-button
                placeholder="Выберите дату"
                :date-format-options="{ day: '2-digit', month: 'short', year: 'numeric'}"
              ></b-form-datepicker>
              <div class="mt-3">
                <b-button variant="success"
                          @click="onSubmit('transfer_date', editableRow)">
                  Изменить
                </b-button>
                <b-button variant="danger"
                          @click="onReset('transfer_date')">
                  Отмена
                </b-button>
              </div>
            </div>
          </b-form>
        </b-modal>
      </template>

      <template #cell(last_check)="row">
        <div @dblclick="editableRow=row.item, getCurrentDate(editableRow)">
          {{ row.item.last_check ? row.item.last_check : '&nbsp' }}
        </div>
      </template>

      <template #cell(serial_n)="row">
        <div @dblclick="showFieldFromModal('serial_n'), editableRow=row.item"
             class="text-center">
          {{ row.item.serial_n ? row.item.serial_n : '&nbsp' }}
        </div>
        <b-modal ref="serial_n"
                 centered
                 title="Измените значение поля"
                 hide-footer
                 hide-header-close>
          <b-form class="w-100">
            <div class="container mt-3">
              <b-form-group label-for="form-input">
                <b-form-input id="form-input"
                              type="text"
                              class="mt-3"
                              v-model="editableRow.serial_n"
                              :value="editableRow.serial_n">
                </b-form-input>
              </b-form-group>
              <div class="mt-3">
                <b-button variant="success" @click="onSubmit('serial_n', editableRow)">
                  Изменить
                </b-button>
                <b-button variant="danger" @click="onReset('serial_n')">Отмена</b-button>
              </div>
            </div>
          </b-form>
        </b-modal>
      </template>

      <template #cell(category)="row">
        <div @dblclick="showFieldFromModal('category'), editableRow=row.item"
             class="text-center">
          {{ row.item.category ? row.item.category : '&nbsp' }}
        </div>
        <b-modal ref="category"
                 centered
                 title="Измените значение поля"
                 hide-footer
                 hide-header-close>
          <b-form class="w-100">
            <div class="container mt-3">
              <b-form-group label-for="form-input">
                <b-form-select id="form-input"
                              type="text"
                              class="mt-3"
                              :options="categories"
                              v-model="editableRow.category"
                              :value="editableRow.category">
                </b-form-select>
              </b-form-group>
              <div class="mt-3">
                <b-button variant="success" @click="onSubmit('category', editableRow)">
                  Изменить
                </b-button>
                <b-button variant="danger" @click="onReset('category')">Отмена</b-button>
              </div>
            </div>
          </b-form>
        </b-modal>
      </template>

      <template #cell(year)="row">
        <div @dblclick="showFieldFromModal('year'), editableRow=row.item"
             class="text-center">
          {{ row.item.year ? row.item.year : '&nbsp' }}
        </div>
        <b-modal ref="year"
                 centered
                 title="Измените значение поля"
                 hide-footer
                 hide-header-close>
          <b-form class="w-100">
            <div class="container mt-3">
              <b-form-group label-for="form-input">
                <b-form-input id="form-input"
                              type="number"
                              min="0"
                              class="mt-3"
                              v-model="editableRow.year"
                              :value="editableRow.year">
                </b-form-input>
              </b-form-group>
              <div class="mt-3">
                <b-button variant="success" @click="onSubmit('year', editableRow)">
                  Изменить
                </b-button>
                <b-button variant="danger" @click="onReset('year')">Отмена</b-button>
              </div>
            </div>
          </b-form>
        </b-modal>
      </template>

      <template #cell(cost)="row">
        <div @dblclick="showFieldFromModal('cost'), editableRow=row.item"
             class="text-center">
          {{ row.item.cost ? row.item.cost : '&nbsp' }}
        </div>
        <b-modal ref="cost"
                 centered
                 title="Измените значение поля"
                 hide-footer
                 hide-header-close>
          <b-form class="w-100">
            <div class="container mt-3">
              <b-form-group label-for="form-input">
                <b-form-input id="form-input"
                              type="number"
                              min="0"
                              class="mt-3"
                              v-model="editableRow.cost"
                              :value="editableRow.cost">
                </b-form-input>
              </b-form-group>
              <div class="mt-3">
                <b-button variant="success" @click="onSubmit('cost', editableRow)">
                  Изменить
                </b-button>
                <b-button variant="danger" @click="onReset('cost')">Отмена</b-button>
              </div>
            </div>
          </b-form>
        </b-modal>
      </template>

      <template #cell(location_object)="row">
        <div @dblclick="showFieldFromModal('location_object'), editableRow=row.item"
             class="text-center">
          {{ row.item.location_object ? row.item.location_object : '&nbsp' }}
        </div>
        <b-modal ref="location_object"
                 centered
                 title="Измените значение поля"
                 hide-footer
                 hide-header-close>
          <b-form class="w-100">
            <div class="container mt-3">
              <b-form-group label-for="form-input">
                <b-form-select id="form-input"
                              type="text"
                              class="mt-3"
                              :options="location_objects"
                              v-model="editableRow.location_object"
                              :value="editableRow.location_object">
                </b-form-select>
              </b-form-group>
              <div class="mt-3">
                <b-button variant="success" @click="onSubmit('location_object', editableRow)">
                  Изменить
                </b-button>
                <b-button variant="danger" @click="onReset('location_object')">Отмена</b-button>
              </div>
            </div>
          </b-form>
        </b-modal>
      </template>

      <template #cell(location_unit)="row">
        <div @dblclick="showFieldFromModal('location_unit'), editableRow=row.item"
             class="text-center">
          {{ row.item.location_unit ? row.item.location_unit : '&nbsp' }}
        </div>
        <b-modal ref="location_unit"
                 centered
                 title="Измените значение поля"
                 hide-footer
                 hide-header-close>
          <b-form class="w-100">
            <div class="container mt-3">
              <b-form-group label-for="form-input">
                <b-form-select id="form-input"
                              type="text"
                              class="mt-3"
                              :options="location_units"
                              v-model="editableRow.location_unit"
                              :value="editableRow.location_unit">
                </b-form-select>
              </b-form-group>
              <div class="mt-3">
                <b-button variant="success" @click="onSubmit('location_unit', editableRow)">
                  Изменить
                </b-button>
                <b-button variant="danger" @click="onReset('location_unit')">Отмена</b-button>
              </div>
            </div>
          </b-form>
        </b-modal>
      </template>

      <template #cell(location_corpus)="row">
        <div @dblclick="showFieldFromModal('location_corpus'), editableRow=row.item"
             class="text-center">
          {{ row.item.location_corpus ? row.item.location_corpus : '&nbsp' }}
        </div>
        <b-modal ref="location_corpus"
                 centered
                 title="Измените значение поля"
                 hide-footer
                 hide-header-close>
          <b-form class="w-100">
            <div class="container mt-3">
              <b-form-group label-for="form-input">
                <b-form-select id="form-input"
                              type="text"
                              class="mt-3"
                              :options="location_corpuses"
                              v-model="editableRow.location_corpus"
                              :value="editableRow.location_corpus">
                </b-form-select>
              </b-form-group>
              <div class="mt-3">
                <b-button variant="success" @click="onSubmit('location_corpus', editableRow)">
                  Изменить
                </b-button>
                <b-button variant="danger" @click="onReset('location_corpus')">Отмена</b-button>
              </div>
            </div>
          </b-form>
        </b-modal>
      </template>

      <template #cell(location_cabinet)="row">
        <div @dblclick="showFieldFromModal('location_cabinet'), editableRow=row.item"
             class="text-center">
          {{ row.item.location_cabinet ? row.item.location_cabinet : '&nbsp' }}
        </div>
        <b-modal ref="location_cabinet"
                 centered
                 title="Измените значение поля"
                 hide-footer
                 hide-header-close>
          <b-form class="w-100">
            <div class="container mt-3">
              <b-form-group label-for="form-input">
                <b-form-select id="form-input"
                              type="text"
                              class="mt-3"
                              :options="location_cabinets"
                              v-model="editableRow.location_cabinet"
                              :value="editableRow.location_cabinet">
                </b-form-select>
              </b-form-group>
              <div class="mt-3">
                <b-button variant="success" @click="onSubmit('location_cabinet', editableRow)">
                  Изменить
                </b-button>
                <b-button variant="danger" @click="onReset('location_cabinet')">Отмена</b-button>
              </div>
            </div>
          </b-form>
        </b-modal>
      </template>

    </b-table>
    <add-modal ref="addItemModal"
               :employee-initials="employeeInitials"
               :categories="categories"
               :location_units="location_units"
               :location_objects="location_objects"
               :location_corpuses="location_corpuses"
               :location_cabinets="location_cabinets"/>

    <edit-modal ref="editItemModal"
                :employee-initials="employeeInitials"
                :edit-item="editItem"
                :categories="categories"
                :location_units="location_units"
                :location_objects="location_objects"
                :location_corpuses="location_corpuses"
                :location_cabinets="location_cabinets"/>
    <confirm-form :payload="selected"
                  :dynamic-id="dynamicId"
                  :message="message"
                  :op="removeItems">

    </confirm-form>
    <excel-exporter-modal ref="excelExporterModal"
                          :titles="titles"
                          :selected="selected"
                          :item-fields="itemFields"/>
    <document-template-modal :selected="selected"/>
  </div>
</template>


<script>
/* eslint-disable */
  import VueRangeSlider from "vue-range-slider";
  import 'vue-range-slider/dist/vue-range-slider.css'
  import {bus} from '../../main'
  import Filters from "./Filters";
  import AddModal from './add/AddModal';
  import EditModal from './edit/EditModal';
  import ConfirmForm from "./ConfirmForm";
  import FieldModalForm from "./FieldModalForm";
  import ExcelExporterModal from "./ExcelExporterModal";
  import DocumentTemplateModal from "./documents/DocumentTemplateModal";


  export default {
    name: "ItemList",
    components: {
      ExcelExporterModal,
      VueRangeSlider,
      AddModal,
      EditModal,
      Filters,
      ConfirmForm,
      FieldModalForm,
      DocumentTemplateModal
    },
    data() {
      return {
        recognizeModalShow: false,
        dismissCountDown: 0,
        dismissCountDownError: 0,
        otss: [1, 2, 3, 'Не секретно'],
        units: [],
        conditions: ['Исправно', 'Неисправно'],
        operation: ['Используется', 'Не используется'],
        m: '',
        editableRow: '',
        categories: [],
        dynamicId: "confirm-modal",
        noCollapse: false,
        full: false,
        filterIcon: 'funnel',
        sortBy: 'name',
        showFilters: false,
        componentFields: [
          'index',
          {
            key: 'name',
            label: "Наименование",
            class: 'text-center'
          },
          {
            key: "serial_n",
            label: "Серийный номер",
            class: 'text-center'
          },
          {
            key: "category",
            label: "Категория",
            class: 'text-center'
          },
          {
            key: "type",
            label: "Тип",
            class: 'text-center'
          }, {
            key: "view",
            label: "Вид",
            class: 'text-center'
          }, {
            key: "location",
            label: "Местонахождение",
            class: 'text-center'
          },{
            key: "year",
            label: "Год выпуска",
            class: 'text-center'
          },{
            key: "cost",
            label: "Цена",
            class: 'text-center'
          },{
            key: "in_operation",
            label: "Используется",
            class: 'text-center'
          },{
            key: "condition",
            label: "Состояние",
            class: 'text-center'
          },{
            key: "user",
            label: "Кому передано в пользование",
            class: 'text-center'
          },
        ],
        titles: [
          {
            key: "Наименование",
            show: true
          },
          // {
          //   key: "Компоненты",
          //   show: false
          // },
          {
            key: "Ответственный",
            show: true
          },
          {
            key: "Инвентарный номер",
            show: true
          },
          {
            key: "Категория ОТСС",
            show: false
          },
          {
            key: "Состояние",
            show: true
          }, {
            // key: "Подразделение, откуда поступила мат. ценность",
            key: "Откуда поступила",
            show: true
          }, {
            key: "Используется?",
            show: true
          }, {
            key: "Документы о неисправности",
            show: false
          }, {
            key: "Дата поступления на учет",
            show: true
          }, {
            key: "Номер требования о поступлении на учет",
            show: false
          }, {
            key: "Реквизиты книги учета мат. ценностей",
            show: false
          }, {
            key: "Дата передачи во временное пользование",
            show: false
          }, {
            key: "Реквизиты документа о категории ОТСС",
            show: false
          }, {
            key: "Реквизиты документа о прохождении СПСИ",
            show: false
          }, {
            key: "Реквизиты о передаче в пользование",
            show: true
          }, {
            key: "Дата последней проверки",
            show: true
          }, {
            key: "Примечания",
            show: true
          },
          {
            key: "Сотрудник, которому передали в пользование",
            show: false
          },
          {
            key: "Заводской номер",
            show: false
          },
          {
            key: "Категория",
            show: false
          },
          {
            key: "Год выпуска",
            show: false
          },
          {
            key: "Цена",
            show: false
          },
          {
            key: "Объект",
            show: false
          },
          {
            key: "Подразделение",
            show: false
          },
          {
            key: "Корпус",
            show: false
          },
          {
            key: "Кабинет",
            show: false
          }
        ],
        itemFields: [
          {
            key: "selected",
            stickyColumn: true,
            isRowHeader: true,
            class: 'text-center'
          },
          {
            key: "index",
            label: "Номер",
            class: 'text-center'
          },
          {
            key: "name",
            label: "Наименование",
            sortable: true,
            class: 'text-center'
          },
          // {
          //   key: "components",
          //   label: "Компоненты",
          //   class: 'text-center'
          // },
          {
            key: "responsible",
            label: "Ответственный",
            sortable: true,
            class: 'text-center'
          },
          {
            key: "inventory_n",
            label: "Инвентарный номер",
            sortable: true,
            class: 'text-center'
          },
          {
            key: "otss_category",
            label: "Категория ОТСС",
            sortable: true,
            class: 'text-center'
          },
          {
            key: "condition",
            label: "Состояние",
            sortable: true,
            class: 'text-center'
          }, {
            key: "unit_from",
            // label: "Подразделение, откуда поступила мат. ценность",
            label: "Откуда поступила",
            sortable: true,
            class: 'text-center'
          }, {
            key: "in_operation",
            label: "Используется?",
            sortable: true,
            class: 'text-center'
          }, {
            key: "fault_document_requisites",
            label: "Документы о неисправности",
            sortable: true,
            class: 'text-center'
          }, {
            key: "date_of_receipt",
            label: "Дата поступления на учет",
            sortable: true,
            class: 'text-center'
          }, {
            key: "number_of_receipt",
            label: "Номер требования о поступлении на учет",
            sortable: true,
            class: 'text-center'
          }, {
            key: "requisites",
            label: "Реквизиты книги учета мат. ценностей",
            sortable: true,
            class: 'text-center'
          }, {
            key: "transfer_date",
            label: "Дата передачи во временное пользование",
            sortable: true,
            class: 'text-center'
          }, {
            key: "otss_requisites",
            label: "Реквизиты документа о категории ОТСС",
            sortable: true,
            class: 'text-center'
          }, {
            key: "spsi_requisites",
            label: "Реквизиты документа о прохождении СПСИ",
            sortable: true,
            class: 'text-center'
          }, {
            key: "transfer_requisites",
            label: "Реквизиты о передаче в пользование",
            sortable: true,
            class: 'text-center'
          }, {
            key: "last_check",
            label: "Дата последней проверки",
            sortable: true,
            class: 'text-center'
          }, {
            key: "comment",
            label: "Примечания",
            sortable: true,
            class: 'text-center'
          },
          {
            key: "user",
            label: "Сотрудник, которому передали в пользование",
            sortable: true,
            class: 'text-center'
          },
          {
            key: "serial_n",
            label: "Заводской номер",
            sortable: true,
            class: 'text-center'
          },
          {
            key: "category",
            label: "Категория",
            sortable: true,
            class: 'text-center'
          },
          {
            key: "year",
            label: "Год выпуска",
            sortable: true,
            class: 'text-center'
          },
          {
            key: "cost",
            label: "Цена",
            sortable: true,
            class: 'text-center'
          },
          {
            key: "location_object",
            label: "Объект",
            sortable: true,
            class: 'text-center'
          },
          {
            key: "location_unit",
            label: "Подразделение",
            sortable: true,
            class: 'text-center'
          },
          {
            key: "location_corpus",
            label: "Корпус",
            sortable: true,
            class: 'text-center'
          },
          {
            key: "location_cabinet",
            label: "Кабинет",
            sortable: true,
            class: 'text-center'
          }
        ],
        items: [],
        selectedItem: {},
        selected: [],
        sliderValue: '',
        employeeList: [],
        employeeInitials: [],
        filters: {
          responsible: null,
          otss_category: null,
          condition: null,
          in_operation: null
        },
        shownItems: null,
        fuseString: '',
        location_units: [],
        location_objects: [],
        location_corpuses: [],
        location_cabinets: [],
      };
    },
    computed: {
      message: function () {
        if (this.selected) {
          if (this.selected.length === 1) {
            this.m = 'Вы уверены, что хотите удалить запись?'
          } else {
            this.m = 'Вы уверены, что хотите удалить выбранные записи?'
          }
        }
        return this.m
      },
      fields: function () {
        let showingFields = []
        bus.$on('clippedTable', () => {
          let indexArr = [1,4,8,10,11,12,13,14,18]
          for(let i = 0; i < indexArr.length; i++){
            this.titles[indexArr[i]].show = false
          }
        })
        for(let i = 0; i < this.itemFields.length; i++){
          showingFields.push(this.itemFields[i])
        }
        for(let i = 0; i < this.titles.length; i++){
          if(this.titles[i].show === false &&
            this.titles[i].key === this.itemFields[i+2].label){
            showingFields.splice(showingFields.indexOf(this.itemFields[i+2]), 1)
          }
        }
        bus.$on('fullTable', () => {
          for (let i = 0; i < this.itemFields.length; i++) {
            showingFields.push(this.itemFields[i])
          }
          for(let i = 0; i < this.titles.length; i++){
            this.titles[i].show = true
          }
        })
        return showingFields
      },
      allRows: function () {
        if(this.selected.length === 0)
          return 'Выбрать все записи'
        else
          return 'Отменить выбор'
      },
      filteredItems: function() {
        if(this.$refs.selectableTable != null) {
          return this.$refs.selectableTable.filteredItems.length
        } else {
          return this.items
        }
      },
      exportToExcelTitle: function(){
        if(this.selected.length === 0)
          return 'Недоступно: выберите записи для экспорта'
        else
          return 'Экспортировать выбранные записи в .xlsx'
      },
      exportToTemplateTitle: function(){
        if(this.selected.length === 0)
          return 'Экспорт данных недоступен:\nвыберите записи для экспорта'
        else
          return 'Экспортировать выбранные записи в шаблоны .docx'
      }
    },
    methods: {
      countDownChanged(dismissCountDown) {
        this.dismissCountDown = dismissCountDown
      },
      countDownChangedError(dismissCountDown) {
        this.dismissCountDownError = dismissCountDown
      },
      showAlert() {
        this.dismissCountDown = 2
      },
      showErrorAlert() {
        this.dismissCountDown = 2
      },
      showFullTable(){
        if (!this.full) {
          bus.$emit('fullTable')
          this.full = true
        }
        else {
          bus.$emit('clippedTable')
          this.full = false
        }
      },
      hideColumn(key){
        for(let i = 0; i < this.titles.length; i++){
          if(this.titles[i].key === key){
            this.titles[i].show = false
            break
          }
        }
      },
      async getCurrentDate(item){
        let today = new Date()
        let dd = String(today.getDate()).padStart(2, '0')
        let mm = String(today.getMonth() + 1).padStart(2, '0')
        let yyyy = today.getFullYear()

        today = yyyy + '-' + mm + '-' + dd

        item.last_check = today
        await this.editItem(item)
      },
      async fetchOTSS() {
        const response = await fetch(`${process.env.ROOT_API}/inventorybase/api/v1/otss/`,
        {
          mode: "cors",
        })
        this.otss = await response.json()
        this.otss = this.otss['otss']
        let temp = []
        for (let i = 0; i < this.otss.length; i++) {
          temp.push(this.otss[i]['category'])
        }
        this.otss = temp
      },
      async fetchLocations() {
        const response = await fetch(`${process.env.ROOT_API}/inventorybase/api/v1/location/`,
        {
          mode: "cors",
        })
        let temp = await response.json()
        temp = temp['locations']
        for(let i = 0; i < temp.length; i++){
          if (temp[i].cabinet !== '') {
            this.location_cabinets.push(temp[i].cabinet)
          }
          if (temp[i].object !== '') {
            this.location_objects.push(temp[i].object)
          }
          if (temp[i].corpus !== '') {
            this.location_corpuses.push(temp[i].corpus)
          }
          if (temp[i].unit !== '') {
            this.location_units.push(temp[i].unit)
          }
        }
      },
      async fetchCategories() {
        const response = await fetch(`${process.env.ROOT_API}/inventorybase/api/v1/category/`,
        {
          mode: "cors",
        })
        this.categories = await response.json()
        this.categories = this.categories['categories']
        let temp = []
        for (let i = 0; i < this.categories.length; i++) {
          temp.push(this.categories[i]['category'])
        }
        this.categories = temp
      },
      async fetchUnits() {
        const response = await fetch(`${process.env.ROOT_API}/inventorybase/api/v1/unit/`,
        {
          mode: "cors",
        })
        this.units = await response.json()
        this.units = this.units['units']
        let temp = []
        for (let i = 0; i < this.units.length; i++) {
          temp.push(this.units[i]['unit'])
        }
        this.units = temp
      },
      stickyHeaderHeightToString() {
        return this.sliderValue.toString() + 'px'
      },
      async fetchEmployees() {
        const response = await fetch(`${process.env.ROOT_API}/inventorybase/api/v1/employee/`,
        {
          mode: "cors",
        })
        this.employeeList = await response.json()
        this.employeeList = this.employeeList['employees']
        this.employeeToString()
      },
      async fetchItems() {
        const response = await fetch(`${process.env.ROOT_API}/inventorybase/api/v1/item/`,
        {
          mode: "cors",
        })
        this.items = await response.json()
        this.items = this.items['items']
      },
      async selectToRemoveItem(item) {
        this.selected.push(item)
      },
      async removeItems(selectedItems) {
        for (let item of selectedItems) {
          const _id = item['_id']
          const response = await fetch(`${process.env.ROOT_API}/inventorybase/api/v1/item/${_id}/`,
            {
              method: 'DELETE',
              mode: 'cors',
              headers: {
                'Accept': 'application/json',
                'Content-type': 'application/json'
              },
            });
          if (response.status !== 204) {
            alert(JSON.stringify(await response.json(), null, 2));
            this.showErrorAlert()
          }
          await this.fetchItems()
        }
        this.showAlert()
        this.selected = []
      },
      async editItem(item) {
        const _id = item['_id']
        const response = await fetch(`${process.env.ROOT_API}/inventorybase/api/v1/item/${_id}/`,
          {
            method: 'PUT',
            mode: "cors",
            body: JSON.stringify(item),
            headers: {
              'Accept': 'application/json',
              'Content-type': 'application/json'
            },
          });
        const json = await response.json();
        console.log(JSON.stringify(json));
        if (response.status !== 202) {
          alert(JSON.stringify(await response.json(), null, 2));
          this.showErrorAlert()
        }
        this.showAlert()
        await this.fetchItems()
      },
      onRowSelected(items) {
        this.selected = items
        this.$refs.selectableTable.sortBy = 'name'
        this.selectedItem = this.selected[0]
      },
      selectAll() {
        if (this.selected.length === 0) {
          this.$refs.selectableTable.selectAllRows()
          this.$refs.selectableTable.sortBy = 'name'
        } else {
          this.selected = []
          this.$refs.selectableTable.sortBy = 'name'
          this.$refs.selectableTable.clearSelected()
        }
      },
      employeeToString() {
        for (let i = 0; i < this.employeeList.length; i++) {
          this.employeeInitials.push(
            this.employeeList[i].surname + ' ' +
            this.employeeList[i].name[0] + '.' +
            this.employeeList[i].secname[0] + '.');
        }
      },
      selectToEditItem(item) {
        this.$refs.editItemModal.itemForm = item
      },
      filterFunction(row, val) {
        const {
          responsible: r,
          otss_category: o,
          condition: c,
          in_operation: op
        } = val;
        return [
          !r || r === row.responsible,
          !o || o === row.otss_category,
          !c || c === row.condition,
          !op || op === row.in_operation
        ].every(Boolean);
      },
      fuseSearch() {
        this.$search(this.fuseString, this.items,
          {
            tokenize: true,
            matchAllTokens: true,
            defaultAll: false,
            keys: [
              "name", "responsible", "inventory_n"
            ]
          }).then(results => {
          this.items = results
        })
        if(this.fuseString === ''){
          this.fetchItems()
        }
      },
      sendToEditItems(){
        this.$parent.$data.dataForChildren = this.selected
      },
      showFieldFromModal(id) {
        this.$refs[id].show()
      },
      onReset(id) {
        this.$refs[id].hide()
      },
      onSubmit(id, form) {
        this.$refs[id].hide();
        const payload = {
          _id: form._id,
          name: form.name,
          user: form.user,
          responsible: form.responsible,
          components: form.components,
          inventory_n: form.inventory_n,
          otss_category: form.otss_category,
          condition: form.condition,
          unit_from: form.unit_from,
          in_operation: form.in_operation,
          fault_document_requisites: form.fault_document_requisites,
          date_of_receipt: form.date_of_receipt,
          number_of_receipt: form.number_of_receipt,
          requisites: form.requisites,
          transfer_date: form.transfer_date,
          otss_requisites: form.otss_requisites,
          spsi_requisites: form.spsi_requisites,
          transfer_requisites: form.transfer_requisites,
          comment: form.comment,
          last_check: form.last_check,
          serial_n: form.serial_n,
          category: form.category,
          year: form.year,
          cost: form.cost,
          location_object: form.location_object,
          location_unit: form.location_unit,
          location_corpus: form.location_corpus,
          location_cabinet: form.location_cabinet
        }
        this.showAlert()
        this.editItem(payload)
        this.fetchItems()

      },

    },
    watch:{
      fuseString: function () {
        this.fuseSearch()
      },
      showFilters: function () {
        if (this.showFilters) {
          let _height = document.documentElement.clientHeight * 0.81 - 117
          this.sliderValue = _height.toString() + 'px'
        } else {
          let _height = document.documentElement.clientHeight * 0.83
          this.sliderValue = _height.toString() + 'px'
        }
      },
    },
    async created() {
      await this.fetchItems()
      await this.fetchCategories()
      await this.fetchEmployees()
      await this.fetchLocations()
      await this.fetchOTSS()
      await this.fetchUnits()
      await bus.$on('updateList', () => this.fetchItems())
      await bus.$on('cancel', () => {
        this.selected = []
      })
      await bus.$on('resetFilters', (data) => {
        this.filters = data;
        this.fuseString = ''
      })

    },
    mounted() {
      let _height = document.documentElement.clientHeight * 0.83
      this.sliderValue = _height.toString() + 'px'
    }
  };
</script>

<style>
  td {
    line-height: 15px;
    color: black;
    padding: 5px;
    word-break: break-all;
  }
  .button-select-rows{
    color: #000000;
    background-color: #FFFFFF;
    border: none;
    border-radius: 10px;
  }
  table{
    white-space: normal;
    overflow-x: scroll;
  }
  /*table {*/
  /*  white-space: nowrap;*/
  /*}*/
  /*p {*/
  /*  text-overflow: ellipsis;*/
  /*  overflow-x: scroll;*/
  /*}*/
  .table thead th {
    vertical-align: sub;
    color: black;
  }
  a {
    color: black;
  }
  .btn-warning:hover {
    color: #000000;
    background-color: #FFFFFF;
    border-color: #FFFFFF;
  }
  .btn-warning {
    color: #000000;
    background-color: #FFFFFF;
    border-color: #FFFFFF;
  }
  .btn-warning.dropdown-toggle {
    color: #000000;
    background-color: #ffffff;
    border-color: #ffffff;
  }
  .tr{
    max-height: 20px;
  }
  #cell-name{
    min-width: 500px;
    text-align: justify;
  }
  p {
    text-align: justify;
  }
  #cell-selected{
    max-width: 150px;
    min-width: 150px;
    text-align: justify;
  }
  #cell-components{
    visibility: hidden;
  }
  th.table-b-table-default{
    vertical-align: middle;
  }
  td.text-center{
    vertical-align: middle;
  }
  /*.dropdown-menu{*/
  /*  overflow-y: scroll;*/
  /*  height: 550px;*/
  /*}*/
  #firstRow{
    width: 98%;
  }
</style>
