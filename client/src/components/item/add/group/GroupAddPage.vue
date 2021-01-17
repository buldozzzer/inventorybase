<template>
  <b-container class="mt-3">
    <b-row>
      <b-col cols="2">
        <b-navbar v-b-scrollspy:scrollspy-nested class="flex-column">
          <b-nav pills vertical>
            <b-nav-item href="#item-1" @click="scrollIntoView">Item 1</b-nav-item>
            <b-nav-item href="#item-2" @click="scrollIntoView">Item 2</b-nav-item>
            <b-nav-item href="#item-3" @click="scrollIntoView">Item 3</b-nav-item>
            <b-nav-item href="#item-4" @click="scrollIntoView">Item 4</b-nav-item>
            <b-nav-item href="#item-5" @click="scrollIntoView">Item 5</b-nav-item>
            <b-nav-item href="#item-6" @click="scrollIntoView">Item 6</b-nav-item>
            <b-nav-item href="#item-7" @click="scrollIntoView">Item 7</b-nav-item>
          </b-nav>
        </b-navbar>
      </b-col>
      <b-col cols="10">
        <div id="scrollspy-nested"
             style="position:relative; height:600px; overflow-y:scroll"
             ref="content">
          <h5 id="item-1" style="">Item 1</h5>
          <group-add-form :employee-initials="employeeInitials">
          </group-add-form>
          <h5 id="item-2" style="">Item 2</h5>
          <group-add-form :employee-initials="employeeInitials">
          </group-add-form>
          <h5 id="item-3" style="">Item 3</h5>
          <group-add-form :employee-initials="employeeInitials">
          </group-add-form>
          <h5 id="item-4" style="">Item 4</h5>
          <group-add-form :employee-initials="employeeInitials">
          </group-add-form>
          <h5 id="item-5" style="">Item 5</h5>
          <group-add-form :employee-initials="employeeInitials">
          </group-add-form>
          <h5 id="item-6" style="">Item 6</h5>
          <group-add-form :employee-initials="employeeInitials">
          </group-add-form>
          <h5 id="item-7" style="">Item 7</h5>
          <group-add-form :employee-initials="employeeInitials">
          </group-add-form>
        </div>
      </b-col>
    </b-row>
  </b-container>
</template>

<script>
/* eslint-disable */
  import GroupAddForm from "./GroupAddForm";

  export default {
    name: "GroupAddPage",
    components: {
      GroupAddForm
    },
    data(){
      return {
        employeeList: [],
        employeeInitials: []
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
    },
    async created() {
      await this.fetchEmployees()
    }
  }
</script>

<style scoped>

</style>
