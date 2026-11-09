<script setup lang="ts">
defineProps<{name:string;size?:number}>()
const normalized = computed(() => name.toLowerCase())
const kind = computed(() => {
 const n=normalized.value
 if(n.includes('nuxt'))return 'nuxt'
 if(n.includes('vue'))return 'vue'
 if(n.includes('typescript'))return 'typescript'
 if(n.includes('javascript'))return 'javascript'
 if(n.includes('pinia')||n.includes('vuex'))return 'pinia'
 if(n.includes('tailwind'))return 'tailwind'
 if(n.includes('git'))return 'git'
 if(n.includes('jest'))return 'jest'
 if(n.includes('scss'))return 'scss'
 if(n.includes('html'))return 'html'
 if(n.includes('storybook'))return 'storybook'
 if(n.includes('ci/cd'))return 'ci'
 return 'code'
})
</script>
<template>
 <svg class="tech-pixel-icon" :width="size ?? 18" :height="size ?? 18" viewBox="0 0 24 24" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" shape-rendering="crispEdges">
  <g v-if="kind==='vue'"><path d="M1 3h6l5 8 5-8h6L12 22z" fill="#41b883"/><path d="M7 3h4l1 2 1-2h4l-5 9z" fill="#35495e"/></g>
  <g v-else-if="kind==='nuxt'"><path d="M1 19L9 4h4l9 15z" fill="#00dc82"/><path d="M10 19l5-10 7 10z" fill="#087f5b"/><path d="M6 17h12v2H6z" fill="#103326"/></g>
  <g v-else-if="kind==='typescript'"><rect width="22" height="22" x="1" y="1" rx="1" fill="#3178c6"/><path d="M4 7h11v3h-4v9H8v-9H4z" fill="#fff"/><path d="M15 15h4v2h-4zM16 12h3v2h-3z" fill="#fff"/></g>
  <g v-else-if="kind==='javascript'"><rect x="1" y="1" width="22" height="22" fill="#f7df1e"/><path d="M11 5h4v12l-3 3-4-2v-3h3zM17 15h4v3l-2 2h-4v-3h2z" fill="#1c1c1c"/></g>
  <g v-else-if="kind==='pinia'"><path d="M11 8h3v12h-3zM9 15h7v6H9z" fill="#dfd342"/><path d="M8 3h2v9H8zM16 2h2v9h-2z" fill="#72a7e3"/><path d="M6 9h4v4H6zM16 8h4v4h-4z" fill="#f6bf44"/><path d="M10 20h6v2h-6z" fill="#76538d"/></g>
  <g v-else-if="kind==='tailwind'"><path d="M2 10c2-5 6-5 9-2 2 2 3 2 5-1h6c-3 6-7 6-11 3-2-1-3-1-5 1zM2 17c2-5 6-5 9-2 2 2 3 2 5-1h6c-3 6-7 6-11 3-2-1-3-1-5 1z" fill="#38bdf8"/></g>
  <g v-else-if="kind==='git'"><path d="M12 1L23 12 12 23 1 12z" fill="#f05032"/><path d="M8 8h3v8H8zM8 10h8v3H8z" fill="#fff"/><rect x="7" y="6" width="3" height="3" fill="#fff"/><rect x="14" y="10" width="3" height="3" fill="#fff"/></g>
  <g v-else-if="kind==='jest'"><path d="M4 17l5-8 4 7 4-9 4 13H3z" fill="#c21325"/><rect x="5" y="19" width="15" height="3" fill="#9a2335"/><path d="M15 2h5v4h-5z" fill="#c21325"/></g>
  <g v-else-if="kind==='html'"><path d="M2 1h20l-2 20-8 2-8-2z" fill="#e44d26"/><path d="M12 3h8l-2 16-6 2z" fill="#f16529"/><path d="M6 6h12v3H9v3h9v3l-2 4-4 1-4-1v-4h3v2l2 1 2-1v-2H6z" fill="#fff"/></g>
  <g v-else-if="kind==='scss'"><path d="M4 16c-1-6 5-13 13-13 4 0 5 4 1 7-2 2-5 3-8 5l5 5-3 2-5-5z" fill="#cc6699"/></g>
  <g v-else-if="kind==='storybook'"><rect x="4" y="2" width="16" height="20" rx="1" fill="#ff4785"/><path d="M9 6h7v3h-4v2h4v6H8v-3h5v-1H9z" fill="#fff"/></g>
  <g v-else-if="kind==='ci'"><path d="M4 3h16v4H4zM2 10h12v4H2zM10 17h12v4H10z" fill="#2c62ef"/><rect x="6" y="4" width="2" height="2" fill="#fff"/><rect x="4" y="11" width="2" height="2" fill="#fff"/></g>
  <g v-else><path d="M8 5L2 12l6 7 2-3-4-4 4-4zM16 5l6 7-6 7-2-3 4-4-4-4zM13 3h3l-5 18H8z" fill="#2869ef"/></g>
 </svg>
</template>
