import {describe,it,expect} from 'vitest'
import {parseCommand,serviceIds,setSelectedService} from '../app/domain/os'
describe('terminal commands',()=>{
  it('supports languages',()=>expect(parseCommand(' LANG CA ')).toEqual({action:'lang',target:'ca'}))
  it('supports themes',()=>expect(parseCommand('theme dark')).toEqual({action:'theme',target:'dark'}))
  it('opens known windows',()=>expect(parseCommand('projects')).toEqual({action:'open',target:'projects'}))
  it('does not execute arbitrary text',()=>expect(parseCommand('sudo rm -rf /').action).toBe('text'))
  it('keeps stable service identifiers',()=>expect(serviceIds).toHaveLength(4))
})

describe('shared service selection', () => {
  it('adds a service selected in the form', () => {
    expect(setSelectedService(['custom'], 'frontend', true)).toEqual(['custom', 'frontend'])
  })
  it('keeps selections idempotent when already checked', () => {
    expect(setSelectedService(['frontend'], 'frontend', true)).toEqual(['frontend'])
  })
  it('removes only the unchecked service, keeping the rest', () => {
    expect(setSelectedService(['custom', 'frontend'], 'custom', false)).toEqual(['frontend'])
  })
  it('orders selections consistently for the email', () => {
    expect(setSelectedService(['consulting'], 'frontend', true)).toEqual(['frontend', 'consulting'])
  })
})
