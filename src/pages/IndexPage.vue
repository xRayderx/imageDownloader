<template>
  <q-page class="bg-grey-9 text-white">
    <div id="app" class="q-pa-xl">
      <h1 class="text-center">Image Downloader App</h1>
      <q-form @submit.prevent="handleSubmitUrl" class="formStyle">
        <span class="text-weight-medium q-mb-sm">
          Ingresa la URL de la página web que deseas descargar:
        </span>
        <q-input color="blue-8" bg-color="grey-2" v-model.trim="url" outlined dense class="q-mb-md full-width" label="Ingresa la URL aqui...">
          <template v-slot:append>
            <q-icon name="link" />
          </template>
        </q-input>
        
        <q-btn label="Descargar" type="submit" no-caps color="blue-8" class="btnDownload"/>
      </q-form>

      <div v-show="images.length > 0" class="galleryBox"> 
        <h2 class="text-center">Imagenes descargadas:</h2>
        <div class="flex q-gutter-md justify-center">
          <div v-for="(image, index) in images" :key="index">
            <img :src="image" alt="imagen" width="300" height="300"/>
          </div>
        </div>
      </div>
    </div>
  </q-page>
</template>

<script setup lang="ts">
import { ref } from 'vue';
import axios from 'axios';

const url = ref('')
const images = ref([])

const handleSubmitUrl = async () => {
  try {
    const res = await axios.post('http://127.0.0.1:5000/descargar', { url: url.value })
    images.value = images.value.concat(res.data)
  } catch (error) {
    console.log("Error al realizar la solicitud: ", error)
  }
}
</script>

<style>
.btnDownload {
  padding: 10px 30px;
  border-radius: 8px;
}

.formStyle {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-items: center;
}

.galleryBox {
  display: flex;
  flex-direction: column;
}

.imgCell {
  display: flex;
}
</style>
