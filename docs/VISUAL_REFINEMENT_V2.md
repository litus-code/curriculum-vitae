# Carles Far OS · Visual Refinement V2

Date: 2026-11-08
Status: APPROVED ART DIRECTION, IMPLEMENTATION PENDING
Parent: PR #1, `feat/carles-far-os-nuxt4-foundation`

## Product goal

Rebuild the user's approved desktop artwork as a responsive, accessible Nuxt 4 interface in genuine HTML/CSS/Vue components. The submitted screenshot is the visual acceptance reference. A screenshot used as the entire desktop background with invisible click targets is expressly **not** the delivery method.

The current GitHub Pages preview is a working foundation, **not** an approved visual match. Keep the current public website untouched.

## Exact desktop composition

Reference artwork has approximately 3:2 proportions (about 922×616 pixels; also supplied in a larger crop). At a comparable viewport aim for the following scene, with intentional overlap and a dedicated right-hand icon rail:

| Element | Visual reference / desktop placement |
| --- | --- |
| CRT / outer bezel | dark beveled enclosure, subtle screen noise and scanlines; do not obscure text |
| Top menu | thin cream-pink bar, retro computer icon and Carles Far OS left, menu items, system controls to right |
| Terminal | upper-left, roughly 44% width; green monospace text on near-black; lime/purple frame |
| About | upper-right, roughly 41% width; **pixel portrait** left and copy / lime highlight strips right |
| Projects | lower middle, layered in front of terminal; three equal tiles |
| Contact | right-lower area, aligned left of icon rail; full form visible without overflow |
| Services note | lower-left, tilted yellow handwritten-style sticky, partially above landscape |
| Desktop shortcuts | single right-hand column with uniform 8/16-bit sprite icons and cream label boxes |
| Wallpaper | dithered mountain layers, sky with pixel clouds and luminous celestial body |

Do not introduce a modern SaaS dashboard aesthetic, standard rounded cards, emojis as icons or off-the-shelf outline icons. Keep text readable even at normal CSS zoom.

## Art direction: Sunset and Night

**Sunset / Light (default visual reference):** purple, violet and pink dusk, warm foreground, dithered mountain ridges, horizontally banded lime-yellow **setting sun** near the horizon and small pixel clouds.

**Night / Dark:** same geography, viewpoint, mountain silhouette and composition; deeper indigo/violet sky, prominent pixel **moon** in the corresponding position, subdued stars, cooler mountain shading and slightly stronger luminous window/terminal accents.

A theme switch changes CSS design tokens, background sprite or the coherent CSS pixel scene and celestial object. It must also update window surfaces/foregrounds for text contrast. It must **not** just apply a global brightness/filter to the whole page. Respect `prefers-reduced-motion` and prevent flashes on refresh. User choice can persist in localStorage only on the client; SSR must avoid hydration drift.

Use stable semantic values `sunset` and `night` for the two appearance modes, and map terminal commands `theme light` / `theme dark` to them for backwards compatibility. Add visible buttons/toggle with translated accessible labels. No background audio autoplay.

## Pixel assets: one coherent sprite family

Produce small authored image assets or a single pixel-sprite sheet (PNG/SVG with pixel grid, crisp edges) with a common grid, stroke/border weight, and dark outline:
- right rail: Macintosh computer/projects, lime folder/services, paper/about, envelope/contact, floppy/CV, metal bin/trash, optional record/audio;
- project identity: waveform/equalizer for Cuebooker (acid lime), wrapped gift for Friends Invisible (lavender), platter/turntable for Cuebooker DJ (purple);
- top bar brand machine and small system status icons.

All sprites use `image-rendering: pixelated` when appropriate, explicit image dimensions, correct labels and focus states. Avoid Unicode placeholder glyphs (`▣`, `◉`, `♫`, `✉`) as final icon assets. Icon hit areas must not overlap each other.

## Personal pixel portrait

