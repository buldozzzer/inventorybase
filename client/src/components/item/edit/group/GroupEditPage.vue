<template>
  <div>
    <h3>Здарова</h3>
    <group-edit-form :itemForm="itemForm"
                     :employeeInitials="employeeInitials">
    </group-edit-form>
  </div>
</template>

<script>
/* eslint-disable */
  import GroupEditForm from "./GroupEditForm";
  import { bus } from "../../../../main";

  export default {
    name: "GroupEditPage",
    components: {
      GroupEditForm
    },
    data() {
      return {
        itemForm: {},
        employeeInitials: [],
        employeeList: [],
        itemsForEdit: []
      }
    },
    methods: {
      employeeToString() {
        for (let i = 0; i < this.employeeList.length; i++) {
          this.employeeInitials.push(
            this.employeeList[i].surname + ' ' +
            this.employeeList[i].name[0] + '.' +
            this.employeeList[i].secname[0] + '.');
        }
      },
      async fetchEmployees() {
        const response = await fetch('http://localhost:8000/api/v1/employee/')
        this.employeeList = await response.json()
        this.employeeList = this.employeeList['employees']
        this.employeeToString()
      },
      fetchItemsForEdit(data){
        debugger;
        this.itemsForEdit = data
      }
    },
    async created() {
      await this.fetchEmployees()
      this.itemsForEdit = this.$parent.$data.dataForChildren
      bus.$emit('clearDataForChildren')
    },
  }
</script>

<style scoped>

</style>
