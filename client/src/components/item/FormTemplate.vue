<!--eslint-disable-->
<template>
  <b-container id="item-container">
    <b-row>
      <b-col cols="12">
        <b-form-group id="form-name-group"
                      label="Наименование:"
                      label-for="form-name-input">
          <b-form-input id="form-name-input"
                        type="text"
                        v-model="itemForm.name"
                        :value="itemForm.name"
                        required
                        placeholder="Введите наименование мат. ценности"
                        :state="isIntroduced(itemForm.name, '')">
          </b-form-input>
        </b-form-group>
      </b-col>
    </b-row>

    <b-row>
      <b-col cols="6">
        <b-form-group id="form-inventory_n-group"
                      label="Инвентарный номер:"
                      label-for="form-inventory_n-input">
<!--                        :state="isIntroduced(itemForm.inventory_n, '')"-->
          <b-form-input id="form-inventory_n-input"
                        type="text"
                        v-model="itemForm.inventory_n"
                        placeholder="Введите инвентарный номер">
          </b-form-input>
        </b-form-group>
      </b-col>

      <b-col cols="6">
        <b-form-group id="form-responsible-group"
                      label="Ответственное лицо:"
                      label-for="form-responsible-input">
<!--          :state="isIntroduced(itemForm.responsible, '')"-->
          <b-form-input id="form-responsible-input"
                        v-model="itemForm.responsible"
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
                         :options="conditions">
<!--                         :state="isIntroduced(itemForm.condition, '')">-->
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
                         :options="otssCategories">
<!--                         :state="isIntroduced(itemForm.otss_category, '')"-->
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
                        v-model="itemForm.unit_from">
<!--                        :state="isIntroduced(itemForm.unit_from, '')"-->
<!--                        required>-->
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
                         :options="operation">
<!--                         :state="isIntroduced(itemForm.in_operation, '')"-->
<!--                         required>-->
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
                        placeholder="Введите номер требования">
<!--            required-->
<!--            :state="isIntroduced(itemForm.number_of_receipt, '')"-->
          </b-form-input>
        </b-form-group>
      </b-col>

      <b-col cols="6">
        <b-form-group id="form-date_of_receipt-group"
                      label="Дата поступления на учёт:"
                      label-for="form-date_of_receipt-input">
          <b-input-group>
<!--            :state="isIntroduced(itemForm.date_of_receipt, null)"-->
            <b-form-datepicker
              v-model="itemForm.date_of_receipt"
              aria-controls="date_of_receipt-input"
              today-button
              reset-button
              close-button
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
<!--            :state="isIntroduced(itemForm.requisites, '')"-->
            <b-form-input
              v-model="itemForm.requisites"
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
              today-button
              reset-button
              close-button
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
              today-button
              reset-button
              close-button
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
<!--          required-->
<!--          :state="isIntroduced(itemForm.otss_requisites, '')"-->
          <b-form-textarea id="form-otss_requisites-input"
                           v-model="itemForm.otss_requisites"
                           placeholder="Введите реквизиты документов">
          </b-form-textarea>
        </b-form-group>
      </b-col>

      <b-col cols="6">
        <b-form-group id="form-spsi_requisites-group"
                      label="Реквизиты документов об СПСИ:"
                      label-for="form-spsi_requisites-input">
<!--          required-->
<!--          :state="isIntroduced(itemForm.spsi_requisites, '')"-->
          <b-form-textarea id="form-spsi_requisites-input"
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
<!--      :state="isIntroduced(itemForm.transfer_requisites, '')"-->
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
</template>

<script>
/* eslint-disable */
  export default {
    name: "FormTemplate",
    props: ['itemForm', 'employeeInitials'],
    data(){
      return {
        otssCategories: [1, 2, 3, 'Не секретно'],
        conditions: ['Исправно', 'Неисправно'],
        operation: ['Используется', 'Не используется'],

      }
    },
    methods:{
      isIntroduced(left, right) {
        return left !== right
      },
    }
  }
</script>

<style scoped>

</style>
