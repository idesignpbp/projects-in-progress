"""
build_prd.py -- regenerate skiffle-marketing/prd/index.html from the PRD Slack canvas.

The /prd page is the ONLY Slack-sourced page on the site. Workflow:
  1. Edit the "PRD [v1.1]" canvas in the #skiffle Slack channel.
  2. Re-pull the canvas markdown into prd_source.md (Claude does this via the
     Slack connector: read canvas F0BJ7S5UT6Y, save the markdown_content field).
  3. Run:  python3 tools/build_prd.py
     -> rewrites ../prd/index.html (tables, status badges, sticky TOC).

Dependency: the `markdown` package  (pip install markdown).
Presentation/layout lives in the TEMPLATE string below; content lives in Slack.
"""
import os, markdown, re, html as _html

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "prd_source.md")
OUT = os.path.join(HERE, "..", "prd", "index.html")

raw = open(SRC).read()

# Version label, read from the canvas title line "# PRD [v1.2]" so page stays in sync.
_mver = re.search(r'#\s*PRD\s*\[([^\]]+)\]', raw)
VERSION = _mver.group(1).strip() if _mver else "v1.1"
SYNCED = "13 Aug 2026"  # date of the last canvas sync

# Split off the two leading H1s (title + doc title) for the hero; body starts at Stakeholder overview
idx = raw.index("## Stakeholder overview")
body_md = raw[idx:]
# Drop the manual "Contents" bullet list (the sticky sidebar TOC replaces it),
# but preserve the author/stakeholder metadata table that follows it.
body_md = re.sub(r'\n## Contents\n.*?(?=\n\|\|\|)', '\n', body_md, count=1, flags=re.S)
# Self-heal stray single-hash numbered section headings ("# 24. Foo" -> "## 24. Foo")
# so every numbered section renders as an H2 and lands in the sidebar TOC.
body_md = re.sub(r'(?m)^#\s+(\d+\.\s)', r'## \1', body_md)

md = markdown.Markdown(extensions=["tables", "fenced_code", "sane_lists", "toc", "attr_list"],
                       extension_configs={"toc": {"permalink": False}})
body = md.convert(body_md)

# ---- Status badges ----
TAGS = {
    "LOCKED": "locked", "DECIDED": "decided", "TENTATIVE": "tentative",
    "NEEDS DISCUSSION": "discuss", "OPEN": "open", "CANDIDATE": "candidate",
    "V2+": "v2", "PRELIMINARY": "prelim", "WATCH": "watch", "FIX": "fix",
    "VERIFIED": "verified",
}
def badge(tag):
    slug = TAGS[tag]
    return f'<span class="badge badge--{slug}">{_html.escape(tag)}</span>'

# Bold bracketed legend form: <strong>[LOCKED]</strong>  (longest first)
for tag in sorted(TAGS, key=len, reverse=True):
    esc = re.escape(tag)
    body = re.sub(r'<strong>\[' + esc + r'\]</strong>', badge(tag), body)

# Bare status-cell form: <td>DECIDED</td>  (and cells that are only the tag)
def cell_repl(m):
    inner = m.group(1).strip()
    if inner in TAGS:
        return f'<td>{badge(inner)}</td>'
    return m.group(0)
body = re.sub(r'<td>([^<]+)</td>', cell_repl, body)

# ---- Wrap tables for horizontal scroll ----
body = body.replace("<table>", '<div class="table-wrap"><table>').replace("</table>", "</table></div>")

# ---- Build sidebar TOC from h2 headings ----
heads = re.findall(r'<h2 id="([^"]+)">(.*?)</h2>', body, re.S)
toc_items = []
for hid, txt in heads:
    label = re.sub(r'<[^>]+>', '', txt).strip()
    toc_items.append(f'<a href="#{hid}">{_html.escape(label)}</a>')
toc_html = "\n        ".join(toc_items)

TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Skiffle PRD __VERSION__ — Product Requirements Document</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,500;0,600;0,700;1,500;1,600&family=Playfair+Display:ital,wght@0,500;0,600;0,700;1,500;1,600&family=IBM+Plex+Mono:wght@400;500&display=swap" rel="stylesheet">
<style>
  :root{
    --paper:#F4F0E6; --white:#FFFFFF; --ink:#14161C;
    --navy:#283466; --navy-soft:rgba(40,52,102,.62);
    --navy-line:rgba(40,52,102,.18); --navy-line-strong:rgba(40,52,102,.32);
    --cream:#EDE7D6; --cream-soft:rgba(237,231,214,.72); --sky:#9BB4E8;
    --serif:'Cormorant Garamond', Georgia, serif;
    --heading:'Playfair Display', 'Cormorant Garamond', Georgia, serif;
    --mono:'IBM Plex Mono', monospace;
    --maxw:1180px;
  }
  *{box-sizing:border-box; margin:0; padding:0;}
  html{scroll-behavior:smooth;}
  body{ background:var(--paper); color:var(--ink); font-family:var(--serif); font-weight:500; -webkit-font-smoothing:antialiased; }
  a{color:inherit;}
  .wrap{ max-width:var(--maxw); margin:0 auto; padding:0 32px; }
  @media (max-width:640px){ .wrap{ padding:0 20px; } }

  /* ---- proto banner ---- */
  .proto-banner{ background:var(--ink); }
  .proto-banner .wrap{ padding:11px 32px; text-align:center; }
  .proto-banner__text{ font-family:var(--mono); font-size:11px; line-height:1.6; letter-spacing:.02em; color:rgba(237,231,214,.75); }
  .proto-banner__text strong{ color:var(--sky); font-weight:600; }

  /* ---- nav ---- */
  nav{ position:sticky; top:0; z-index:50; background:rgba(244,240,230,.9); backdrop-filter:blur(8px); -webkit-backdrop-filter:blur(8px); border-bottom:1px solid var(--navy-line-strong); }
  nav .wrap{ display:flex; align-items:center; justify-content:space-between; height:78px; }
  .brand{ display:flex; align-items:baseline; gap:11px; text-decoration:none; }
  .brand .word{ font-family:var(--heading); font-weight:700; font-size:23px; letter-spacing:.03em; color:var(--navy); }
  .nav-right{ display:flex; gap:26px; align-items:center; }
  .nav-link{ font-family:var(--mono); font-size:11px; letter-spacing:.14em; text-transform:uppercase; color:rgba(20,22,28,.58); text-decoration:none; position:relative; padding-bottom:5px; transition:color .2s; }
  .nav-link::after{ content:''; position:absolute; left:0; right:100%; bottom:0; height:1px; background:var(--navy); transition:right .2s; }
  .nav-link:hover{ color:var(--navy); } .nav-link:hover::after{ right:0; }
  .nav-cta{ font-family:var(--mono); font-size:11px; letter-spacing:.14em; text-transform:uppercase; color:var(--navy); border:1px solid var(--navy); padding:10px 18px; text-decoration:none; transition:background .2s,color .2s; }
  .nav-cta:hover{ background:var(--navy); color:var(--paper); }
  @media (max-width:520px){ .nav-right{ gap:16px; } }

  /* ---- title block ---- */
  .doc-head{ border-bottom:1px solid var(--navy-line); padding:72px 0 44px; }
  .eyebrow{ font-family:var(--mono); font-size:11px; letter-spacing:.24em; text-transform:uppercase; color:var(--navy); }
  .doc-head h1{ font-family:var(--heading); font-weight:600; font-size:clamp(34px,5vw,58px); line-height:1.06; color:var(--ink); margin:18px 0 0; letter-spacing:.002em; }
  .doc-head h1 em{ font-style:italic; font-weight:500; color:var(--navy); }
  .doc-head .lede{ font-size:19px; line-height:1.7; color:var(--ink); max-width:640px; margin-top:22px; }
  .doc-meta{ display:flex; flex-wrap:wrap; gap:8px 26px; margin-top:30px; font-family:var(--mono); font-size:11px; letter-spacing:.04em; color:var(--navy-soft); text-transform:uppercase; }
  .doc-meta b{ color:var(--navy); font-weight:600; }

  /* ---- layout: sidebar + content ---- */
  .doc-layout{ display:grid; grid-template-columns:230px minmax(0,1fr); gap:56px; padding:56px 0 100px; align-items:start; }
  @media (max-width:900px){ .doc-layout{ grid-template-columns:1fr; gap:0; } }

  .toc{ position:sticky; top:104px; }
  @media (max-width:900px){ .toc{ display:none; } }
  .toc .toc-label{ font-family:var(--mono); font-size:10px; letter-spacing:.2em; text-transform:uppercase; color:var(--navy-soft); margin-bottom:16px; }
  .toc a{ display:block; font-family:var(--mono); font-size:11px; line-height:1.5; letter-spacing:.02em; color:rgba(20,22,28,.6); text-decoration:none; padding:6px 0 6px 12px; border-left:1px solid var(--navy-line); transition:color .18s,border-color .18s; }
  .toc a:hover{ color:var(--navy); border-left-color:var(--navy); }

  /* ---- prose ---- */
  .prose{ max-width:760px; }
  .prose > *{ scroll-margin-top:104px; }
  .prose h2{ font-family:var(--heading); font-weight:600; font-size:clamp(24px,3vw,34px); line-height:1.2; color:var(--ink); margin:56px 0 8px; padding-top:26px; border-top:1px solid var(--navy-line); letter-spacing:.002em; }
  .prose h2:first-child{ margin-top:0; border-top:none; padding-top:0; }
  .prose h3{ font-family:var(--heading); font-weight:600; font-size:21px; color:var(--navy); margin:38px 0 6px; }
  .prose h4{ font-family:var(--mono); font-size:11px; letter-spacing:.14em; text-transform:uppercase; color:var(--navy); margin:26px 0 4px; }
  .prose p{ font-size:16.5px; line-height:1.75; color:var(--ink); margin:14px 0; }
  .prose ul, .prose ol{ margin:14px 0 14px 24px; }
  .prose li{ font-size:16.5px; line-height:1.72; color:var(--ink); margin:7px 0; }
  .prose strong{ font-weight:600; color:var(--ink); }
  .prose em{ font-style:italic; }
  .prose a{ color:var(--navy); text-underline-offset:3px; }
  .prose hr{ border:none; border-top:1px solid var(--navy-line); margin:34px 0; }
  .prose code{ font-family:var(--mono); font-size:12.5px; background:var(--cream); border:1px solid var(--navy-line); border-radius:3px; padding:1px 6px; color:var(--navy); }
  .prose pre{ background:var(--ink); color:var(--cream-soft); font-family:var(--mono); font-size:13px; line-height:1.6; padding:18px 20px; overflow-x:auto; margin:18px 0; }
  .prose pre code{ background:none; border:none; padding:0; color:inherit; }
  .prose blockquote{ border-left:2px solid var(--navy); padding:4px 0 4px 20px; margin:18px 0; color:var(--navy-soft); font-style:italic; }

  /* ---- tables ---- */
  .table-wrap{ overflow-x:auto; margin:22px 0; border:1px solid var(--navy-line); }
  table{ border-collapse:collapse; width:100%; min-width:520px; background:var(--white); }
  thead th{ font-family:var(--mono); font-size:10px; letter-spacing:.12em; text-transform:uppercase; color:var(--navy); text-align:left; padding:12px 16px; background:var(--cream); border-bottom:1px solid var(--navy-line-strong); white-space:nowrap; }
  tbody td{ font-family:var(--serif); font-size:15px; line-height:1.6; color:var(--ink); padding:12px 16px; border-bottom:1px solid var(--navy-line); vertical-align:top; }
  tbody tr:last-child td{ border-bottom:none; }
  tbody tr:nth-child(even) td{ background:rgba(237,231,214,.32); }

  /* ---- status badges ---- */
  .badge{ display:inline-block; font-family:var(--mono); font-size:9.5px; font-weight:500; letter-spacing:.1em; text-transform:uppercase; padding:3px 8px; border-radius:2px; white-space:nowrap; border:1px solid transparent; }
  .badge--locked{ background:var(--navy); color:var(--paper); }
  .badge--decided{ background:rgba(40,52,102,.12); color:var(--navy); border-color:var(--navy-line-strong); }
  .badge--verified{ background:rgba(46,110,74,.14); color:#2E6E4A; border-color:rgba(46,110,74,.4); }
  .badge--tentative,.badge--discuss,.badge--watch{ background:rgba(176,124,32,.14); color:#8A5E12; border-color:rgba(176,124,32,.4); }
  .badge--open,.badge--fix{ background:rgba(158,54,44,.13); color:#9E362C; border-color:rgba(158,54,44,.4); }
  .badge--candidate,.badge--prelim,.badge--v2{ background:rgba(20,22,28,.07); color:var(--navy-soft); border-color:var(--navy-line); }

  /* ---- footer ---- */
  footer{ background:var(--ink); padding:56px 0; }
  footer .word{ font-family:var(--heading); font-weight:700; font-size:28px; color:var(--paper); letter-spacing:.02em; }
  footer .tag{ font-family:var(--mono); font-size:10px; letter-spacing:.24em; text-transform:uppercase; color:var(--sky); margin-top:9px; }
  footer .desc{ font-family:var(--serif); font-size:14px; line-height:1.8; max-width:420px; color:rgba(237,231,214,.65); margin-top:14px; }
  footer a{ color:var(--sky); }
</style>
</head>
<body>

<div class="proto-banner">
  <div class="wrap">
    <p class="proto-banner__text"><strong>Vision Marketing Site:</strong> This site is to help communicate the project internally, not to customers.</p>
  </div>
</div>

<nav>
  <div class="wrap">
    <a class="brand" href="../"><span class="word">Skiffle</span></a>
    <div class="nav-right">
      <a class="nav-link" href="../current-app/">Current App</a>
      <a class="nav-cta" href="../prd/">Review the PRD</a>
    </div>
  </div>
</nav>

<header class="doc-head">
  <div class="wrap">
    <span class="eyebrow">Product Requirements Document &middot; __VERSION__</span>
    <h1>Skiffle Rebuild<br><em>Mobile-first native app</em></h1>
    <p class="lede">Rebuilding the Skiffle dealer app as a true native app for iPhone and Android, replacing today's desktop build stretched onto a phone, so dealers get a faster, native experience they can trust in front of a client.</p>
    <div class="doc-meta">
      <span><b>Target release</b> &nbsp;v1 · Late Dec 2026</span>
      <span><b>Build</b> &nbsp;React Native · Expo · Replit</span>
      <span><b>Status</b> &nbsp;In review</span>
      <span><b>Last synced</b> &nbsp;__SYNCED__</span>
    </div>
  </div>
</header>

<div class="wrap">
  <div class="doc-layout">
    <aside class="toc">
      <div class="toc-label">Contents</div>
      <nav>
        __TOC__
      </nav>
    </aside>
    <main class="prose">
      __BODY__
    </main>
  </div>
</div>

<footer>
  <div class="wrap">
    <div class="word">Skiffle</div>
    <div class="tag">v1 &middot; Native rebuild</div>
    <p class="desc">Built for the floor, not the desktop. This PRD is maintained by the product team &mdash; <a href="../">return to the marketing site</a>.</p>
  </div>
</footer>

</body>
</html>
"""

page = (TEMPLATE.replace("__TOC__", toc_html).replace("__BODY__", body)
        .replace("__VERSION__", VERSION).replace("__SYNCED__", SYNCED))
import os
os.makedirs(os.path.dirname(OUT), exist_ok=True)
open(OUT, "w").write(page)
print("Wrote", OUT, len(page), "chars")
print("TOC entries:", len(toc_items))
print("Tables:", body.count("<table>"))
print("Badges:", page.count('class="badge'))
