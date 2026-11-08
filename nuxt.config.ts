export default defineNuxtConfig({
  compatibilityDate: '2026-11-01',
  modules: ['@nuxtjs/i18n'],
  css: ['~/assets/css/os.css'],
  i18n: {
    defaultLocale: 'es',
    strategy: 'no_prefix',
    locales: [
      { code: 'ca', language: 'ca-ES', name: 'Català' },
      { code: 'es', language: 'es-ES', name: 'Español' },
      { code: 'en', language: 'en-GB', name: 'English' }
    ],
    vueI18n: './i18n.config.ts'
  },
  app: { head: { title: 'Carles Far OS | Frontend Developer',
    meta: [{ name: 'description', content: 'Carles Far, frontend engineer and independent product builder in Barcelona.' }] } }
})
