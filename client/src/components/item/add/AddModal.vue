<!--eslint-disable-->
<template>
  <b-modal ref="addItemModal"
           id="add-item-modal"
           title="Добавить запись в базу мат. ценностей"
           size="xl"
           no-close-on-backdrop
           hide-footer
           hide-header-close>
    <!--no-close-on-backdrop или настроить очистку формы при нажатии на задний фон-->

    <b-form @submit="onSubmit" @reset="onReset" class="w-100">
      <div class="container">
        <div class="row">
          <div class="col">
            <b-container id="item-container">
              <b-row>
                <b-col cols="12">
                  <b-form-group id="form-name-group"
                                label="Наименование:"
                                label-for="form-name-input">
                    <b-form-input id="form-name-input"
                                  type="text"
                                  v-model="itemForm.name"
                                  required
                                  :state="isIntroduced(itemForm.name, '')"
                                  placeholder="Введите наименование мат. ценности">
                    </b-form-input>
                  </b-form-group>
                </b-col>

              </b-row>

              <b-row>
                <b-col cols="6">
                  <b-form-group id="form-inventory_n-group"
                                label="Инвентарный номер:"
                                label-for="form-inventory_n-input">
                    <b-form-input id="form-inventory_n-input"
                                  type="text"
                                  v-model="itemForm.inventory_n"
                                  required
                                  :state="isIntroduced(itemForm.inventory_n, '')"
                                  placeholder="Введите инвентарный номер">
                    </b-form-input>
                  </b-form-group>
                </b-col>

                <b-col cols="6">
                  <b-form-group id="form-responsible-group"
                                label="Ответственное лицо:"
                                label-for="form-responsible-input">
                    <b-form-input id="form-responsible-input"
                                  v-model="itemForm.responsible"
                                  required
                                  :state="isIntroduced(itemForm.responsible, '')"
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

              <b-row>
                <b-col cols="6">
                  <b-form-group id="form-condition-group"
                                label="Состояние:"
                                label-for="form-condition-input">
                    <b-form-select id="form-condition-input"
                                   type="radio"
                                   v-model="itemForm.condition"
                                   :options="conditions"
                                   :state="isIntroduced(itemForm.condition, '')"
                                   required>
                    </b-form-select>
                  </b-form-group>
                </b-col>

                <b-col cols="6">
                  <b-form-group id="form-otss_category-group"
                                label="Категория ОТСС:"
                                label-for="form-otss_category-input">
                    <b-form-select id="form-otss_category-input"
                                   type="radio"
                                   v-model="itemForm.otss_category"
                                   :options="otssCategories"
                                   :state="isIntroduced(itemForm.otss_category, '')"
                                   required>
                    </b-form-select>
                  </b-form-group>
                </b-col>
              </b-row>

              <b-row>
                <b-col cols="6">
                  <b-form-group id="form-unit_from-group"
                                label="Подразделение, откуда поступило:"
                                label-for="form-unit_from-input">
                    <b-form-input id="form-unit_from-input"
                                  type="text"
                                  v-model="itemForm.unit_from"
                                  :state="isIntroduced(itemForm.unit_from, '')"
                                  required>
                    </b-form-input>
                  </b-form-group>
                </b-col>

                <b-col cols="6">
                  <b-form-group id="form-in_operation-group"
                                label="Находится в использовании:"
                                label-for="form-in_operation-input">
                    <b-form-select id="form-in_operation-input"
                                   type="radio"
                                   v-model="itemForm.in_operation"
                                   :options="operation"
                                   :state="isIntroduced(itemForm.in_operation, '')"
                                   required>
                    </b-form-select>
                  </b-form-group>
                </b-col>
              </b-row>

              <b-row>
                <b-col cols="6">
                  <b-form-group id="form-number_of_receipt-group"
                                label="Номер требования о поступлении на учёт:"
                                label-for="form-number_of_receipt-input">
                    <b-form-input id="form-number_of_receipt-input"
                                  v-model="itemForm.number_of_receipt"
                                  required
                                  :state="isIntroduced(itemForm.number_of_receipt, '')"
                                  placeholder="Введите номер требования">
                    </b-form-input>
                  </b-form-group>
                </b-col>

                <b-col cols="6">
                  <b-form-group id="form-date_of_receipt-group"
                                label="Дата поступления на учёт:"
                                label-for="form-date_of_receipt-input">
                    <b-input-group>
                      <b-form-datepicker
                        v-model="itemForm.date_of_receipt"
                        :state="isIntroduced(itemForm.date_of_receipt, null)"
                        aria-controls="date_of_receipt-input"
                        required
                        placeholder="Выберите дату"
                        :date-format-options="{ day: '2-digit', month: 'short', year: 'numeric'}"
                      ></b-form-datepicker>
                    </b-input-group>
                  </b-form-group>
                </b-col>
              </b-row>

              <b-row>
                <b-col cols="6">
                  <b-form-group id="form-requisites-group"
                                label="Реквизиты книги учёта:"
                                label-for="form-requisites-input">
                    <b-input-group>
                      <b-form-input
                        required
                        v-model="itemForm.requisites"
                        :state="isIntroduced(itemForm.requisites, '')"
                        placeholder="Введите реквизиты документов">
                      </b-form-input>
                    </b-input-group>
                  </b-form-group>
                </b-col>

                <b-col cols="6">
                  <b-form-group id="form-last_check-group"
                                label="Дата последней проверки:"
                                label-for="form-last_check-input">
                    <b-input-group>
                      <!--                :state="isIntroduced(itemForm.last_check, '')"-->
                      <b-form-datepicker
                        v-model="itemForm.last_check"
                        aria-controls="last_check-input"
                        placeholder="Выберите дату"
                        :date-format-options="{ day: '2-digit', month: 'short', year: 'numeric'}"
                      ></b-form-datepicker>
                    </b-input-group>
                  </b-form-group>
                </b-col>
              </b-row>

              <b-row>
                <b-col cols="6">
                  <b-form-group id="form-user-group"
                                label="Лицо,которому передано в пользование:"
                                label-for="form-user-input">
                    <!--              :state="isIntroduced(itemForm.user, '')"-->
                    <b-form-input id="form-user-input"
                                  v-model="itemForm.user"
                                  list="employee-list"
                                  placeholder="Иванов И.И.">
                    </b-form-input>
                  </b-form-group>
                </b-col>

                <b-col cols="6">
                  <b-form-group id="form-date_of_transfer-group"
                                label="Дата передачи во временное пользование:"
                                label-for="form-date_of_transfer-input">
                    <b-input-group>
                      <!--                :state="isIntroduced(itemForm.transfer_date, '')"-->
                      <b-form-datepicker
                        v-model="itemForm.transfer_date"
                        aria-controls="date_of_transfer-input"
                        placeholder="Выберите дату"
                        :date-format-options="{ day: '2-digit', month: 'short', year: 'numeric'}"
                      ></b-form-datepicker>
                    </b-input-group>
                  </b-form-group>
                </b-col>
              </b-row>

              <b-row>
                <b-col cols="6">
                  <b-form-group id="form-otss_requisites-group"
                                label="Реквизиты документов о категории:"
                                label-for="form-otss_requisites-input">
                    <b-form-textarea id="form-otss_requisites-input"
                                     required
                                     :state="isIntroduced(itemForm.otss_requisites, '')"
                                     v-model="itemForm.otss_requisites"
                                     placeholder="Введите реквизиты документов">
                    </b-form-textarea>
                  </b-form-group>
                </b-col>

                <b-col cols="6">
                  <b-form-group id="form-spsi_requisites-group"
                                label="Реквизиты документов об СПСИ:"
                                label-for="form-spsi_requisites-input">
                    <b-form-textarea id="form-spsi_requisites-input"
                                     required
                                     :state="isIntroduced(itemForm.spsi_requisites, '')"
                                     v-model="itemForm.spsi_requisites"
                                     placeholder="Введите реквизиты документов">
                    </b-form-textarea>
                  </b-form-group>
                </b-col>
              </b-row>

              <b-row>
                <b-col cols="6">
                  <b-form-group id="form-fault_document_requisites-group"
                                label="Реквизиты документов о неисправности:"
                                label-for="form-fault_document_requisites-input">
                    <!--              :state="isIntroduced(itemForm.fault_document_requisites, '')"-->
                    <b-form-textarea id="form-fault_document_requisites-input"
                                     v-model="itemForm.fault_document_requisites"
                                     placeholder="Введите реквизиты документов">
                    </b-form-textarea>
                  </b-form-group>
                </b-col>

                <b-col cols="6">
                  <b-form-group id="form-transfer_requisites-group"
                                label="Реквизиты документов о передаче:"
                                label-for="form-transfer_requisites-input">
                    <!--                               :state="isIntroduced(itemForm.transfer_requisites, '')"-->
                    <b-form-textarea id="form-transfer_requisites-input"
                                     v-model="itemForm.transfer_requisites"
                                     placeholder="Введите реквизиты документов">
                    </b-form-textarea>
                  </b-form-group>
                </b-col>
              </b-row>

              <b-row>
                <b-col cols="12">
                  <b-form-group id="form-comment-group"
                                label="Примечание:"
                                label-for="form-comment-input">
                    <!--              :state="isIntroduced(itemForm.comment, '')"-->
                    <b-form-textarea id="form-comment-input"

                                     v-model="itemForm.comment"
                                     placeholder="Примечание">
                    </b-form-textarea>
                  </b-form-group>
                </b-col>
              </b-row>
            </b-container>
          </div>
          <div class="col">
            <component-scrollable-list ref="componentScrollableList"/>
          </div>
        </div>
      </div>
      <div class="submit-reset-buttons">
        <b-button type="submit" variant="primary">Добавить запись</b-button>
        <b-button type="reset" variant="danger" @click="initForm">Отмена</b-button>
      </div>
    </b-form>
  </b-modal>
