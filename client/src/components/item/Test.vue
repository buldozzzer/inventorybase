<template>
  <b-container>
    <b-row>
    <form class="mt-3">
      <div ref="dropZone" id="dropZone" v-if="file == null">
        Добавьте файл.
      </div>
      <img v-else
           ref="preview"
           src=""
           alt=""/>
    </form>
    <input type="file"
           class="mt-3"
           ref="uploadImage"
           @change="getFileFromInputTag"
           accept=".jpg, .jpeg, .png"
           multiple>
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
    line-height: 500px;
    align-content: center;
    background-color: #95999c;
    border-radius: 5px;
  }

  #dropZone {
    color: #555;
    font-size: 18px;
    text-align: center;
    width: 400px;
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
    margin: auto;
  }
</style>
