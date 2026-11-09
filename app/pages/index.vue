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
  { id:'cv', icon:'floppy' },
  { id:'trash', icon:'trash' }
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
onMounted(() => {
  const savedTheme = localStorage.getItem('carlesfar-os-theme')
  if (savedTheme === 'dark' || savedTheme === 'light') theme.value = savedTheme
  const savedLocale = localStorage.getItem('carlesfar-os-locale')
  if (savedLocale === 'ca' || savedLocale === 'es' || savedLocale === 'en') locale.value = savedLocale
})
watch(theme, value => { if (import.meta.client) localStorage.setItem('carlesfar-os-theme', value) })
watch(locale, value => { if (import.meta.client) localStorage.setItem('carlesfar-os-locale', value) })
const assetsBase = useRuntimeConfig().app.baseURL
const portraitUrl = assetsBase + 'portrait-carles-pixel.png'
const isNight = computed(() => theme.value === 'dark')
const wallpaperUrl = computed(() => assetsBase + (isNight.value ? 'wallpapers/night-hd.webp' : 'wallpapers/sunset-hd.webp'))
const wallpaperFallbackUrl = computed(() => assetsBase + (isNight.value ? 'wallpapers/night.webp' : 'wallpapers/sunset.webp'))
const wallpaperReady = ref(true)
const wallpaperFallback = ref(false)
const currentWallpaperUrl = computed(() => wallpaperFallback.value ? wallpaperFallbackUrl.value : wallpaperUrl.value)
watch(isNight, () => { wallpaperReady.value = true; wallpaperFallback.value = false })
function wallpaperError() {
  if (!wallpaperFallback.value) wallpaperFallback.value = true
  else wallpaperReady.value = false
}
const toggleTheme = () => { theme.value = isNight.value ? 'light' : 'dark' }
useHead(() => ({ htmlAttrs:{ lang:locale.value }, title:'Carles Far OS · Frontend & Product Creator' }))
</script>

<template>
  <main class="os-shell" :class="isNight ? 'theme-night' : 'theme-sunset'">
    <div class="crt"><div class="desktop">
      <header class="menu">
        <button class="brand" type="button" @click="open('terminal')"><RetroIcon name="computer" :size="23" /> <span>Carles Far OS</span></button>
        <nav aria-label="System menu">
          <button type="button" @click="open('projects')">{{ t('fileMenu') }}</button>
          <button type="button" @click="open('services')">{{ t('editMenu') }}</button>
          <button type="button" @click="open('about')">{{ t('viewMenu') }}</button>
          <button type="button" @click="open('contact')">{{ t('goMenu') }}</button>
          <button type="button" @click="open('terminal')">{{ t('helpMenu') }}</button>
        </nav>
        <div class="system">
          <button type="button" :aria-label="t('audio')" @click="open('audio')"><RetroIcon name="record" :size="22" /></button>
          <button class="theme-switch" type="button" :aria-label="isNight ? t('sunsetMode') : t('nightMode')" :title="isNight ? t('sunsetMode') : t('nightMode')" @click="toggleTheme"><RetroIcon :name="isNight ? 'sun' : 'moon'" :size="22" /></button>
          <select v-model="locale" :aria-label="t('language')"><option value="ca">CAT</option><option value="es">ES</option><option value="en">EN</option></select>
        </div>
      </header>
      <div class="wallpaper" :class="{ 'wallpaper-approved': wallpaperReady }" aria-hidden="true">
        <img v-if="wallpaperReady" class="wallpaper-image" :src="currentWallpaperUrl" :class="{ 'wallpaper-hd': !wallpaperFallback }" alt="" width="1536" height="1024" decoding="async" fetchpriority="high" @error="wallpaperError" />
        <div class="pixel-stars"></div><div class="pixel-cloud cloud-a"></div><div class="pixel-cloud cloud-b"></div>
        <div class="celestial"></div><div class="ridge ridge-far"></div><div class="ridge ridge-near"></div>
      </div>
      <aside class="desktop-shortcuts" :aria-label="t('projects')">
        <button v-for="item in desktopIcons" :key="item.id" type="button" @click="item.id === 'cv' || item.id === 'trash' ? undefined : open(item.id as WindowId)" :title="item.id === 'cv' || item.id === 'trash' ? 'Próximamente' : t(item.id)" :aria-disabled="item.id === 'cv' || item.id === 'trash'">
          <RetroIcon :name="item.icon" :size="53" />
          <span>{{ t(item.id) }}</span>
        </button>
      </aside>
      <OsWindow id="terminal" title="Terminal – carles@far:~"><OsTerminal /></OsWindow>
      <OsWindow id="about" :title="t('about')"><OsAbout :portrait-url="portraitUrl" :portrait-alt="t('portraitAlt')" /></OsWindow>
      <OsWindow id="projects" :title="t('projects')">
        <div class="project-grid">
          <article v-for="p in projects" :key="p.id" class="project" :class="'project-'+p.id">
            <RetroIcon :name="p.icon" :size="66" />
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
        <div class="music"><RetroIcon name="turntable" :size="84" />
          <label>{{ t('load') }}<input type="file" accept="audio/*" @change="loadAudio" /></label>
          <p>{{ track }}</p><audio ref="audio" controls preload="none" />
        </div>
      </OsWindow>
    </div></div>
  </main>
</template>
