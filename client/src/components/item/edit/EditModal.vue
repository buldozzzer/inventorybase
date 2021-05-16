<!-- eslint-disable -->
<template>
  <b-modal id="edit-item-modal"
           ref="editItemModal"
           title="Изменить запись в базе мат. ценностей"
           size="xl"
           hide-footer>
    <!--no-close-on-backdrop или настроить очистку формы при нажатии на задний фон-->

    <b-form @submit="onSubmit" @reset="onReset" class="w-100">
      <div class="submit-reset-buttons mt-3">
        <b-button type="submit"
                  :disabled="itemForm.name === ''"
                  variant="primary">
          Изменить запись
        </b-button>
        <!--        @click="initForm"-->
        <b-button type="reset" variant="danger">Отмена</b-button>

        <b-button id="add-component-button"
                  @click="showComponents = !showComponents">
          {{!showComponents ? 'Добавить компоненты' : 'Убрать компоненты'}}
        </b-button>
      </div>
      <b-container class="mt-3">
        <b-row>
          <b-col :cols="colsize">
            <form-template :itemForm="itemForm"
                           :employeeInitials="employeeInitials"></form-template>
          </b-col>
          <b-col>
            <b-card v-if="showComponents"
                    no-body
                    class="mt-3">
              <b-nav pills card-header slot="header" v-b-scrollspy:nav-scroller>
                <b-nav-item @click="scrollIntoView"
                            v-for="component in itemForm['components']"
                            :key="component.id"
                            :href="'#component'+component.id">
                  {{ component.name ? component.name : 'Компонент ' + (component.id + 1) }}
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
                                :component="component"/>
                <b-row>
                  <b-col cols="6">
                    <b-button @click="addComponent"
                              variant="primary">
                      Добавить компонент
                    </b-button>
                  </b-col>
                  <b-col cols="6">
                    <b-button v-if="itemForm['components'].length > 0"
                              variant="danger"
                              @click="deleteLastComponent">
                      Удалить компонент
                    </b-button>
                  </b-col>
                </b-row>

              </b-card-body>
            </b-card>
          </b-col>
        </b-row>
      </b-container>
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
        itemForm: {
          components: []
        },
        index: 0,
        showComponents: false
      }
    },
    computed:{
      colsize: function(){
        if(this.showComponents)
          return 6
        else
          return 12
      }
    },
    methods: {
      async fetchEmployees() {
        const response = await fetch(`${process.env.ROOT_API}/inventorybase/api/v1/employee/`,
        {
          mode: "cors",
        })
        this.employeeList = await response.json()
      },
      onReset(evt) {
        evt.preventDefault();
        this.$refs.editItemModal.hide();
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
      addComponent(){
        let componentForm = {
          id: this.index,
          name: '',
          serial_n: '',
          category: '',
          type: '',
          view: '',
          year: '',
          cost: '',
          location: {
            object: '',
            corpus: '',
            cabinet: '',
            unit: ''
          }
        }
        this.itemForm.components.push(componentForm)
        this.index += 1
      },
      deleteLastComponent(){
        this.itemForm.components.splice( this.itemForm.components.length-1, 1)
        this.index -= 1
      },
      showComponentForm(){
        if(!this.showComponents){
          this.showComponents = true
          this.addComponent()
        } else {
          this.showComponents = false
          this.itemForm.components = []
          this.index = 0
        }
      }
    },
  };
</script>

<style>
  .add-component {
    display: flow;
  }

  #add-component-button {
    position: absolute;
    right: 1.5%;
  }
</style>
