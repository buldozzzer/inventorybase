<template>
  <b-card no-body>
    <b-card no-body>
      <b-nav pills card-header slot="header" v-b-scrollspy:nav-scroller>
        <b-nav-item v-for="component in components"
                    :key="component.id"
                    :href="'#component-' + component.id"
                    @click="scrollIntoView">
          {{ component.name !== '' ? component.name : 'Компонент ' + (component.id + 1) }}
        </b-nav-item>
      </b-nav>

      <b-card-body
        id="nav-scroller"
        ref="content"
        style="position:relative; height:650px; overflow-y:scroll;">
        <component-form v-for="component in components"
                        :key="component.id"
                        :component="component"
        />
        <b-row>
          <b-col cols="6">
            <b-button @click="addComponent">Добавить компонент</b-button>
          </b-col>
          <b-col cols="6">
            <b-button variant="danger"
                      v-if="components.length > 0"
                      @click="deleteComponent">Удалить компонент</b-button>
          </b-col>
        </b-row>
      </b-card-body>
    </b-card>
  </b-card>
</template>

<script>
/* eslint-disable */
  import {bus} from '../../../main'
  import ComponentForm from "./ComponentForm";

  export default {
    name: "ComponentList",
    props: ['payload'],
    components: {
      ComponentForm
    },
    data() {
      return {
        index: 0,
        components: [],
        showArray: [],
      }
    },
    methods: {
      scrollIntoView(evt) {
        evt.preventDefault()
        const href = evt.target.getAttribute('href')
        const el = href ? document.querySelector(href) : null
        if (el) {
          this.$refs.content.scrollTop = el.offsetTop
        }
      },
      initComponentForm() {
        this.components = []
      },
      init(){
        if(this.payload == null) {
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
          this.components.push(componentForm)
          this.index += 1
        } else {
          this.components = this.payload
          this.index = this.components.length
        }
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
        this.components.push(componentForm)
        this.index += 1
      },
      deleteComponent(){
        this.components.splice(this.components.length-1, 1)
        this.index -= 1
      },
      createComponentList() {
        return this.components
      }
    },
    async created() {
      this.init()
      await bus.$on('clearComponentForm', () => this.initComponentForm())
    }
  }
</script>

<style>

</style>
