"""Genera el sitio estático a partir de content.py.

Uso:  python3 build/build.py
Crea index.html en la raíz y <slug>/index.html por página, para conservar
las mismas URLs que la web original (/concursal, /contacto, ...).
Todas las rutas se escriben relativas, así que la web funciona igual en un
dominio propio que dentro de una subcarpeta (GitHub Pages).
"""
import re
from datetime import date
from html import escape
from pathlib import Path

from content import (FOOTER, HOME_IMAGE, HOME_IMAGE_ALT, NAV, PAGES, REDIRECTS,
                     SITE_TITLE, pexels)

ROOT = Path(__file__).resolve().parent.parent

HERO_TITLE = "Conectando contigo"
HERO_TEXT = "Escuchamos tu historia y elegimos juntos el mejor camino a seguir"
ADDRESS = "C. Mayor Principal, 15, Piso 2D, 34001 Palencia, España"
PHONE = "(+34) 979 74 43 58"
PHONE_HREF = "tel:+34979744358"
EMAIL = "info@urracaasesores.com"
MAP_URL = "https://www.google.com/maps/search/?api=1&query=" + "C.+Mayor+Principal+15+34001+Palencia"
MAP_EMBED = "https://www.google.com/maps?q=C.+Mayor+Principal+15,+34001+Palencia&output=embed"

# Carpeta donde se publica la web (solo la usa la página 404, que GitHub Pages
# sirve desde cualquier ruta). Con dominio propio, dejar en "".
BASE_PATH = "/Urracaasesores"

ABOGADOS = next(t for l, t in NAV if isinstance(t, list))
ASESORES_SLUG = "urraca-asesores"


# ---------------------------------------------------------------- utilidades

def img(src, alt, cls="", eager=False):
    c = f' class="{cls}"' if cls else ""
    loading = "eager" if eager else "lazy"
    return f'<img{c} src="{src}" alt="{escape(alt)}" loading="{loading}" decoding="async">'


def blocks_html(blocks):
    out = []
    for b in blocks:
        kind = b[0]
        if kind == "h":
            lvl = max(2, b[1])
            out.append(f"<h{lvl}>{escape(b[2])}</h{lvl}>")
        elif kind == "p":
            out.append(f"<p>{escape(b[1])}</p>")
        elif kind == "ul":
            cls = ' class="cols"' if len(b[1]) >= 8 else ""
            out.append(f"<ul{cls}>" + "".join(f"<li>{escape(i)}</li>" for i in b[1]) + "</ul>")
        elif kind == "pendiente":
            out.append(f'<p class="pendiente">[Texto pendiente — {escape(b[1])}]</p>')
    return "\n".join(out)


def normalize(page):
    """Extrae de la estructura original: título, imagen y cuerpo."""
    heading = image = alt = None
    body = []
    for s in page["sections"]:
        if s["layout"] == "banner":
            heading, image, alt = s["heading"], s["image"], s["image_alt"]
            continue
        if s.get("image") and image is None:
            image, alt = s["image"], s["image_alt"]
        if "columns" in s:
            body.append(("columns", s["columns"]))
            continue
        blocks = list(s["blocks"])
        if heading is None and blocks and blocks[0][0] == "h":
            heading = blocks.pop(0)[2]
        if blocks:
            body.append(("card" if s["layout"] == "card" else "blocks", blocks))
    return heading, image, alt, body


def section_of(slug):
    if slug == ASESORES_SLUG:
        return "Urraca Asesores"
    if any(h == f"/{slug}" for _, h in ABOGADOS):
        return "Urraca Abogados"
    return None


# ---------------------------------------------------------------- piezas

def nav_html(current):
    items = []
    for label, target in NAV:
        if isinstance(target, list):
            active = any(href == current for _, href in target)
            sub = "".join(
                f'<li><a href="{href}"{" aria-current=page" if href == current else ""}>{escape(l)}</a></li>'
                for l, href in target
            )
            items.append(
                f'<li class="has-sub{" active" if active else ""}">'
                f'<button type="button" aria-expanded="false">{escape(label)}'
                f'<svg viewBox="0 0 10 6" aria-hidden="true"><path d="M1 1l4 4 4-4"/></svg></button>'
                f'<ul class="sub">{sub}</ul></li>'
            )
        else:
            cur = " aria-current=page" if target == current else ""
            items.append(f'<li><a href="{target}"{cur}>{escape(label)}</a></li>')
    return "".join(items)


def cta_html():
    return f"""
<section class="cta">
  <div class="wrap">
    <h2>{HERO_TITLE}</h2>
    <p>{HERO_TEXT}</p>
    <a class="btn" href="/contacto">Contacto</a>
  </div>
</section>"""


