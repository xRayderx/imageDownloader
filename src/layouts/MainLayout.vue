<template>
  <q-layout view="hHr lpR lFr">

    <q-header bordered class="bg-grey-9 text-white">
      <q-toolbar>
        <q-toolbar-title class="text-center">
          <q-avatar>
            <q-icon name="download" size="24px"/>
          </q-avatar>
          Image Downloader
        </q-toolbar-title>
      </q-toolbar>
    </q-header>

    <q-drawer show-if-above side="right" bordered class="bg-grey-9">
      <div class="drawer q-py-md q-px-sm q-gutter-y-md">
        <span class="text-center text-weight-bold text-h6 text-white">Find the repo here:</span>
        <essential-link icon="link" title="Github" link="https://github.com/xRayderx/imageDownloader" class="text-white"/>
        <q-separator color="white"/>
      </div>
    </q-drawer>

    <q-page-container>
      <router-view />
    </q-page-container>

  </q-layout>
</template>

<script setup lang="ts">
import EssentialLink from 'src/components/EssentialLink.vue';
</script>

<style>
.drawer {
  display: flex;
  flex-direction: column;
}
</style>