<script setup lang="ts">
const { locale }=useI18n()
const base=useRuntimeConfig().app.baseURL
const wallpaper=base+'wallpapers/night-hd.webp'
useHead(()=>({title:'Privacidad | Carles Far OS',meta:[{name:'robots',content:'index,follow'}]}))
const content=computed(()=>({
 es:{
  title:'Privacidad y contacto',intro:'Información sobre el formulario de contacto de Carles Far OS.',
  controller:'Responsable',controllerText:'Carles Far, Barcelona. Contacto: contacto@carlesfar.com.',
  purpose:'Finalidad',purposeText:'Responder a las consultas enviadas voluntariamente a través del formulario. No se utiliza para crear cuentas ni enviar publicidad.',
  data:'Datos tratados',dataText:'Nombre, correo electrónico, mensaje, servicios seleccionados y dirección de la página desde la que se envía el formulario.',
  processor:'Proveedor de envío',processorText:'El formulario transmite los datos a FormSubmit (formsubmit.co), proveedor externo encargado de gestionar la entrega al buzón de contacto.',
  basis:'Base del tratamiento',basisText:'Atender la solicitud que nos remites voluntariamente. Puedes escribir directamente por correo si prefieres no utilizar el formulario.',
  retention:'Conservación',retentionText:'FormSubmit indica que conserva los mensajes en su archivo durante 30 días. El correo recibido puede conservarse el tiempo necesario para responder y gestionar la consulta.',
  rights:'Consultas sobre tus datos',rightsText:'Puedes solicitar acceso, rectificación o eliminación de tus datos escribiendo a contacto@carlesfar.com.',
  info:'Más información del proveedor',back:'Volver a Carles Far OS'
 },
 ca:{
  title:'Privacitat i contacte',intro:'Informació sobre el formulari de contacte de Carles Far OS.',
  controller:'Responsable',controllerText:'Carles Far, Barcelona. Contacte: contacto@carlesfar.com.',
  purpose:'Finalitat',purposeText:'Respondre les consultes enviades voluntàriament mitjançant el formulari. No es fa servir per crear comptes ni enviar publicitat.',
  data:'Dades tractades',dataText:'Nom, correu electrònic, missatge, serveis seleccionats i adreça de la pàgina des de la qual s’envia el formulari.',
  processor:'Proveïdor d’enviament',processorText:'El formulari transmet les dades a FormSubmit (formsubmit.co), proveïdor extern encarregat de gestionar el lliurament a la bústia de contacte.',
  basis:'Base del tractament',basisText:'Atendre la petició que ens envies voluntàriament. Pots escriure directament per correu si prefereixes no fer servir el formulari.',
  retention:'Conservació',retentionText:'FormSubmit indica que conserva els missatges a l’arxiu durant 30 dies. El correu rebut es pot conservar el temps necessari per respondre i gestionar la consulta.',
  rights:'Consultes sobre les teves dades',rightsText:'Pots sol·licitar accés, rectificació o supressió de les teves dades escrivint a contacto@carlesfar.com.',
  info:'Més informació del proveïdor',back:'Tornar a Carles Far OS'
 },
 en:{
  title:'Privacy and contact',intro:'Information about the Carles Far OS contact form.',
  controller:'Data controller',controllerText:'Carles Far, Barcelona. Contact: contacto@carlesfar.com.',
  purpose:'Purpose',purposeText:'To respond to messages voluntarily sent through the form. The form is not used to create accounts or send marketing.',
  data:'Personal data',dataText:'Name, email address, message, selected services and the URL of the page where the form was submitted.',
  processor:'Delivery provider',processorText:'The form sends the data to FormSubmit (formsubmit.co), an external service that manages forwarding to the contact inbox.',
  basis:'Reason for processing',basisText:'To handle the request you voluntarily send. You can contact us directly by email instead of using the form.',
  retention:'Retention',retentionText:'FormSubmit states that messages remain in its submissions archive for 30 days. Emails received may be kept as long as necessary to manage and reply to your request.',
  rights:'Your data',rightsText:'You may request access, correction or deletion by emailing contacto@carlesfar.com.',
  info:'Provider information',back:'Back to Carles Far OS'
 }
})[locale.value as 'es'|'ca'|'en'] || {
 title:'Privacidad y contacto',intro:'Información sobre el formulario de contacto de Carles Far OS.',
 controller:'Responsable',controllerText:'Carles Far, Barcelona. Contacto: contacto@carlesfar.com.',
 purpose:'Finalidad',purposeText:'Responder las consultas enviadas voluntariamente.',
 data:'Datos tratados',dataText:'Nombre, correo electrónico, mensaje y servicios seleccionados.',
 processor:'Proveedor',processorText:'FormSubmit (formsubmit.co).',
 basis:'Motivo',basisText:'Atender tu solicitud.',retention:'Conservación',retentionText:'FormSubmit mantiene un archivo de 30 días.',
 rights:'Tus datos',rightsText:'Contacto: contacto@carlesfar.com.',info:'Proveedor',back:'Volver'
}))
</script>
<template>
 <main class="privacy-page" :style="{backgroundImage: `url(${wallpaper})`}">
  <div class="privacy-window">
   <header class="privacy-titlebar"><span aria-hidden="true" class="privacy-lights">● ● ●</span><strong>Carles Far OS · {{ content.title }}</strong><NuxtLink :to="'/'" aria-label="Cerrar">×</NuxtLink></header>
   <div class="privacy-body">
    <h1>{{ content.title }}</h1>
    <p>{{ content.intro }}</p>
    <section v-for="key in (['controller','purpose','data','processor','basis','retention','rights'] as const)" :key="key">
      <h2>{{ content[key] }}</h2><p>{{ content[(key+'Text') as 'controllerText'] }}</p>
    </section>
    <p><a href="https://formsubmit.co/documentation" target="_blank" rel="noopener noreferrer">{{ content.info }} ↗</a></p>
    <NuxtLink class="privacy-back" :to="'/'">{{ content.back }}</NuxtLink>
   </div>
  </div>
 </main>
</template>
<style scoped>
.privacy-page{min-height:100dvh;background-color:#111835;background-position:center;background-size:cover;background-attachment:fixed;padding:clamp(18px,5vw,55px);font-family:'Courier New',monospace;color:#192643}
.privacy-window{max-width:820px;margin:0 auto;border:3px solid #222e4c;background:#ecf1fa;box-shadow:5px 5px #2a5ded}
.privacy-titlebar{display:flex;align-items:center;gap:13px;background:repeating-linear-gradient(0deg,#bbc8e5 0 2px,#d2dbef 2px 4px);border-bottom:3px solid #2d3f65;padding:7px 12px}
.privacy-titlebar strong{flex:1}.privacy-titlebar a{display:grid;place-items:center;border:2px solid #243451;width:26px;height:26px;text-decoration:none;color:#1c2640;background:#f5f7fb;font-size:23px}
.privacy-lights{color:#3074eb;letter-spacing:2px}.privacy-body{padding:clamp(18px,4vw,36px)}h1{font-size:clamp(25px,4vw,40px);margin-top:0}h2{font-size:15px;margin:21px 0 5px}p{font-size:14px;line-height:1.55;margin:5px 0}a{color:#174abe}.privacy-back{display:inline-block;background:#245bff;color:#fff;text-decoration:none;font-weight:700;padding:12px 18px;margin-top:18px}
</style>