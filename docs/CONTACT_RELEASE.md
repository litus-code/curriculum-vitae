# Carles Far OS · Contacto y publicación

## Estado (9 noviembre 2026)

El formulario antes abría `mailto:`. Ahora envía datos mediante POST JSON a FormSubmit (AJAX) y mantiene al visitante en Carles Far OS. Contiene validación de nombre, correo y mensaje; prevención de doble envío; campo trampa antispam; aviso de privacidad breve; estado de envío, aceptación y error; enlace alternativo de correo y servicios seleccionados desde el post-it.

## Destinatario

**Destinatario confirmado por el propietario: `contacto@carlesfar.com` (9 de noviembre de 2026).** El formulario, los enlaces de respuesta y el aviso de privacidad utilizan esta dirección. La activación de FormSubmit y la recepción real en el buzón todavía deben comprobarse. No se ha enviado ningún mensaje de prueba desde GitHub.

## Activación obligatoria

FormSubmit requiere activar el destinatario. El propietario debe:

1. Abrir la preview publicada, entrar en Contacto, rellenar un mensaje de prueba legítimo y enviarlo.
2. Consultar el buzón del destinatario elegido y la carpeta de correo no deseado.
3. Confirmar el enlace de activación recibido de FormSubmit.
4. Enviar una segunda prueba desde el formulario y confirmar su recepción.
5. Comprobar que el campo Reply-To corresponde al visitante, que el servicio seleccionado llega y que el formulario muestra mensajes de error ante fallos.
6. Probar en móvil, con teclado, y con los idiomas ES/CA/EN.

El mensaje de éxito de la web solo significa que el proveedor aceptó la solicitud, no que el correo haya llegado al buzón. La página de privacidad se encuentra en `/privacidad` y la acción de enviar requiere aceptar ese aviso.

Documentación del servicio: https://formsubmit.co/documentation y https://formsubmit.co/ajax-documentation

## Privacidad

FormSubmit es un tercero que procesa nombre, dirección de correo, servicio seleccionado y mensaje; su documentación indica que conserva envíos en archivo durante 30 días. La web debería incorporar un aviso de privacidad accesible antes de publicar comercialmente, especificando responsable y tratamiento de consultas. Evitar añadir contraseñas u otros datos confidenciales al formulario.

## Publicación y reversión

Actualmente la preview está en `litus-code.github.io/curriculum-vitae/`, desde la rama `feat/carles-far-os-nuxt4-foundation`; `main` no despliega el dominio público. No se debe anunciar `carlesfar.com` actualizado hasta decidir dónde se alojará, configurar dominio y DNS, fusionar PR, comprobar HTTPS, verificar el CV PDF, formulario y funcionalidad móvil.

La activación de FormSubmit y el despliegue a `carlesfar.com` **quedan pendientes de validación del propietario**.
