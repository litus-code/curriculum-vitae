<script setup lang="ts">
defineProps<{ portraitUrl: string; portraitAlt: string }>()
const { locale } = useI18n()
type AboutTab = 'intro' | 'experience' | 'education' | 'hobbies'
const tab = ref<AboutTab>('intro')
const tabIds: AboutTab[] = ['intro','experience','education','hobbies']
const translations = {
  es: {
    heading: 'Frontend Developer & Independent Product Builder',
    summary: 'Desarrollo productos digitales, interfaces complejas y experiencias que funcionan.',
    years: '10 años de experiencia en desarrollo frontend',
    tabs: ['Quién soy','Experiencia','Formación','Hobbies'],
    hello: 'Hola, soy Carles.',
    bio1: 'Desarrollador frontend de Barcelona, curioso, creativo y apasionado por la tecnología, la música y los productos digitales.',
    bio2: 'Me gusta construir aplicaciones con identidad propia, cuidar los detalles de las interfaces y convertir ideas en productos reales.',
    location: 'Barcelona', music: 'Música', products: 'Producto',
    tech: 'Tecnologías principales', own: 'Proyectos propios',
    cue: 'Gestión de bookings para DJs y agencias.',
    friends: 'Amigo invisible online.',
    dj: 'Software de mezcla y herramientas DJ.',
    experience: 'Experiencia profesional',
    current: 'Actualidad', ey: 'Lead Frontend · Proyecto Radisson Hotels',
    bershka: 'Senior Frontend Developer · Bershka, Inditex',
    experienceDetail: 'Vue, Nuxt, TypeScript, SSR y desarrollo de interfaces para productos digitales.',
    previousEy: 'Senior Frontend Developer · EY Barcelona',
    education: 'Formación académica y técnica',
    educationNote: 'Centros y periodos documentados. Titulaciones pendientes de confirmar.',
    hobbies: 'Más allá del código',
    hobby1: 'Música electrónica, cultura DJ y experimentación con software musical.',
    hobby2: 'Cine de terror, arte, diseño retro y proyectos creativos.',
    hobby3: 'Me gusta explorar nuevas ideas y construir mis propias herramientas.'
  },
  ca: {
    heading: 'Frontend Developer & Independent Product Builder',
    summary: 'Desenvolupo productes digitals, interfícies complexes i experiències que funcionen.',
    years: '10 anys d’experiència en desenvolupament frontend',
    tabs: ['Qui soc','Experiència','Formació','Aficions'],
    hello: 'Hola, soc en Carles.',
    bio1: 'Desenvolupador frontend de Barcelona, curiós, creatiu i apassionat per la tecnologia, la música i els productes digitals.',
    bio2: 'M’agrada construir aplicacions amb identitat pròpia, cuidar els detalls de les interfícies i convertir idees en productes reals.',
    location: 'Barcelona', music: 'Música', products: 'Producte',
    tech: 'Tecnologies principals', own: 'Projectes propis',
    cue: 'Gestió de bookings per a DJs i agències.',
    friends: 'Amic invisible en línia.',
    dj: 'Software de mescla i eines DJ.',
    experience: 'Experiència professional',
    current: 'Actualitat', ey: 'Lead Frontend · Projecte Radisson Hotels',
    bershka: 'Senior Frontend Developer · Bershka, Inditex',
    experienceDetail: 'Vue, Nuxt, TypeScript, SSR i desenvolupament d’interfícies per a productes digitals.',
    previousEy: 'Senior Frontend Developer · EY Barcelona',
    education: 'Formació acadèmica i tècnica',
    educationNote: 'Centres i períodes documentats. Titulacions pendents de confirmar.',
    hobbies: 'Més enllà del codi',
    hobby1: 'Música electrònica, cultura DJ i experimentació amb software musical.',
    hobby2: 'Cinema de terror, art, disseny retro i projectes creatius.',
    hobby3: 'M’agrada explorar idees noves i construir les meves eines.'
  },
  en: {
    heading: 'Frontend Developer & Independent Product Builder',
    summary: 'I build digital products, complex interfaces and experiences that work.',
    years: '10 years of frontend development experience',
    tabs: ['About me','Experience','Education','Hobbies'],
    hello: 'Hi, I’m Carles.',
    bio1: 'Barcelona-based frontend developer, curious and creative, with a passion for technology, music and digital products.',
    bio2: 'I enjoy building apps with their own personality, refining interface details and turning ideas into working products.',
    location: 'Barcelona', music: 'Music', products: 'Products',
    tech: 'Main technologies', own: 'Personal projects',
    cue: 'Booking management for DJs and agencies.',
    friends: 'Online Secret Santa.',
    dj: 'DJ mixing software and tools.',
    experience: 'Professional experience',
    current: 'Present', ey: 'Lead Frontend · Radisson Hotels project',
    bershka: 'Senior Frontend Developer · Bershka, Inditex',
    experienceDetail: 'Vue, Nuxt, TypeScript, SSR and interface development for digital products.',
    previousEy: 'Senior Frontend Developer · EY Barcelona',
    education: 'Education and training',
    educationNote: 'Schools and dates confirmed. Qualifications to be verified.',
    hobbies: 'Outside of coding',
    hobby1: 'Electronic music, DJ culture and experiments with music software.',
    hobby2: 'Horror cinema, art, retro design and creative projects.',
    hobby3: 'I like exploring new ideas and building my own tools.'
  }
} as const
const copy = computed(() => translations[locale.value as keyof typeof translations] ?? translations.es)
const schools = [
  { dates: '2019–2020', name: 'Campus MVP' },
  { dates: '2016–2017', name: 'ISDI Coders' },
  { dates: '2013–2017', name: 'STUCOM' },
  { dates: '2012–2013', name: 'Universitat de Barcelona' }
]
const tech = ['Vue 3','Nuxt 4','TypeScript','Pinia','Tailwind','Jest','SSR','Git','CI/CD']
const projects = [
  {name:'Cuebooker',desc:'cue',url:'https://cuebooker.com'},
  {name:'Friends Invisible',desc:'friends',url:''},
  {name:'Cuebooker DJ',desc:'dj',url:''}
] as const
</script>

