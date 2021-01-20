<template>
  <div class="mt-3">
    <h3>
      {{ itemForm.name }}
    </h3>
    <b-form>
      <b-container>
        <b-row>
          <b-col>
            <form-template :item-form="itemForm"
                   :employee-initials="employeeInitials"/>
          </b-col>
          <div class="col">
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
          </div>
        </b-row>
      </b-container>
    </b-form>

  </div>
</template>

<script>
/* eslint-disable */
  import ComponentCard from "../ComponentCard";
  import FormTemplate from "../../FormTemplate";
  export default {
    name: "GroupEditForm",
    components: {FormTemplate, ComponentCard},
    props:['employeeInitials', 'itemForm'],
    methods:{
      scrollIntoView(evt) {
        evt.preventDefault()
        const href = evt.target.getAttribute('href')
        const el = href ? document.querySelector(href) : null
        if (el) {
          this.$refs.content.scrollTop = el.offsetTop
        }
      },
    }
  }
</script>

<style>
h3 {
  text-align: center
}
</style>
