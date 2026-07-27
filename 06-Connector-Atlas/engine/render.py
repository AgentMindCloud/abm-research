#!/usr/bin/env python3
"""Render atlas.html — a static, readable gallery of the discovered use cases.

No interactivity: a page you scan and evaluate. Claude is the hub; the page leads with a
"most potential" leaderboard across all sizes (so the highest-value use cases surface
regardless of connector count), features the one huge system that runs like a company, and
then lists the full catalogue grouped small -> medium -> large. Every use case plainly states
what it is for and which connectors it uses (with the one-line job each connector does).

Reuses only the HTML scaffolding (<!DOCTYPE>/charset/viewport) and the Cinnabar/jade palette
from the skill's atlas.py, plus a load-time scaffolding self-check (compatMode=CSS1Compat).

Usage:
    python3 render.py --out ../atlas.html
"""

import argparse
import html
import json
import math
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(HERE, "..", "data")

DOMAIN_COLOR = {
    "sales": "#E64A2E", "marketing": "#d2789b", "finance": "#5bc0be",
    "product_eng": "#7d9bd2", "support": "#d49a78", "hr": "#c9d478",
    "ops": "#e0b13e", "data_bi": "#b678d4", "legal": "#d4788f",
    "comms": "#35A481", "design": "#78c3d4", "research": "#8fd478",
}
# the four potential dimensions and their colours (label, key, colour)
POT_DIMS = [("applicability", "#35A481"), ("leverage", "#E64A2E"),
            ("reach", "#e0b13e"), ("tightness", "#7d9bd2")]
SE_ORDER = ["read", "create", "mutate", "irreversible"]


def esc(s):
    return html.escape(str(s), quote=True)


def load(name):
    with open(os.path.join(DATA, name), encoding="utf-8") as fh:
        return json.load(fh)


# ---------------------------------------------------------------------------
# small pieces
# ---------------------------------------------------------------------------

def pot_bars(p, compact=False):
    rows = []
    for key, color in POT_DIMS:
        v = p.get(key, 0)
        rows.append(
            f'<div class="pbar"><span class="pl">{key[0].upper()}</span>'
            f'<span class="pt"><i style="width:{v / 25 * 100:.0f}%;background:{color}"></i></span>'
            f'<span class="pv">{v}</span></div>')
    cls = "pot compact" if compact else "pot"
    legend = "" if compact else ('<div class="pkey">A applicability · L leverage · '
                                 'R reach · T tightness</div>')
    return (f'<div class="{cls}"><div class="pnum">{p["total"]}<span>/100</span></div>'
            f'<div class="pbars">{"".join(rows)}</div>{legend}</div>')


def chips(members, cap_domain):
    out = []
    for m in members:
        dom = cap_domain.get(m["capabilities"][0], "ops")
        c = DOMAIN_COLOR.get(dom, "#8a8a93")
        arrow = "◀" if m["role"] == "source" else "▶"
        out.append(f'<span class="chip" style="border-color:{c}66">'
                   f'<i style="background:{c}"></i>{esc(m["name"])}<b>{arrow}</b></span>')
    return '<div class="chips">' + "".join(out) + "</div>"


def member_rows(members, cap_domain, caps_meta):
    out = []
    for m in members:
        dom = cap_domain.get(m["capabilities"][0], "ops")
        c = DOMAIN_COLOR.get(dom, "#8a8a93")
        caplabels = ", ".join(caps_meta[cap]["label"] for cap in m["capabilities"])
        out.append(
            f'<div class="m"><span class="mdot" style="background:{c}"></span>'
            f'<div class="mbody"><div class="mtop"><b>{esc(m["name"])}</b>'
            f'<span class="mrole {m["role"]}">{m["role"]}</span>'
            f'<span class="mcap">{esc(caplabels)}</span>'
            f'<span class="mse se-{m["side_effect"]}">{m["side_effect"]}</span></div>'
            f'<div class="mfn">{esc(m.get("function", ""))}</div></div></div>')
    return '<div class="mlist">' + "".join(out) + "</div>"