The user supplied a black-and-white photograph with **yellow rectangular sunglasses**, textured light hair, moustache and a nose ring. Include the authorised portrait as a real repository asset, export a dithered/pixelated version with recognizable features and preserve the yellow glasses.

The approved composition places the portrait in the **left portion of the About window**. Provide accurate alternative text and ensure the image doesn't stretch or crop off the glasses. Do not invent biographical facts or overstate years of experience. Do not substitute initials `CF` when the photo asset is available. Make asset filenames and provenance explicit.

## Interaction and content contracts

- All overlapping windows remain genuine semantic components; mouse and keyboard support closing, focusing and opening. Allow dragging by title bar only on desktop; constrain movement to visible area, preserve focus stacking and avoid accidental drag from close buttons.
- Terminal starts with period-appropriate boot messages and supports `help`, `whoami`, `ls`, `projects`, `services`, `about`, `contact`, `music`, `lang ca/es/en`, `theme light/dark`, `clear`. It must never execute arbitrary shell commands.
- Services sticky contains four **visible native checked states**, synchronized with the full services window and contact form. Selecting one or several items gives an obvious checkmark and remains usable at mobile sizes.
- Projects each have a real visual identity, correct current-development disclosure and an intentional click action (detail window or verified URL), never a decorative dead button.
- CAT/ES/EN applies to window titles, dock labels, sticky, form, terminal UI affordances, theme labels and accessibility names. Avoid hardcoded Spanish outside translation dictionaries.
- Contact is honest about being a `mailto:` demo until a validated delivery service exists; no claim of messages sent. Never publish fictitious contacts.
- Audio window supports voluntarily loading a local file, playback controls and cleanup of object URLs; no autoplay or copyrighted bundled track.
- CV shortcut must have real content before being presented as downloadable. Otherwise disabled or clearly labelled as pending.

## Engineering boundaries

Use Nuxt 4, Vue 3, TypeScript, pure domain types, composable state and focused components. Do not rebuild in standalone HTML. Create `app/components/desktop/` and `app/components/icons/` only where warranted; avoid massive one-file page and monolithic CSS.

Define design tokens for CRT, frame, titlebar, canvas, surfaces, accents, focus, shadows, sizes, and `sunset/night` surfaces. Keep static assets in `public/` with source provenance in docs. No Supabase or additional service needed for the static visual system.

## Acceptance matrix

1. Desktop 1440×900, 1280×800 and **922×616** screenshots side by side with approved screenshot; review element geometry, icon scale, art style, window overlap, portrait and labels.
2. Mobile 390×844 and tablet 768×1024: no clipped controls, unusable overflow or inaccessible contact form. Use a mobile-specific window stack; do not merely shrink the whole desktop.
3. Validate both themes at all viewports, including sun/moon, legible contrast, correct persistence, and reduced-motion.
4. Verify all three languages, native checkbox state, terminal keyboard commands, opening/closing/dragging/focus and links.
5. Run `npm ci` after committing lockfile; run `npm run check`; screenshot smoke tests and axe checks. Document results in HANDOFF.
6. Push into existing PR #1. Never merge or deploy to carlesfar.com. GitHub Pages preview remains the acceptance environment.
7. Report differences honestly. Art is accepted only when user reviews live preview.

## Execution order

1. Restore actual photo/pixel portrait and author visual sprite assets with pixel-grid consistency.
2. Build theme-specific wallpaper art (same composition, sun ↔ moon) and tokens.
3. Align frame/menu/dock/window geometry against reference screenshot at 922×616.
4. Integrate icons + three project tiles and refine title bars/typography/CRT.
5. Complete service checkmarks/contact synchronization, terminal interactions and persistent theme/language.
6. Dragging, responsive layouts, accessibility, performance.
7. Automated checks, screenshots, revised HANDOFF and review preview in PR #1.

### Design decision
The screenshot is **acceptance reference**, not DOM markup or a baked background. All UI content remains accessible, translated, interactive and responsive.