</template>

<script>
// eslint-disable-next-line
import ComponentScrollableList from "./ComponentScrollableList";
// eslint-disable-next-line
import {bus} from '../../../main'

export default {
  /* eslint-disable */
  name: "AddModal",
  props:{
    employeeInitials: Array,
  },
  components: {
    ComponentScrollableList
  },
  data() {
    return {
      otssCategories: [1, 2, 3, 'Не секретно'],
      conditions: ['Исправно', 'Неисправно'],
      operation: ['Используется', 'Не используется'],
      employeeList: [],
      itemForm: {
        name: '',
        user: '',
        responsible: '',
        components: [],
        inventory_n: '',
        otss_category: '',
        condition: '',
        unit_from: '',
        in_operation: '',
        date_of_receipt: null,
        number_of_receipt: '',
        requisites: '',
        transfer_date: null,
        otss_requisites: '',
        fault_document_requisites: '',
        spsi_requisites: '',
        transfer_requisites: '',
        comment: '',
        last_check: null
      },
      employeeInitials: [],
    }

  },
  methods: {
    /* eslint-disable */
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
      bus.$emit('updateList')
    },
    initForm() {
      this.itemForm.name = '';
      this.itemForm.user = '';
      this.itemForm.responsible = '';
      this.itemForm.components = [];
      this.itemForm.inventory_n = '';
      this.itemForm.otss_category = '';
      this.itemForm.condition = '';
      this.itemForm.unit_from = '';
      this.itemForm.in_operation = '';
      this.itemForm.fault_document_requisites = '';
      this.itemForm.date_of_receipt = null;
      this.itemForm.number_of_receipt = '';
      this.itemForm.requisites = '';
      this.itemForm.transfer_date = null;
      this.itemForm.otss_requisites = '';
      this.itemForm.spsi_requisites = '';
      this.itemForm.transfer_requisites = '';
      this.itemForm.comment = '';
      this.itemForm.last_check = null;

      this.$refs.componentScrollableList.initComponentForm()
    },

    onReset(evt) {
      evt.preventDefault();
      this.$refs.addItemModal.hide();
      this.initForm();
    },
    onSubmit(evt) {
      evt.preventDefault();
      debugger;
      this.$refs.addItemModal.hide();
      this.itemForm.components = this.$refs.componentScrollableList.createComponentList()
      const payload = {
        name: this.itemForm.name,
        user: this.itemForm.user,
        responsible: this.itemForm.responsible,
        components: this.itemForm.components,
        inventory_n: this.itemForm.inventory_n,
        otss_category: this.itemForm.otss_category,
        condition: this.itemForm.condition,
        unit_from: this.itemForm.unit_from,
        in_operation: this.itemForm.in_operation,
        fault_document_requisites: this.itemForm.fault_document_requisites,
        date_of_receipt: this.itemForm.date_of_receipt,
        number_of_receipt: this.itemForm.number_of_receipt,
        requisites: this.itemForm.requisites,
        transfer_date: this.itemForm.transfer_date,
        otss_requisites: this.itemForm.otss_requisites,
        spsi_requisites: this.itemForm.spsi_requisites,
        transfer_requisites: this.itemForm.transfer_requisites,
        comment: this.itemForm.comment,
        last_check: this.itemForm.last_check,
      };
      this.createItem(payload);
      this.initForm();
    },
    isIntroduced: function (left, right) {
      return left !== right
    },
  },
  async created() {
  }
}
</script>

<style scoped>
</style>
