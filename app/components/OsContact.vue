<script setup lang="ts">
const { services } = useDesktop()
const { t, locale } = useI18n()
const name = ref('')
const email = ref('')
const message = ref('')
const website = ref('')
const privacyAccepted = ref(false)
const submitting = ref(false)
const status = ref<'idle' | 'success' | 'error'>('idle')
const chosen = computed(() => services.value.map(id => t(id)).join(', '))
const recipient = 'contacto@carlesfar.com'
const endpoint = `https://formsubmit.co/ajax/${recipient}`
const copy = computed(() => ({
 es: {
  sending:'Enviando...', success:'El servicio ha recibido tu solicitud. La entrega al buzón depende de que el destinatario haya activado el formulario.',
  error:'No se ha podido enviar. Inténtalo de nuevo o escribe directamente por correo.',
  info:'El servicio FormSubmit procesará tu nombre, correo y mensaje para enviarme tu consulta.',
  privacy:'Acepto que FormSubmit gestione estos datos para responder a mi consulta.', messageLabel:'Mensaje',
  direct:'Escribir por correo', invalid:'Revisa los campos antes de enviar.'
 },
 ca: {
  sending:'Enviant...',success:'El servei ha rebut la sol·licitud. El lliurament a la bústia depèn de l’activació del formulari pel destinatari.',
  error:'No s’ha pogut enviar. Torna-ho a provar o escriu directament per correu.',
  info:'FormSubmit tractarà el nom, el correu i el missatge per enviar-me la consulta.',
  privacy:'Accepto que FormSubmit gestioni aquestes dades per respondre la consulta.', messageLabel:'Missatge',
  direct:'Escriure un correu',invalid:'Revisa els camps abans d’enviar.'
 },
 en: {
  sending:'Sending...',success:'The service accepted your request. Inbox delivery depends on the recipient activating the form.',
  error:'We could not send your message. Try again or contact me by email.',
  info:'FormSubmit processes your name, email and message to forward the enquiry to me.',
  privacy:'I agree to FormSubmit processing these details to handle my request.', messageLabel:'Message',
  direct:'Send an email',invalid:'Please check the form fields.'
 }
}[locale.value as 'es'|'ca'|'en'] ?? {
 sending:'Enviando...',success:'El servicio ha recibido tu solicitud. La entrega al buzón depende de que el destinatario haya activado el formulario.',
 error:'No se ha podido enviar. Inténtalo de nuevo o escribe directamente por correo.',
 info:'FormSubmit procesará los datos para enviarme tu consulta.',privacy:'Acepto el envío de mis datos mediante FormSubmit para responder a mi consulta.',messageLabel:'Mensaje',direct:'Escribir por correo',invalid:'Revisa los campos antes de enviar.'
}))
const directLink = computed(() => `mailto:${recipient}?subject=${encodeURIComponent('Carles Far OS · Contacto')}`)
async function submit() {
 if (submitting.value || !privacyAccepted.value) return
 status.value = 'idle'
 if (website.value.trim()) return
 const cleanName=name.value.trim()
 const cleanEmail=email.value.trim()
 const cleanMessage=message.value.trim()
 if (!cleanName || cleanName.length>100 || !/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(cleanEmail) || cleanEmail.length>254 || cleanMessage.length<10 || cleanMessage.length>3000) {
   status.value='error'
   return
 }
 submitting.value=true
 try {
   const response=await fetch(endpoint,{
     method:'POST',
     headers:{'Content-Type':'application/json','Accept':'application/json'},
     body:JSON.stringify({
       name:cleanName,email:cleanEmail,message:cleanMessage,
       services:chosen.value || 'Sin servicio seleccionado',
       _subject:'Carles Far OS | Nuevo contacto',
       _template:'table',
       _honey:website.value,
       _url:window.location.href
     })
   })
   const result=await response.json() as {success?:boolean|string;message?:string}
   if (!response.ok || !(result.success===true || result.success==='true')) throw new Error('FormSubmit rejected request')
   status.value='success'
   name.value=''
   email.value=''
   message.value=''
   privacyAccepted.value=false
 } catch {
   status.value='error'
 } finally {
   submitting.value=false
 }
}
</script>
<template>
  <form class="contact-form" @submit.prevent="submit" aria-label="Contacto">
    <h2>{{ t('ask') }}</h2>
    <label>{{ t('name') }} *
      <input v-model.trim="name" name="name" required maxlength="100" autocomplete="name" :disabled="submitting" @input="status='idle'" />
    </label>
    <label>{{ t('email') }} *
      <input v-model.trim="email" name="email" required type="email" maxlength="254" autocomplete="email" :disabled="submitting" @input="status='idle'" />
    </label>
    <label>{{ t('select') }}<output>{{ chosen || '—' }}</output></label>
    <label>{{ copy.messageLabel }} *
      <textarea v-model.trim="message" name="message" required minlength="10" maxlength="3000" :disabled="submitting" @input="status='idle'" />
    </label>
    <div class="contact-honeypot" aria-hidden="true">
      <label>Website <input v-model="website" type="text" tabindex="-1" autocomplete="off" /></label>
    </div>
    <label class="contact-privacy-consent">
      <input v-model="privacyAccepted" type="checkbox" name="privacy" required :disabled="submitting" />
      <span>{{ copy.privacy }} <a :href="useRuntimeConfig().app.baseURL + 'privacidad'" target="_blank" rel="noopener noreferrer">{{ locale==='ca' ? 'Privacitat' : locale==='en' ? 'Privacy notice' : 'Información de privacidad' }}</a></span>
    </label>
    <button class="retro-btn" type="submit" :disabled="submitting || !privacyAccepted">
      {{ submitting ? copy.sending : t('send') }} <span aria-hidden="true">↵</span>
    </button>
    <p v-if="status!=='idle'" class="contact-feedback" :class="'contact-feedback-'+status" role="status" aria-live="polite">
      {{ status==='success' ? copy.success : copy.error }}
    </p>
    <small>{{ copy.info }} <a :href="directLink">{{ copy.direct }}</a></small>
  </form>
</template>