def constellation(members, cap_domain, size, hub_r, node_r, label):
    cx = cy = size / 2
    n = len(members)
    rings = 1 if n <= 14 else (2 if n <= 30 else 3)
    parts = [f'<svg viewBox="0 0 {size} {size}" class="cons" role="img" aria-label="constellation of connectors around Claude">']
    positions = []
    for i, m in enumerate(members):
        ring = i % rings
        per = math.ceil(n / rings)
        span = (size / 2 - hub_r - node_r - 8 - (hub_r + 26))
        rad = (hub_r + 26) + (ring * (span / max(1, rings - 1)) if rings > 1 else 0)
        idx_in = i // rings if rings > 1 else i
        ang = (2 * math.pi * (idx_in + ring * 0.5)) / max(1, per) - math.pi / 2
        positions.append((cx + rad * math.cos(ang), cy + rad * math.sin(ang), m))
    for x, y, m in positions:
        c = DOMAIN_COLOR.get(cap_domain.get(m["capabilities"][0], "ops"), "#8a8a93")
        parts.append(f'<line x1="{cx:.1f}" y1="{cy:.1f}" x2="{x:.1f}" y2="{y:.1f}" '
                     f'stroke="{c}" stroke-opacity="0.28" stroke-width="1"/>')
    parts.append(f'<circle cx="{cx}" cy="{cy}" r="{hub_r}" fill="#E64A2E22" stroke="#E64A2E" '
                 f'stroke-width="1.5" stroke-dasharray="3 3"/>')
    parts.append(f'<text x="{cx}" y="{cy + 3:.0f}" text-anchor="middle" class="hub-t">Claude</text>')
    for x, y, m in positions:
        c = DOMAIN_COLOR.get(cap_domain.get(m["capabilities"][0], "ops"), "#8a8a93")
        fill = c if m["role"] == "sink" else c + "aa"
        parts.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{node_r}" fill="{fill}" stroke="{c}" stroke-width="1"/>')
        if label:
            anchor = "start" if x > cx + 4 else ("end" if x < cx - 4 else "middle")
            dx = node_r + 3 if x > cx + 4 else (-(node_r + 3) if x < cx - 4 else 0)
            parts.append(f'<text x="{x + dx:.1f}" y="{y + 3:.1f}" text-anchor="{anchor}" class="node-t">'
                         f'{esc(m["name"][:16])}</text>')
    parts.append("</svg>")
    return "".join(parts)


def se_line(se):
    return (f'<div class="se">side effects — verbs actually used: '
            f'<b class="se-{se["headline"]}">{esc(se["headline"])}</b> · '
            f'read-only footprint: {esc(se["observe"])}</div>')


# ---------------------------------------------------------------------------
# sections
# ---------------------------------------------------------------------------

def leaderboard_row(uc, rank, cap_domain):
    star = ' <span class="star">★ featured</span>' if uc.get("featured") else ""
    return f"""<div class="lbrow">
  <div class="rank">{rank}</div>
  <div class="lbmain">
    <div class="lbhead"><span class="lbname">{esc(uc['name'])}</span>
      <span class="badge {uc['rating']}">{uc['rating']}</span>
      <span class="meta">{uc['scale']} connectors · {uc['n_domains']}/12 domains</span>{star}</div>
    <div class="why">{esc(uc['why_short'])}</div>
    {chips(uc['members'], cap_domain)}
  </div>
  {pot_bars(uc['potential'], compact=True)}
</div>"""


