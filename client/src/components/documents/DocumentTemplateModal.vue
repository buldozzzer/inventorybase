<template>
  <b-modal ref="documentTemplateModal"
           id="document-template-modal"
           title="Экспорт записей в шаблоны документов"
           centered
           hide-footer>
    <b-container>
      <b-row>
        <b-col cols="12">
        <b-input-group id="documents"
                      label="Сохранённые шаблоны:"
                      label-for="documents-input">
<!--          :state="isIntroduced(itemForm.responsible, '')"-->
          <b-form-select id="documents-input"
                        v-model="doc"
                        :options="docs"
                        placeholder="Выберите документ из списка">
          </b-form-select>
          <b-input-group-append>
            <b-button variant="outline-success">Добавить шаблон</b-button>
          </b-input-group-append>
        </b-input-group>
      </b-col>
      </b-row>
    </b-container>
  </b-modal>
</template>

<script>
/* eslint-disable */
  export default {
    name: "DocumentTemplateModal",
    props: ["selected"],
    data(){
      return {
        docs: [],
        doc: null
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
    },
    async created(){
      await this.fetchDocs()
    }
  }
</script>

<style scoped>

</style>
