<template>
  <!--    eslint-disable-->
  <div>
    <b-form-group>
      <b-button variant="danger" class="mt-3" @click="removeItems(selected)">Удалить выбранные</b-button>
      <b-button variant="danger" class="mt-3" @click="selectAllRows">Выбрать все записи</b-button>
    </b-form-group>
    <!--    sticky-header="850px"-->
    <b-table striped hover
             ref="selectableTable"
             selectable
             :sort-by.sync="sortBy"
             v-bind:sticky-header="stickyHeaderHeight"
             :items="items"
             :fields="itemFields"
             @row-selected="onRowSelected">
      <template #head()="scope">
        <div class="text-nowrap">
          {{ scope.label }}
        </div>
      </template>

      <template #head(selected)="scope">
        <div class="text-nowrap"></div>
      </template>
      <template #head(index)="scope">
        <div class="text-nowrap">Номер</div>
      </template>

      <template #head(edit_remove)="scope">
        <div class="text-nowrap">Изменить/Удалить</div>
      </template>
      <template #cell(edit_remove)="row">
        <div class="text-nowrap">
          <b-button variant="warning" @click="editItem(row.item)">Редактировать</b-button>
          <br>
          <b-button variant="danger" class="mt-3" @click="removeItem(row.item)">Удалить</b-button>
        </div>
      </template>

      <template #cell(index)="data">
        {{ data.index + 1 }}
      </template>

      <template #cell(Компоненты)="row">
        <b-button size="sm" @click="row.toggleDetails" class="mr-2">
          {{ row.detailsShowing ? 'Скрыть' : 'Показать' }} Компоненты
        </b-button>
        <b-form-checkbox v-model="row.detailsShowing" @change="row.toggleDetails">
          Отобржать компоненты
        </b-form-checkbox>
      </template>

      <template #row-details="row">
        <b-table resposive :items="row.item.components" :fields="componentFields">
          <template #cell(index)="data">
            {{ data.index + 1 }}
          </template>
          <b-button size="sm" @click="row.toggleDetails">Скрыть компоненты</b-button>
        </b-table>
      </template>

      <template #cell(selected)="{ rowSelected }">
        <template v-if="rowSelected">
          <span aria-hidden="true">&check;</span>
          <span class="sr-only">Selected</span>
        </template>
        <template v-else>
          <span aria-hidden="true">&nbsp;</span>
          <span class="sr-only">Not selected</span>
        </template>

      </template>
    </b-table>
  </div>
</template>


<script>
export default {
  /* eslint-disable */
  name: "ItemList",
  props:['SliderValue', 'SliderValueString'],
  data() {
    return {
      /* eslint-disable */
      modes: ['multi', 'range'],
      stickyHeaderHeight: "300px",
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
          label: "Серйный номер",
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

        },
        'Компоненты',
        {
          key: "response",
          label: "Ответсвенный сотрудник",
          sortable: true
        },
        {
          key: "inventory_n",
          label: "Инвентрный номер",
          sortable: true,
        },
        {
          key: "otss_category",
          label: "Категория ОТСС",
          sortable: true,
        },
        {
          key: "condition",
          label: "состояние",
          sortable: true,
        }, {
          key: "unit_from",
          label: "подразделение, откуда поступила мат. ценность",
          sortable: true,
        }, {
          key: "in_operation",
          label: "Используется?",
          sortable: true,
        }, {
          key: "fault_document_requisites",
          label: "документы о неисправности",
          sortable: true,
        }, {
          key: "date_of_receipt",
          label: "Дата передачи во времнное пользование",
          sortable: true,
        }, {
          key: "number_of_receipt",
          label: "номер требования о поступлении на учет",
          sortable: true,
        }, {
          key: "requisites",
          label: "реквизиты книги учета мат. ценностей",
          sortable: true,
        }, {
          key: "transfer_date",
          label: "дата передачи во временное пользование",
          sortable: true,
        }, {
          key: "otss_requisites",
          label: "реквизиты документа о категории ОТСС",
          sortable: true,
        }, {
          key: "spsi_requisites",
          label: "реквизиты документа о прохождении СПСИ",
          sortable: true,
        }, {
          key: "trnasfer_requisites",
          label: "реквизиты о передаче во временное пользование",
          sortable: true,
        }, {
          key: "last_check",
          label: "дата последней проверки",
          sortable: true,
        }, {
          key: "comment",
          label: "примечания",
          sortable: true,
        },
        {
          key: "user",
          label: "сотрудник, которому передали мат. ценность в пользование",
          sortable: true
        },
      ],
      items: [],
      createdItem: {},
      selectMode: 'range',
      selected: []
    };
  },
  methods: {
    async fetchItems() {
      const response = await fetch('http://localhost:8000/api/v1/wealth/')
      this.items = await response.json()
    },
    /* eslint-disable */
    async removeItem(item) {
      const {id} = item;
      const response = await fetch(`http://localhost:8000/api/v1/item/${id}/`, {
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
    },
    async removeItems(selectedItems) {
      for (let element of selectedItems) {
        const {id} = element;
        const response = await fetch(`http://localhost:8000/api/v1/item/${id}/`, {
          method: 'DELETE',
          headers: {
            'Accept': 'application/json',
            'Content-type': 'application/json'
          },
        })
        if (response.status !== 204) {
          alert(JSON.stringify(await response.json(), null, 2));
        }
      }
      await this.fetchItems()
    },
    async editItem(item) {
      const {id} = item;
      const response = await fetch(`http://localhost:8000/api/v1/item/${id}/`, {
        method: 'PUT',
        body: JSON.stringify(data),
        headers: {
          'Accept': 'application/json',
          'Content-type': 'application/json'
        },
      });
      const json = await response.json();
      console.log('Успех:', JSON.stringify(json));
      if (response.status !== 201) {
        alert(JSON.stringify(await response.json(), null, 2));
      }
      await this.fetchItems()
    },
    onRowSelected(items) {
      this.selected = items
    },
    selectAllRows() {
      this.$refs.selectableTable.selectAllRows()
    },
    clearSelected() {
      this.$refs.selectableTable.clearSelected()
    },
  },
  async created() {
    await this.fetchItems()
  },
};
</script>

<style>
.myTable {
  margin-left: ;
}
</style>
