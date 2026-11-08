<script setup lang="ts">
import type { WindowId } from '~/domain/os'
const props=defineProps<{id:WindowId;title:string}>()
const {opened,active,open,close}=useDesktop()
const shown=computed(()=>opened.value.includes(props.id))
const style=computed(()=>({zIndex:opened.value.indexOf(props.id)+2}))
</script>
<template>
  <section v-if="shown" class="os-window" :class="['win-'+id,{focused:active===id}]" :style="style" :aria-label="title" @pointerdown="open(id)">
    <header class="window-bar"><span class="lights"><i/><i/><i/></span><strong>{{title}}</strong><button type="button" :aria-label="'Cerrar '+title" @click.stop="close(id)">×</button></header>
    <div class="window-body"><slot/></div>
  </section>
</template>
