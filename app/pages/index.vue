<script setup lang="ts">
const {locale,t}=useI18n()
const {opened,theme,open}=useDesktop()
const projects=[
  {id:'cue',name:'Cuebooker',glyph:'▂▅█▅▂',url:'https://cuebooker.com'},
  {id:'friends',name:'Friends Invisible',glyph:'▣',url:''},
  {id:'dj',name:'Cuebooker DJ',glyph:'◉',url:''}
]
const icons=[{id:'projects',glyph:'▣'},{id:'services',glyph:'▤'},{id:'about',glyph:'▧'},{id:'contact',glyph:'✉'},{id:'audio',glyph:'♫'}] as const
const audio=ref<HTMLAudioElement>()
const track=ref('')
let audioUrl:string|undefined
function loadAudio(event:Event){const f=(event.target as HTMLInputElement).files?.[0];if(!f||!f.type.startsWith('audio/'))return;if(audioUrl)URL.revokeObjectURL(audioUrl);audioUrl=URL.createObjectURL(f);track.value=f.name;if(audio.value)audio.value.src=audioUrl}
onBeforeUnmount(()=>{if(audioUrl)URL.revokeObjectURL(audioUrl)})
useHead(()=>({htmlAttrs:{lang:locale.value},bodyAttrs:{class:'theme-'+theme.value}}))
</script>
<template>
<main class="os-shell" :class="'theme-'+theme">
  <div class="crt"><div class="desktop">
    <header class="menu"><button class="brand" @click="open('terminal')">▣ Carles Far OS</button>
      <nav aria-label="Navegación"><button @click="open('projects')">{{t('projects')}}</button><button @click="open('services')">{{t('services')}}</button><button @click="open('about')">{{t('about')}}</button><button @click="open('contact')">{{t('contact')}}</button></nav>
      <div class="system"><button @click="open('audio')" aria-label="Audio">♫</button><button @click="theme=theme==='dark'?'light':'dark'" aria-label="Cambiar tema">{{theme==='dark'?'☾':'☼'}}</button><select v-model="locale" aria-label="Idioma"><option value="ca">CAT</option><option value="es">ES</option><option value="en">EN</option></select></div>
    </header>
    <div class="wallpaper" aria-hidden="true"><div class="sun"/><div class="mountains far"/><div class="mountains near"/></div>
    <aside class="desktop-shortcuts"><button v-for="item in icons" :key="item.id" @click="open(item.id)"><span class="shortcut-pixel">{{item.glyph}}</span><span>{{t(item.id)}}</span></button></aside>
    <OsWindow id="terminal" title="Terminal"><OsTerminal/></OsWindow>
    <OsWindow id="about" :title="t('about')"><div class="about-layout"><div class="portrait" role="img" aria-label="Retrato pixelado pendiente de integrar">CF</div><div><h1>Carles Far</h1><strong>Frontend Engineer / Product Builder</strong><p>{{t('intro')}}</p><mark>→ {{t('skill')}}</mark><mark>→ {{t('hobby')}}</mark></div></div></OsWindow>
    <OsWindow id="projects" :title="t('projects')"><div class="project-grid"><article v-for="p in projects" :key="p.id" class="project" :class="'project-'+p.id"><div class="glyph">{{p.glyph}}</div><h2>{{p.name}}</h2><p>{{t(p.id)}}</p><a v-if="p.url" :href="p.url" target="_blank" rel="noopener noreferrer">↗ {{t('projects')}}</a><span v-else>En desarrollo</span></article></div></OsWindow>
    <div class="note"><OsServices/></div>
    <OsWindow id="contact" :title="t('contact')"><OsContact/></OsWindow>
    <OsWindow id="services" :title="t('services')"><OsServices/></OsWindow>
    <OsWindow id="audio" :title="t('audio')"><div class="music"><span class="record">◉</span><label>{{t('load')}}<input type="file" accept="audio/*" @change="loadAudio"/></label><p>{{track}}</p><audio ref="audio" controls preload="none"/></div></OsWindow>
  </div></div>
</main>
</template>
