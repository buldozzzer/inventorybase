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
             :key="item.name">
          <h5 :id="'item-'+item.index">Наименование:</h5>
          <label>
            <textarea id="name" v-model="item.name"></textarea>
          </label>
          <h5 class=" mt-3" >Количество:</h5>
          <label>
            <input id="count"
                   type="number"
                   min="0"
                   max="100"
                   v-model="item.count">
          </label>
          <hr/>
        </div>

      </b-card-body>
    </b-card>
  </b-card>
</template>

<script>
/* eslint-disable */
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
    }
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
</style>
