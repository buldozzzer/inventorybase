<template>
  <!--    eslint-disable-->
  <div>
    <b-container>
      <b-row class="text-center">
        <b-col cols="3">
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
        <b-col cols="3">
          <b-button variant="success" class="mt-3" v-b-modal.add-item-modal>
            <b-icon icon="download"
                    data-toggle="tooltip"
                    data-placement="top"
                    font-scale="1"
                    aria-hidden="false"></b-icon>
            Добавить запись
          </b-button>
        </b-col>
        <b-col cols="3">
          <b-button variant="light"
                    @click="showFilters = !showFilters"
                    class="mt-3">
            <b-icon :icon="filterIcon"
                    data-toggle="tooltip"
                    data-placement="top"
                    font-scale="1"
                    aria-hidden="false"></b-icon>
            {{showFilters ? 'Скрыть фильтры' : 'Показать фильтры' }}
          </b-button>
        </b-col>
        <b-col cols="3" align-self="center">
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
            Редактровать
          </b-button>
        </b-col>
      </b-row>
      <b-row>
        <b-col cols="3">
          <b-button variant="light"
                    @click="toExcel"
                    class="mt-3">
            Экспорт
          </b-button>
        </b-col>
      </b-row>
    </b-container>
    <filters class="mt-3"
             v-show="showFilters === true"
             ref="filtersForList"
             :employee-initials="employeeInitials">
    </filters>
    <b-alert
      :show="dismissCountDown"
      dismissible
      @dismissed="dismissCountDown=0"
      @dismiss-count-down="countDownChanged">
      <p>
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
      <p>
        <b-icon icon="x"
                variant="danger"
                font-scale="2"
                data-toggle="tooltip"
                data-placement="top">
        </b-icon>
        Ошибка
      </p>
    </b-alert>
    <!--    sticky-header="850px"-->
    <!--    v-bind:sticky-header="sliderValue+'px'"-->
    <b-table striped hover
             bordered
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
        <b-button-group>
          <button :title="allRows"
                  class="button-select-rows"
                  @click="selectAllRows">
            <b-icon icon="check-square"
                    v-if="selected.length === 0"
                    data-toggle="tooltip"
                    data-placement="top"
                    font-scale="1.5"
                    aria-hidden="false"></b-icon>
            <b-icon icon="check-square-fill"
                    v-else
                    v-if="selected.length !== 0"
                    data-toggle="tooltip"
                    data-placement="top"
                    font-scale="1.5"
                    aria-hidden="false"></b-icon>
          </button>
          <b-dropdown text="Поля таблицы"
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
            <b-dropdown-text class="text-nowrap">
              <b-form-checkbox v-for="title in titles"
                               style="text-align: left"
                               v-model="title['show']"
                               @click="title['show'] = !title['show']"
                               :key="title['key']">
                {{ title['key'] }}
              </b-form-checkbox>
            </b-dropdown-text>
          </b-dropdown>
        </b-button-group>
      </template>
      <template #head(index)="scope">
        <div>Номер</div>
      </template>
      <template #cell(index)="data">
        {{ data.index + 1 }}
      </template>

      <template #cell(name)="row">
        <div @dblclick="showFieldFromModal('name'), editableRow=row.item">
          <p>{{ row.item.name ? row.item.name : '&nbsp' }}</p>
        </div>
        <b-modal ref="name" centered
                 title="Измените значение поля"
                 size="sm" hide-footer
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
             class="text-nowrap">
          {{ row.item.responsible ? row.item.responsible : '&nbsp' }}
        </div>
        <b-modal ref="responsible"
                 centered
                 title="Измените значение поля"
                 size="sm"
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
             class="text-nowrap">
          <p>{{ row.item.user ? row.item.user : '&nbsp' }}</p>
        </div>
        <b-modal ref="user"
                 centered
                 title="Измените значение поля"
                 size="sm"
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
             class="text-nowrap">
          <p>{{ row.item.inventory_n ? row.item.inventory_n : '&nbsp' }}</p>
        </div>
        <b-modal ref="inventory_n"
                 centered
                 title="Измените значение поля"
                 size="sm"
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
             class="text-nowrap">
          <p>{{ row.item.in_operation ? row.item.in_operation : '&nbsp' }}</p>
        </div>
        <b-modal ref="in_operation"
                 centered
                 title="Измените значение поля"
                 size="sm"
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
             class="text-nowrap">
          <p>{{ row.item.in_operation ? row.item.in_operation : '&nbsp' }}</p>
        </div>
        <b-modal ref="in_operation"
                 centered
                 title="Измените значение поля"
                 size="sm"
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
             class="text-nowrap">
          <p>{{ row.item.condition ? row.item.condition : '&nbsp' }}</p>
        </div>
        <b-modal ref="condition"
                 centered
                 title="Измените значение поля"
                 size="sm"
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
        <div @dblclick="showFieldFromModal('unit_from'), editableRow=row.item">
          <p>{{ row.item.unit_from ? row.item.unit_from : '&nbsp' }}</p>
        </div>
        <b-modal ref="unit_from" centered
                 title="Измените значение поля"
                 size="sm" hide-footer
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
        <div @dblclick="showFieldFromModal('fault_document_requisites'), editableRow=row.item">
          <p>{{ row.item.fault_document_requisites ? row.item.fault_document_requisites : '&nbsp' }}</p>
        </div>
        <b-modal ref="fault_document_requisites"
                 centered
                 title="Измените значение поля"
                 size="sm" hide-footer
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
          <p>{{ row.item.number_of_receipt ? row.item.number_of_receipt : '&nbsp' }}</p>
        </div>
        <b-modal ref="number_of_receipt"
                 centered
                 title="Измените значение поля"
                 size="sm" hide-footer
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
                 size="sm" hide-footer
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

      <template #cell(components)="row">
        <b-icon v-if="row.detailsShowing"
                icon="eye-slash"
                font-scale="2"
                @click="row.toggleDetails">
        </b-icon>
        <b-icon v-else
                icon="eye"
                font-scale="2"
                @click="row.toggleDetails">
        </b-icon>
      </template>

      <template #row-details="row">
        <b-table resposive :items="row.item.components" :fields="componentFields">
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

      <template #cell(selected)="{ rowSelected }">
        <b-container>
          <b-row class="text-center">
            <b-col cols="6">
              <b-icon icon="check2"
                      v-show="rowSelected"
                      data-toggle="tooltip"
                      data-placement="top"
                      title="Выбрано"
                      font-scale="1.8">
              </b-icon>
            </b-col>
            <b-col cols="6">
              <b-icon icon="pencil-square"
                      variant="warning"
                      data-toggle="tooltip"
                      data-placement="top"
                      title="Редактировать"
                      font-scale="1.8"
                      v-b-modal.edit-item-modal
                      @click="selectToEditItem(row.item)">
              </b-icon>
              <b-icon icon="trash"
                      variant="danger"
                      font-scale="1.8"
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
          <p>{{ row.item.otss_requisites ? row.item.otss_requisites : '&nbsp' }}</p>
        </div>
        <b-modal ref="otss_requisites"
                 centered
                 title="Измените значение поля"
                 size="sm" hide-footer
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
          <p>{{ row.item.spsi_requisites ? row.item.spsi_requisites : '&nbsp' }}</p>
        </div>
        <b-modal ref="spsi_requisites"
                 centered
                 title="Измените значение поля"
                 size="sm" hide-footer
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
          <p>{{ row.item.spsi_requisites ? row.item.spsi_requisites : '&nbsp' }}</p>
        </div>
        <b-modal ref="spsi_requisites"
                 centered
                 title="Измените значение поля"
                 size="sm" hide-footer
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
          <p>{{ row.item.transfer_requisites ? row.item.transfer_requisites : '&nbsp' }}</p>
        </div>
        <b-modal ref="transfer_requisites"
                 centered
                 title="Измените значение поля"
                 size="sm" hide-footer
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
          <p>{{ row.item['comment'] ? row.item['comment'] : '&nbsp' }}</p>
        </div>
        <b-modal ref="comment"
                 centered
                 title="Измените значение поля"
                 size="sm" hide-footer
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
          <p>{{ row.item.date_of_receipt ? row.item.date_of_receipt : '&nbsp' }}</p>
        </div>
        <b-modal ref="date_of_receipt"
                 centered
                 title="Измените значение поля"
                 size="sm" hide-footer
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
          <p>{{ row.item.transfer_date ? row.item.transfer_date : '&nbsp' }}</p>
        </div>
        <b-modal ref="transfer_date"
                 centered
                 title="Измените значение поля"
                 size="sm" hide-footer
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
          <p>{{ row.item.last_check ? row.item.last_check : '&nbsp' }}</p>
        </div>
      </template>

    </b-table>
    <add-modal ref="addItemModal" :employee-initials="employeeInitials"/>
    <edit-modal ref="editItemModal"
                :employee-initials="employeeInitials"
                :edit-item="editItem"/>
    <confirm-form :payload="selected"
                  :dynamic-id="dynamicId"
                  :message="message"
                  :op="removeItems">

    </confirm-form>
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

  export default {
    name: "ItemList",
    components: {
      VueRangeSlider,
      AddModal,
      EditModal,
      Filters,
      ConfirmForm,
      FieldModalForm
    },
    data() {
      return {
        dismissCountDown: 0,
        dismissCountDownError: 0,
        otss: [1, 2, 3, 'Не секретно'],
        units: [],
        conditions: ['Исправно', 'Неисправно'],
        operation: ['Используется', 'Не используется'],
        m: '',
        editableRow: '',
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
          },
          {
            key: "serial_n",
            label: "Серийный номер",
          },
          {
            key: "category",
            label: "Категория",
          },
          {
            key: "type",
            label: "Тип",
          }, {
            key: "view",
            label: "Вид",
          }, {
            key: "location",
            label: "Местонахождение",
          },
        ],
        titles: [
          {
            key: "Наименование",
            show: true
          }, {
            key: "Компоненты",
            show: false
          }, {
            key: "Ответственный сотрудник",
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
          }, {
            key: "components",
            label: "Компоненты",
            class: 'text-center'
          }, {
            key: "responsible",
            label: "Ответственный сотрудник",
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
        ],
        items: [],
        selectedItem: {},
        selected: [],
        sliderValue: '540px',
        employeeList: [],
        employeeInitials: [],
        filters: {
          responsible: null,
          otss_category: null,
          condition: null,
          in_operation: null
        },
        fuseString: '',
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
          debugger
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
      }
    },
    methods: {
      async toExcel(){
        let titlesInPayload = []
        let payload = []
        for (let index = 2; index < this.itemFields.length; index++){
          if(this.titles[index-2].show === true) {
            let field = {}
            field.key = this.itemFields[index].key
            titlesInPayload.push(field)
          }
        }
        debugger
        for (let item = 0; item < this.items.length; item++){
          let itemToExport = {}
          for (let i = 0; i < titlesInPayload.length; i++){
            let t = titlesInPayload[i].key
            itemToExport[t] = this.items[item][t.toString()]
          }
          payload.push(itemToExport)
        }

        const response = await fetch(`http://localhost:8000/api/v1/to_excel/`, {
          method: 'POST',
          mode: 'cors',
          headers: {
            'Accept': 'application/json',
            'Content-type': 'application/json'
          },
          body: JSON.stringify(payload)
        });
        /* eslint-disable */
        if (response.status !== 201) {
          alert(JSON.stringify(await response.json(), null, 2));
          this.$parent.showErrorAlert()
        }
        this.$parent.showAlert()
      },
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
        const response = await fetch('http://localhost:8000/api/v1/otss/',
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
      async fetchUnits() {
        const response = await fetch('http://localhost:8000/api/v1/unit/',
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
        const response = await fetch('http://localhost:8000/api/v1/employee/',
        {
          mode: "cors",
        })
        this.employeeList = await response.json()
        this.employeeList = this.employeeList['employees']
        this.employeeToString()
      },
      async fetchItems() {
        const response = await fetch('http://localhost:8000/api/v1/item/',
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
          const response = await fetch(`http://localhost:8000/api/v1/item/${_id}/`,
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
        const response = await fetch(`http://localhost:8000/api/v1/item/${_id}/`,
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
        this.selectedItem = this.selected[0]
      },
      selectAllRows() {
        if (this.selected.length === 0) {
          this.$refs.selectableTable.selectAllRows()
        } else {
          this.selected = []
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
      setFilters() {
        if(this.showFilters) {
          this.filters = this.$refs.filtersForList.filters
        }
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
      showFilters: function(){
        if (this.showFilters){
          this.sliderValue = '410px'
        }else{
          this.sliderValue = '540px'
        }
      }
    },
    async created() {
      await this.fetchItems()
      await this.fetchEmployees()
      await this.setFilters()
      await this.fetchOTSS()
      await this.fetchUnits()
      await bus.$on('updateList', () => this.fetchItems())
      await bus.$on('cancel', () => {this.selected = []})
      await bus.$on('resetFilters', (data) => {
        this.filters = data;
        this.fuseString = ''
      })

    },
  };
</script>

<style>
  td {
    max-width: 250px;
    min-width: 150px;
    line-height: 15px;
    max-height: 40px;
    height: 40px;
    min-height: 40px;
    color: black;
  }
  .button-select-rows{
    color: #000000;
    background-color: #FFFFFF;
    border: none;
    border-radius: 10px;
  }
  table {
    white-space: nowrap;
  }
  p {
    text-overflow: ellipsis;
    overflow-x: auto;
  }
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
</style>
