<template>
  <b-col class="mt-3">
    <b-row id="firstRow">
      <b-col :cols=9 id="colname">
        <h3 :title="itemForm.name">
          {{ itemForm.name }}
        </h3>
      </b-col>
      <b-col>
        <b-button id="add-component-button"
                  @click="showComponentsFunc">
          Изменить компоненты
        </b-button>
      </b-col>
    </b-row>
    <b-form>
      <b-container>
        <b-row>
          <b-col>
            <form-template :item-form="itemForm"
                           :categories="categories"
                           :location_units="location_units"
                           :location_objects="location_objects"
                           :location_corpuses="location_corpuses"
                           :location_cabinets="location_cabinets"
                           :employee-initials="employeeInitials"/>
          </b-col>
          <b-col v-if="showComponents">
            <b-card no-body class="mt-3">
              <b-nav card-header slot="header" v-b-scrollspy:nav-scroller>
                <b-nav-item @click="scrollIntoView"
                            v-for="component in itemForm['components']"
                            :key="component.id"
                            :href="'#component'+component.id">
                  {{ component.name ? component.name : 'Компонент ' + component.id}}
                </b-nav-item>
              </b-nav>
              <b-card-body
                id="nav-scroller"
                ref="content"
                style="position:relative; height:1105px; overflow-y:scroll;">
                <component-card ref="componentCard"
                                v-for="component in itemForm['components']"
                                :key="component.id"
                                :components="itemForm['components']"
                                :component="component"
                />
                <b-row>
                  <b-col cols="6">
                    <b-button @click="addComponent" variant="primary">
                      Добавить компонент
                    </b-button>
                  </b-col>
                  <b-col cols="6">
                    <b-button variant="danger"
                              v-if="itemForm['components'].length > 0"
                              @click="deleteComponent">Удалить компонент
                    </b-button>
                  </b-col>
                </b-row>
              </b-card-body>
            </b-card>
          </b-col>
        </b-row>
      </b-container>
    </b-form>
  </b-col>
</template>

<script>
/* eslint-disable */
  import ComponentCard from "../ComponentCard";
  import FormTemplate from "../../FormTemplate";
  export default {
    name: "GroupEditForm",
    components: {FormTemplate, ComponentCard},
    props:['employeeInitials', 'itemForm'],
    data(){
      return {
        categories: [],
        location_units: [],
        location_objects: [],
        location_corpuses: [],
        location_cabinets: [],
        showComponents: false,
        componentCount: 0,
        index: 0
      }
    },
    methods:{
      scrollIntoView(evt) {
        evt.preventDefault()
        const href = evt.target.getAttribute('href')
        const el = href ? document.querySelector(href) : null
        if (el) {
          this.$refs.content.scrollTop = el.offsetTop
        }
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
      addComponent() {
        let componentForm = {
          id: this.index,
          name: '',
          serial_n: '',
          type: '',
          category: '',
          year: '',
          cost: '',
          location: {
            object: '',
            corpus: '',
            unit: '',
            cabinet: ''
          }
        }
        this.itemForm['components'].push(componentForm)
        this.index += 1
      },
      deleteComponent(){
        this.itemForm['components'].splice(this.itemForm['components'].length-1, 1)
        this.index -= 1
      },
      showComponentsFunc(){
        this.showComponents = !this.showComponents
        if(this.showComponents === false) {
          for (let i = 0; i < this.index - this.componentCount - 1; i++) {
            this.itemForm['components'].splice(this.itemForm['components'].length - 1, 1)
          }
        }
      }
    },
    async created(){
      await this.fetchLocations()
      await this.fetchCategories()
      this.index = this.itemForm['components'].length + 1
      this.componentCount = this.itemForm['components'].length
    },
  }
</script>

<style scoped>
  #firstRow {
    text-align: center;
  }
  h3 {
    width: 99%;
    white-space: nowrap;
    overflow: hidden;
    text-overflow: ellipsis;
  }
  #colname{
    white-space: nowrap;
    text-overflow: ellipsis;
  }
</style>
