<template>
  <b-modal ref="excelExporterModal"
           id="excel-exporter-modal"
           title="Экспорт записей в .xlsx"
           centered
           hide-footer>
    <b-form>
      <div class="submit-reset-buttons mt-2">
        <b-button type="submit"
                  variant="success"
                  @click="onSubmit">
          Экспорт
        </b-button>
        <b-button type="reset"
                  variant="danger"
                  @click="onReset">
          Отмена
        </b-button>
      </div>
      <h5 class="mt-2">Подтвердите выбор полей</h5>
      <b-form-checkbox v-for="title in titles"
                       style="text-align: left"
                       v-model="title['show']"
                       @click="title['show'] = !title['show']"
                       :key="title['key']">
        {{ title['key'] }}
      </b-form-checkbox>
    </b-form>
  </b-modal>
</template>

<script>
/* eslint-disable */
  export default {
    name: "ExcelExporterModal",
    props: ["titles", "itemFields", "selected"],
    data(){
      return {
        fields: []
      }
    },
    methods:{
      async toExcel(){
        let titlesInPayload = []
        let payload = []
        for (let index = 2; index < this.itemFields.length; index++){
          if(this.titles[index-2].show === true) {
            let field = {}
            field.key = this.itemFields[index].key
            titlesInPayload.push(field)
          }
        }
        for (let item = 0; item < this.selected.length; item++){
          let itemToExport = {}
          for (let i = 0; i < titlesInPayload.length; i++){
            let t = titlesInPayload[i].key
            itemToExport[t] = this.selected[item][t.toString()]
          }
          payload.push(itemToExport)
        }

        const response = await fetch(`${process.env.ROOT_API}/inventorybase/api/v1/to_excel/`, {
          method: 'POST',
          mode: 'cors',
          headers: {
            'Accept': 'application/json',
            'Content-type': 'application/json'
          },
          body: JSON.stringify(payload)
        }).then(response => response.blob())
          .then(blob => {
            let url = window.URL.createObjectURL(blob);
            let a = document.createElement('a');
            a.href = url;
            a.download = "Документы.zip";
            document.body.appendChild(a);
            a.click();
            a.remove();
          });
        if (response.status !== 201) {
          alert(JSON.stringify(await response.json(), null, 2));
        }
      },
      onReset(evt) {
        evt.preventDefault()
        this.$refs.excelExporterModal.hide()
      },
      onSubmit(evt) {
        evt.preventDefault();
        this.$refs.excelExporterModal.hide();
        this.toExcel()
      }
    }
  }
</script>

<style scoped>

</style>
