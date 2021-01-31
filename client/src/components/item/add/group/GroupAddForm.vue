<template>
  <div>
    <h5>
      {{itemForm.name ? itemForm.name : 'Материальная ценность ' + (itemForm.index + 1) }}
    </h5>
    <b-form>
      <b-container>
        <b-row>
          <b-col :cols="colsize">
            <form-template :itemForm="itemForm"
                           :employeeInitials="employeeInitials">
            </form-template>
          </b-col>
          <b-col>
            <b-button @click="showComponents = !showComponents">
              {{!showComponents ? 'Добавить компоненты' : 'Убрать компоненты'}}
            </b-button>
            <component-list ref="componentList"
                            class="mt-3"
                            v-if="showComponents"
                            :payload="itemForm['components']">
            </component-list>
          </b-col>
        </b-row>
      </b-container>
    </b-form>
  </div>
</template>

<script>
/* eslint-disable */
  import FormTemplate from "../../FormTemplate";
  import ComponentList from "../ComponentList";
  import {bus} from "../../../../main";

  export default {
    name: "GroupAddForm",
    components:{
      FormTemplate,
      ComponentList
    },
    props:['employeeInitials', 'itemForm'],
    data(){
      return {
        showComponents: false
      }
    },
    computed:{
      colsize: function(){
        if(this.showComponents)
          return 6
        else
          return 10
      }
    },
    methods:{
      setComponents(){
        let item = this.$parent.$data.listOfNewItems.find(item => item.index === this.itemForm.index)
        let index = this.$parent.$data.listOfNewItems.indexOf(item)
        this.$parent.$data.listOfNewItems[index].components = this.$refs.componentList.createComponentList()
      }
    },
    async created() {
      await bus.$on('fetchComponents', () => this.setComponents())
    }
  }
</script>

<style>

</style>
