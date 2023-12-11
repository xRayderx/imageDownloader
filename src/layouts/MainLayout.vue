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

        <!--<q-btn dense flat round icon="menu" @click="toggleLeftDrawer" />-->
      </q-toolbar>
    </q-header>

    <q-drawer show-if-above side="right" bordered class="bg-grey-9">
      <div class="drawer q-py-md q-px-sm q-gutter-y-md">
        <span class="text-center text-weight-bold text-h6 text-white">Find the repo here:</span>
        <essential-link icon="link" title="Github" link="https://github.com/xRayderx" class="text-white"/>
        <q-separator color="white"/>
      </div>
    </q-drawer>

    <q-page-container>
      <router-view />
    </q-page-container>

  </q-layout>
</template>

<script setup lang="ts">
//import { ref } from 'vue'

import EssentialLink from 'src/components/EssentialLink.vue';

//const leftDrawerOpen = ref(false)

/*const toggleLeftDrawer = () => {
  leftDrawerOpen.value = !leftDrawerOpen.value
}*/
</script>

<style>
.drawer {
  display: flex;
  flex-direction: column;
}
</style>