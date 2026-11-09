<script setup lang="ts">
import {parseCommand} from '~/domain/os'
const {open,theme}=useDesktop()
const {locale,t}=useI18n()
const input=ref('')
const lines=ref<string[]>(['> booting Carles Far OS v1.0...','> system ready.'])
function execute(){
  const raw=input.value.trim()
  if(!raw)return
  lines.value.push('carles@far:~$ '+raw)
  const command=parseCommand(raw)
  switch(command.action){
    case 'open': open(command.target);lines.value.push('opening '+command.target+'...');break
    case 'lang': locale.value=command.target;lines.value.push('locale = '+command.target);break
    case 'theme': theme.value=command.target;lines.value.push('theme = '+command.target);break
    case 'text':
      if(command.target==='clear')lines.value=[]
      else if(command.target==='help')lines.value.push('ls | whoami | projects | services | contact | audio | lang ca/es/en | theme dark/light | clear')
      else if(command.target==='ls')lines.value.push('projects/ services/ about/ contact/ audio/')
      else lines.value.push('command not found: '+command.target)
  }
  input.value=''
}
</script>
<template>
  <div class="terminal"><div class="terminal-output" role="log"><div v-for="(line,i) in lines" :key="i">{{line}}</div><div class="help">{{t('help')}}</div></div>
  <form class="terminal-entry" @submit.prevent="execute"><label for="cmd">carles@far:~$</label><input id="cmd" v-model="input" spellcheck="false" autocomplete="off" aria-label="Comando"/><span class="blink">▌</span></form></div>
</template>
