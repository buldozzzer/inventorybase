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
      clearComponent(component) {
        for (let key in component) {
          component[key] = ''
        }
        component['location'] = {
          object: '',
          corpus: '',
          cabinet: '',
          unit: ''
        }
      },
      initComponentForm() {
        if (this.components.length > 0) {
          for (let component in this.components) {
            this.clearComponent(component)
          }
        }
      },
      addComponent() {
        let componentForm = {
          id: this.index,
          name: '',
          serial_n: '',
          type: '',
          view: '',
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
        let check = true
        for (let component in this.components) {
          if (component['name'] === '') {
            check = false
          }
        }
        if (check) {
          return this.components
        } else {
          return 0
        }
      }
    },
    async created() {
      this.addComponent()
      await bus.$on('clearComponentForm', () => this.initComponentForm())
    }
  }
</script>

<style>

</style>
