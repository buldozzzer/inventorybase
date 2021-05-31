<template>
<!--eslint-disable-->
  <div>
    <b-modal ref="documentTemplateModal"
             id="document-template-modal"
             title="Экспорт записей в шаблоны документов"
             centered
             size="xl"
             @hidden="clear"
             @show="clear"
             hide-footer>
      <b-container>
        <b-row id="firstRow">
          <b-col cols="5" align="center">
            <b-input-group id="documents"
                           label="Сохранённые шаблоны:"
                           label-for="documents-input">
              <b-form-select id="documents-input"
                             :options="docs"
                             v-model="doc">
                <template #first>
                  <b-form-select-option :value="null"
                                        disabled>
                    Выберите документ из списка
                  </b-form-select-option>
                </template>
              </b-form-select>
            </b-input-group>
          </b-col>
          <b-col align="center">
            <b-button @click="showFieldFromModal('control')"
                      :disabled="docs.length === 0"
                      variant="primary">
              Упаврление шаблонами
            </b-button>
            <b-modal ref="control"
                 centered
                 title="Управление шаблонами"
                 hide-footer>
              <b-container>
                <div v-for="doc in docs" :v-key="doc">
                  <b-row>
                    <b-col cols="10">
                      {{doc}}
                    </b-col>
                    <b-col cols="1">
                      <b-icon icon="trash"
                              variant="danger"
                              font-scale="1"
                              type="button"
                              @click="removeTemplate(doc)"
                              data-toggle="tooltip"
                              data-placement="top">
                      </b-icon>
                    </b-col>
                    <b-col cols="1">
                      <b-icon icon="download"
                              variant="success"
                              font-scale="1"
                              type="button"
                              @click="downloadTemplate(doc)"
                              data-toggle="tooltip"
                              data-placement="top">
                      </b-icon>
                    </b-col>
                  </b-row>
                </div>
              </b-container>
            </b-modal>
          </b-col>

          <b-col cols="3" align="center">
            <label for="uploadFile" class="btn">Добавьте файл</label>
            <input type="file"
                   id="uploadFile"
                   ref="uploadFile"
                   style="visibility:hidden;"
                   @change="getFileFromInputTag">
          </b-col>
          <b-col cols="1" align="center">
            <b-icon icon="info-circle"
                    data-toggle="tooltip"
                    data-placement="top"
                    font-scale="1"
                    :title="info"
                    aria-hidden="false"></b-icon>
          </b-col>
        </b-row>
        <b-row class="mt-3">
          <b-col class="ml-3">
            <b-form-checkbox
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
        <b-row id="withoutItems" class="mt-3" v-if="selected.length === 0">
          <div id="warn">
            Выберите мат. ценности
          </div>
        </b-row>
        <b-row v-else class="mt-3">
          <b-button block
                    @click="downloadFiles"
                    variant="success">
            Скачать шаблон
          </b-button>
        </b-row>
      </b-container>
    </b-modal>
  </div>
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
        merge_docs: false,
        info: 'Допустимые шаблоны:\n'
      }
    },
    methods: {
      async fetchDocs() {
        const response = await fetch(`${process.env.ROOT_API}/inventorybase/api/v1/docs/`,
        {
          mode: "cors",
        })
        let temp = await response.json()
        this.docs = temp['docs']
        this.info += temp['info']
      },
      async addDoc() {
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
      },
      getFileFromInputTag() {
        this.file = this.$refs.uploadFile.files[0]
      },
      async downloadFiles() {
        let payload = {
          filename: this.doc,
          items: this.selected,
          merge_doc: this.merge_docs
        }
        const response = await fetch(`${process.env.ROOT_API}/inventorybase/api/v1/download-docs/`,
          {
            method: 'POST',
            mode: "cors",
            body: JSON.stringify(payload),
            headers: {
              'Accept': 'application/json',
              'Content-type': 'application/json'
            },
          }).then(response => response.blob())
          .then(blob => {
            let url = window.URL.createObjectURL(blob);
            let a = document.createElement('a');
            a.href = url;
            let today = new Date();
            let dd = String(today.getDate()).padStart(2, '0');
            let mm = String(today.getMonth() + 1).padStart(2, '0');
            let yyyy = today.getFullYear();
            today = mm + '-' + dd + '-' + yyyy;
            a.download = "Документы_" + today + ".zip";
            document.body.appendChild(a);
            a.click();
            a.remove();
          });
      },
      showFieldFromModal(id) {
        this.$refs[id].show()
      },
      async removeTemplate(filename){
        const response = await fetch(`${process.env.ROOT_API}/inventorybase/api/v1/docs/${filename}/`,
            {
              method: 'DELETE',
              mode: 'cors',
              headers: {
                'Accept': 'application/json',
                'Content-type': 'application/json'
              },
            });
          if (response.status !== 204) {
            alert(JSON.stringify(await response.json(), null, 2));
          }
          await this.fetchDocs()
      },
      async downloadTemplate(filename){
        const response = await fetch(`${process.env.ROOT_API}/inventorybase/api/v1/docs/${filename}/`,
            {
              method: 'PUT',
              mode: 'cors',
              headers: {
                'Accept': 'application/json',
                'Content-type': 'application/json'
              },
            }).then(response => response.blob())
          .then(blob => {
            let url = window.URL.createObjectURL(blob);
            let a = document.createElement('a');
            a.href = url;
            a.download = filename;
            document.body.appendChild(a);
            a.click();
            a.remove();
          });
        await this.fetchDocs()
      },

    },
    watch:{
      file: function () {
        this.addDoc()
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
  #firstRow{
    max-height: 39px;
  }
</style>
