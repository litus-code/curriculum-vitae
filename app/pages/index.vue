<script setup lang="ts">
import type { WindowId } from '~/domain/os'
const { locale, t } = useI18n()
const { theme, open } = useDesktop()
const projects = [
  { id:'cue', name:'Cuebooker', icon:'wave', url:'https://cuebooker.com' },
  { id:'friends', name:'Friends Invisible', icon:'gift', url:'' },
  { id:'dj', name:'Cuebooker DJ', icon:'turntable', url:'' }
]
const desktopIcons = [
  { id:'projects', icon:'computer' },
  { id:'services', icon:'folder' },
  { id:'about', icon:'paper' },
  { id:'contact', icon:'mail' },
  { id:'audio', icon:'record' }
] as const
const audio = ref<HTMLAudioElement>()
const track = ref('')
let audioUrl: string | undefined
function loadAudio(event:Event) {
  const f = (event.target as HTMLInputElement).files?.[0]
  if (!f || !f.type.startsWith('audio/')) return
  if (audioUrl) URL.revokeObjectURL(audioUrl)
  audioUrl = URL.createObjectURL(f)
  track.value = f.name
  if (audio.value) audio.value.src = audioUrl
}
onBeforeUnmount(() => { if (audioUrl) URL.revokeObjectURL(audioUrl) })
const portraitUrl = useRuntimeConfig().app.baseURL + 'portrait-carles-pixel.png'
const isNight = computed(() => theme.value === 'dark')
const toggleTheme = () => { theme.value = isNight.value ? 'light' : 'dark' }
useHead(() => ({ htmlAttrs:{ lang:locale.value }, title:'Carles Far OS · Frontend & Product Creator' }))
</script>

<template>
  <main class="os-shell" :class="isNight ? 'theme-night' : 'theme-sunset'">
    <div class="crt"><div class="desktop">
      <header class="menu">
        <button class="brand" type="button" @click="open('terminal')"><PixelIcon name="computer" :size="23" /> <span>Carles Far OS</span></button>
        <nav :aria-label="t('projects')">
          <button type="button" @click="open('projects')">{{ t('projects') }}</button>
          <button type="button" @click="open('services')">{{ t('services') }}</button>
          <button type="button" @click="open('about')">{{ t('about') }}</button>
          <button type="button" @click="open('contact')">{{ t('contact') }}</button>
        </nav>
        <div class="system">
          <button type="button" :aria-label="t('audio')" @click="open('audio')"><PixelIcon name="record" :size="22" /></button>
          <button class="theme-switch" type="button" :aria-label="isNight ? 'Sunset' : 'Night'" :title="isNight ? 'Sunset' : 'Night'" @click="toggleTheme"><PixelIcon :name="isNight ? 'sun' : 'moon'" :size="22" /></button>
          <select v-model="locale" aria-label="Language"><option value="ca">CAT</option><option value="es">ES</option><option value="en">EN</option></select>
        </div>
      </header>
      <div class="wallpaper" aria-hidden="true">
        <div class="pixel-stars"></div><div class="pixel-cloud cloud-a"></div><div class="pixel-cloud cloud-b"></div>
        <div class="celestial"></div><div class="ridge ridge-far"></div><div class="ridge ridge-near"></div>
      </div>
      <aside class="desktop-shortcuts" :aria-label="t('projects')">
        <button v-for="item in desktopIcons" :key="item.id" type="button" @click="open(item.id as WindowId)">
          <PixelIcon :name="item.icon" :size="53" />
          <span>{{ t(item.id) }}</span>
        </button>
      </aside>
      <OsWindow id="terminal" title="Terminal – carles@far:~"><OsTerminal /></OsWindow>
      <OsWindow id="about" :title="t('about')">
        <div class="about-layout">
          <img class="portrait"  :src="portraitUrl" alt="Carles Far, retrato pixelado con gafas amarillas" width="240" height="240" />
          <div class="about-copy">
            <h1>Carles Far</h1>
            <strong>Frontend Engineer /<br> Product Creator</strong>
            <p>{{ t('intro') }}</p>
            <mark>→ {{ t('skill') }}</mark>
            <mark>→ Product builder</mark>
            <mark>→ {{ t('hobby') }}</mark>
          </div>
        </div>
      </OsWindow>
      <OsWindow id="projects" :title="t('projects')">
        <div class="project-grid">
          <article v-for="p in projects" :key="p.id" class="project" :class="'project-'+p.id">
            <PixelIcon :name="p.icon" :size="66" />
            <h2>{{ p.name }}</h2>
            <p>{{ t(p.id) }}</p>
            <a v-if="p.url" :href="p.url" target="_blank" rel="noopener noreferrer">{{ t('projects') }} ↗</a>
            <span v-else>{{ locale === 'en' ? 'In development' : locale === 'ca' ? 'En desenvolupament' : 'En desarrollo' }}</span>
          </article>
        </div>
      </OsWindow>
      <div class="note"><OsServices /></div>
      <OsWindow id="contact" :title="t('contact')"><OsContact /></OsWindow>
      <OsWindow id="services" :title="t('services')"><OsServices /></OsWindow>
      <OsWindow id="audio" :title="t('audio')">
        <div class="music"><PixelIcon name="turntable" :size="84" />
          <label>{{ t('load') }}<input type="file" accept="audio/*" @change="loadAudio" /></label>
          <p>{{ track }}</p><audio ref="audio" controls preload="none" />
        </div>
      </OsWindow>
    </div></div>
  </main>
</template>
