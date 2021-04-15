<template>
  <b-container>
    <b-row>
      <b-col>
        <form class="dropForm mt-3">
          <div ref="dropZone" id="dropZone" class="doc" v-if="file == null">
            <h6 id="header">Добавьте файл.</h6>
          </div>
          <img v-if="file"
               ref="preview"
               class="doc"
               src=""
               alt=""/>
          <div>
            <div>
              <label for="uploadImage" class="btn">Открыть проводник</label>
              <input type="file"
                     class="mt-3"
                     id="uploadImage"
                     ref="uploadImage"
                     style="visibility:hidden;"
                     @change="getFileFromInputTag"
                     accept=".jpg, .jpeg, .png">
            </div>
          </div>
        </form>
      </b-col>
      <b-col>
        <label>
          <textarea class="mt-3" v-model="text"></textarea>
        </label>
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
        text: null
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
      file: async function(){
        if (!['image/jpeg', 'image/png', 'image/gif', 'image/svg+xml'].includes(this.file.type)) {
            alert('Разрешены только изображения.');
            document.getElementById('header')
        }
        if (this.file != null){
          const response = await fetch(`http://localhost:8000/api/v1/recognizer/`, {
            method: 'POST',
            mode: 'cors',
            headers: {
              'Content-Disposition': 'attachment; filename=' + this.file.name,
            },
            body: this.file
          });
          this.text = response['text']
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

    },
    async created() {
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
  h6{
    text-align: center;
    margin-top: 220px;
  }
</style>