def featured_block(uc, cap_domain, caps_meta, doms_meta):
    # domain-by-domain: which connector fills each capability slot
    by_dom = {}
    for m in uc["members"]:
        for cap in m["capabilities"]:
            d = caps_meta[cap]["domain"]
            by_dom.setdefault(d, []).append((caps_meta[cap]["label"], m["name"]))
    cols = []
    for d in [d for d in doms_meta if d in by_dom]:
        c = DOMAIN_COLOR.get(d, "#8a8a93")
        items = "".join(f'<li><span>{esc(lbl)}</span> {esc(name)}</li>'
                        for lbl, name in sorted(set(by_dom[d])))
        cols.append(f'<div class="fdom"><h4 style="color:{c}">{esc(doms_meta[d]["label"])}</h4>'
                    f'<ul>{items}</ul></div>')
    cov = int(round(uc["n_domains"] / 12 * 100))
    return f"""<section class="featured">
  <div class="fhead">
    <div>
      <span class="star">★ the huge one</span>
      <h3>{esc(uc['name'])}</h3>
      <p class="why">{esc(uc['why_short'])}</p>
      {f'<div class="scale-note">{esc(uc["scale_note"])}</div>' if uc.get("scale_note") else ""}
      <div class="cov"><div class="covbar"><i style="width:{cov}%"></i></div>
        <span>{uc['n_domains']}/12 domains · {uc['scale']} connectors</span></div>
      {pot_bars(uc['potential'])}
    </div>
    <div class="fcons">{constellation(uc['members'], cap_domain, 440, 38, 5, label=False)}</div>
  </div>
  <div class="fgrid">{"".join(cols)}</div>
  {se_line(uc['side_effects'])}
</section>"""


def catalogue_block(uc, cap_domain, caps_meta):
    dropped = ""
    if uc["dropped"]:
        items = "".join(f'<li><s>{esc(d["name"])}</s> — {esc(d["reason"])}</li>' for d in uc["dropped"][:10])
        dropped = f'<details class="dropped"><summary>left out ({len(uc["dropped"])})</summary><ul>{items}</ul></details>'
    small_cons = constellation(uc["members"], cap_domain, 220, 26, 5, label=False) if uc["scale"] > 3 else ""
    return f"""<article class="uc">
  <header>
    <span class="badge {uc['rating']}">{uc['rating']}</span>
    <h3>{esc(uc['name'])}</h3>
    <span class="meta">{uc['scale']} connectors · {uc['n_domains']}/12 domains</span>
    <span class="potpill">potential {uc['potential']['total']}</span>
  </header>
  <p class="why">{esc(uc['why_short'])}</p>
  <div class="ucbody">
    <div class="ucmembers">{member_rows(uc['members'], cap_domain, caps_meta)}{dropped}</div>
    <div class="ucside">{small_cons}{pot_bars(uc['potential'])}</div>
  </div>
  {se_line(uc['side_effects'])}
</article>"""


def build(cat, caps_data, doms_data):
    cap_domain = {k: v["domain"] for k, v in caps_data["capabilities"].items()}
    caps_meta = caps_data["capabilities"]
    doms_meta = doms_data["domains"]

    featured = next((u for u in cat if u.get("featured")), None)
    ranked = sorted(cat, key=lambda u: -u["potential"]["total"])
    top = [u for u in ranked if not u.get("featured")][:9]
    if featured:
        top = [featured] + top[:8]

    tiers = {"small": [], "medium": [], "large": []}
    for uc in cat:
        tiers[uc["tier"]].append(uc)
    for t in tiers:
        tiers[t].sort(key=lambda u: -u["potential"]["total"])

    n_uc = len(cat)
    n_conn = len(set(m["id"] for uc in cat for m in uc["members"]))
    biggest = max((uc["scale"] for uc in cat), default=0)

    legend = "".join(f'<span class="leg"><i style="background:{DOMAIN_COLOR[k]}"></i>{esc(v["label"])}</span>'
                     for k, v in doms_meta.items())
    lb = "".join(leaderboard_row(uc, i + 1, cap_domain) for i, uc in enumerate(top))
    feat = featured_block(featured, cap_domain, caps_meta, doms_meta) if featured else ""
    small = "".join(catalogue_block(uc, cap_domain, caps_meta) for uc in tiers["small"])
    medium = "".join(catalogue_block(uc, cap_domain, caps_meta) for uc in tiers["medium"])
    large = "".join(catalogue_block(uc, cap_domain, caps_meta) for uc in tiers["large"])

    return TEMPLATE.format(n_uc=n_uc, n_conn=n_conn, biggest=biggest, legend=legend,
                           leaderboard=lb, featured=feat, small=small, medium=medium, large=large)


