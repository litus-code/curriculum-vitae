<script setup lang="ts">
const props = withDefaults(defineProps<{name:string;size?:number}>(),{size:36})
const kind = computed(() => {
 const n=props.name.toLowerCase()
 if(n==='ey'||n.includes('radisson')) return 'ey'
 if(n.includes('inditex')||n.includes('bershka')) return 'inditex'
 if(n.includes('t2client')) return 't2'
 if(n.includes('coneptum')) return 'ai'
 if(n.includes('casals')) return 'casals'
 if(n.includes('music')||n.includes('música')||n.includes('musica')) return 'music'
 if(n.includes('gaming')||n.includes('juego')) return 'gaming'
 if(n.includes('sport')||n.includes('deporte')||n.includes('esport')) return 'sport'
 if(n.includes('paint')||n.includes('pintura')||n.includes('art')) return 'paint'
 if(n.includes('construction')||n.includes('obra')) return 'construction'
 return 'code'
})
</script>
<template>
 <svg class="career-pixel-icon" :width="props.size" :height="props.size" viewBox="0 0 48 48" xmlns="http://www.w3.org/2000/svg" role="img" :aria-label="props.name" shape-rendering="crispEdges">
  <g v-if="kind==='ey'">
   <path d="M5 9L41 2V9L5 15Z" fill="#ffe500"/>
   <path d="M6 17h36v29H6z" fill="#f7f9fe"/>
   <text x="5" y="40" fill="#11131b" font-size="27" font-family="Arial,sans-serif" font-weight="900">EY</text>
  </g>
  <g v-else-if="kind==='inditex'">
   <path d="M12 12V8h24v4" fill="none" stroke="#161a25" stroke-width="3"/>
   <path d="M6 12h36v32H6z" fill="#f0f3fa" stroke="#161a25" stroke-width="3"/>
   <path d="M9 18h30v20H9z" fill="#dce5f4"/>
   <text x="24" y="30" text-anchor="middle" fill="#101624" font-size="10" font-family="Arial,sans-serif" font-weight="900">INDITEX</text>
  </g>
  <g v-else-if="kind==='t2'">
   <rect x="4" y="19" width="5" height="12" fill="#19b4e7"/><rect x="11" y="11" width="5" height="28" fill="#0888cf"/>
   <rect x="18" y="5" width="5" height="38" fill="#46d6ee"/><rect x="25" y="13" width="5" height="24" fill="#1475d1"/>
   <rect x="32" y="8" width="5" height="32" fill="#1bbbe2"/><rect x="39" y="18" width="5" height="14" fill="#2773db"/>
  </g>
  <g v-else-if="kind==='ai'">
   <path d="M13 7h22l9 15-8 18H12L4 22Z" fill="#eef5ff" stroke="#121c36" stroke-width="3"/>
   <path d="M14 19h18M17 12v21M25 13v25M33 17v18M10 25h28" stroke="#3084f7" stroke-width="3"/>
   <rect x="15" y="9" width="5" height="5" fill="#1834a8"/><rect x="29" y="17" width="5" height="5" fill="#162b8f"/>
   <rect x="12" y="28" width="5" height="5" fill="#1b6ee2"/>
  </g>
  <g v-else-if="kind==='casals'">
   <path d="M7 34V8h34v28H7Z" fill="#f9fbff" stroke="#14223c" stroke-width="3"/>
   <path d="M11 29h5v4h-5zM18 23h5v10h-5zM25 17h5v16h-5zM32 12h5v21h-5z" fill="#2872ef"/>
   <path d="M3 38h42v5H3z" fill="#223957"/>
  </g>
  <g v-else-if="kind==='music'">
   <path d="M6 27v-8C6 3 42 3 42 19v8" fill="none" stroke="#101a32" stroke-width="5"/>
   <path d="M4 23h10v18H4zM34 23h10v18H34z" fill="#78b3ff" stroke="#14234a" stroke-width="3"/>
  </g>
  <g v-else-if="kind==='gaming'">
   <path d="M9 18h30l6 11-3 10-9-1-6-7h-6l-6 7-9 1-3-10z" fill="#f9fbff" stroke="#152449" stroke-width="3"/>
   <path d="M12 23v12M6 29h12" stroke="#101d42" stroke-width="3"/>
   <rect x="31" y="22" width="5" height="5" fill="#287dff"/><rect x="36" y="29" width="5" height="5" fill="#287dff"/>
  </g>
  <g v-else-if="kind==='sport'">
   <rect x="2" y="20" width="9" height="9" fill="#233659"/><rect x="11" y="16" width="6" height="17" fill="#75b8fa"/>
   <rect x="17" y="22" width="14" height="5" fill="#213661"/><rect x="31" y="16" width="6" height="17" fill="#75b8fa"/>
   <rect x="37" y="20" width="9" height="9" fill="#233659"/>
  </g>
  <g v-else-if="kind==='paint'">
   <path d="M9 8h21l12 12-8 13H20L9 43 3 31z" fill="#fafcff" stroke="#1c2a48" stroke-width="3"/>
   <rect x="11" y="16" width="6" height="6" fill="#ff784d"/><rect x="21" y="10" width="6" height="6" fill="#2488f5"/>
   <rect x="31" y="19" width="6" height="6" fill="#f7c844"/><path d="M21 32l22-22" stroke="#152c58" stroke-width="5"/>
  </g>
  <g v-else-if="kind==='construction'">
   <path d="M8 30v-8c0-14 32-14 32 0v8" fill="#ffd344" stroke="#172138" stroke-width="3"/>
   <path d="M20 10v16h8V10M5 28h38v6H5z" fill="#ffb72d" stroke="#172138" stroke-width="3"/>
   <rect x="7" y="37" width="34" height="5" fill="#14203a"/><rect x="11" y="37" width="6" height="5" fill="#f4cc40"/><rect x="25" y="37" width="6" height="5" fill="#f4cc40"/>
  </g>
  <g v-else><path d="M13 9L4 24l9 15M35 9l9 15-9 15M29 4L19 44" fill="none" stroke="#2765e9" stroke-width="5"/></g>
 </svg>
</template>