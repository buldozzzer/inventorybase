<template>
  <form>
    <div ref="dropZone" id="dropZone" v-if="file == null">
      <input type="file"
             ref="uploadImage"
             @change="getFileFromInputTag"
             accept=".jpg, .jpeg, .png"
             multiple>
    </div>
    <img v-else
         ref="preview"
         src=""
         alt=""/>
  </form>
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
            this.$refs['preview'].src = reader.result;
          }.bind(this), false);
          reader.readAsDataURL(this.file);
        }
      },
      getFileFromInputTag() {
        this.file = this.$refs.uploadImage.files[0]
        this.getImagePreview()
      }
    }
  }
</script>

<style>
  form {
    display: block;
    width: 400px;
    margin: auto;
    margin-top: 40px;
    line-height: 400px;
    align-content: center;
  }

  #dropZone {
    color: #555;
    font-size: 18px;
    text-align: center;

    width: 400px;
    padding: 50px 0;
    margin: 50px auto;

    background: #eee;
    border: 1px solid #ccc;

    -webkit-border-radius: 5px;
    -moz-border-radius: 5px;
    border-radius: 5px;
  }

  #dropZone.hover {
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
    margin: inherit;
    display: block;
    border-radius: 5px;
  }
</style>
