<script setup lang="ts">
const {services}=useDesktop()
const {t}=useI18n()
const name=ref(''),email=ref(''),message=ref('')
const chosen=computed(()=>services.value.map(id=>t(id)).join(', '))
function submit(){
  const body=encodeURIComponent('Name: '+name.value+'\nEmail: '+email.value+'\nServices: '+chosen.value+'\n\n'+message.value)
  if(import.meta.client)window.location.href='mailto:hola@carlesfar.com?subject=Carles%20Far%20OS%20contact&body='+body
}
</script>
<template>
  <form class="contact-form" @submit.prevent="submit">
    <h2>{{t('ask')}}</h2><label>{{t('name')}} *<input v-model.trim="name" required maxlength="100" autocomplete="name"/></label>
    <label>{{t('email')}} *<input v-model.trim="email" required type="email" maxlength="254" autocomplete="email"/></label>
    <label>{{t('select')}}<output>{{chosen||'—'}}</output></label>
    <label>{{t('message')}} *<textarea v-model.trim="message" required minlength="10" maxlength="3000"/></label>
    <button class="retro-btn" type="submit">{{t('send')}} ↵</button>
    <small>Demo: abre el cliente de correo. El envío real requiere configurar el endpoint y verificar el destinatario.</small>
  </form>
</template>
