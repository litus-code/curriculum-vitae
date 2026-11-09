# Carles Far OS · Architecture
Status: foundation draft · 2026-11-08

## Product and boundaries
Nuxt 4 + Vue 3 + TypeScript. A static public portfolio with a functional retro desktop. No Supabase or other database is required for the portfolio. Visitor-facing content lives in translation messages and typed project/service definitions.

## Layers
- `app/domain`: pure TypeScript, terminal parsing and stable identifiers.
- `app/composables`: desktop state, open windows, selected services, theme.
- `app/components`: small window, terminal, services and contact.
- `app/pages`: composition, project content and keyboard/mouse controls.
- `app/assets/css`: authentic retro visual system.

## Data and security
The terminal is a whitelisted router, never shell execution or eval. Selected services are client-side and displayed in contact. Current form is mailto-only, not server delivery. Verify real recipient before publication. For future contact API use validation, spam protection, rate limiting and private server secrets.

## Accessibility and performance
Keyboard support and focus visibility; reduced motion; mobile scroll layout. Use local assets and explicit licensing. No default autoplay. Keep pixelation CSS / image preprocessing outside runtime. Target static generation and Cloudflare Pages only after approving domain routing.

## Design acceptance
The reference is the user's approved purple CRT desktop, lime terminal, about window with yellow-glasses pixel portrait, tri-color project tiles, hand-written service note and right dock. This first foundation approximates layout using real DOM and CSS. Do not claim pixel-perfect fidelity before screenshot comparison.
