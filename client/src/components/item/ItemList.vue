<template>
  <!--    eslint-disable-->
  <div>
    <b-container>
      <b-row>
        <b-col>
          <b-button variant="danger"
                    class="mt-3"
                    v-if="selected.length !== 0" v-b-modal.confirm-modal>
            Удалить выбранные
          </b-button>
        </b-col>
        <b-col>
          <b-button class="mt-3"
                    variant="primary"
                    href="#/items/groupedit"
                    v-if="selected.length !== 0"
                    @click="sendToEditItems">
            Редактровать
          </b-button>
        </b-col>
        <b-col>
          <!--          variant="danger"-->
          <b-button class="mt-3" @click="selectAllRows">
            {{ selected.length === 0 ? 'Выбрать записи' : 'Снять отметку' }}
          </b-button>
        </b-col>
        <b-col>
          <b-button variant="success" class="mt-3" v-b-modal.add-item-modal>
            Добавить запись
          </b-button>
        </b-col>
<!--        <b-col>-->
<!--          <vue-range-slider class="mt-3" ref="slider"-->
<!--                            v-model="sliderValue"-->
<!--                            @change="stickyHeaderHeightToString"-->
<!--                            min="300"-->
<!--                            max="1000"-->
<!--          ></vue-range-slider>-->
<!--        </b-col>-->
      </b-row>
    </b-container>
    <filters class="mt-3"
             ref="filtersForList"
             :employee-initials="employeeInitials">
    </filters>
    <!--    sticky-header="850px"-->
