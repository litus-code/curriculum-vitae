import type { ServiceId, Theme, WindowId } from '~/domain/os'
export function useDesktop() {
  const opened=useState<WindowId[]>('cf-open',()=>['terminal','about','projects','contact'])
  const active=useState<WindowId>('cf-active',()=> 'contact')
  const services=useState<ServiceId[]>('cf-services',()=>[])
  const theme=useState<Theme>('cf-theme',()=> 'dark')
  function open(id:WindowId){opened.value=[...opened.value.filter(item=>item!==id),id];active.value=id}
  function close(id:WindowId){opened.value=opened.value.filter(item=>item!==id);active.value=opened.value.at(-1)??'terminal'}
  function toggleService(id:ServiceId){services.value=services.value.includes(id)?services.value.filter(s=>s!==id):[...services.value,id]}
  return {opened,active,services,theme,open,close,toggleService}
}
