<script setup lang="ts">
const { locale } = useI18n()
const active = ref<'experience'|'education'|'stack'|'projects'>('experience')
const tabs = ['experience','education','stack','projects'] as const
const labels = {
  es: { experience:'Experiencia',education:'Formación',stack:'Tecnologías',projects:'Proyectos',contact:'Contacto',skills:'Competencias',download:'Descargar CV (PDF)',intro:'Frontend Lead, desarrollador web y creador de productos digitales.',summary:'10 años de experiencia frontend',history:'Trayectoria profesional',training:'Formación',detail:'Responsabilidades',schools:'Centros y estudios',built:'Productos propios',note:'La titulaciones de Campus MVP y UB están pendientes de precisar. El PDF se genera desde el navegador mediante Imprimir > Guardar como PDF.' },
  ca: { experience:'Experiència',education:'Formació',stack:'Tecnologies',projects:'Projectes',contact:'Contacte',skills:'Competències',download:'Descarregar CV (PDF)',intro:'Frontend Lead, desenvolupador web i creador de productes digitals.',summary:'10 anys d’experiència frontend',history:'Trajectòria professional',training:'Formació',detail:'Responsabilitats',schools:'Centres i estudis',built:'Productes propis',note:'Els títols de Campus MVP i UB estan pendents de concretar. El PDF es genera des del navegador amb Imprimir > Desar com a PDF.' },
  en: { experience:'Experience',education:'Education',stack:'Technologies',projects:'Projects',contact:'Contact',skills:'Skills',download:'Download CV (PDF)',intro:'Frontend Lead, web developer and independent product builder.',summary:'10 years of frontend experience',history:'Professional experience',training:'Education',detail:'Responsibilities',schools:'Schools and studies',built:'My products',note:'Campus MVP and UB qualifications need confirmation. Generate a PDF with Print > Save as PDF.' }
}
const t = computed(() => labels[locale.value as keyof typeof labels] ?? labels.es)
const roles = [
 {years:'2026 –',company:'EY / Radisson Hotels',title:'Lead Frontend',details:'Frontend lead en el proyecto Radisson Hotels, desarrollo con Nuxt, Vue, TypeScript y SSR.'},
 {years:'2025–2026',company:'Inditex / Bershka',title:'Senior Frontend Developer',details:'Mantenimiento y nuevas funcionalidades, migración a Nuxt 3 y Pinia, trabajo entre squads.'},
 {years:'2021–2025',company:'EY Barcelona',title:'Senior Frontend · Referente técnico',details:'Referente frontend del equipo AM, evolución y mantenimiento de un portal del sector turístico con Vue 2 y Nuxt.'},
 {years:'2020–2021',company:'T2CLIENT',title:'Frontend Developer · Referente de equipo',details:'Arquitectura de aplicaciones Vue 2/3 para logística, Storybook y gestión de datos JSON.'},
 {years:'2020',company:'Coneptum AI',title:'Frontend Developer',details:'Desarrollo de aplicación para el sector del ocio con Vue 2 y Vuetify.'},
 {years:'2017–2019',company:'Casals Online',title:'Junior Frontend Developer',details:'Maquetación de landing pages y desarrollo JavaScript para marketing digital.'}
]
const schools = [
 {years:'2019–2020',name:'Campus MVP',note:''},
 {years:'2016–2017',name:'ISDI Coders',note:'Bootcamp intensivo de JavaScript full stack.'},
 {years:'2013–2017',name:'STUCOM',note:'Técnico Superior en Desarrollo de Aplicaciones Web (DAW).'},
 {years:'2012–2013',name:'Universitat de Barcelona',note:''}
]
const stack = ['Vue 2 / 3','Nuxt 2 / 3 / 4','TypeScript','JavaScript','Pinia / Vuex','SSR','Tailwind','SCSS','HTML / CSS','Jest','Storybook','Git','CI/CD']
const projects = [
 {name:'Cuebooker',text:'Plataforma de gestión de bookings de DJs y agencias.',url:'https://cuebooker.com'},
 {name:'Friends Invisible',text:'Sorteos de amigo invisible, invitaciones y listas de deseos.',url:''},
 {name:'Cuebooker DJ',text:'Aplicación DJ con stems y compatibilidad MIDI.',url:''}
]
function printCv(){ if(import.meta.client) window.print() }
</script>
<template>
  <div class="cv-os">
    <div class="cv-os-head">
      <div class="cv-os-avatar"><img :src="useRuntimeConfig().app.baseURL + 'portrait-carles-pixel.png'" alt="Carles Far" width="112" height="112"/></div>
      <div class="cv-os-title">
        <h1>Carles Far</h1>
        <h2>Frontend Lead & Product Builder</h2>
        <p>{{ t.intro }}</p>
        <mark>→ {{ t.summary }}</mark>
      </div>
      <RetroIcon class="cv-os-mac" name="computer" :size="78"/>
    </div>
    <div class="cv-os-main">
      <aside class="cv-os-side">
        <section class="cv-os-box"><h3>✉ {{ t.contact }}</h3>
          <p><a href="mailto:contacto@carlesfar.com">contacto@carlesfar.com</a></p>
          <p>⌖ Barcelona</p>
          <p><a href="https://www.carlesfar.com" target="_blank" rel="noopener noreferrer">carlesfar.com</a></p>
          <p><a href="https://www.linkedin.com/in/carles-far-pierres-390160139/" target="_blank" rel="noopener noreferrer">LinkedIn ↗</a></p>
        </section>
        <section class="cv-os-box"><h3>⌘ {{ t.skills }}</h3><div class="cv-os-chips"><span v-for="tech in stack.slice(0,8)" :key="tech">{{ tech }}</span></div></section>
        <section class="cv-os-box"><h3>♫ Hobbies</h3><p>Música · DJ · Arte · Cine de terror · Deporte</p></section>
      </aside>
      <div class="cv-os-content">
        <div class="cv-os-tabs" role="tablist">
          <button v-for="id in tabs" :key="id" type="button" role="tab" :aria-selected="active===id" :class="{selected:active===id}" @click="active=id">{{ t[id] }}</button>
        </div>
        <div class="cv-os-panel" role="tabpanel">
          <template v-if="active==='experience'"><h3>{{ t.history }}</h3>
            <div class="cv-os-timeline"><article v-for="role in roles" :key="role.company">
              <span class="cv-os-period">{{ role.years }}</span><div class="cv-os-position"><h4>{{ role.company }}</h4><strong>{{ role.title }}</strong><p>{{ role.details }}</p></div>
            </article></div>
          </template>
          <template v-else-if="active==='education'"><h3>{{ t.training }}</h3>
            <div class="cv-os-school"><article v-for="school in schools" :key="school.name"><span>{{ school.years }}</span><h4>{{ school.name }}</h4><p v-if="school.note">{{ school.note }}</p></article></div>
          </template>
          <template v-else-if="active==='stack'"><h3>{{ t.skills }}</h3>
            <div class="cv-os-stack"><span v-for="tech in stack" :key="tech">{{ tech }}</span></div>
          </template>
          <template v-else><h3>{{ t.built }}</h3>
            <div class="cv-os-school"><article v-for="project in projects" :key="project.name">
              <h4><a v-if="project.url" :href="project.url" target="_blank" rel="noopener noreferrer">{{ project.name }} ↗</a><span v-else>{{ project.name }}</span></h4><p>{{ project.text }}</p>
            </article></div>
          </template>
        </div>
      </div>
    </div>
    <footer class="cv-os-foot"><span>▣ Carles Far OS · CV v2.0</span><div class="cv-os-actions"><button type="button" @click="printCv">⎙ {{ locale === 'en' ? 'Print' : 'Imprimir' }}</button><a :href="useRuntimeConfig().app.baseURL + 'carles-far-cv.pdf'" download="Carles_Far_CV_2.0.pdf">↓ {{ t.download }}</a></div></footer>
    <p class="cv-os-print-note">{{ t.note }}</p>
    <div class="cv-os-print-only">
      <h2>{{ t.history }}</h2>
      <article v-for="role in roles" :key="role.company"><strong>{{ role.years }} · {{ role.company }} · {{ role.title }}</strong><p>{{ role.details }}</p></article>
      <h2>{{ t.training }}</h2>
      <p v-for="school in schools" :key="school.name">{{ school.years }} · {{ school.name }}. {{ school.note }}</p>
      <h2>{{ t.skills }}</h2><p>{{ stack.join(' · ') }}</p>
      <h2>{{ t.built }}</h2><p v-for="project in projects" :key="project.name">{{ project.name }} · {{ project.text }}</p>
    </div>
  </div>
</template>