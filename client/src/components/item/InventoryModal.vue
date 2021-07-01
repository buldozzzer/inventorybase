<template>
  <b-modal ref="androidModal"
             id="android-modal"
             title="Актуализация местоположения"
             centered
             @hidden="clear"
             @show="clear"
           hide-footer>
    <b-container>
      <b-row class="firstRow">
        <b-col cols="1" v-if="file == null" >
          <input type="file"
                 id="uploadFile"
                 ref="uploadFile"
                 style="visibility:hidden;"
                 @change="getFileFromInputTag">
        </b-col>
        <b-col v-if="file == null" align="center">
          <label for="uploadFile" class="btn">Добавьте файл &nbsp; &nbsp; &nbsp; &nbsp;</label>
        </b-col>
        <b-col align="center" v-else>
          <b-row>
            <b-col>
              {{ file.name }}
              <b-icon icon="x"
                      variant="danger"
                      font-scale="1.5"
                      type="button"
                      @click="removeFile"
                      data-toggle="tooltip"
                      data-placement="top">
              </b-icon>
            </b-col>
          </b-row>
        </b-col>
      </b-row>
      <b-row class="mt-3">
          <b-button block
                    :disabled="!file"
                    @click="setChanges"
                    variant="success">
            Обновить
          </b-button>
        </b-row>
    </b-container>
  </b-modal>
</template>

<script>
/* eslint-disable */
import {bus} from "../../main";

export default {
  name: "InventoryModal",
  data() {
    return {
      file: null,
    }
  },
  methods: {
    clear() {
      this.file = null
    },
    getFileFromInputTag() {
      this.file = this.$refs.uploadFile.files[0]
    },
    async setChanges(evt) {
      const response = await fetch(`${process.env.ROOT_API}/inventorybase/api/v1/android/`, {
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
        evt.preventDefault();
        this.$refs.androidModal.hide();
        await bus.$emit('updateList')
        this.$parent.showAlert()
      }
    },
    removeFile(){
      this.file = null
    }
  }
}
</script>

<style scoped>
  .firstRow{
    max-height: 39px;
    min-height: 39px;
    align-items: center;
  }
</style>