TEMPLATE = r"""<!DOCTYPE html>
<html lang="en"><head><meta charset="utf-8"/>
<meta name="viewport" content="width=device-width,initial-scale=1"/>
<title>Connector Atlas — use cases around Claude</title>
<style>
:root{{--cinnabar:#E64A2E;--jade:#35A481;--ink:#0d0d10;--ink2:#131318;--parch:#efe9dd;
--mute:#8a8a93;--line:rgba(239,233,221,.10);--glass:rgba(19,19,24,.72)}}
*{{box-sizing:border-box;margin:0;padding:0}}
html{{scroll-behavior:smooth}}
body{{background:var(--ink);color:var(--parch);font-family:'IBM Plex Mono',ui-monospace,monospace;
line-height:1.55;overflow-x:hidden;font-size:14px}}
#bg{{position:fixed;inset:0;z-index:0;pointer-events:none;filter:blur(90px);opacity:.5}}
.orb{{position:absolute;border-radius:50%;mix-blend-mode:screen;animation:drift 26s ease-in-out infinite alternate}}
.o1{{width:44vw;height:44vw;background:radial-gradient(circle,#E64A2E33,transparent 70%);top:-12%;left:-8%}}
.o2{{width:38vw;height:38vw;background:radial-gradient(circle,#35A48130,transparent 70%);bottom:-10%;right:-6%;animation-delay:-9s}}
.o3{{width:26vw;height:26vw;background:radial-gradient(circle,#7d9bd226,transparent 70%);top:40%;left:46%;animation-delay:-17s}}
@keyframes drift{{from{{transform:translate(0,0) scale(1)}}to{{transform:translate(6vw,-4vh) scale(1.14)}}}}
.wrap{{position:relative;z-index:1;max-width:1120px;margin:0 auto;padding:0 20px 80px}}
header.hero{{text-align:center;padding:60px 0 26px}}
h1{{font-family:'Instrument Serif',Georgia,serif;font-weight:400;font-size:clamp(34px,6vw,58px)}}
h1 em{{color:var(--cinnabar);font-style:normal}}
.tagline{{color:var(--mute);max-width:660px;margin:14px auto 0;font-size:13.5px}}
.hub{{margin:30px auto 6px;width:132px;height:132px;border-radius:50%;display:flex;align-items:center;
justify-content:center;border:2px dashed var(--cinnabar);background:radial-gradient(circle,#E64A2E22,transparent 72%);
font-family:'Instrument Serif',Georgia,serif;font-size:24px;box-shadow:0 0 60px #E64A2E33}}
.stats{{display:flex;gap:26px;justify-content:center;flex-wrap:wrap;margin-top:16px;font-size:12px;color:var(--mute)}}
.stats b{{color:var(--jade);font-size:22px;display:block;font-family:'Instrument Serif',Georgia,serif}}
.legend{{display:flex;flex-wrap:wrap;gap:6px 14px;justify-content:center;margin:24px auto 0;max-width:900px;font-size:11px;color:var(--mute)}}
.leg{{display:inline-flex;align-items:center}}
.leg i,.chip i,.mdot{{width:9px;height:9px;border-radius:50%;margin-right:6px;flex:none;display:inline-block}}
h2.tier{{font-family:'Instrument Serif',Georgia,serif;font-weight:400;font-size:25px;margin:52px 0 4px;
border-bottom:1px solid var(--line);padding-bottom:9px}}
h2.tier em{{color:var(--cinnabar);font-style:normal}}
.tier-sub{{color:var(--mute);font-size:12.5px;margin-bottom:18px}}
.why{{font-size:13px;color:var(--parch);opacity:.92}}
.badge{{font-size:9.5px;letter-spacing:.07em;text-transform:uppercase;padding:2px 7px;border-radius:20px;border:1px solid;flex:none}}
.badge.strong{{color:var(--jade);border-color:#35A48166}}
.badge.partial{{color:#e0b13e;border-color:#e0b13e66}}
.meta{{font-size:11px;color:var(--mute)}}
.star{{font-size:10px;color:var(--cinnabar);letter-spacing:.05em}}
.chips{{display:flex;flex-wrap:wrap;gap:5px;margin-top:8px}}
.chip{{font-size:10.5px;padding:3px 8px;border-radius:20px;border:1px solid var(--line);
display:inline-flex;align-items:center;background:rgba(0,0,0,.18)}}
.chip b{{color:var(--mute);margin-left:5px;font-weight:400}}
/* potential */
.pot{{min-width:190px}}
.pnum{{font-family:'Instrument Serif',Georgia,serif;font-size:30px;color:var(--parch);line-height:1}}
.pnum span{{font-size:13px;color:var(--mute)}}
.pbars{{margin-top:6px;display:flex;flex-direction:column;gap:3px}}
.pbar{{display:flex;align-items:center;gap:6px;font-size:10px;color:var(--mute)}}
.pbar .pl{{width:12px;flex:none;text-align:center}}
.pbar .pt{{flex:1;height:5px;border-radius:3px;background:rgba(239,233,221,.09);overflow:hidden}}
.pbar .pt i{{display:block;height:100%;border-radius:3px}}
.pbar .pv{{width:16px;text-align:right;flex:none}}
.pkey{{font-size:9.5px;color:var(--mute);margin-top:5px;opacity:.7}}
.pot.compact{{min-width:150px}}.pot.compact .pnum{{font-size:24px}}.pot.compact .pkey{{display:none}}
/* leaderboard */
.lb{{display:flex;flex-direction:column;gap:10px}}
.lbrow{{display:flex;gap:14px;align-items:flex-start;background:var(--glass);border:1px solid var(--line);
border-radius:12px;padding:14px 16px;backdrop-filter:blur(12px)}}
.lbrow:first-child{{border-color:#E64A2E55;box-shadow:0 0 30px #E64A2E22}}
.rank{{font-family:'Instrument Serif',Georgia,serif;font-size:26px;color:var(--mute);width:30px;flex:none;text-align:center}}
.lbmain{{flex:1;min-width:0}}
.lbhead{{display:flex;align-items:center;gap:8px;flex-wrap:wrap}}
.lbname{{font-family:'Instrument Serif',Georgia,serif;font-size:19px}}
.lbpot,.lbrow .pot{{flex:none}}
/* featured */
.featured{{background:linear-gradient(160deg,rgba(230,74,46,.10),var(--glass));border:1px solid #E64A2E44;
border-radius:16px;padding:22px;margin-top:14px;backdrop-filter:blur(14px)}}
.fhead{{display:grid;grid-template-columns:1fr 440px;gap:20px;align-items:center}}
.featured h3{{font-family:'Instrument Serif',Georgia,serif;font-weight:400;font-size:30px;margin:4px 0 6px}}
.scale-note{{font-size:11.5px;color:var(--jade);opacity:.9;margin:8px 0}}
.cov{{display:flex;align-items:center;gap:10px;margin:10px 0;font-size:11px;color:var(--mute)}}
.covbar{{flex:1;max-width:260px;height:7px;border-radius:4px;background:rgba(239,233,221,.09);overflow:hidden}}
.covbar i{{display:block;height:100%;background:linear-gradient(90deg,var(--cinnabar),var(--jade))}}
.fcons{{display:flex;justify-content:center}}.fcons .cons{{width:100%;max-width:440px;height:auto}}
.fgrid{{display:grid;grid-template-columns:repeat(auto-fill,minmax(180px,1fr));gap:12px;margin:18px 0 6px;
border-top:1px solid var(--line);padding-top:16px}}
.fdom h4{{font-size:12px;font-weight:400;letter-spacing:.04em;margin-bottom:5px}}
.fdom ul{{list-style:none;font-size:11px}}
.fdom li{{padding:2px 0;color:var(--parch)}}
.fdom li span{{color:var(--mute);display:inline-block;min-width:96px}}
/* catalogue */
.grid{{display:grid;grid-template-columns:repeat(auto-fill,minmax(430px,1fr));gap:16px}}
.uc{{background:var(--glass);border:1px solid var(--line);border-radius:14px;padding:16px;backdrop-filter:blur(12px);
display:flex;flex-direction:column}}
.uc:hover{{border-color:#E64A2E44}}
.uc header{{display:flex;align-items:center;gap:8px;flex-wrap:wrap;margin-bottom:5px}}
.uc h3{{font-family:'Instrument Serif',Georgia,serif;font-weight:400;font-size:20px}}
.potpill{{margin-left:auto;font-size:11px;color:var(--cinnabar);border:1px solid #E64A2E44;border-radius:20px;padding:2px 9px}}
.ucbody{{display:grid;grid-template-columns:1fr 200px;gap:14px;margin-top:10px}}
.mlist{{display:flex;flex-direction:column;gap:9px}}
.m{{display:flex;gap:8px}}
.m .mdot{{margin-top:5px}}
.mbody{{min-width:0}}
.mtop{{display:flex;align-items:center;gap:7px;flex-wrap:wrap}}
.mtop b{{font-size:12.5px}}
.mrole{{font-size:9px;letter-spacing:.05em;text-transform:uppercase;color:var(--mute);border:1px solid var(--line);border-radius:10px;padding:1px 6px}}
.mrole.sink{{color:var(--cinnabar);border-color:#E64A2E44}}.mrole.source{{color:var(--jade);border-color:#35A48144}}
.mcap{{font-size:10.5px;color:var(--mute)}}
.mse{{font-size:9.5px;margin-left:auto}}
.mfn{{font-size:11px;color:var(--mute);opacity:.85;margin-top:1px}}
.ucside{{display:flex;flex-direction:column;gap:10px;align-items:center}}
.ucside .cons{{width:100%;max-width:200px;height:auto}}
.dropped{{font-size:11px;color:var(--mute);margin-top:6px}}
.dropped summary{{cursor:pointer;color:#e0b13e}}.dropped ul{{margin:6px 0 0 14px}}.dropped s{{color:var(--parch)}}
.se{{font-size:11px;color:var(--mute);border-top:1px solid var(--line);padding-top:8px;margin-top:12px}}
.se-read{{color:var(--jade)}}.se-create{{color:#7d9bd2}}.se-mutate{{color:#e0b13e}}.se-irreversible{{color:var(--cinnabar)}}
.hub-t{{fill:var(--cinnabar);font-family:'Instrument Serif',Georgia,serif;font-size:12px}}
.node-t{{fill:var(--parch);opacity:.82;font-size:8px}}
#selfcheck{{position:fixed;bottom:10px;right:12px;z-index:9;font-size:10px;padding:4px 9px;border-radius:20px;
background:var(--glass);border:1px solid var(--line);backdrop-filter:blur(10px)}}
#selfcheck.ok{{color:var(--jade);border-color:#35A48155}}#selfcheck.bad{{color:var(--cinnabar);border-color:#E64A2E88}}
footer{{text-align:center;color:var(--mute);font-size:11.5px;margin-top:60px;line-height:1.9}}
@media (max-width:860px){{.fhead{{grid-template-columns:1fr}}.fcons{{order:-1}}.grid{{grid-template-columns:1fr}}
.ucbody{{grid-template-columns:1fr}}.ucside{{flex-direction:row;flex-wrap:wrap}}.ucside .cons{{max-width:150px}}}}
</style></head><body>
<div id="bg"><div class="orb o1"></div><div class="orb o2"></div><div class="orb o3"></div></div>
<div class="wrap">
  <header class="hero">
    <h1>Connector <em>Atlas</em></h1>
    <div class="hub">Claude</div>
    <p class="tagline">Claude is the brain in the centre. Which combinations of directory connectors
    make a real use case, and <em style="color:var(--cinnabar);font-style:normal">why</em>? Below: the
    highest-<b>potential</b> use cases regardless of size, one huge system that runs like a company, and
    the full catalogue — each with what it's for and which connectors it uses.</p>
    <div class="stats">
      <span><b>{n_uc}</b>use cases</span>
      <span><b>{n_conn}</b>connectors composed</span>
      <span><b>{biggest}</b>in the biggest system</span>
      <span><b>12</b>functional domains</span>
    </div>
    <div class="legend">{legend}</div>
  </header>

  <h2 class="tier" id="top">Most <em>potential</em> — no matter the size</h2>
  <p class="tier-sub">Ranked by a composite of applicability · leverage · reach · tightness. A two-connector
  desk and a whole company can sit side by side — each bar shows why it scores where it does.</p>
  <div class="lb">{leaderboard}</div>

  <h2 class="tier" id="huge">The <em>huge</em> one</h2>
  <p class="tier-sub">Best connector for every capability, across all twelve domains — how much of an
  operation Claude + one big combination can run. Functional reach, shown honestly; never autonomy.</p>
  {featured}

  <h2 class="tier" id="small">Small — Claude + <em>2–5</em> connectors</h2>
  <p class="tier-sub">A source, something acted on, an output — the smallest workflows worth having.</p>
  <div class="grid">{small}</div>

  <h2 class="tier" id="medium">Medium — a <em>whole domain desk</em></h2>
  <p class="tier-sub">Grow a small one until it runs an entire function.</p>
  <div class="grid">{medium}</div>

  <h2 class="tier" id="large">Large — a combination that <em>runs like a company</em></h2>
  <p class="tier-sub">Broad multi-domain systems.</p>
  <div class="grid">{large}</div>

  <footer>
    Claude in the middle · a static gallery of discovered use cases, ranked by potential.<br/>
    Coherence and potential are judged on functional capabilities — no join keys, no popularity, no personal context.<br/>
    Generated by <code>engine/render.py</code> from <code>engine/discover.py</code>.
  </footer>
</div>
<div id="selfcheck">checking…</div>
<script>
(function(){{
  // load-time scaffolding self-check (not user interaction): the <!DOCTYPE> must trigger standards
  // mode and the viewport meta must give a real device width, not the 980px quirks fallback.
  var standards = document.compatMode === 'CSS1Compat';
  var w = document.documentElement.clientWidth || 0;
  var realWidth = w > 0 && w < 6000 && w !== 980;
  var el = document.getElementById('selfcheck');
  if (standards && realWidth) {{ el.textContent = '✓ standards · ' + w + 'px'; el.className = 'ok'; }}
  else {{ el.textContent = '✗ scaffolding (' + document.compatMode + ' · ' + w + 'px)'; el.className = 'bad'; }}
}})();
</script>
</body></html>"""


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", default=os.path.join(HERE, "..", "atlas.html"))
    ap.add_argument("--usecases", default=os.path.join(DATA, "usecases.json"))
    args = ap.parse_args()
    cat = json.load(open(args.usecases, encoding="utf-8"))["usecases"]
    out_html = build(cat, load("capabilities.json"), load("domains.json"))
    with open(args.out, "w", encoding="utf-8") as fh:
        fh.write(out_html)
    print(f"wrote {args.out}  ({len(out_html):,} bytes, {len(cat)} use cases)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
