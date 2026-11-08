<script setup lang="ts">
const props = withDefaults(defineProps<{name:string;size?:number}>(),{size:48})
const ink='#20152c'
const glyphs:Record<string,string[]> = {
 computer:[
 '............','..kkkkkkkk..','..kbbbbbbk...','..kbyybbbk...','..kbyybbbk...','..kbbbbbbk...','..kkkkkkkk...','....kkkk.....','...kkkkkk....','..kkkkkkkk...','............','............'
 ],
 folder:[
 '............','............','.yyyy.......','.ykkkyyyyyy.','.yllllllllk','.ylllllyyllk','.ylllllyyllk','.ylllllyyllk','.ylllllllllk','.kkkkkkkkkkk','............','............'
 ],
 paper:[
 '............','...kkkkkk...','...kwwwwk...','...kwkkwk...','...kwwwwk...','...kwkkwk...','...kwwwwk...','...kwkkwk...','...kwwwwk...','...kkkkkk...','............','............'
 ],
 mail:[
 '............','............','.kkkkkkkkkk.','.kwwwwwwwwk.','.kwkwwwwkwk.','.kwwkkkkwwk.','.kwwwkkwwwk.','.kwwwwwwwwk.','.kkkkkkkkkk.','............','............','............'
 ],
 record:[
 '............','...kkkkkk...','..kppppppk..','.kppppppppk.','.kpppkkpppk.','.kppkwwkppk.','.kppkwwkppk.','.kpppkkpppk.','.kppppppppk.','..kppppppk..','...kkkkkk...','............'
 ],
 wave:[
 '............','.....k......','...k.k.k....','...k.k.k.k..','.k.k.k.k.k..','.k.k.k.k.k..','.k.k.k.k.k..','.k.k.k.k.k..','...k.k.k.k..','...k.k.k....','.....k......','............'
 ],
 gift:[
 '............','...pp..pp...','..pkkppkkp..','..pkkkkkkp..','...kkkkkk...','.kkkkkkkkkk.','.kyyykkyyyk.','.kyyykkyyyk.','.kyyykkyyyk.','.kkkkkkkkkk.','............','............'
 ],
 turntable:[
 '............','..kkkkkkkk..','.kppppppppk.','.kppkkkkppk.','.kpkppppkpk.','.kpkpwwpkpk.','.kpkpwwpkpk.','.kpkppppkpk.','.kppkkkkppk.','.kppppppppk.','..kkkkkkkk..','..........kk'
 ],
 sun:[
 '............','....yyyy....','...yyyyyy...','..yyyyyyyy..','..yyyyyyyy..','..yyyyyyyy..','..yyyyyyyy..','...yyyyyy...','....yyyy....','............','............','............'
 ],
 moon:[
 '............','....wwwww...','...wwwwwww..','..wwwwwwwk..','..wwwwwkkk..','..wwwwkkkk..','...wwwkkkk..','....kkkkk...','......kk....','............','............','............'
 ]
}
const palette:Record<string,string>={k:ink,b:'#46bfee',y:'#dcf65a',l:'#b6f74b',w:'#f8e6eb',p:'#ae82fc'}
const pixels=computed(()=> (glyphs[props.name] ?? glyphs['folder'] ?? []).flatMap((row,y)=>[...row].flatMap((c,x)=>c==='.'?[]:[{x,y,color:palette[c]??ink}])))
</script>
<template>
  <svg class="pixel-icon" :width="size" :height="size" viewBox="0 0 12 12" xmlns="http://www.w3.org/2000/svg" role="img" :aria-label="name" shape-rendering="crispEdges">
    <rect v-for="(pixel,i) in pixels" :key="i" :x="pixel.x" :y="pixel.y" width="1" height="1" :fill="pixel.color"/>
  </svg>
</template>
