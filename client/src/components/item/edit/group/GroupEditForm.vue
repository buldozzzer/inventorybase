<template>
  <b-col class="mt-3">
    <h3>
      {{ itemForm.name }}
    </h3>
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
          <b-col v-if="itemForm['components'].length > 0">
            <b-card no-body>
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
                style="position:relative; height:650px; overflow-y:scroll;">
                <component-card ref="componentCard"
                                v-for="component in itemForm['components']"
                                :key="component.id"
                                :components="itemForm['components']"
                                :component="component"
                />
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
        location_cabinets: []
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
    },
    async created(){
      await this.fetchLocations()
      await this.fetchCategories()

    }
  }
</script>

<style>
h3 {
  text-align: center
}
</style>