<!--    v-bind:sticky-header="sliderValue+'px'"-->
    <b-table class="mt-3"
             striped hover
             ref="selectableTable"
             selectable
             :sort-by.sync="sortBy"
             sticky-header="380px"
             :items="items"
             :fields="itemFields"
             :filter-function="filterFunction"
             :filter="filters"
             @row-selected="onRowSelected">
      <template #head()="scope">
        <div class="text-nowrap">
          {{ scope.label }}
        </div>
      </template>

      <template #head(selected)="scope">
        <div>&nbsp;&nbsp;</div>
      </template>
      <template #head(index)="scope">
        <div class="text-nowrap">Номер</div>
      </template>
      <template #cell(index)="data">
        {{ data.index + 1 }}
      </template>

      <template #cell(name)="row">
        <div @dblclick="showFieldFromModal('name'), editableRow=row.item">
          {{ row.item.name ? row.item.name : '&nbsp' }}
        </div>
        <b-modal ref="name" centered
                 title="Измените значение поля"
                 size="sm" hide-footer
                 hide-header-close>
          <b-form class="w-100">
            <div class="container mt-3">
              <b-form-input id="form-input"
                            type="text"
                            class="mt-3"
                            v-model="editableRow.name"
                            :value="editableRow.name">
              </b-form-input>
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
                 size="sm"
                 hide-footer
                 hide-header-close>
          <b-form class="w-100">
            <div class="container mt-3">
              <b-form-group label="Измените значение поля"
                            label-for="form-input">
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

      <template #head(edit_remove)="scope">
        <div class="text-nowrap">Изменить/Удалить</div>
      </template>
      <template #cell(edit_remove)="row">
        <div class="text-nowrap">
          <b-icon icon="pencil-square"
                  variant="warning"
                  data-toggle="tooltip"
                  data-placement="top"
                  title="Редактировать"
                  font-scale="2"
                  v-b-modal.edit-item-modal
                  @click="selectToEditItem(row.item)">
          </b-icon>
          <b-icon icon="trash"
                  variant="danger"
                  font-scale="2"
                  data-toggle="tooltip"
                  data-placement="top"
                  title="Удалить"
                  v-b-modal.confirm-modal
                  @click="selectToRemoveItem(row.item)">
          </b-icon>
        </div>
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
        <template v-if="rowSelected">
          <b-icon icon="check2"
                  data-toggle="tooltip"
                  data-placement="top"
                  title="Редактировать"
                  font-scale="0.5"
                  aria-hidden="false"></b-icon>
          <span class="sr-only">Selected</span>
        </template>
        <template v-else>
          <span aria-hidden="true">&nbsp;</span>
          <span class="sr-only">Not selected</span>
        </template>
      </template>

    </b-table>
    <add-modal ref="addItemModal" :employee-initials="employeeInitials"/>
    <edit-modal ref="editItemModal"
                :employee-initials="employeeInitials"
                :edit-item="editItem"/>
    <confirm-form :payload="selected"
                  :dynamic-id="dynamicId"
                  :message="message"
                  :op="removeItems"
    ></confirm-form>
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
        m: '',
        editableRow: '',
        dynamicId: "confirm-modal",
        noCollapse: false,
        sortBy: 'name',
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
        itemFields: [
          {
            key: "selected",
            class: 'text-center'
          }, {
            key: "edit_remove",
            stickyColumn: true,
            isRowHeader: true,
            class: 'text-center'
          },
          'index',
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
            label: "Ответсвенный сотрудник",
            sortable: true,
            class: 'text-center'
          },
          {
            key: "inventory_n",
            label: "Инвентрный номер",
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
            label: "состояние",
            sortable: true,
            class: 'text-center'
          }, {
            key: "unit_from",
            label: "подразделение, откуда поступила мат. ценность",
            sortable: true,
            class: 'text-center'
          }, {
            key: "in_operation",
            label: "Используется?",
            sortable: true,
            class: 'text-center'
          }, {
            key: "fault_document_requisites",
            label: "документы о неисправности",
            sortable: true,
            class: 'text-center'
          }, {
            key: "date_of_receipt",
            label: "Дата передачи во времнное пользование",
            sortable: true,
            class: 'text-center'
          }, {
            key: "number_of_receipt",
            label: "номер требования о поступлении на учет",
            sortable: true,
            class: 'text-center'
          }, {
            key: "requisites",
            label: "реквизиты книги учета мат. ценностей",
            sortable: true,
            class: 'text-center'
          }, {
            key: "transfer_date",
            label: "дата передачи во временное пользование",
            sortable: true,
            class: 'text-center'
          }, {
            key: "otss_requisites",
            label: "реквизиты документа о категории ОТСС",
            sortable: true,
            class: 'text-center'
          }, {
            key: "spsi_requisites",
            label: "реквизиты документа о прохождении СПСИ",
            sortable: true,
            class: 'text-center'
          }, {
            key: "transfer_requisites",
            label: "реквизиты о передаче во временное пользование",
            sortable: true,
            class: 'text-center'
          }, {
            key: "last_check",
            label: "дата последней проверки",
            sortable: true,
            class: 'text-center'
          }, {
            key: "comment",
            label: "примечания",
            sortable: true,
            class: 'text-center'
          },
          {
            key: "user",
            label: "сотрудник, которому передали мат. ценность в пользование",
            sortable: true,
            class: 'text-center'
          },
        ],
        items: [],
        selectedItem: {},
        selected: [],
        sliderValue: 405,
        employeeList: [],
        employeeInitials: [],
        filters: {
          responsible: null,
          otss_category: null,
          condition: null,
          in_operation: null
        },
        fuseString: "",
      };
    },
    computed:{
      message: function () {
        if(this.selected) {
          if (this.selected.length === 1) {
            this.m = 'Вы уверены, что хотите удалить запись?'
          } else {
            this.m = 'Вы уверены, что хотите удалить выбранные записи?'
          }
        }
        return this.m
      }
    },
    methods: {
      isRowDetail(data){
        if (data) {
          this.eye = 'eye'
        } else {
          this.eye = 'eye-slash'
        }
      },
      stickyHeaderHeightToString() {
        return this.sliderValue.toString() + 'px'
      },
      async fetchEmployees() {
        const response = await fetch('http://localhost:8000/api/v1/employee/')
        this.employeeList = await response.json()
        this.employeeList = this.employeeList['employees']
        this.employeeToString()
      },
      async fetchItems() {
        const response = await fetch('http://localhost:8000/api/v1/item/')
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
              headers: {
                'Accept': 'application/json',
                'Content-type': 'application/json'
              },
            });
          if (response.status !== 204) {
            alert(JSON.stringify(await response.json(), null, 2));
          }
          await this.fetchItems()
        }
        this.selected = []
      },
      async editItem(item) {
        const _id = item['_id']
        const response = await fetch(`http://localhost:8000/api/v1/item/${_id}/`,
          {
          method: 'PUT',
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
        }
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
        this.filters = this.$refs.filtersForList.filters
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
              "name", "responsible"
            ]
          }).then(results => {
          this.items = results
        })
        if(this.fuseString == ""){
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
        debugger;
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
        this.editItem(payload)
        this.fetchItems()
      },
    },
    watch:{
      fuseString: function () {
        this.fuseSearch()
      }
    },
    async created() {
      await this.fetchItems()
      await this.fetchEmployees()
      await this.setFilters()
      await bus.$on('updateList', () => this.fetchItems())
      await bus.$on('cancel', () => {this.selected = []})
      await bus.$on('resetFilters', (data) => {
        this.filters = data;
        this.fuseString = null
      })

    },
  };
</script>

<style>
</style>
