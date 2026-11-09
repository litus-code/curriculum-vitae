<script setup lang="ts">
import type { WindowId } from '~/domain/os'
const { locale, t } = useI18n()
const { theme, opened, open, recentlyClosed, restore, emptyTrash } = useDesktop()
const desktopInitialized = ref(false)
const mobileWelcome = ref(false)
onMounted(() => {
  // A fresh mobile visit opens on the sticky note; desktop keeps its terminal.
  mobileWelcome.value = window.innerWidth <= 800
  if (mobileWelcome.value) {
    opened.value = []
  }
  desktopInitialized.value = true
})
const projects = [
  { id:'cue', name:'Cuebooker', icon:'wave', url:'https://cuebooker.com' },
  { id:'friends', name:'Friends Invisible', icon:'gift', url:'' },
  { id:'dj', name:'Cuebooker DJ', icon:'turntable', url:'' }
]
const desktopIcons = [
  { id:'projects', icon:'computer' },
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
const portraitUrl = assetsBase + 'portrait-carles-retro-silver.webp'
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
const systemClock = ref('')
let systemClockTimer: ReturnType<typeof setInterval> | undefined
function updateSystemClock() {
  if (!import.meta.client) return
  const language = locale.value === 'ca' ? 'ca-ES' : locale.value === 'en' ? 'en-GB' : 'es-ES'
  systemClock.value = new Intl.DateTimeFormat(language, {
    weekday:'short', day:'2-digit', month:'short', hour:'2-digit', minute:'2-digit',
    hour12:false
  }).format(new Date())
}
onMounted(() => { updateSystemClock(); systemClockTimer = setInterval(updateSystemClock, 30000) })
watch(locale, updateSystemClock)
onBeforeUnmount(() => { if (systemClockTimer) clearInterval(systemClockTimer) })
useHead(() => ({ htmlAttrs:{ lang:locale.value }, title:'Carles Far OS · Frontend & Product Creator' }))
</script>

<template>
  <main class="os-shell" :class="[isNight ? 'theme-night' : 'theme-sunset', { 'os-initialized': desktopInitialized, 'os-mobile-welcome': mobileWelcome && opened.length === 0 }]">
    <div class="crt"><div class="desktop">
      <footer class="menu os-taskbar">
        <button class="brand" type="button" @click="open('terminal')"><RetroIcon name="computer" :size="23" /> <span>Carles Far OS</span></button>
        <nav class="os-taskbar-nav" aria-label="System menu">
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
          <time class="os-taskbar-clock" aria-label="Hora local">{{ systemClock }}</time>
        </div>
      </footer>
      <div class="wallpaper" :class="{ 'wallpaper-approved': wallpaperReady }" aria-hidden="true">
        <img v-if="wallpaperReady" class="wallpaper-image" :src="currentWallpaperUrl" :class="{ 'wallpaper-hd': !wallpaperFallback }" alt="" width="1536" height="1024" decoding="async" fetchpriority="high" @error="wallpaperError" />
        <div class="pixel-stars"></div><div class="pixel-cloud cloud-a"></div><div class="pixel-cloud cloud-b"></div>
        <div class="celestial"></div><div class="ridge ridge-far"></div><div class="ridge ridge-near"></div>
      </div>
      <aside class="desktop-shortcuts" :aria-label="t('projects')">
        <button v-for="item in desktopIcons" :key="item.id" type="button" @click="open(item.id as WindowId)" :title="t(item.id)">
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
            <span v-else class="project-construction"><CareerPixelIcon name="construction" :size="23" />{{ locale === 'en' ? 'Under construction' : locale === 'ca' ? 'En construcció' : 'En construcción' }}</span>
          </article>
        </div>
      </OsWindow>
      <div class="note"><OsServices /></div>
      <OsWindow id="cv" :title="locale === 'en' ? 'Curriculum Vitae' : 'Currículum Vitae'"><OsCv /></OsWindow>
      <OsWindow id="contact" :title="t('contact')"><OsContact /></OsWindow>
      <OsWindow id="services" :title="t('services')"><OsServices /></OsWindow>
      <OsWindow id="trash" :title="t('trash')">
        <div class="os-trash">
          <RetroIcon name="trash" :size="57" />
          <h2>{{ locale==='ca' ? 'Finestres tancades' : locale==='en' ? 'Recently closed windows' : 'Ventanas cerradas' }}</h2>
          <p>{{ locale==='ca' ? 'Recupera una finestra tancada des d’aquí.' : locale==='en' ? 'Reopen a window you closed earlier.' : 'Recupera una ventana que hayas cerrado antes.' }}</p>
          <div v-if="recentlyClosed.length" class="os-trash-list">
            <button v-for="id in recentlyClosed" :key="id" type="button" @click="restore(id)">
              <RetroIcon :name="id==='cv' ? 'floppy' : id==='about' ? 'paper' : id==='contact' ? 'mail' : id==='projects' ? 'computer' : id==='audio' ? 'turntable' : 'folder'" :size="29" />
              <span>{{ id==='terminal' ? 'Terminal' : id==='cv' ? 'CV' : t(id) }}</span>
              <span aria-hidden="true">↗</span>
            </button>
          </div>
          <p v-else class="os-trash-empty">{{ locale==='ca' ? 'No hi ha finestres per recuperar.' : locale==='en' ? 'No windows to restore.' : 'No hay ventanas para recuperar.' }}</p>
          <button v-if="recentlyClosed.length" class="os-trash-clear" type="button" @click="emptyTrash">
            {{ locale==='ca' ? 'Buidar historial' : locale==='en' ? 'Clear history' : 'Vaciar historial' }}
          </button>
          <small>{{ locale==='ca' ? 'No s’eliminen fitxers ni dades.' : locale==='en' ? 'No files or personal data are deleted.' : 'No se eliminan archivos ni datos personales.' }}</small>
        </div>
      </OsWindow>
      <OsWindow id="audio" :title="t('audio')">
        <div class="music"><RetroIcon name="turntable" :size="84" />
          <label>{{ t('load') }}<input type="file" accept="audio/*" @change="loadAudio" /></label>
          <p>{{ track }}</p><audio ref="audio" controls preload="none" />
        </div>
      </OsWindow>
    </div></div>
  </main>
</template>
