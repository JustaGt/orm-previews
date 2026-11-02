#!/usr/bin/env python3
"""Build an ORM sample site from a JSON spec using the Ash & Ember design system."""
import json, sys, html, os, re

HERE = os.path.dirname(os.path.abspath(__file__))
BASE_CSS = open(os.path.join(HERE, 'base.css')).read()
BASE_JS = open(os.path.join(HERE, 'base.js')).read()
HOURS_JS = open(os.path.join(HERE, 'hours.js')).read()

FONTS = {
    'gambarino': ("gambarino@400", "'Gambarino', 'Times New Roman', serif", 400, '-0.02em', '0.92', '0'),
    'clash': ("clash-display@500,600", "'Clash Display', 'Arial Narrow', sans-serif", 600, '-0.012em', '0.94', '.06em'),
    'zodiak': ("zodiak@400,500", "'Zodiak', Georgia, serif", 400, '-0.02em', '0.94', '0'),
    'cabinet': ("cabinet-grotesk@700,800", "'Cabinet Grotesk', 'Arial Narrow', sans-serif", 800, '-0.02em', '0.92', '0'),
    'sentient': ("sentient@400,500", "'Sentient', Georgia, serif", 400, '-0.02em', '0.95', '0'),
}

ARROW = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M5 12h14M13 6l6 6-6 6"/></svg>'

def e(t):
    return html.escape(t, quote=True)

def u(pid, w, h):
    return f"https://images.unsplash.com/{pid}?w={w}&h={h}&q=78&auto=format&fit=crop"

def pane_img(pid, k, on=False, eager=False):
    srcset = ", ".join(f"{u(pid, w, h)} {w}w" for w, h in [(700, 900), (1100, 1400), (1500, 1900)])
    cls = ' class="on"' if on else ''
    load = ' fetchpriority="high"' if eager else ' loading="lazy"'
    return f'<img{cls} data-k="{k}" src="{u(pid,1100,1400)}" srcset="{srcset}" sizes="(max-width:900px) 100vw, 46vw" alt=""{load}>'

def link_attrs(href):
    return f'href="{e(href)}"'

def a(label, href, cls=''):
    c = f' class="{cls}"' if cls else ''
    return f'<a{c} {link_attrs(href)}>{label}</a>'

def rows_html(groups):
    out = []
    for g in groups:
        rs = []
        for r in g['rows']:
            name, val = r[0], r[1]
            small = f'<small>{r[2]}</small>' if len(r) > 2 and r[2] else ''
            soft = ' soft' if (len(r) > 3 and r[3]) else ''
            rs.append(f'<div class="row"><span class="n">{name}{small}</span><span class="v{soft}">{val}</span></div>')
        h3 = f"<h3>{g['h3']}</h3>" if g.get('h3') else ''
        out.append(f'<div class="g rise">{h3}{"".join(rs)}</div>')
    return f'<div class="rows">{"".join(out)}</div>'

