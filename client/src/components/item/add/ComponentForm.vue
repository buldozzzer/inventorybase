<template>
<!--eslint-disable-->
  <div>
    <h4 :id="'component-'+component.id">
      {{ component.name !== '' ? component.name : 'Компонент ' + (component.id + 1) }}
    </h4>
    <b-container id="comp">
      <b-row>
        <b-col cols="12">
          <b-form-group id="form-comp_name-group"
                        label="Название составляющей:"
                        label-for="form-comp_name-input">
            <b-form-input id="form-comp_name-input"
                          type="text"
                          required
                          :state="check(component.name, '')"
                          v-model="component.name"
                          placeholder="Введите название составляющей">
            </b-form-input>
          </b-form-group>
        </b-col>
      </b-row>

      <b-row>
        <b-col cols="12">
          <b-form-group id="form-comp_serial_n-group"
                        label="Заводской номер составляющей:"
                        label-for="form-comp_serial_n-input">
            <!--                  required-->
            <!--                  :state="check(component.serial_n, '')"-->
            <b-form-input id="form-comp_serial_n-input"
                          type="text"
                          v-model="component.serial_n"
                          placeholder="Введите заводской номер">
            </b-form-input>
          </b-form-group>
        </b-col>
      </b-row>

      <b-row>
        <b-col cols="6">
          <b-form-group id="form-comp_type-group"
                        label="Тип составляющей:"
                        label-for="form-comp_type-input">
            <!--                  required-->
            <!--                  :state="check(component.type, '')">-->
            <b-form-input id="form-comp_type-input"
                          type="text"
                          list="type-list"
                          v-model="component.type">
            </b-form-input>
            <datalist id="type-list">
              <option>---------</option>
              <option v-for="type in types"
                      :key="type['_id']">
                {{ type.type }}
              </option>
            </datalist>
          </b-form-group>
        </b-col>
        <b-col cols="6">
          <b-form-group id="form-comp_cost-group"
                        label="Цена:"
                        label-for="form-comp_cost-input">
            <b-form-input id="form-comp_cost-input"
                          type="number"
                          min="0"
                          v-model="component.cost">
              <!--                                required-->
              <!--                                :state="check(component.cost, '')"-->
            </b-form-input>
          </b-form-group>
        </b-col>
      </b-row>

      <b-row>
        <b-col cols="6">
          <b-form-group id="form-comp_category-group"
                        label="Категория:"
                        label-for="form-comp_category-input">
            <b-form-input id="form-comp_category-input"
                          type="text"
                          list="category-list"
                          v-model="component.category">
              <!--                                required-->
              <!--                                :state="check(component.category, '')"-->
            </b-form-input>
            <datalist id="category-list">
              <option>---------</option>
              <option v-for="category in categories"
                      :key="category['_id']">
                {{ category.category }}
              </option>
            </datalist>
          </b-form-group>
        </b-col>
        <b-col cols="6">
          <b-form-group id="form-comp_year-group"
                        label="Год выпуска:"
                        label-for="form-comp_year-input">
            <b-form-input id="form-comp_year-input"
                          type="text"
                          placeholder="YYYY"
                          v-model="component.year">
              <!--                                required-->
              <!--                                :state="check(component.year, '')"-->
            </b-form-input>
          </b-form-group>
        </b-col>
      </b-row>
      <b-row>
        <b-col cols="6">
          <b-form-group id="form-comp_object-group"
                        label="Объект:"
                        label-for="form-comp_object-input">
            <b-form-input id="form-comp_object-input"
                          type="text"
                          list="object-list"
                          v-model="component.location.object">
              <!--                                required-->
              <!--                                :state="check(component.location.object, '')"-->
            </b-form-input>
            <datalist id="object-list">
              <option>---------</option>
              <option v-for="object in points[0]"
                      :key="object">{{ object }}
              </option>
            </datalist>
          </b-form-group>
        </b-col>
        <b-col cols="6">
          <b-form-group id="form-comp_corpus-group"
                        label="Корпус:"
                        label-for="form-comp_corpus-input">
            <b-form-input id="form-comp_corpus-input"
                          type="text"
                          list="corpus-list"
                          v-model="component.location.corpus">
              <!--                                required-->
              <!--                                :state="check(component.location.corpus, '')"-->
            </b-form-input>
            <datalist id="corpus-list">
              <option>---------</option>
              <option v-for="corpus in points[2]"
                      :key="corpus">
                {{ corpus }}
              </option>
            </datalist>
          </b-form-group>
        </b-col>
      </b-row>

      <b-row>
        <b-col cols="6">
          <b-form-group id="form-comp_unit-group"
                        label="Подразделение:"
                        label-for="form-comp_unit-input">
            <b-form-input id="form-comp_unit-input"
                          type="text"
                          list="unit-list"
                          v-model="component.location.unit">
              <!--                                required-->
              <!--                                :state="check(component.location.unit, '')"-->
            </b-form-input>
            <datalist id="unit-list">
              <option>---------</option>
              <option v-for="unit in points[3]"
                      :key="unit">{{ unit }}
              </option>
            </datalist>
          </b-form-group>
        </b-col>

        <b-col cols="6">
          <b-form-group id="form-comp_cabinet-group"
                        label="Кабинет:"
                        label-for="form-comp_cabinet-input">
            <b-form-input id="form-comp_cabinet-input"
                          type="text"
                          list="cabinet-list"
                          v-model="component.location.cabinet">
              <!--                                required-->
              <!--                                :state="check(component.location.cabinet, '')"-->
            </b-form-input>
            <datalist id="cabinet-list">
              <option>---------</option>
              <option v-for="cabinet in points[1]"
                      :key="cabinet">{{ cabinet }}
              </option>
            </datalist>
          </b-form-group>
        </b-col>
      </b-row>
      <b-row>
        <b-col>
          <b-form-group id="form-user-group"
                        label="Лицо,которому передано в пользование:"
                        label-for="form-user-input">
            <!--              :state="isIntroduced(itemForm.user, '')"-->
            <b-form-input id="form-user-input"
                          v-model="component.user"
                          list="employee-list"
                          placeholder="Иванов И.И.">
            </b-form-input>
            <datalist id="employee-list">
              <option>---------</option>

              <option v-for="employee in employeeInitials" :v-key="employee">{{ employee }}</option>
            </datalist>
          </b-form-group>
        </b-col>
      </b-row>
    </b-container>
  </div>
