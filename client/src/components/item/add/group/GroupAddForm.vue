<template>
  <div>
    <h5>
      {{itemForm.name ? itemForm.name : 'Материальная ценность ' + (itemForm.index + 1) }}
    </h5>
    <b-form>
      <b-container>
        <b-row>
          <b-col>
            <form-template :itemForm="itemForm"
                           :employeeInitials="employeeInitials">
            </form-template>
          </b-col>
          <b-col>
            <component-list ref="componentList"
                            v-if="itemForm">
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
