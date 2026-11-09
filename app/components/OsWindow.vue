<script setup lang="ts">
import type { WindowId } from '~/domain/os'
const props=defineProps<{id:WindowId;title:string}>()
const {opened,active,open,close}=useDesktop()
const shown=computed(()=>opened.value.includes(props.id))
const { locale } = useI18n()
watch(shown, async value => {
  if (!value || !import.meta.client || window.innerWidth>800) return
  await nextTick()
  frame.value?.scrollIntoView({behavior:window.matchMedia('(prefers-reduced-motion: reduce)').matches ? 'instant' : 'smooth',block:'start'})
}, {flush:'post'})
const frame=ref<HTMLElement>()
const maximized=ref(false)
function toggleMaximize(){
  maximized.value=!maximized.value
  offset.x=0
  offset.y=0
  open(props.id)
}
const offset=reactive({x:0,y:0})
const drag=reactive({active:false,pointer:-1,startX:0,startY:0,x:0,y:0})
const style=computed(()=>({zIndex:30 + opened.value.indexOf(props.id),transform:maximized.value ? 'none' : `translate(${offset.x}px, ${offset.y}px)`}))
function startDrag(event:PointerEvent){
  if (!import.meta.client || window.innerWidth<=800 || maximized.value || event.button!==0 || (event.target as HTMLElement).closest('button')) return
  const el=frame.value
  if (!el) return
  open(props.id)
  drag.active=true
  drag.pointer=event.pointerId
  drag.startX=event.clientX
  drag.startY=event.clientY
  drag.x=offset.x
  drag.y=offset.y
  ;(event.currentTarget as HTMLElement).setPointerCapture(event.pointerId)
}
function moveDrag(event:PointerEvent){
  if (!drag.active || drag.pointer!==event.pointerId || !frame.value) return
  const rect=frame.value.getBoundingClientRect()
  const parent=frame.value.closest('.desktop')?.getBoundingClientRect()
  if (!parent) return
  const dx=drag.x+event.clientX-drag.startX-offset.x
  const dy=drag.y+event.clientY-drag.startY-offset.y
  offset.x += Math.max(parent.left+4-rect.left,Math.min(parent.right-4-rect.right,dx))
  offset.y += Math.max(parent.top+12-rect.top,Math.min(parent.bottom-55-rect.bottom,dy))
}
function stopDrag(event:PointerEvent){
  if (drag.pointer!==event.pointerId) return
  drag.active=false
  drag.pointer=-1
}
</script>
<template>
  <section v-if="shown" ref="frame" class="os-window" :class="['win-'+id,{focused:active===id,maximized}]" :style="style" :aria-label="title" @pointerdown="open(id)">
    <header class="window-bar" @pointerdown="startDrag" @pointermove="moveDrag" @pointerup="stopDrag" @pointercancel="stopDrag">
      <span class="lights" aria-hidden="true"><i/><i/><i/></span>
      <strong>{{title}}</strong>
      <button class="window-maximize" type="button" :aria-label="maximized ? (locale==='ca' ? 'Restaura '+title : locale==='es' ? 'Restaurar '+title : 'Restore '+title) : (locale==='ca' ? 'Maximitza '+title : locale==='es' ? 'Maximizar '+title : 'Maximize '+title)" :title="maximized ? (locale==='es' ? 'Restaurar' : locale==='ca' ? 'Restaura' : 'Restore') : (locale==='es' ? 'Maximizar' : locale==='ca' ? 'Maximitza' : 'Maximize')" @pointerdown.stop @click.stop="toggleMaximize">{{ maximized ? '❐' : '□' }}</button>
      <button class="window-close" type="button" :aria-label="locale==='ca' ? 'Tanca '+title : locale==='es' ? 'Cerrar '+title : 'Close '+title" @pointerdown.stop @click.stop="close(id)">×</button>
    </header>
    <div class="window-body"><slot/></div>
  </section>
</template>
