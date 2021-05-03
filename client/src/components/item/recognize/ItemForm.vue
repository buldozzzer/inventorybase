<template>
  <b-card no-body id="recognized-text">
    <b-card no-body>
      <b-nav pills card-header slot="header" v-b-scrollspy:nav-scroller>

      </b-nav>

      <b-card-body
        id="nav-scroller"
        ref="content">
        <div class="mt-3"
             v-for="item in items"
             :key="item.name">
          <h5>Наименование:</h5>
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
    height: 475px;
    overflow-y:scroll;
    align-content: center;
  }
  #count {
    width: 350px;
    align-content: center;
  }
  #name {
    width: 350px;
    max-height: 350px;
    min-height: 76px;
    -webkit-border-radius: 5px;
    -moz-border-radius: 5px;
    border-radius: 5px;
  }
</style>
