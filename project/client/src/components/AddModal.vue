<!--eslint-disable-->
<template>
  <b-modal ref="addItemModal"
           id="add-item-modal"
           title="Добавить запись в базу мат. ценностей"
           size="xl"
           hide-footer>
    <b-form @submit="onSubmit" @reset="onReset" class="w-100">
      <b-container>
        <b-row>

          <b-col cols="8">
            <b-form-group id="form-name-group"
                          label="Наименование:"
                          label-for="form-name-input">
              <b-form-input id="form-name-input"
                            type="text"
                            v-model="itemForm.name"
                            required
                            :state="false"
                            placeholder="Введите наименование мат. ценности">
              </b-form-input>
            </b-form-group>
          </b-col>

        </b-row>

        <b-row>
          <b-col cols="4">
            <b-form-group id="form-inventory_n-group"
                          label="Инвентарный номер:"
                          label-for="form-inventory_n-input">
              <b-form-input id="form-inventory_n-input"
                            type="text"
                            v-model="itemForm.inventory_n"
                            required
                            :state="false"
                            placeholder="Введите инвентарный номер">
              </b-form-input>
            </b-form-group>
          </b-col>

          <b-col cols="4">
            <b-form-group id="form-responsible-group"
                          label="Ответственный сотрудник:"
                          label-for="form-responsible-input">
              <b-form-input id="form-responsible-input"
                            v-model="itemForm.responsible"
                            required
                            :state="false"
                            list="employee-list"
                            placeholder="Введите/Выберете ФИО сотрудника">
              </b-form-input>
              <datalist id="employee-list">
                <option>---------</option>
                <option v-for="employee in employeeInitials">{{ employee }}</option>
              </datalist>
            </b-form-group>
          </b-col>
        </b-row>

        <b-row>
          <b-col cols="4">
            <b-form-group id="form-condition-group"
                          label="Состояние:"
                          label-for="form-condition-input">
              <b-form-select id="form-condition-input"
                             type="radio"
                             v-model="itemForm.condition"
                             :options="conditions"
                             :state="false"
                             required>
              </b-form-select>
            </b-form-group>
          </b-col>

          <b-col cols="4">
            <b-form-group id="form-otss_category-group"
                          label="Категория ОТСС:"
                          label-for="form-otss_category-input">
              <b-form-select id="form-otss_category-input"
                             type="radio"
                             v-model="itemForm.otss_category"
                             :options="otssCategories"
                             :state="false"
                             required>
              </b-form-select>
            </b-form-group>
          </b-col>
        </b-row>

        <b-row>
          <b-col cols="4">
            <b-form-group id="form-unit_from-group"
                          label="Подразделение, откуда поступило:"
                          label-for="form-unit_from-input">
              <b-form-input id="form-unit_from-input"
                            type="text"
                            v-model="itemForm.unit_from"
                            :state="false"
                            required>
              </b-form-input>
            </b-form-group>
          </b-col>

          <b-col cols="4">
            <b-form-group id="form--group"
                          label="Категория ОТСС:"
                          label-for="form-otss_category-input">
              <b-form-select id="form-otss_category-input"
                             type="radio"
                             v-model="itemForm.otss_category"
                             :options="otssCategories"
                             :state="false"
                             required>
              </b-form-select>
            </b-form-group>
          </b-col>
        </b-row>
        <b-form-group id="form-component-group" v-model="itemForm.components">
        </b-form-group>
        <b-button type="submit" variant="primary">Добавить запись</b-button>
        <b-button type="reset" variant="danger">Отмена</b-button>
      </b-container>
    </b-form>
  </b-modal>
</template>

<script>

export default {
  /* eslint-disable */
  name: "AddModal",
  data() {
    return {
      otssCategories: [1, 2, 3, 'не секретно'],
      conditions: ['Рабочее', 'Нерабочее'],
      employeeList: [],
      itemForm: {
        name: '',
        user: '',
        responsible: '',
        components: [],
        inventory_n: '',
        otss_category: null,
        condition: '',
        unit_from: '',
        in_operation: null,
        fault_document_requisites: '',
        date_of_receipt: null,
        number_of_receipt: '',
        requisites: '',
        transfer_date: '',
        otss_requisites: '',
        spsi_requisites: '',
        trnasfer_requisites: '',
        comment: '',
        last_check: ''
      },
      ComponentForm: {
        name: '',
        serial_n: '',
        category: null,
        type: null,
        view: null,
        location: null
      },
      employeeInitials: []
    }

  },
  methods: {
    /* eslint-disable */
    async fetchEmployees() {
      const response = await fetch('http://localhost:8000/api/v1/employee/')
      this.employeeList = await response.json()
    },
    async createItem(payload) {
      const response = await fetch('http://localhost:8000/api/v1/item/', {
        method: 'POST',
        headers: {
          'Accept': 'application/json',
          'Content-type': 'application/json'
        },
        body: JSON.stringify(payload)
      });
      /* eslint-disable */
      if (response.status !== 201) {
        alert(JSON.stringify(await response.json(), null, 2));
      }
      await this.fetchItems()
    },
    initForm() {
      this.ItemForm.name = '';
      this.ItemForm.user = {};
      this.ItemForm.responsible = {};
      this.ItemForm.components = [];
      this.ItemForm.inventory_n = '';
      this.ItemForm.otss_category = '';
      this.ItemForm.condition = '';
      this.ItemForm.unit_from = '';
      this.ItemForm.in_operation = '';
      this.ItemForm.fault_document_requisites = '';
      this.ItemForm.date_of_receipt = '';
      this.ItemForm.number_of_receipt = '';
      this.ItemForm.requisites = '';
      this.ItemForm.transfer_date = '';
      this.ItemForm.otss_requisites = '';
      this.ItemForm.spsi_requisites = '';
      this.ItemForm.trnasfer_requisites = '';
      this.ItemForm.comment = '';
      this.ItemForm.last_check = '';
    },
    onReset(evt) {
      evt.preventDefault();
      this.$refs.addItemModal.hide();
      this.initForm();
    },
    onSubmit(evt) {
      evt.preventDefault();
      this.$refs.addItemModal.hide();
      const payload = {
        title: this.ItemForm.name,
        inventory_n: this.ItemForm.inventory_n,
        otss_category: this.ItemForm.otss_category
      };
      this.createItem(payload);
      this.initForm();
    },
    employeeToString() {
      for (let i = 0; i < this.employeeList.length; i++) {
        this.employeeInitials.push(
          this.employeeList[i].sirname + ' ' +
          this.employeeList[i].name[0] + '.' +
          this.employeeList[i].secname[0] + '.');
      }
    },
  },
  async created() {
    await this.fetchEmployees()
    this.employeeToString()
  }
}
</script>

<style scoped>
.btn_close {
  color: white;
  background: red;
}

.btn_edit {
  color: white;
  background: #26ae68;
}
</style>
