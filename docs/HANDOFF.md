# Handoff · 2026-11-08
Current branch: feat/carles-far-os-nuxt4-foundation
Repo was nearly empty (only README) before this feature branch.

Scope implemented: Nuxt 4 scaffold, CSS-built vintage desktop, terminal command parser, project cards, services selection, contact mailto demo, audio file picker, CAT/ES/EN and theme toggle, domain tests.

Known limitations:
- Pixelated personal portrait has not yet been committed to this branch; placeholder CF remains.
- Visual fidelity requires real browser screenshots and comparison at 922×616 and mobile.
- No direct contact delivery, no verified destination address.
- Project detail screens and public production URL not yet wired.
- GitHub Actions CI has passed on the existing Nuxt foundation. Browser screenshot comparison, UI integration tests and lockfile remain pending.
- No production deployment, DNS changes or merge.

Next: execute `docs/VISUAL_REFINEMENT_V2.md` in dependency order. This contains the approved Sunset/Night art direction, sprite and portrait requirements, exact screenshot comparison, interaction and responsive acceptance criteria. Generate and commit lockfile, implement visual assets, complete UI acceptance and update this handoff before design approval.

## Visual V2 implementation increment · 2026-11-08
Commits on the same draft PR #1:
- Real 12px-grid pixel-art icons for the dock, product cards and menu, with consistent colors.
- Integrated approved pixelated portrait at `public/portrait-carles-pixel.png` (112×112 optimized PNG). The image retains the yellow glasses.
- Two CSS-generated landscapes: Sunset with banded lime sun, and Night with a pixel moon and stars. Design tokens replace the earlier simplistic theme filter.
- Reworked viewport-relative window positioning, CRT frame, menus, contact, service note and project grid toward the reference illustration.
- Desktop title bar pointer drag with boundary guards; mobile remains non-draggable.
- Sunset defaults; CAT/ES/EN and appearance preferences saved on the client.
- Nuxt static-asset paths respect `NUXT_APP_BASE_URL=/curriculum-vitae/`.

Validation note: an intermediate commit passed CI after fixing strict sprite typing. The final branch SHA and Pages deployment must be checked separately before declaring this increment verified. Screenshot-diff and mobile/keyboard acceptance remain pending; do not claim exact illustration parity.

## Approved wallpaper assets · 2026-11-09

The user approved two generated 1536x1024 landscape illustrations: Sunset (lime striped setting sun, violet/pink mountains) and Night (moon, cool blue/violet mountains). `app/pages/index.vue` now computes baseURL-aware image paths and renders the appropriate image for the existing theme control. `app/assets/css/os.css` displays image assets beneath the real desktop UI. Failed image loads fall back to the existing CSS landscape.

**Outstanding blocker:** binary WebP assets could not be uploaded through this session's GitHub text-file connector. The intended files, already prepared in a separate ZIP, MUST be committed before this visual change is considered implemented:
- `public/wallpapers/sunset.webp` (1536x1024)
- `public/wallpapers/night.webp` (1536x1024)

After upload: verify GitHub Pages assets return HTTP 200, both appearance modes, crop on 922x616 and 390x844, and latest CI. Do not claim that GitHub Pages has the approved art until both files are present in the repository. Do not merge or publish the site yet.
