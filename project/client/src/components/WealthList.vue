<template>
  <!--    eslint-disable-->
  <div>
    <b-form-group label="">
      <b-form-select v-model="selectMode" :options="modes"></b-form-select>
    </b-form-group>
    <div class="mb-2">
    </div>
<!--    sticky-header="850px"-->
    <b-table
             sticky-header="500px"
             :items="items"
             :fields="itemFields"
             @row-selected="onRowSelected">
      <template #head()="scope">
        <div class="text-nowrap">
          {{ scope.label }}
        </div>
      </template>

      <template #head(index)="scope">
        <div class="text-nowrap">Номер</div>
      </template>
      <template #cell(edit_remove)="row">
        <div class="text-nowrap">
          <b-button variant="danger" @click="removeItem(row.item)">X</b-button>
          <b-button variant="warning" @click="editItem(row.item)">edit</b-button>
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
    </b-table>
  </div>
</template>


<script>
export default {
  /* eslint-disable */
  name: "WealthList",

  data() {
    return {
      /* eslint-disable */
      modes: ['multi', 'range'],
      stickyHeader: false,
      noCollapse: false,
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
        'index',
        {
          key: "edit_remove",
          stickyColumn: true,
          isRowHeader: true,
          variant: 'primary'
        },{
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
    async createItems() {
      const response = await fetch('http://localhost:8000/api/v1/wealth/', {
        method: 'POST',
        headers: {
          'Accept': 'application/json',
          'Content-type': 'application/json'
        },
        body: JSON.stringify(this.createdItem)
      });

      if (response.status !== 201) {
        alert(JSON.stringify(await response.json(), null, 2));
      }
      await this.fetchItems()
    },
    /* eslint-disable */
    async removeItem(item) {
      const {id} = item;
      const response = await fetch(`http://localhost:8000/api/v1/wealth/${id}/`, {
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
    async editItem(item) {
      const {id} = item;
      const response = await fetch(`http://localhost:8000/api/v1/wealth/${id}/`, {
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
