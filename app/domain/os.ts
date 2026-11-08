export const serviceIds = ['custom','frontend','performance','consulting'] as const
export type ServiceId = typeof serviceIds[number]
export const windowIds = ['terminal','about','projects','contact','services','audio'] as const
export type WindowId = typeof windowIds[number]
export type Theme = 'dark' | 'light'
export type Command =
  | { action:'open', target:WindowId }
  | { action:'lang', target:'es'|'ca'|'en' }
  | { action:'theme', target:Theme }
  | { action:'text', target:string }
export function parseCommand(input:string):Command {
  const value=input.trim().toLowerCase().replace(/\s+/g,' ')
  const aliases:Record<string,WindowId>={whoami:'about',about:'about',sobre:'about',projects:'projects',proyectos:'projects',projectes:'projects',services:'services',servicios:'services',serveis:'services',contact:'contact',contacto:'contact',contacte:'contact',audio:'audio',music:'audio',terminal:'terminal'}
  if (aliases[value]) return {action:'open',target:aliases[value]}
  if (value.startsWith('open ') && (windowIds as readonly string[]).includes(value.slice(5))) return {action:'open',target:value.slice(5) as WindowId}
  if (/^lang (es|ca|en)$/.test(value)) return {action:'lang',target:value.slice(5) as 'es'|'ca'|'en'}
  if (/^theme (dark|light)$/.test(value)) return {action:'theme',target:value.slice(6) as Theme}
  return {action:'text',target:value}
}
