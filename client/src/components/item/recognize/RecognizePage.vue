<template>
  <b-container class="mt-3">
    <b-row v-if="check">
      <b-col cols="6">
        <form class="dropForm mt-3 mb-3">
          <div ref="dropZone" id="dropZone" class="doc" v-if="file == null">
            <label id="header" for="uploadImage" class="btn">Добавьте файл</label>
          </div>
          <b-icon icon="x"
                  id="removeImage"
                  v-if="file"
                  type="btn"
                  title="Удалить изображение"
                  @click="removeImage"
                  data-toggle="tooltip"
                  data-placement="top"
                  font-scale="2"
                  aria-hidden="false"></b-icon>
          <img v-if="file"
               ref="preview"
               class="doc"
               src=""
               alt=""/>
          <input type="file"
                 class="mt-3"
                 id="uploadImage"
                 ref="uploadImage"
                 style="visibility:hidden;"
                 @change="getFileFromInputTag"
                 accept=".jpg, .jpeg, .png">
        </form>
      </b-col>
      <b-col cols="6"
             v-if="file"
             id="recognized-text">
        <div id="load" v-if="isLoad === 1">
          <b-icon icon="binoculars"
                  animation="throb"
                  font-scale="3"></b-icon>
          <br/>
          <h5>Обработка...</h5>
        </div>
        <div v-else
             class="mt-3">
          <item-form :items="extracting_data['items']"/>
        </div>
      </b-col>
    </b-row>
    <b-row v-else>
      <b-col align="center">
        <h3>Модуль распознавания не запущен</h3>
        <b-button @click="checkConnection" variant="primary">
          Проверить активность модуля
        </b-button>
      </b-col>
    </b-row>
  </b-container>
</template>

<script>
/* eslint-disable */
  import {bus} from '../../../main'
  import ItemForm from "./ItemForm";

  export default {
    name: "RecognizePage",
    components:{
      ItemForm
    },
    data(){
      return {
        dropZone: null,
        file: null,
        extracting_data: null,
        isLoad: null,
        check: false
      }
    },
    mounted() {
      if (typeof (window.FileReader) == null) {
        this.$refs.dropZone.text('Не поддерживается браузером!');
        this.$refs.dropZone.addClass('error');
      } else {
        ['drag', 'dragstart', 'dragend', 'dragover', 'dragenter', 'dragleave', 'drop'].forEach(
          function (evt) {
            this.$refs.dropZone.addEventListener(evt, function (e) {
              e.preventDefault()
              e.stopPropagation()
            }.bind(this), false)
          }.bind(this))
        this.$refs.dropZone.addEventListener('drop', function (e) {
            this.file = e.dataTransfer.files[0]
            this.getImagePreview()
        }.bind(this));
      }
    },
    watch: {
      file: async function () {
        if (this.file != null) {
          this.isLoad = 1
          if (!['image/jpeg', 'image/png', 'image/gif', 'image/svg+xml'].includes(this.file.type)) {
            alert('Разрешены только изображения.');
            document.getElementById('header')
          }
          // `${process.env.ROOT_API}/inventorybase/api/v1/recognizer/`
          const response = await fetch(
            `${process.env.OCR_API}`,
            {
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
      }
    },
    methods: {
      async checkConnection() {
        const response = await fetch(
          `${process.env.OCR_API}`,
          {
            headers: {
              'Accept': 'application/json',
            },
            mode: "cors",
          }
        )
        this.check = await response.json()
        this.check = this.check['check']
      },
      getImagePreview() {
        if (/\.(jpe?g|png)$/i.test(this.file.name)) {
          let reader = new FileReader();
          reader.addEventListener("load", function () {
            this.$refs['preview'].src = reader.result
          }.bind(this), false)
          reader.readAsDataURL(this.file)
        }
      },
      getFileFromInputTag() {
        this.file = this.$refs.uploadImage.files[0]
        this.getImagePreview()
      },
      removeImage(){
        this.file=null
        this.isLoad=null
        bus.$emit('removeImage')
      },
    },
    async created() {
      await bus.$on('removeImage', () => {this.isLoad = null})
      await this.checkConnection()
    },
  }
</script>

<style scoped>
  form {
    display: block;
    width: 400px;
    margin: auto auto auto;
    height: 502px;
    background: #eee;
    border: 1px solid #ccc;
    padding-bottom: 30px;
    align-content: center;
    border-radius: 5px;
    text-align: center;
  }

  #dropZone {
    color: #555;
    font-size: 18px;
    text-align: center;
    width: 400px;
    height: 502px;
    margin: auto;

    background: #eee;
    border: 1px solid #ccc;

    -webkit-border-radius: 5px;
    -moz-border-radius: 5px;
    border-radius: 5px;
  }

  #dropZone.error {
    background: #faa;
    border-color: #f00;
  }

  #dropZone.drop {
    background: #afa;
    border-color: #0f0;
  }

  img{
    max-height: 500px;
    margin: auto;
    display: block;
    max-width: 360px;
  }

  .dropFrom img:hover:after {
    padding: 90px;
    position: absolute;
    margin-left: -250px;
    content: 'x';
    font-size: 50px;
    font-weight: bold;
    text-align: center;
    background: rgba(0, 0, 0, 0.5);
    color: black;
  }
  input{
    text-align: center;
    bottom: 0;
    width: 300px;
  }

  #header{
    margin-top: 220px;
    font-size: 22px;
  }
  textarea{
    min-width: 400px;
    min-height: 250px;
    max-height: 374px;
    -webkit-border-radius: 5px;
    -moz-border-radius: 5px;
    border-radius: 5px;
  }
  #removeImage{
    display: inline;
    position: absolute;
    margin-left: 145px;
    z-index: 999;
    color: #007bff;
  }
  #recognized-text {
    align-content: center;
    vertical-align: center;
  }
  #load {
    text-align: center;
    margin-left: auto;
    margin-right: auto;
    margin-top: 180px;
  }

</style>
