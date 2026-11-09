#!/usr/bin/env bash
set -euo pipefail

# Cloudflare Pages: produce a static Nuxt 4 site with the CURRENT CV PDF.
# Cloudflare Pages needs NODE_VERSION=24.15.0 (or a compatible Node 24).
# Nuxt's GitHub Pages preview uses /curriculum-vitae/; production uses /.
export NUXT_APP_BASE_URL="/"

python3 -m venv /tmp/carlesfar-cv-build-venv
/tmp/carlesfar-cv-build-venv/bin/python -m pip install --disable-pip-version-check reportlab pillow
/tmp/carlesfar-cv-build-venv/bin/python scripts/build_cv_pdf.py

npm run generate

test -s .output/public/index.html
test -s .output/public/carles-far-cv-v2-1.pdf
test -s .output/public/carles-far-cv.pdf
test -s .output/public/privacidad/index.html
cmp .output/public/carles-far-cv-v2-1.pdf .output/public/carles-far-cv.pdf
printf 'Cloudflare Pages output ready: .output/public\n'
