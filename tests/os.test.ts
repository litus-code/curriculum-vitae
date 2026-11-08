import {describe,it,expect} from 'vitest'
import {parseCommand,serviceIds} from '../app/domain/os'
describe('terminal commands',()=>{
  it('supports languages',()=>expect(parseCommand(' LANG CA ')).toEqual({action:'lang',target:'ca'}))
  it('supports themes',()=>expect(parseCommand('theme dark')).toEqual({action:'theme',target:'dark'}))
  it('opens known windows',()=>expect(parseCommand('projects')).toEqual({action:'open',target:'projects'}))
  it('does not execute arbitrary text',()=>expect(parseCommand('sudo rm -rf /').action).toBe('text'))
  it('keeps stable service identifiers',()=>expect(serviceIds).toHaveLength(4))
})
