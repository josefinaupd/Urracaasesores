# Urraca Asesores y Abogados — web estática

Rediseño de www.urracaasesores.com como web estática: mismas páginas, mismas URLs, mismo menú y mismos textos, con un diseño nuevo.

## Estructura
- `index.html` y `<pagina>/index.html`: páginas generadas, listas para subir a cualquier hosting (GitHub Pages, Netlify, etc.).
- `assets/`: estilos, script del menú, logo y favicon.
- `build/content.py`: todo el contenido de la web (textos, listas, imágenes).
- `build/build.py`: generador. Tras editar el contenido: `python3 build/build.py`.

## Imágenes
Todas las fotos son de **Pexels** (licencia gratuita) y se cargan directamente desde su CDN por URL,
así que no hay que alojarlas. Para cambiar una, sustituye el número de foto de Pexels en `build/content.py`
(`pexels(ID)`). Solo el logo (`logo.png` oscuro y `logo-white.png` para el pie) y el favicon están en `assets/`.

## Textos pendientes
Los párrafos largos de redacción (introducciones de algunas áreas y los apartados del aviso legal) aparecen
como recuadros `[Texto pendiente — ...]`. Para completarlos, cambia cada `("pendiente", "...")` en
`build/content.py` por `("p", "texto del párrafo")` y vuelve a generar.

## Formulario de contacto
Al ser una web estática, el formulario abre el cliente de correo (`mailto:info@urracaasesores.com`).
Para que envíe directamente, hay que conectarlo a un servicio de formularios (Netlify Forms, Formspree...).

## Publicación
- Publicada con GitHub Pages en `https://josefinaupd.github.io/Urracaasesores/`.
- Si se pasa a dominio propio, cambia `BASE_PATH` a `""` en `build/build.py` (solo afecta a la página 404) y vuelve a generar.
- `/urraca-abogados-1` (una copia de "Concursal" en la web original) redirige a `/concursal`.