<template>
  <div class="about-os">
    <div class="about-os-hero">
      <div class="about-os-portrait-frame"><img class="about-os-portrait" :src="portraitUrl" :alt="portraitAlt" width="112" height="112" /></div>
      <div class="about-os-identity">
        <h1>Carles Far</h1>
        <h2>{{ copy.heading }}</h2>
        <p>{{ copy.summary }}</p>
        <strong class="about-os-years">→ {{ copy.years }}</strong>
      </div>
      <div class="about-os-mac" aria-hidden="true">
        <span class="about-os-mac-rays">✦</span>
        <RetroIcon name="computer" :size="102" />
      </div>
    </div>
    <div class="about-os-tabs" role="tablist" :aria-label="locale === 'en' ? 'About sections' : locale === 'ca' ? 'Seccions' : 'Secciones'">
      <button v-for="(id,i) in tabIds" :key="id" type="button" role="tab"
        :aria-selected="tab === id" :tabindex="tab === id ? 0 : -1"
        :class="{ selected: tab === id }" @click="tab = id"
        @keydown.left.prevent="tab = tabIds[(i+3)%4]!"
        @keydown.right.prevent="tab = tabIds[(i+1)%4]!">
        <span class="about-os-tab-icon" aria-hidden="true">{{ ['♙','▣','◇','✣'][i] }}</span>{{ copy.tabs[i] }}
      </button>
    </div>
    <div class="about-os-content" role="tabpanel">
      <template v-if="tab === 'intro'">
        <div class="about-os-intro">
          <div class="about-os-bio">
            <h3>{{ copy.hello }}</h3><div class="about-os-underline"></div>
            <p>{{ copy.bio1 }}</p><p>{{ copy.bio2 }}</p>
            <div class="about-os-tags"><span>⌖ {{ copy.location }}</span><span>▣ Frontend</span><span>♫ {{ copy.music }}</span><span>♡ {{ copy.products }}</span></div>
          </div>
          <div class="about-os-side">
            <section class="about-os-panel"><h4><span>&lt;/&gt;</span> {{ copy.tech }}</h4>
              <div class="about-os-tech"><span v-for="item in tech" :key="item">{{ item }}</span></div>
            </section>
            <section class="about-os-panel"><h4><span>↗</span> {{ copy.own }}</h4>
              <ul class="about-os-projects"><li v-for="project in projects" :key="project.name">
                <i aria-hidden="true"></i>
                <a v-if="project.url" :href="project.url" target="_blank" rel="noopener noreferrer">{{ project.name }}</a>
                <strong v-else>{{ project.name }}</strong>
                <span> · {{ copy[project.desc] }}</span>
              </li></ul>
            </section>
          </div>
        </div>
      </template>
      <template v-else-if="tab === 'experience'">
        <h3>{{ copy.experience }}</h3>
        <div class="about-os-timeline">
          <article><span>2026 → {{ copy.current }}</span><h4>EY · Radisson Hotels</h4><p>{{ copy.ey }}</p><small>{{ copy.experienceDetail }}</small></article>
          <article><span>2026</span><h4>Inditex · Bershka</h4><p>{{ copy.bershka }}</p></article>
          <article><span>2021–2025</span><h4>EY Barcelona</h4><p>{{ copy.previousEy }}</p></article>
          <article><span>2020–2021</span><h4>T2CLIENT</h4></article>
          <article><span>2020</span><h4>CONEPTUM AI</h4></article>
          <article><span>2017–2019</span><h4>CASALS ONLINE</h4></article>
        </div>
      </template>
      <template v-else-if="tab === 'education'">
        <h3>{{ copy.education }}</h3>
        <div class="about-os-schoolgrid"><article v-for="school in schools" :key="school.name"><span>{{ school.dates }}</span><h4>{{ school.name }}</h4></article></div>
        <p class="about-os-education-note">{{ copy.educationNote }}</p>
      </template>
      <template v-else>
        <h3>{{ copy.hobbies }}</h3>
        <div class="about-os-hobbygrid">
          <article><span>♫</span><p>{{ copy.hobby1 }}</p></article>
          <article><span>✧</span><p>{{ copy.hobby2 }}</p></article>
          <article><span>⌘</span><p>{{ copy.hobby3 }}</p></article>
        </div>
      </template>
    </div>
  </div>
</template>
