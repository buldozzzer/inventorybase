<template>
  <b-container>
    <b-row>
      <b-col>
        <form class="dropForm mt-3">
          <div ref="dropZone" id="dropZone" class="doc" v-if="file == null">
<!--            <h6 id="header">Добавьте файл.</h6>-->
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
      <b-col>
        <b-icon v-if="isLoad === 1"
                icon="circle-fill"
                animation="throb"
                font-scale="4"></b-icon>
        <div v-else class="mt-3">
          <h5>Наименование:</h5>
          <label>
            <textarea v-model="extracting_data"></textarea>
          </label>
          <h5 class=" mt-3" >Количество:</h5>
          <label>
            <input id="count" type="number" min="0" max="100" v-model="count">
          </label>
        </div>
      </b-col>
    </b-row>
  </b-container>
</template>

<script>
/* eslint-disable */
  import {bus} from '../../main'

  export default {
    name: "RecognizerModal",
    data(){
      return {
        dropZone: null,
        file: null,
        extracting_data: null,
        isLoad: null,
        count: 0
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
          const response = await fetch(`${process.env.ROOT_API}/inventorybase/api/v1/recognizer/`, {
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
      onSubmit(evt) {
        evt.preventDefault();
        for(let i = 0; i < this.count; i++) {
          const payload = {
            name: this.extracting_data,
            user: '',
            responsible: '',
            components: [],
            inventory_n: '',
            otss_category: '',
            condition: '',
            unit_from: '',
            in_operation: '',
            fault_document_requisites: '',
            date_of_receipt: null,
            number_of_receipt: '',
            requisites: '',
            transfer_date: null,
            otss_requisites: '',
            spsi_requisites: '',
            transfer_requisites: '',
            comment: '',
            last_check: null,
          }
        }
      },
      removeImage(){
        this.file=null
        this.isLoad=null
        bus.$emit('removeImage')
      }
    },
    async created() {
      await bus.$on('removeImage', () => {this.isLoad = null})
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
  #count {
    width: 400px;
  }
  #removeImage{
    display: inline;
    position: absolute;
    margin-left: 145px;
    z-index: 999;
    color: #007bff;
  }
</style>
