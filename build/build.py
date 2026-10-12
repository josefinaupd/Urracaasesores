"""Genera el sitio estático a partir de content.py.

Uso:  python3 build/build.py
Crea index.html en la raíz y <slug>/index.html por página, para conservar
las mismas URLs que la web original (/concursal, /contacto, ...).
"""
import re
from html import escape
from pathlib import Path

from content import FOOTER, NAV, PAGES, SITE_TITLE, pexels

ROOT = Path(__file__).resolve().parent.parent


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
                f'<button type="button" aria-expanded="false">{escape(label)}</button>'
                f'<ul class="sub">{sub}</ul></li>'
            )
        else:
            cur = " aria-current=page" if target == current else ""
            items.append(f'<li><a href="{target}"{cur}>{escape(label)}</a></li>')
    return "".join(items)


def blocks_html(blocks):
    out = []
    for b in blocks:
        kind = b[0]
        if kind == "h":
            out.append(f"<h{b[1]}>{escape(b[2])}</h{b[1]}>")
        elif kind == "p":
            out.append(f"<p>{escape(b[1])}</p>")
        elif kind == "ul":
            out.append("<ul>" + "".join(f"<li>{escape(i)}</li>" for i in b[1]) + "</ul>")
        elif kind == "pendiente":
            out.append(f'<p class="pendiente">[Texto pendiente — {escape(b[1])}]</p>')
    return "\n".join(out)


def img(src, alt):
    return f'<img src="{src}" alt="{escape(alt)}" loading="lazy">'


def section_html(s):
    layout = s["layout"]
    if layout == "banner":
        return (f'<section class="banner"><div class="bg">{img(s["image"], s["image_alt"])}</div>'
                f'<h1>{escape(s["heading"])}</h1></section>')
    if layout == "text":
        return f'<section class="text"><div class="wrap narrow">{blocks_html(s["blocks"])}</div></section>'
    if layout == "columns":
        cols = "".join(f'<div class="col">{blocks_html(c)}</div>' for c in s["columns"])
        return f'<section class="columns n{len(s["columns"])}"><div class="wrap">{cols}</div></section>'
    if layout == "split":
        cls = "split img-first" if s.get("image_first") else "split"
        return (f'<section class="{cls}"><div class="wrap">'
                f'<div class="content">{blocks_html(s["blocks"])}</div>'
                f'<div class="media">{img(s["image"], s["image_alt"])}</div></div></section>')
    if layout == "card":
        return (f'<section class="card"><div class="wrap">'
                f'<div class="content">{blocks_html(s["blocks"])}</div>'
                f'<div class="media">{img(s["image"], s["image_alt"])}</div></div></section>')
    raise ValueError(layout)


HOME = f"""
<section class="hero">
  <div class="bg">{img(pexels(6077447), "Firma de un documento")}</div>
  <div class="wrap">
    <h1>Conectando contigo</h1>
    <p>Escuchamos tu historia y elegimos juntos el mejor camino a seguir</p>
    <a class="btn" href="/contacto">Contacto</a>
  </div>
</section>
"""

CONTACT = """
<section class="contact"><div class="wrap">
  <div class="info">
    <h2>Contacto</h2>
    <hr>
    <p>C. Mayor Principal, 15</p>
    <p>Piso 2D, 34001 Palencia, España</p>
    <p>(+34) 979 74 43 58</p>
  </div>
  <form class="form" action="mailto:info@urracaasesores.com" method="post" enctype="text/plain">
    <fieldset>
      <legend>Nombre</legend>
      <div class="row">
        <label>Nombre <span>(obligatorio)</span><input name="Nombre" required></label>
        <label>Apellido <span>(obligatorio)</span><input name="Apellido" required></label>
      </div>
    </fieldset>
    <label>Email <span>(obligatorio)</span><input type="email" name="Email" required></label>
    <label>Asunto <span>(obligatorio)</span><input name="Asunto" required></label>
    <label>Mensaje <span>(obligatorio)</span><textarea name="Mensaje" rows="5" required></textarea></label>
    <button class="btn dark" type="submit">Enviar</button>
  </form>
</div></section>
"""


def footer_html():
    cols = "".join(
        f'<div><h4>{escape(h)}</h4>{"".join(f"<p>{escape(l)}</p>" for l in lines)}</div>'
        for h, lines in FOOTER.items()
    )
    return (f'<footer><div class="info"><div class="wrap">{cols}</div></div>'
            f'<div class="legal"><a href="/aviso-legal">Aviso legal</a></div></footer>')


def page(path, title, body):
    full_title = SITE_TITLE if not title else f"{title} — {SITE_TITLE}"
    return f"""<!doctype html>
<html lang="es">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{escape(full_title)}</title>
<link rel="icon" href="/assets/favicon.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=DM+Sans:wght@300;400;500&display=swap" rel="stylesheet">
<link rel="stylesheet" href="/assets/style.css">
</head>
<body>
<a class="skip" href="#page">Saltar al contenido</a>
<header>
  <div class="wrap">
    <a class="brand" href="/"><img src="/assets/logo.webp" alt="{SITE_TITLE}"></a>
    <button class="burger" type="button" aria-label="Menú" aria-expanded="false"><span></span><span></span></button>
    <nav><ul>{nav_html(path)}</ul></nav>
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


def relativize(path, html):
    """Convierte las rutas absolutas (/assets, /concursal...) en relativas para que
    la web funcione también dentro de una subcarpeta (p. ej. GitHub Pages)."""
    prefix = "" if path == "/" else "../"

    def fix(m):
        attr, target = m.group(1), m.group(2)
        if target == "":
            url = prefix or "./"
        elif target.startswith("assets/"):
            url = prefix + target
        else:
            url = prefix + target + "/"
        return f'{attr}="{url}"'

    return re.sub(r'(href|src)="/(?!/)([^"]*)"', fix, html)


def write(path, html):
    html = relativize(path, html)
    out = ROOT / ("index.html" if path == "/" else f"{path.strip('/')}/index.html")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(html, encoding="utf-8")
    print("escrito", out.relative_to(ROOT))


def main():
    write("/", page("/", "", HOME))
    write("/contacto", page("/contacto", "Contacto", CONTACT))
    for slug, p in PAGES.items():
        body = "\n".join(section_html(s) for s in p["sections"])
        write(f"/{slug}", page(f"/{slug}", p["title"], body))


if __name__ == "__main__":
    main()
