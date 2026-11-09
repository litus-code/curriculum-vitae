<script setup lang="ts">
const { services } = useDesktop()
const { t, locale } = useI18n()
const name = ref('')
const email = ref('')
const message = ref('')
const website = ref('')
const privacyAccepted = ref(false)
const submitting = ref(false)
const sendingSlow = ref(false)
let sendingSlowTimer: ReturnType<typeof setTimeout> | undefined
onBeforeUnmount(() => { if (sendingSlowTimer) clearTimeout(sendingSlowTimer) })
const status = ref<'idle' | 'success' | 'error' | 'activation'>('idle')
const failureDetail = ref('')
const chosen = computed(() => services.value.map(id => t(id)).join(', '))
const recipient = 'contacto@carlesfar.com'
const endpoint = `https://formsubmit.co/ajax/${recipient}`
const copy = computed(() => ({
 es: {
  sending:'Enviando mensaje...', slow:'El envío está tardando un poco más de lo habitual.', success:'Mensaje enviado correctamente. Me pondré en contacto contigo lo antes posible.',
  error:'El proveedor ha rechazado la solicitud. Puedes escribir directamente por correo.',
  activation:'Hay que activar este formulario desde contacto@carlesfar.com. Revisa la bandeja y el spam para encontrar el correo de FormSubmit.',
  technical:'Respuesta del proveedor:',
  info:'El servicio FormSubmit procesará tu nombre, correo y mensaje para enviarme tu consulta.',
  privacy:'Acepto que FormSubmit gestione estos datos para responder a mi consulta.', messageLabel:'Mensaje',
  direct:'Escribir por correo', invalid:'Revisa los campos antes de enviar.'
 },
 ca: {
  sending:'Enviant missatge...',slow:'L’enviament està trigant una mica més del que és habitual.',success:'Missatge enviat correctament. Em posaré en contacte amb tu tan aviat com pugui.',
  error:'El proveïdor ha rebutjat la sol·licitud. Pots escriure directament per correu.',
  activation:'Cal activar el formulari des de contacto@carlesfar.com. Revisa la bústia i el correu brossa per trobar el missatge de FormSubmit.',
  technical:'Resposta del proveïdor:',
  info:'FormSubmit tractarà el nom, el correu i el missatge per enviar-me la consulta.',
  privacy:'Accepto que FormSubmit gestioni aquestes dades per respondre la consulta.', messageLabel:'Missatge',
  direct:'Escriure un correu',invalid:'Revisa els camps abans d’enviar.'
 },
 en: {
  sending:'Sending message...',slow:'Sending is taking a little longer than usual.',success:'Message sent successfully. I’ll get back to you as soon as possible.',
  error:'The provider rejected the request. You can email me directly.',
  activation:'The form must be activated from contacto@carlesfar.com. Please check the inbox and spam folder for an email from FormSubmit.',
  technical:'Provider response:',
  info:'FormSubmit processes your name, email and message to forward the enquiry to me.',
  privacy:'I agree to FormSubmit processing these details to handle my request.', messageLabel:'Message',
  direct:'Send an email',invalid:'Please check the form fields.'
 }
}[locale.value as 'es'|'ca'|'en'] ?? {
 sending:'Enviando mensaje...',slow:'El envío está tardando un poco más de lo habitual.',success:'Mensaje enviado correctamente. Me pondré en contacto contigo lo antes posible.',
 error:'El proveedor ha rechazado la solicitud.',activation:'Hay que activar FormSubmit desde contacto@carlesfar.com.',technical:'Respuesta del proveedor:',
 info:'FormSubmit procesará los datos para enviarme tu consulta.',privacy:'Acepto el envío de mis datos mediante FormSubmit para responder a mi consulta.',messageLabel:'Mensaje',direct:'Escribir por correo',invalid:'Revisa los campos antes de enviar.'
}))
const directLink = computed(() => `mailto:${recipient}?subject=${encodeURIComponent('Carles Far OS · Contacto')}`)
async function submit() {
 if (submitting.value || !privacyAccepted.value) return
 status.value = 'idle'
 failureDetail.value=''
 if (website.value.trim()) return
 const cleanName=name.value.trim()
 const cleanEmail=email.value.trim()
 const cleanMessage=message.value.trim()
 if (!cleanName || cleanName.length>100 || !/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(cleanEmail) || cleanEmail.length>254 || cleanMessage.length<10 || cleanMessage.length>3000) {
   status.value='error'
   return
 }
 submitting.value=true
 sendingSlow.value=false
 sendingSlowTimer=setTimeout(() => { sendingSlow.value=true }, 6000)
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
   if (!response.ok || !(result.success===true || result.success==='true')) {
     const detail = String(result.message ?? `HTTP ${response.status}`).slice(0,220)
     failureDetail.value=detail
     status.value=/activat|confirm.*email|check.*inbox/i.test(detail) ? 'activation' : 'error'
     return
   }
   status.value='success'
   name.value=''
   email.value=''
   message.value=''
   privacyAccepted.value=false
 } catch (error) {
   failureDetail.value=error instanceof TypeError ? 'Network request failed, check browser privacy settings, connectivity or CORS.' : 'Unexpected response from the mail service.'
   status.value='error'
 } finally {
   if (sendingSlowTimer) clearTimeout(sendingSlowTimer)
   sendingSlow.value=false
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
    <p v-if="submitting && sendingSlow" class="contact-slow" role="status" aria-live="polite">{{ copy.slow }}</p>
    <p v-if="status!=='idle'" class="contact-feedback" :class="'contact-feedback-'+status" role="status" aria-live="polite">
      <span v-if="status==='success'" class="contact-success-mark" aria-hidden="true">✓</span>{{ status==='success' ? copy.success : status==='activation' ? copy.activation : copy.error }}
      <small v-if="status!=='success' && failureDetail">{{ copy.technical }} {{ failureDetail }}</small>
    </p>
  </form>
</template>