def build(s):
    t = s['theme']
    f = FONTS[s.get('font', 'gambarino')]
    root = (f":root{{--bg:{t['bg']};--surface:{t['surface']};--ink:{t['ink']};--muted:{t['muted']};--accent:{t['accent']};"
            f"--accent-ink:{t['accent_ink']};--band:{t.get('band', t['accent'])};--band-ink:{t.get('band_ink', t['accent_ink'])};--ok:{t.get('ok', '#3fbf6a')};"
            f"--display:{f[1]};--dw:{f[2]};--dt:{f[3]};--dl:{f[4]};--dws:{f[5]}}}")
    P = s['photos']
    name, short = s['name'], s['short']
    prim, sec = s['primary'], s.get('secondary')
    nav = ''.join(a(l, h) for l, h in s['nav'])
    langs = ''
    if s.get('bilingual'):
        langs = '<div class="langs" role="group" aria-label="Language"><button type="button" data-l="es" aria-pressed="true">Español</button><button type="button" data-l="en" aria-pressed="false">English</button></div>'
    head = f'''<!doctype html>
<html lang="{s.get('lang','en')}"{' data-lang="es"' if s.get('bilingual') else ''}>
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{e(s['title'])}</title>
<meta name="description" content="{e(s['desc'])}">
<meta property="og:title" content="{e(s['title'])}">
<meta property="og:description" content="{e(s['desc'])}">
<meta property="og:image" content="{e(u(P['h'],1200,630))}">
<meta property="og:type" content="website">
<meta name="twitter:card" content="summary_large_image">
<meta name="theme-color" content="{t['bg']}">
<meta name="robots" content="noindex">
<link rel="icon" href="data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 64 64'><rect width='64' height='64' rx='14' fill='{t['accent'].replace('#','%23')}'/><text x='32' y='44' font-family='Georgia,serif' font-size='36' text-anchor='middle' fill='{t['accent_ink'].replace('#','%23')}'>{e(short[0])}</text></svg>">
<link rel="preconnect" href="https://api.fontshare.com">
<link rel="preconnect" href="https://cdn.fontshare.com" crossorigin>
<link rel="preconnect" href="https://images.unsplash.com">
<link href="https://api.fontshare.com/v2/css?f[]={f[0]}&f[]=general-sans@400,500,600&display=swap" rel="stylesheet">
<style>{root}
{BASE_CSS}{s.get('extra_css','')}</style>
</head>
<body>
'''
    ribbon = f'<div class="ribbon" id="top"><span>{s.get("ribbon","Sample website by Onyx Rise Media")}</span><span class="r2">Made for {e(name)}</span></div>\n'
    hero_btn = f'<a class="btn" {link_attrs(prim[1])}>{prim[0]}{ARROW}</a>'
    hero_link = f'<a class="link" {link_attrs(sec[1])}>{sec[0]}</a>' if sec else ''
    facts = ''.join(f'<span>{x}</span>' for x in s.get('facts', []))
    status = s.get('status_default', '')
    has_hours = bool(s.get('hours', {}).get('H'))
    dot_style = s.get('dot_style', '')
    status_html = (f'<p class="status rise" data-status><span class="dot" aria-hidden="true"></span><span class="st">{status}</span></p>' if has_hours
                   else f'<p class="status rise"><span class="dot" aria-hidden="true"{dot_style}></span><span class="st">{status}</span></p>')
    long = ' long' if len(short) > 12 else ''
    sv = s['services']
    about = s['about']
    stage1 = f'''<div class="stage s1">
<aside class="pane"><div class="mtop"><a class="mk" href="#top">{e(short)}</a>{langs}</div><div class="frame">{pane_img(P['h'],'h',True,True)}{pane_img(P['menu'],'menu')}{pane_img(P['about'],'about')}{f'<figcaption>{s["caption"]}</figcaption>' if s.get('caption') else ''}</div></aside>
<main class="col">
<header class="top"><a class="mark d" href="#top">{e(short)}</a><nav aria-label="Main">{nav}</nav>{langs}</header>
<section class="hero" data-k="h">
{status_html}
<h1 class="name d rise{long}">{s.get('h1_html', e(short))}</h1>
<p class="lead rise">{s['lead']}</p>
<div class="acts rise">{hero_btn}{hero_link}</div>
<div class="facts rise">{facts}</div>
</section>
<section class="sec" id="{sv.get('id','services')}" data-k="menu">
<h2 class="d rise">{sv['h2']}</h2>
{f'<p class="sub rise">{sv["sub"]}</p>' if sv.get('sub') else ''}
{sv.get('panel','')}
{rows_html(sv['groups'])}
{f'<p class="note rise">{sv["note"]}</p>' if sv.get('note') else ''}
</section>
<section class="sec" id="{about.get('id','about')}" data-k="about">
<h2 class="d rise">{about['h2']}</h2>
<div class="letter rise">{''.join(f'<p>{p}</p>' for p in about['ps'])}</div>
</section>
</main>
</div>
'''
    b = s['band']
    strip = ''.join(f'<img src="{u(pid, 1200 if i == 0 else 800, 900)}" alt="" loading="lazy">' for i, pid in enumerate(P['strip']))
    band = f'''<section class="band" aria-label="Reviews">
<div class="bt"><p class="fig d rise{' word' if b.get('word') else ''}">{b['fig']}</p><p class="bx rise">{b['bx']}<small>{b['small']}</small></p></div>
<div class="strip">{strip}</div>
</section>
'''
    hrs = s.get('hours', {'rows': []})
    hour_rows = ''.join(f'<div class="row"{f" data-day=\"{d}\"" if d is not None else ""}><span class="n">{lab}</span><span class="v">{val}</span></div>' for d, lab, val in hrs['rows'])
    vis = s['visit']
    vrows = []
    for r in vis['rows']:
        small, text, href = r[0], r[1], r[2]
        em = ' em' if len(r) > 3 and r[3] else ''
        if href:
            vrows.append(f'<a class="vrow d rise{em}" {link_attrs(href)}><small>{small}</small>{text}</a>')
        else:
            vrows.append(f'<p class="vrow d rise{em}"><small>{small}</small>{text}</p>')
    go = vis['go']
    s2a_html = s.get('areas_html') or f'''<section class="sec" id="hours" data-k="s2a">
<h2 class="d rise">{hrs.get('h2','Hours')}</h2>
<p class="sub rise"{' data-status' if has_hours else ''}><span class="st">{status}</span></p>
<div class="rows"><div class="g rise">{hour_rows}</div></div>
{f'<p class="note rise">{hrs["note"]}</p>' if hrs.get('note') else ''}
</section>'''
    stage2 = f'''<div class="stage flip s2">
<aside class="pane"><div class="frame">{pane_img(P['s2a'],'s2a',True)}{pane_img(P['visit'],'visit')}</div></aside>
<main class="col">
{s2a_html}
<section class="visit" id="visit" data-k="visit">
<h2 class="d rise">{vis.get('h2','Visit')}</h2>
{''.join(vrows)}
<a class="go d rise" {link_attrs(go[1])}>{go[0]}<i>{ARROW}</i></a>
</section>
</main>
</div>
'''
    ft = s['footer']
    fnav = ''.join(a(l, h, 'd') for l, h in ft['nav'])
    follow = ''.join(a(l, h) for l, h in ft['follow'])
    foot = f'''<footer class="foot">
<div class="fp"><img src="{u(P['foot'],1400,1600)}" alt="" loading="lazy"></div>
<div class="fm">
<p class="wm d">{e(short)}</p>
<nav aria-label="Footer">{fnav}</nav>
<div class="fc"><div><b>{e(name)}</b>{ft['contact']}</div><div><b>Follow</b>{follow}</div></div>
<p class="legal">Sample website made by <a href="https://justagt.github.io/orm-previews/">Onyx Rise Media</a> for {e(name)}. Stock photos stand in until yours go in. {ft['legal']}</p>
</div>
</footer>
'''
    dock = '<nav class="dock" aria-label="Quick actions">' + ''.join(
        f'<a class="{"p" if i == 0 else ""}" {link_attrs(h)}>{l}</a>' for i, (l, h) in enumerate(s['dock'])) + '</nav>\n'
    js = BASE_JS
    if has_hours:
        H = json.dumps(hrs['H'])
        hj = re.sub(r'var H=\[.*?\], L=', f'var H={H}, L=', HOURS_JS, count=1, flags=re.S)
        js += hj
    js += s.get('extra_js', '')
    return head + ribbon + stage1 + band + stage2 + foot + dock + '<script>\n' + js + '</script>\n</body>\n</html>\n'

if __name__ == '__main__':
    spec = json.load(open(sys.argv[1]))
    out = build(spec)
    open(sys.argv[2], 'w').write(out)
    print('wrote', sys.argv[2], len(out))
