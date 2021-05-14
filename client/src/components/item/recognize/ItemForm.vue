<template>
  <b-card no-body id="recognized-text">
    <b-card no-body id="card-body">
      <b-nav pills card-header slot="header" v-b-scrollspy:nav-scroller>
        <b-nav-item v-for="i in items.length"
                    :key="i"
                    :href="'#item-' + i"
                    @click="scrollIntoView">
          {{ 'Мат. ценность ' + i }}
        </b-nav-item>
      </b-nav>

      <b-card-body
        id="nav-scroller"
        ref="content">
        <div v-for="item in items"
             :key="item.index">
          <h5 :id="'item-'+item.index">Наименование:</h5>
          <label>
            <textarea id="name" v-model="item.name"></textarea>
          </label>
          <h5 class=" mt-3">Количество:</h5>
          <label>
            <input id="count"
                   type="number"
                   min="0"
                   max="100"
                   v-model="item.count">
          </label>
          <h5 class=" mt-3">Инвентарный номер:</h5>
          <label>
            <input id="inventory_n"
                   v-model="item.inventory_n">
          </label>
          <div class="submit-reset-buttons mt-3">
            <b-button type="submit"
                      id="add-button"
                      variant="success"
                      @click="onSubmit(item)">
              Добавить запись
            </b-button>
          </div>
          <hr/>
        </div>
      </b-card-body>
    </b-card>
  </b-card>
</template>

<script>
/* eslint-disable */
  import {bus} from "../../../main";

export default {
    name: "ItemForm",
    props: ["items"],
    data(){
      return {

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
      onSubmit(item) {
        for(let i = 0; i < item.count; i++) {
          const payload = {
            name: item.name,
            user: '',
            responsible: '',
            components: [],
            inventory_n: item.inventory_n,
            otss_category: '',
            condition: '',
            unit_from: '',
            in_operation: '',
            fault_document_requisites: '',
            date_of_receipt: null,
            number_of_receipt: '',
            requisites: '',
            transfer_date: null,
            otss_requisites: '',
            spsi_requisites: '',
            transfer_requisites: '',
            comment: '',
            last_check: null,
          }
          this.createItem(payload)
        }
      },
      async createItem(payload) {
        const response = await fetch(`${process.env.ROOT_API}/inventorybase/api/v1/item/`, {
          method: 'POST',
          mode: 'cors',
          headers: {
            'Content-type': 'application/json'
          },
          body: JSON.stringify(payload)
        });
        /* eslint-disable */
        if (response.status !== 201) {
          alert(JSON.stringify(await response.json(), null, 2));
          this.$parent.showErrorAlert()
        }
        bus.$emit('updateList')
        this.$parent.showAlert()
      },
    },
  }
</script>

<style scoped>
  #recognized-text {
    width: 400px;
  }
  #nav-scroller {
    position:relative;
    overflow-y:scroll;
    align-content: center;
  }
  #count {
    width: 350px;
    align-content: center;
  }
  #name {
    width: 350px;
    max-height: 300px;
    min-height: 76px;
    -webkit-border-radius: 5px;
    -moz-border-radius: 5px;
    border-radius: 5px;
  }
  #card-body{
    min-height: 500px;
    max-height: 500px;
  }
  #inventory_n {
    width: 350px;
  }
  #add-button {
    margin: auto;
  }
</style>
