<template>
  <b-container>
    <b-row>
    <form class="mt-3">
      <div ref="dropZone" id="dropZone" v-if="file == null">
        <h6>Добавьте файл.</h6>
      </div>
      <img v-else
           ref="preview"
           src=""
           alt=""/>
      <input type="file"
           class="mt-3"
           ref="uploadImage"
           @change="getFileFromInputTag"
           accept=".jpg, .jpeg, .png">
    </form>
    </b-row>
  </b-container>
</template>

<script>
/* eslint-disable */

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
    created() {

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
      }
    }
  }
</script>

<style scoped>
  form {
    display: block;
    width: 400px;
    margin: auto auto auto;
    height: 530px;
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
    height: 500px;
    margin: auto;

    background: #eee;
    border: 1px solid #ccc;

    -webkit-border-radius: 5px;
    -moz-border-radius: 5px;
    border-radius: 5px;
  }

  #dropZone:hover {
    background: #ddd;
    border-color: #aaa;
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
    height: 500px;
    margin: auto;
    display: block;
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
