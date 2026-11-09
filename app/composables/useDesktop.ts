import { setSelectedService } from '../domain/os'
import type { ServiceId, Theme, WindowId } from '~/domain/os'
export function useDesktop() {
  const opened=useState<WindowId[]>('cf-open',()=>['terminal'])
  const active=useState<WindowId>('cf-active',()=> 'terminal')
  const recentlyClosed=useState<WindowId[]>('cf-recently-closed',()=>[])
  const services=useState<ServiceId[]>('cf-services',()=>[])
  const theme=useState<Theme>('cf-theme',()=> 'light')
  function open(id:WindowId){
    opened.value=[...opened.value.filter(item=>item!==id),id]
    active.value=id
    if (id!=='trash') recentlyClosed.value=recentlyClosed.value.filter(item=>item!==id)
  }
  function close(id:WindowId){
    if (id!=='trash' && opened.value.includes(id)) {
      recentlyClosed.value=[id,...recentlyClosed.value.filter(item=>item!==id)].slice(0,12)
    }
    opened.value=opened.value.filter(item=>item!==id)
    active.value=opened.value.at(-1)??'terminal'
  }
  function restore(id:WindowId){open(id)}
  function emptyTrash(){recentlyClosed.value=[]}
  function setService(id:ServiceId, checked:boolean){
    services.value=setSelectedService(services.value,id,checked)
  }
  function toggleService(id:ServiceId){
    setService(id,!services.value.includes(id))
  }
  return {opened,active,recentlyClosed,services,theme,open,close,restore,emptyTrash,toggleService,setService}
}
