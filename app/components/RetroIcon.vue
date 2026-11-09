<script setup lang="ts">
withDefaults(defineProps<{ name:string; size?:number }>(),{ size:48 })
</script>

<template>
  <svg class="retro-icon" :width="size" :height="size" viewBox="0 0 48 48"
    xmlns="http://www.w3.org/2000/svg" shape-rendering="crispEdges" aria-hidden="true">
    <!-- Macintosh desktop computer, cream case, blue glass and disk slot -->
    <g v-if="name==='computer'">
      <path fill="#140f25" d="M8 2h30v3h3v28h-3v3H10v-3H7V6h1zM4 36h38v4h3v6H2v-7h2z"/>
      <path fill="#f4e6b8" d="M10 4h27v2h2v25h-3v3H10V31H9V7h1zM6 38h34v2h2v4H5v-4h1z"/>
      <path fill="#7b657e" d="M37 8h2v23h-3v2h-2v-2h2zM40 40h2v3h-3z"/>
      <rect x="13" y="9" width="23" height="21" fill="#110c2a"/>
      <rect x="15" y="11" width="19" height="17" fill="#239dc1"/>
      <path fill="#70d4eb" d="M16 12h10v3h-5v4h-5z"/>
      <path fill="#d7f35d" d="M16 13h7v2h-3v4h-4z"/>
      <path fill="#092b50" d="M29 18h2v2h-2zM27 20h2v2h-2zM31 22h2v2h-2zM24 23h2v2h-2zM28 24h3v2h-3z"/>
      <rect x="10" y="39" width="15" height="3" fill="#8f8880"/>
      <rect x="12" y="40" width="11" height="1" fill="#201329"/>
      <rect x="29" y="39" width="5" height="3" fill="#d4f360"/>
      <rect x="35" y="39" width="4" height="3" fill="#5fa969"/>
      <rect x="43" y="41" width="2" height="5" fill="#140f25"/>
    </g>

    <!-- Fat lime-green folder with tab and offset dark edge -->
    <g v-else-if="name==='folder'">
      <path fill="#120d22" d="M2 11h3V7h19v3h4v2h16v3h2v28h-3v2H4v-3H2z"/>
      <path fill="#d6f94c" d="M5 10h18v3h19v2H5z"/>
      <path fill="#c0f440" d="M5 16h38v25H5z"/>
      <path fill="#edff73" d="M7 17h33v18H7z"/>
      <path fill="#8aa551" d="M41 16h2v25h-3zM7 39h34v2H7z"/>
      <path fill="#ffffff" opacity=".25" d="M9 19h29v2H9z"/>
      <rect x="44" y="17" width="2" height="22" fill="#61536b"/>
    </g>

    <!-- Folded document with typewritten lines -->
    <g v-else-if="name==='paper'">
      <path fill="#160f25" d="M8 2h22l11 12v31H7V4h1z"/>
      <path fill="#f8e7de" d="M10 5h18v13h11v24H10z"/>
      <path fill="#dac9cf" d="M30 7v9h8z"/>
      <path fill="#160f25" d="M30 3v12h11z"/>
      <path fill="#f8e7de" d="M32 8v5h5z"/>
      <path fill="#372b3e" d="M14 14h12v2H14zM14 21h21v2H14zM14 27h21v2H14zM14 33h20v2H14zM14 39h17v2H14z"/>
      <path fill="#9e879c" d="M37 18h2v24h-2z"/>
    </g>

    <!-- Classic envelope, heavy crisp diagonal fold -->
    <g v-else-if="name==='mail'">
      <rect x="2" y="8" width="44" height="33" fill="#130f24"/>
      <rect x="5" y="11" width="38" height="27" fill="#f9e7df"/>
      <path d="M5 12L24 27 43 12M5 37L18 24M43 37L30 24" fill="none" stroke="#1c1428" stroke-width="3" stroke-linejoin="miter"/>
      <path fill="#ddc5d3" d="M7 35l11-10 5 5 4 0 5-5 9 10v2H7z" opacity=".5"/>
    </g>

    <!-- 3.5 inch floppy disk, violet window and paper label -->
    <g v-else-if="name==='floppy'">
      <path fill="#120d24" d="M7 2h29l7 8v35H4V5h3z"/>
      <path fill="#d7f750" d="M8 5h27v7h5v29H8z"/>
      <path fill="#6d567f" d="M35 5v8h5z"/>
      <rect x="12" y="5" width="24" height="16" fill="#171328"/>
      <rect x="16" y="7" width="16" height="11" fill="#514e8f"/>
      <rect x="29" y="6" width="3" height="10" fill="#b3a4b6"/>
      <rect x="11" y="26" width="28" height="17" fill="#0d0e1e"/>
      <rect x="14" y="28" width="22" height="13" fill="#f5e3dc"/>
      <path fill="#76647b" d="M17 32h15v2H17zM17 37h15v2H17z"/>
      <rect x="8" y="5" width="3" height="36" fill="#f1ff77"/>
      <rect x="41" y="13" width="2" height="30" fill="#6e5a80"/>
    </g>

    <!-- Tin can trash, metal lid and raised ribs -->
    <g v-else-if="name==='trash'">
      <path fill="#160f25" d="M15 5h18v4h9v4h3v7h-4v22h-4v3H11v-3H8V20H4v-7h4V9h7z"/>
      <path fill="#eee6bb" d="M17 7h14v4H17zM9 12h32v6H9zM12 20h27v20h-3v2H15v-2h-3z"/>
      <path fill="#9e967f" d="M11 15h30v3H11zM14 21h4v19h-4zM25 21h4v19h-4zM35 21h3v19h-3z"/>
      <path fill="#171328" d="M19 22h3v19h-3zM30 22h3v19h-3z"/>
      <path fill="#fff9dd" d="M13 21h3v18h-3zM24 21h3v18h-3zM34 21h2v18h-2z"/>
      <path fill="#eedcbe" d="M6 14h38v2H6z"/>
      <rect x="14" y="43" width="21" height="2" fill="#21172a"/>
    </g>

    <!-- Cuebooker bar-wave logo matching screenshot silhouette -->
    <g v-else-if="name==='wave'">
      <rect x="2" y="21" width="4" height="7" fill="#100e19"/>
      <rect x="9" y="14" width="4" height="20" fill="#100e19"/>
      <rect x="16" y="7" width="5" height="34" fill="#100e19"/>
      <rect x="24" y="3" width="5" height="42" fill="#100e19"/>
      <rect x="32" y="11" width="5" height="25" fill="#100e19"/>
      <rect x="40" y="20" width="5" height="9" fill="#100e19"/>
    </g>

    <!-- Pixel gift with peach/purple bow and pale yellow package -->
    <g v-else-if="name==='gift'">
      <path fill="#170f23" d="M10 3h8l6 7 6-7h8l4 6-2 8h6v9h-4v18H6V26H2v-9h6L6 9z"/>
      <path fill="#d386ef" d="M11 6h6l7 9-10-2-4-4zM31 6h6l2 4-4 4-10 1z"/>
      <path fill="#ffa566" d="M12 8l8 5-6-1zM35 8l-8 5 6-1z"/>
      <rect x="6" y="19" width="36" height="6" fill="#fbb76b"/>
      <rect x="9" y="27" width="30" height="14" fill="#ffe17b"/>
      <rect x="22" y="18" width="5" height="23" fill="#8d50d2"/>
      <path fill="#ffd55f" d="M12 29h8v9h-8zM29 29h7v9h-7z"/>
      <rect x="4" y="18" width="40" height="2" fill="#2a142c"/>
    </g>

    <!-- Turntable platter with tonearm -->
    <g v-else-if="name==='turntable' || name==='record'">
      <path fill="#180e27" d="M5 14h35v3h3v28H3V17h2z"/>
      <path fill="#b58de1" d="M6 17h34v25H6z"/>
      <circle cx="22" cy="28" r="16" fill="#160e26"/>
      <circle cx="22" cy="28" r="13" fill="#8e5fce"/>
      <circle cx="22" cy="28" r="10" fill="#a985e9"/>
      <circle cx="22" cy="28" r="7" fill="#6b489a"/>
      <circle cx="22" cy="28" r="5" fill="#e2d7e8"/>
      <circle cx="22" cy="28" r="2" fill="#25152c"/>
      <path fill="#24182c" d="M40 8h4v28h-4zM34 34h9v4h-9z"/>
      <path fill="#e7e2dc" d="M41 9h2v26h-2z"/>
      <rect x="39" y="6" width="7" height="5" fill="#170d25"/>
      <rect x="35" y="33" width="6" height="3" fill="#d8f958"/>
    </g>

    <g v-else-if="name==='sun'">
      <rect x="14" y="4" width="20" height="4" fill="#1b1129"/>
      <rect x="8" y="8" width="32" height="6" fill="#f2e767"/>
      <rect x="4" y="14" width="40" height="21" fill="#d8f757"/>
      <rect x="8" y="35" width="32" height="6" fill="#f3e767"/>
      <rect x="14" y="41" width="20" height="3" fill="#1b1129"/>
    </g>
    <g v-else-if="name==='moon'">
      <path fill="#f8f2c8" d="M21 2h12v5H22v5H16v8h-4v10h4v7h6v5h11v4H19v-4h-7v-7H7v-9H4V18h3v-8h6V5h8z"/>
      <rect x="20" y="17" width="4" height="3" fill="#e5d8a1"/>
    </g>

    <g v-else><rect x="7" y="7" width="34" height="34" fill="#d7f758" stroke="#160d26" stroke-width="3"/></g>
  </svg>
</template>
