<template>
  <div>
    <b-modal id="field-modal"
             centered
             size="sm"
             :title="itemField"
             hide-footer
             hide-header-close>

    </b-modal>
  </div>
</template>

<script>
/* eslint-disable */
  export default {
    name: "FieldModalForm",
    props:['item', 'itemField'],
    data(){
      return {
        form: {}
      }
    },
    methods:{
      initForm(){
        for(let key in this.item){
          this.form['key'] = this.item['key']
        }
      },
      async editItem(item) {
        const _id = item['_id']
        const response = await fetch(`http://localhost:8000/api/v1/item/${_id}/`,
          {
          method: 'PUT',
          body: JSON.stringify(item),
          headers: {
            'Accept': 'application/json',
            'Content-type': 'application/json'
          },
        });
        const json = await response.json();
        console.log(JSON.stringify(json));
        if (response.status !== 202) {
          alert(JSON.stringify(await response.json(), null, 2));
        }
        await this.fetchItems()
      },
    }
  }
</script>

<style scoped>

</style>
