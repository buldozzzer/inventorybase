<template>
  <b-container>
    <b-row>
      <form class="dropForm mt-3">
        <div ref="dropZone" id="dropZone" class="doc" v-if="file == null">
          <h6>Добавьте файл.</h6>
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
        file: null
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
