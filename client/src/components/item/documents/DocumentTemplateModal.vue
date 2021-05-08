<template>
  <b-modal ref="documentTemplateModal"
           id="document-template-modal"
           title="Экспорт записей в шаблоны документов"
           centered
           @hidden="clear"
           @show="clear"
           hide-footer>
    <b-container>
      <b-row>
        <b-col cols="8">
          <b-input-group id="documents"
                         label="Сохранённые шаблоны:"
                         label-for="documents-input">
            <b-form-select id="documents-input"
                           v-model="doc"
                           :options="docs"
                           placeholder="Выберите документ из списка">
            </b-form-select>
          </b-input-group>
        </b-col>
        <b-col cols="4">
          <b-form-file plain
                       accept="application/msword, application/vnd.ms-excel"
                       v-model="file"></b-form-file>
        </b-col>
      </b-row>
      <b-row>
        <b-col>
          <b-form-checkbox
            class="mt-3"
            :disabled="!doc"
            id="checkbox-1"
            v-model="merge_docs"
            name="checkbox-1"
            :value="true"
            :unchecked-value="false">
            Слить документы в один
          </b-form-checkbox>
        </b-col>
      </b-row>
      <b-row id="withoutItems"
             class="mt-3">
        <div id="warn"
             v-if="selected.length === 0">
          Выберите мат. ценности
        </div>
        <b-button block
                  v-else
                  variant="success">
          Скачать шаблон
        </b-button>
      </b-row>
    </b-container>
  </b-modal>
</template>

<script>
/* eslint-disable */
  import {bus} from "../../../main";

export default {
    name: "DocumentTemplateModal",
    props: ["selected"],
    data(){
      return {
        docs: [],
        doc: null,
        file: null,
        merge_docs: false
      }
    },
    methods: {
      async fetchDocs() {
        const response = await fetch(`${process.env.ROOT_API}/inventorybase/api/v1/docs/`,
        {
          mode: "cors",
        })
        this.docs = await response.json()
        this.docs = this.docs['docs']
      },
      async addDoc() {
        debugger
        const response = await fetch(`${process.env.ROOT_API}/inventorybase/api/v1/docs/`, {
          method: 'POST',
          mode: 'cors',
          headers: {
            'Content-Disposition': 'attachment; filename=' + this.file.name,
          },
          body: this.file
        })
        if (response.status !== 201) {
          alert(JSON.stringify(await response.json(), null, 2));
        } else {
          bus.$emit('updateDocList')
        }
      },
      clear(){
        this.doc = null
        this.file = null
        this.merge_docs = false
      }
    },
    watch:{
      file: function () {
        this.addDoc()
        this.doc = this.file
        this.file = null
      }
    },
    async created(){
      await this.fetchDocs()
      await bus.$on('updateDocList', () => this.fetchDocs())
    }
  }
</script>

<style scoped>
  #withoutItems {
    background: #f6cdd1;
    -webkit-border-radius: 5px;
    -moz-border-radius: 5px;
    border-radius: 5px;
    min-height: 38px;
  }
  #warn{
    text-align: center;
    margin: auto;
    vertical-align: center;
  }
</style>