def footer_html():
    loc, hours, contact = FOOTER["Ubicación"], FOOTER["Horario de verano"], FOOTER["Contacto"]
    return f"""
<footer>
  <div class="wrap grid">
    <div class="f-brand">
      <a href="/"><img src="/assets/logo-white.png" alt="{SITE_TITLE}" width="1000" height="115"></a>
    </div>
    <div>
      <h4>Ubicación</h4>
      <p><a href="{MAP_URL}" target="_blank" rel="noopener">{escape(loc[0])}<br>{escape(loc[1])}</a></p>
    </div>
    <div>
      <h4>Horario de verano</h4>
      {"".join(f"<p>{escape(l)}</p>" for l in hours)}
    </div>
    <div>
      <h4>Contacto</h4>
      <p><a href="{PHONE_HREF}">{escape(contact[0])}</a></p>
      <p>e-mail: <a href="mailto:{EMAIL}">{EMAIL}</a></p>
    </div>
  </div>
  <div class="wrap bottom">
    <span>© {date.today().year} Urraca Asesores, SL.</span>
    <a href="/aviso-legal">Aviso legal</a>
  </div>
</footer>"""


def page_header(eyebrow, heading, image, alt):
    eb = f'<p class="eyebrow">{escape(eyebrow)}</p>' if eyebrow else ""
    if not image:
        return f'<section class="page-head plain"><div class="wrap">{eb}<h1>{escape(heading)}</h1></div></section>'
    return (f'<section class="page-head"><div class="bg">{img(image, alt, eager=True)}</div>'
            f'<div class="wrap">{eb}<h1>{escape(heading)}</h1></div></section>')


def other_areas(current):
    links = "".join(
        f'<li><a href="{h}"{" aria-current=page" if h == current else ""}>{escape(l)}</a></li>'
        for l, h in ABOGADOS
    )
    return f'<aside class="areas"><h2 class="label">Urraca Abogados</h2><ul>{links}</ul></aside>'


# ---------------------------------------------------------------- páginas

def service_page(slug, page):
    heading, image, alt, body = normalize(page)
    path = f"/{slug}"
    group = section_of(slug)
    parts = [page_header(group, heading, image, alt)]
    content = []
    for kind, data in body:
        if kind == "columns":
            cols = "".join(f'<div class="col">{blocks_html(c)}</div>' for c in data)
            content.append(f'<div class="columns n{len(data)}">{cols}</div>')
        elif kind == "card":
            content.append(f'<div class="card">{blocks_html(data)}</div>')
        else:
            content.append(f'<div class="prose">{blocks_html(data)}</div>')
    side = other_areas(path) if group == "Urraca Abogados" else ""
    layout = "article with-side" if side else "article"
    parts.append(f'<section class="{layout}"><div class="wrap"><div class="main">{"".join(content)}</div>{side}</div></section>')
    if slug != "aviso-legal":
        parts.append(cta_html())
    return "\n".join(parts)


def home_page():
    _, ases_img, ases_alt, ases_body = normalize(PAGES[ASESORES_SLUG])
    ases_cols = ases_body[0][1]
    ases_cards = "".join(
        f'<a class="svc" href="/{ASESORES_SLUG}"><h3>{escape(c[0][2].capitalize())}</h3>'
        f'<p>{escape(c[1][1])}</p><span class="more" aria-hidden="true">→</span></a>'
        for c in ases_cols
    )
    tiles = []
    for label, href in ABOGADOS:
        _, image, alt, _ = normalize(PAGES[href.strip("/")])
        thumb = image.replace("w=2000", "w=900")
        tiles.append(
            f'<a class="tile" href="{href}">{img(thumb, alt)}<span>{escape(label)}</span></a>'
        )
    return f"""
<section class="hero">
  <div class="bg">{img(HOME_IMAGE, HOME_IMAGE_ALT, eager=True)}</div>
  <div class="wrap">
    <h1>{HERO_TITLE}</h1>
    <p>{HERO_TEXT}</p>
    <a class="btn" href="/contacto">Contacto</a>
  </div>
</section>

<section class="home-block">
  <div class="wrap split">
    <div class="intro">
      <h2 class="label">Urraca Asesores</h2>
      <h3 class="big">ASESORIA.</h3>
      {img(ases_img.replace("w=2000", "w=1200"), ases_alt, "intro-img")}
    </div>
    <div class="svc-list">{ases_cards}</div>
  </div>
</section>

<section class="home-block alt">
  <div class="wrap">
    <h2 class="label">Urraca Abogados</h2>
    <div class="tiles">{"".join(tiles)}</div>
  </div>
</section>
{cta_html()}
"""


