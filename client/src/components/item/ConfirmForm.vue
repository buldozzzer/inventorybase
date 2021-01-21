<template>
  <div>
    <b-modal ref="confirmModal"
             id="confirm-modal"
             :title="title"
             hide-footer
             hide-header-close>
      <p>{{message}}</p>
      <b-button variant="success"
                @click="operation">
        Да
      </b-button>
      <b-button variant="danger"
                @click="reset">
        Отмена
      </b-button>
    </b-modal>
  </div>
</template>

<script>
/* eslint-disable */
  export default {
    name: "ConfirmForm",
    props:['title', 'op', 'message'],
    data(){
      return {
        title: 'Подтвердите операцию',
      }
    },
    methods:{
      reset(evt) {
        evt.preventDefault();
        this.$refs.confirmModal.hide();
      },
      operation(evt){
        this.op()
        evt.preventDefault();
        this.$refs.confirmModal.hide();
      }
    }
  }
</script>

<style>
  p {
    text-align: center;
  }
</style>
