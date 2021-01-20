<!-- eslint-disable -->
<template>
  <b-modal id="edit-item-modal"
           ref="editItemModal"
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
            <form-template :itemForm="itemForm"
                           :employeeInitials="employeeInitials"></form-template>
          </div>
          <div class="col">
            <b-card no-body>
              <b-nav pills card-header slot="header" v-b-scrollspy:nav-scroller>
                <b-nav-item @click="scrollIntoView"
                            v-for="component in itemForm['components']"
                            :key="component.id"
                            :href="'#component'+component.id">
                  {{ component.name }}
                </b-nav-item>

              </b-nav>
              <b-card-body
                id="nav-scroller"
                ref="content"
                style="position:relative; height:650px; overflow-y:scroll;">
                <component-card ref="componentCard"
                                v-for="component in itemForm['components']"
                                :key="component.id"
                                :components="itemForm['components']"
                                :component="component"
                />
              </b-card-body>
            </b-card>
          </div>
        </div>
      </div>
      <div class="submit-reset-buttons">
        <b-button type="submit" variant="primary">Добавить запись</b-button>
        <!--        @click="initForm"-->
        <b-button type="reset" variant="danger">Отмена</b-button>
      </div>
    </b-form>
  </b-modal>
</template>

<script>
/* eslint-disable */
  import ComponentCard from "./ComponentCard";
  import FormTemplate from "../FormTemplate";

  export default {
    name: 'editModal',
    props: ['employeeInitials', 'editItem'],
    components: {
      ComponentCard,
      FormTemplate
    },
    data() {
      return {
        otssCategories: [1, 2, 3, 'Не секретно'],
        conditions: ['Исправно', 'Неисправно'],
        operation: ['Используется', 'Не используется'],
        itemForm: {}
      }
    },
    methods: {
      async fetchEmployees() {
        const response = await fetch('http://localhost:8000/api/v1/employee/')
        this.employeeList = await response.json()
      },
      onReset(evt) {
        evt.preventDefault();
        this.$refs.editItemModal.hide();
        this.initForm();
      },
      onSubmit(evt) {
        evt.preventDefault();
        this.$refs.editItemModal.hide();
        // this.itemForm.components = this.$refs.componentScrollableList.createComponentList()
        const payload = this.itemForm
        this.editItem(payload)
      },
      scrollIntoView(evt) {
        evt.preventDefault()
        const href = evt.target.getAttribute('href')
        const el = href ? document.querySelector(href) : null
        if (el) {
          this.$refs.content.scrollTop = el.offsetTop
        }
      },
      initForm() {
        this.itemForm = {}
      },
    },
  };
</script>

<style scoped>

</style>
