<template>
  <b-modal ref="documentTemplateModal"
           id="document-template-modal"
           title="Экспорт записей в шаблоны документов"
           centered
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
        <b-form-file plain v-model="file"></b-form-file>
      </b-col>
      </b-row>
    </b-container>
  </b-modal>
</template>

<script>
/* eslint-disable */
  import {bus} from "../../main";

export default {
    name: "DocumentTemplateModal",
    props: ["selected"],
    data(){
      return {
        docs: [],
        doc: null,
        file: null,
        filename: ''
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
        const response = await fetch(`${process.env.ROOT_API}/inventorybase/api/v1/docs/`, {
            method: 'POST',
            mode: 'cors',
            headers: {
              'Content-Disposition': 'attachment; filename=' + this.file.name,
            },
            body: this.file
          });
          this.extracting_data = await response.json()
          this.extracting_data = this.extracting_data['extracting_data']
          this.isLoad = null
          if (response.status !== 201) {
            alert(JSON.stringify(await response.json(), null, 2));
          }

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
    }
  }
</script>

<style scoped>

</style>