</template>

<script>
/* eslint-disable */
  export default {
    name: "ComponentForm",
    props: ['component', 'employeeInitials'],
    data(){
      return{
        locations: [],
        categories: [],
        types: [],
      }
    },
    computed:{
      points: function () {
        let objects = []
        let cabinets = []
        let corpuses = []
        let units =[]
        for(let i = 0; i < this.locations.length; ++i){
          objects.push(this.locations[i]['object'])
          cabinets.push(this.locations[i]['cabinet'])
          corpuses.push(this.locations[i]['corpus'])
          units.push(this.locations[i]['unit'])
        }
        return [objects, cabinets, corpuses, units]
      }
    },
    methods:{
      check(left, right){
        return left !== right
      },
      async fetchLocations() {
        const response = await fetch(`${process.env.ROOT_API}/inventorybase/api/v1/location/`,
        {
          mode: "cors",
        })
        this.locations = await response.json()
        this.locations = this.locations['locations']
      },
      async fetchCategories() {
        const response = await fetch(`${process.env.ROOT_API}/inventorybase/api/v1/category/`,
        {
          mode: "cors",
        })
        this.categories = await response.json()
        this.categories = this.categories['categories']
      },
      async fetchTypes() {
        const response = await fetch(`${process.env.ROOT_API}/inventorybase/api/v1/type/`,
        {
          mode: "cors",
        })
        this.types = await response.json()
        this.types = this.types['types']
      },
    },
    async created(){
      await this.fetchLocations()
      await this.fetchCategories()
      await this.fetchTypes()
    }
  }
</script>

<style scoped>

</style>
