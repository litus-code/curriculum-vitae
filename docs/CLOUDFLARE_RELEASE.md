# Publicación en Cloudflare Pages · carlesfar.com

Estado: **repositorio preparado, Cloudflare sin conectar todavía**.

## Configuración de Cloudflare Pages

Desde la cuenta de Cloudflare, selecciona **Workers & Pages → Create → Pages → Import an existing Git repository** y conecta `litus-code/curriculum-vitae`.

| Ajuste | Valor |
|---|---|
| Project name | carles-far-os (si está disponible) |
| Framework | Nuxt (salida estática) |
| Production branch | main |
| Node.js | NODE_VERSION=24.15.0 |
| Build command | npm run build:cloudflare |
| Build output directory | .output/public |
| Root directory | / |
| Environment variables | NUXT_APP_BASE_URL=/ (el script también lo fija) |

El script `scripts/build-cloudflare.sh` genera el PDF vigente con un entorno virtual de Python, construye Nuxt para raíz (`/`), comprueba la existencia de `index.html`, la página de privacidad y ambos enlaces al CV. **No publicar sin un primer despliegue satisfactorio en `*.pages.dev`.**

## Dominio y correo

1. Crear el proyecto y verificar el acceso en `*.pages.dev`, incluyendo las ventanas, modo Sunset/Night, menú móvil, formularios, correo de prueba y descarga del CV.
2. Obtener una copia de todos los DNS actuales de Arsys **antes** de transferir los servidores de nombres. Deben mantenerse MX, SPF, DKIM, DMARC y cualquier CNAME de correo / verificación. No cambiar la zona hasta identificar los valores efectivos.
3. Añadir `carlesfar.com` en **Pages → Custom domains**. Cloudflare exige que el dominio raíz sea una zona de Cloudflare, con sus nameservers delegados. No inventar los nameservers; utilizar los asignados por esa cuenta.
4. Configurar `www.carlesfar.com` como dominio adicional o redirección 301 a la raíz, conservando HTTPS.
5. Validar después de la delegación: web en raíz, `www`, /privacidad, PDF actualizado, FormSubmit activo y correo de Arsys (recepción y salida).

## GitHub

La PR #1 sigue en borrador. Fusionar en `main` solo cuando la compilación de Cloudflare en preview sea correcta y se haya confirmado el plan de salida. Los últimos trabajos GitHub Actions estaban bloqueados/fallidos: verificar el estado real de las ejecuciones y la cuenta de facturación antes de usar CI como evidencia de aceptación.

GitHub Pages y Cloudflare Pages son proveedores diferentes. Esta documentación no cambia DNS, no crea proyectos de Cloudflare ni despliega a carlesfar.com.

Referencias:
- https://developers.cloudflare.com/pages/framework-guides/deploy-a-nuxt-site/
- https://developers.cloudflare.com/pages/configuration/custom-domains/
- https://developers.cloudflare.com/pages/configuration/build-image/
- https://developers.cloudflare.com/dns/manage-dns-records/how-to/email-records/
