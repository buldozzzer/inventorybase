<template>
  <div>
    <b-modal ref="confirmModal"
             :id="dynamicId"
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
  import {bus} from '../../main'
  export default {
    name: "ConfirmForm",
    props:['op', 'message', 'payload', 'dynamicId'],
    data(){
      return {
        title: 'Подтвердите операцию'
      }
    },
    methods:{
      reset(evt) {
        evt.preventDefault();
        this.$refs.confirmModal.hide();
        bus.$emit('cancel')
      },
      operation(evt) {
        this.op(this.payload)
        evt.preventDefault();
        this.$refs.confirmModal.hide();
        bus.$emit('cancel')
      }
    }
  }
</script>

<style>
  p {
    text-align: center;
  }
</style>
