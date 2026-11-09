<script setup lang="ts">
import type { WindowId } from '~/domain/os'
const props=defineProps<{id:WindowId;title:string}>()
const {opened,active,open,close}=useDesktop()
const shown=computed(()=>opened.value.includes(props.id))
const frame=ref<HTMLElement>()
const offset=reactive({x:0,y:0})
const drag=reactive({active:false,pointer:-1,startX:0,startY:0,x:0,y:0})
const style=computed(()=>({zIndex:30 + opened.value.indexOf(props.id),transform:`translate(${offset.x}px, ${offset.y}px)`}))
function startDrag(event:PointerEvent){
  if (!import.meta.client || window.innerWidth<=800 || event.button!==0 || (event.target as HTMLElement).closest('button')) return
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
  offset.y += Math.max(parent.top+43-rect.top,Math.min(parent.bottom-4-rect.bottom,dy))
}
function stopDrag(event:PointerEvent){
  if (drag.pointer!==event.pointerId) return
  drag.active=false
  drag.pointer=-1
}
</script>
<template>
  <section v-if="shown" ref="frame" class="os-window" :class="['win-'+id,{focused:active===id}]" :style="style" :aria-label="title" @pointerdown="open(id)">
    <header class="window-bar" @pointerdown="startDrag" @pointermove="moveDrag" @pointerup="stopDrag" @pointercancel="stopDrag">
      <span class="lights" aria-hidden="true"><i/><i/><i/></span>
      <strong>{{title}}</strong>
      <button type="button" :aria-label="'Close '+title" @pointerdown.stop @click.stop="close(id)">×</button>
    </header>
    <div class="window-body"><slot/></div>
  </section>
</template>
