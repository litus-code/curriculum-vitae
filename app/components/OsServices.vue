<script setup lang="ts">
import {serviceIds} from '~/domain/os'
const {services,toggleService,open}=useDesktop()
const {t}=useI18n()
</script>
<template>
  <div class="sticky-note"><span class="tape"/><h3>{{t('services')}}</h3>
  <label v-for="id in serviceIds" :key="id"><input type="checkbox" :checked="services.includes(id)" @change="toggleService(id)"/><span>{{t(id)}}</span></label>
  <button type="button" @click="open('contact')">{{t('contact')}} ↗</button></div>
</template>