def contact_page():
    loc = FOOTER["Ubicación"]
    return f"""
<section class="page-head plain"><div class="wrap"><h1>Contacto</h1></div></section>
<section class="contact">
  <div class="wrap">
    <div class="info">
      <p><a href="{MAP_URL}" target="_blank" rel="noopener">C. Mayor Principal, 15<br>Piso 2D, 34001 Palencia, España</a></p>
      <p><a href="{PHONE_HREF}">{PHONE}</a></p>
      <p><a href="mailto:{EMAIL}">{EMAIL}</a></p>
      <div class="hours">
        <h4>Horario de verano</h4>
        {"".join(f"<p>{escape(l)}</p>" for l in FOOTER["Horario de verano"])}
      </div>
    </div>
    <form class="form" action="mailto:{EMAIL}" method="post" enctype="text/plain">
      <fieldset>
        <legend>Nombre</legend>
        <div class="row">
          <label>Nombre <span>(obligatorio)</span><input name="Nombre" autocomplete="given-name" required></label>
          <label>Apellido <span>(obligatorio)</span><input name="Apellido" autocomplete="family-name" required></label>
        </div>
      </fieldset>
      <label>Email <span>(obligatorio)</span><input type="email" name="Email" autocomplete="email" required></label>
      <label>Asunto <span>(obligatorio)</span><input name="Asunto" required></label>
      <label>Mensaje <span>(obligatorio)</span><textarea name="Mensaje" rows="6" required></textarea></label>
      <button class="btn dark" type="submit">Enviar</button>
    </form>
  </div>
</section>
<section class="map">
  <iframe src="{MAP_EMBED}" title="Mapa: {escape(loc[0])}, Palencia" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe>
</section>
"""


# ---------------------------------------------------------------- plantilla

def page(path, title, body, image=None, description=None):
    full_title = SITE_TITLE if not title else f"{title} — {SITE_TITLE}"
    desc = description or HERO_TEXT
    og_image = (image or HOME_IMAGE).replace("w=2000", "w=1200")
    return f"""<!doctype html>
<html lang="es">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{escape(full_title)}</title>
<meta name="description" content="{escape(desc)}">
<meta property="og:type" content="website">
<meta property="og:site_name" content="{SITE_TITLE}">
<meta property="og:title" content="{escape(full_title)}">
<meta property="og:description" content="{escape(desc)}">
<meta property="og:image" content="{og_image}">
<meta property="og:locale" content="es_ES">
<meta name="twitter:card" content="summary_large_image">
<meta name="theme-color" content="#1c2229">
<link rel="icon" href="/assets/favicon.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="preconnect" href="https://images.pexels.com">
<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@500;600&family=DM+Sans:opsz,wght@9..40,300;9..40,400;9..40,500&display=swap" rel="stylesheet">
<link rel="stylesheet" href="/assets/style.css">
</head>
<body>
<a class="skip" href="#page">Saltar al contenido</a>
<header class="site">
  <div class="wrap">
    <a class="brand" href="/"><img src="/assets/logo.png" alt="{SITE_TITLE}" width="1000" height="115"></a>
    <button class="burger" type="button" aria-label="Menú" aria-expanded="false"><span></span><span></span></button>
    <nav aria-label="Principal"><ul>{nav_html(path)}</ul></nav>
  </div>
</header>
<main id="page">
{body}
</main>
{footer_html()}
<script src="/assets/site.js"></script>
</body>
</html>
"""


def redirect_page(target):
    return f"""<!doctype html>
<html lang="es"><head><meta charset="utf-8">
<title>{SITE_TITLE}</title>
<meta http-equiv="refresh" content="0; url=/{target}">
<link rel="canonical" href="/{target}">
</head><body><a href="/{target}">Continuar</a></body></html>
"""


def relativize(path, html):
    """Convierte las rutas absolutas (/assets, /concursal...) en relativas."""
    prefix = "" if path == "/" else "../"

    def fix(m):
        attr, target = m.group(1), m.group(2)
        if target == "":
            url = prefix or "./"
        elif target.startswith("assets/") or "." in target.split("/")[-1]:
            url = prefix + target
        else:
            url = prefix + target + "/"
        return f'{attr}="{url}"'

    html = re.sub(r'(href|src)="/(?!/)([^"]*)"', fix, html)
    return re.sub(r'url=/([^"]*)"', lambda m: f'url={prefix}{m.group(1)}/"', html)


def write(path, html):
    html = relativize(path, html)
    out = ROOT / ("index.html" if path == "/" else f"{path.strip('/')}/index.html")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(html, encoding="utf-8")
    print("escrito", out.relative_to(ROOT))


def main():
    write("/", page("/", "", home_page()))
    write("/contacto", page("/contacto", "Contacto", contact_page(),
                            description=f"Contacto — {ADDRESS} · {PHONE}"))
    for slug, p in PAGES.items():
        heading, image, _, _ = normalize(p)
        desc = f"{p['title']} — {SITE_TITLE}. {ADDRESS}."
        write(f"/{slug}", page(f"/{slug}", p["title"], service_page(slug, p), image, desc))
    for slug, target in REDIRECTS.items():
        write(f"/{slug}", redirect_page(target))
    (ROOT / "404.html").write_text(
        page("/404", "Página no encontrada",
             '<section class="page-head plain"><div class="wrap"><h1>404</h1>'
             '<p><a class="btn dark" href="/">Inicio</a></p></div></section>'
             ).replace('href="/', f'href="{BASE_PATH}/').replace('src="/', f'src="{BASE_PATH}/'),
        encoding="utf-8")


if __name__ == "__main__":
    main()
