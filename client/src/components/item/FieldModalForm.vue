<template>
  <div>
    <b-modal ref="name"
             centered
             size="sm"
             hide-footer
             hide-header-close>
      <b-form class="w-100">
        <div class="container mt-3">
          <b-form-group id="form-category-group"
                        label=""
                        label-for="form-input">
            <b-form-input id="form-input"
                          type="text"
                          class="mt-3"
                          v-model="form[itemField]"
                          :value="form[itemField]">
            </b-form-input>
          </b-form-group>
        </div>
      </b-form>
    </b-modal>
  </div>
</template>

<script>
/* eslint-disable */
  export default {
    name: "FieldModalForm",
    props:['item', 'itemField', 'id'],
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
            mode: 'cors',
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
      onReset(evt) {
        evt.preventDefault()
        this.$refs.fieldModalForm.hide()
        for(let key in this.form){
          this.form['key'] = ''
        }
      },
      onSubmit(evt) {
        evt.preventDefault();
        this.$refs.fieldModalForm.hide();
        const payload = this.form
        this.editItem(payload)
        for(let key in this.form){
          this.form['key'] = ''
        }
      },
    }
  }
</script>

<style scoped>

</style>
