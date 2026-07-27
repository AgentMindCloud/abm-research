#!/usr/bin/env python3
"""Render atlas.html — Claude in the centre, a gallery of discovered use cases.

Reuses only the correct HTML scaffolding (<!DOCTYPE>/charset/viewport) and the
Cinnabar/jade palette from the skill's atlas.py. Claude is the hub in the middle; around
it a gallery of the use cases discover.py found, ordered small -> huge — each a
constellation of its connectors with the use-case name and the one-line why. The big
multi-domain systems are the centrepieces, showing how much of an operation Claude + that
combination can run. Ships with a minimal scaffolding self-check (compatMode=CSS1Compat,
real device width).

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


def esc(s):
    return html.escape(str(s), quote=True)


def load(name):
    with open(os.path.join(DATA, name), encoding="utf-8") as fh:
        return json.load(fh)


def constellation(members, cap_domain, size, hub_r, node_r, label):
    """SVG hub-and-spoke: Claude at centre, connectors on ring(s), coloured by domain."""
    cx = cy = size / 2
    n = len(members)
    rings = 1 if n <= 14 else (2 if n <= 30 else 3)
    parts = [f'<svg viewBox="0 0 {size} {size}" class="cons" role="img" aria-label="constellation">']
    # edges first
    positions = []
    for i, m in enumerate(members):
        ring = i % rings
        per = math.ceil(n / rings)
        rad = (hub_r + 26) + ring * ((size / 2 - hub_r - node_r - 6 - (hub_r + 26)) / max(1, rings - 1) if rings > 1 else 0)
        idx_in = i // rings if rings > 1 else i
        ang = (2 * math.pi * (idx_in + (ring * 0.5))) / max(1, per) - math.pi / 2
        x = cx + rad * math.cos(ang)
        y = cy + rad * math.sin(ang)
        positions.append((x, y, m))
    for x, y, m in positions:
        dom = cap_domain.get(m["capabilities"][0], "ops")
        c = DOMAIN_COLOR.get(dom, "#8a8a93")
        parts.append(f'<line x1="{cx:.1f}" y1="{cy:.1f}" x2="{x:.1f}" y2="{y:.1f}" '
                     f'stroke="{c}" stroke-opacity="0.28" stroke-width="1"/>')
    # hub
    parts.append(f'<circle cx="{cx}" cy="{cy}" r="{hub_r}" fill="#E64A2E22" stroke="#E64A2E" '
                 f'stroke-width="1.5" stroke-dasharray="3 3"/>')
    parts.append(f'<text x="{cx}" y="{cy+3:.0f}" text-anchor="middle" class="hub-t">Claude</text>')
    # nodes
    for x, y, m in positions:
        dom = cap_domain.get(m["capabilities"][0], "ops")
        c = DOMAIN_COLOR.get(dom, "#8a8a93")
        sink = m["role"] == "sink"
        parts.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{node_r}" fill="{c}{"" if sink else "aa"}" '
                     f'stroke="{c}" stroke-width="1"/>')
        if label:
            anchor = "start" if x > cx + 4 else ("end" if x < cx - 4 else "middle")
            dx = node_r + 3 if x > cx + 4 else (-(node_r + 3) if x < cx - 4 else 0)
            parts.append(f'<text x="{x+dx:.1f}" y="{y+3:.1f}" text-anchor="{anchor}" class="node-t">'
                         f'{esc(m["name"][:18])}</text>')
    parts.append("</svg>")
    return "".join(parts)


def chips(members, cap_domain):
    out = []
    for m in members:
        dom = cap_domain.get(m["capabilities"][0], "ops")
        c = DOMAIN_COLOR.get(dom, "#8a8a93")
        role = "◀" if m["role"] == "source" else "▶"
        out.append(f'<span class="chip" style="border-color:{c}66"><i style="background:{c}"></i>'
                   f'{esc(m["name"])} <b>{role}</b></span>')
    return "".join(out)


def card(uc, cap_domain, big=False):
    badge = "strong" if uc["rating"] == "strong" else "partial"
    dot = "●" if uc["rating"] == "strong" else "◐"
    doms = " ".join(
        f'<span class="dl" style="color:{DOMAIN_COLOR.get(d,"#8a8a93")}">{esc(d)}</span>'
        for d in uc["domains"])
    if big:
        cons = constellation(uc["members"], cap_domain, 460, 40, 5, label=(uc["scale"] <= 16))
    else:
        cons = constellation(uc["members"], cap_domain, 300, 30, 6, label=(uc["scale"] <= 8))
    se = uc["side_effects"]
    scale_note = f'<div class="scale-note">{esc(uc["scale_note"])}</div>' if uc.get("scale_note") else ""
    dropped = ""
    if uc["dropped"]:
        items = "".join(f'<li><s>{esc(d["name"])}</s> — {esc(d["reason"])}</li>' for d in uc["dropped"][:8])
        dropped = f'<details class="dropped"><summary>left out ({len(uc["dropped"])})</summary><ul>{items}</ul></details>'
    return f"""<article class="card{' big' if big else ''}">
  <header>
    <span class="badge {badge}">{dot} {esc(uc['rating'])}</span>
    <h3>{esc(uc['name'])}</h3>
    <span class="meta">{uc['scale']} connectors · {uc['n_domains']}/12 domains</span>
  </header>
  <p class="why">{esc(uc['why_short'])}</p>
  {scale_note}
  <div class="cons-wrap">{cons}</div>
  <div class="chips">{chips(uc['members'], cap_domain)}</div>
  {dropped}
  <div class="se">side effects, verbs actually used: <b class="se-{se['headline']}">{esc(se['headline'])}</b>
     · read-only footprint: {esc(se['observe'])}</div>
</article>"""


def build(cat, caps_data, doms_data):
    cap_domain = {k: v["domain"] for k, v in caps_data["capabilities"].items()}
    tiers = {"small": [], "medium": [], "large": []}
    for uc in cat:
        tiers[uc["tier"]].append(uc)

    n_uc = len(cat)
    n_conn_total = len(set(m["id"] for uc in cat for m in uc["members"]))
    biggest = max((uc["scale"] for uc in cat), default=0)

    legend = "".join(
        f'<span class="leg"><i style="background:{DOMAIN_COLOR[k]}"></i>{esc(v["label"])}</span>'
        for k, v in doms_data["domains"].items())

    small_cards = "".join(card(uc, cap_domain) for uc in tiers["small"])
    medium_cards = "".join(card(uc, cap_domain) for uc in tiers["medium"])
    large_cards = "".join(card(uc, cap_domain, big=True) for uc in tiers["large"])

    return TEMPLATE.format(
        n_uc=n_uc, n_conn=n_conn_total, biggest=biggest,
        legend=legend, small=small_cards, medium=medium_cards, large=large_cards)


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
line-height:1.55;overflow-x:hidden}}
#bg{{position:fixed;inset:0;z-index:0;pointer-events:none;filter:blur(90px);opacity:.5}}
.orb{{position:absolute;border-radius:50%;mix-blend-mode:screen;animation:drift 26s ease-in-out infinite alternate}}
.o1{{width:44vw;height:44vw;background:radial-gradient(circle,#E64A2E33,transparent 70%);top:-12%;left:-8%}}
.o2{{width:38vw;height:38vw;background:radial-gradient(circle,#35A48130,transparent 70%);bottom:-10%;right:-6%;animation-delay:-9s}}
.o3{{width:26vw;height:26vw;background:radial-gradient(circle,#7d9bd226,transparent 70%);top:40%;left:46%;animation-delay:-17s}}
@keyframes drift{{from{{transform:translate(0,0) scale(1)}}to{{transform:translate(6vw,-4vh) scale(1.14)}}}}
.wrap{{position:relative;z-index:1;max-width:1180px;margin:0 auto;padding:0 20px 80px}}
header.hero{{text-align:center;padding:64px 0 30px}}
h1{{font-family:'Instrument Serif',Georgia,serif;font-weight:400;font-size:clamp(34px,6vw,60px);letter-spacing:.01em}}
h1 em{{color:var(--cinnabar);font-style:normal}}
.tagline{{color:var(--mute);max-width:640px;margin:14px auto 0;font-size:14px}}
.hub{{margin:34px auto 10px;width:150px;height:150px;border-radius:50%;display:flex;align-items:center;
justify-content:center;border:2px dashed var(--cinnabar);background:radial-gradient(circle,#E64A2E22,transparent 72%);
font-family:'Instrument Serif',Georgia,serif;font-size:26px;box-shadow:0 0 60px #E64A2E33}}
.stats{{display:flex;gap:28px;justify-content:center;flex-wrap:wrap;margin-top:18px;font-size:13px;color:var(--mute)}}
.stats b{{color:var(--jade);font-size:22px;display:block;font-family:'Instrument Serif',Georgia,serif}}
.legend{{display:flex;flex-wrap:wrap;gap:6px 14px;justify-content:center;margin:26px auto 6px;max-width:900px;font-size:11px;color:var(--mute)}}
.leg,.leg i{{display:inline-flex;align-items:center}}
.leg i,.chip i{{width:9px;height:9px;border-radius:50%;margin-right:6px;flex:none}}
h2.tier{{font-family:'Instrument Serif',Georgia,serif;font-weight:400;font-size:26px;margin:52px 0 6px;
border-bottom:1px solid var(--line);padding-bottom:10px}}
h2.tier em{{color:var(--cinnabar);font-style:normal}}
.tier-sub{{color:var(--mute);font-size:12.5px;margin-bottom:20px}}
.grid{{display:grid;grid-template-columns:repeat(auto-fill,minmax(320px,1fr));gap:18px}}
.card{{background:var(--glass);border:1px solid var(--line);border-radius:14px;padding:16px 16px 14px;
backdrop-filter:blur(14px);transition:.25s;display:flex;flex-direction:column}}
.card:hover{{border-color:#E64A2E55;transform:translateY(-2px)}}
.card.big{{grid-column:1/-1}}
.card header{{display:flex;align-items:baseline;gap:9px;flex-wrap:wrap;margin-bottom:6px}}
.card h3{{font-family:'Instrument Serif',Georgia,serif;font-weight:400;font-size:21px}}
.badge{{font-size:9.5px;letter-spacing:.08em;text-transform:uppercase;padding:2px 7px;border-radius:20px;border:1px solid}}
.badge.strong{{color:var(--jade);border-color:#35A48166}}
.badge.partial{{color:#e0b13e;border-color:#e0b13e66}}
.meta{{font-size:11px;color:var(--mute);margin-left:auto}}
.why{{font-size:13px;color:var(--parch);opacity:.92;margin:4px 0 8px}}
.scale-note{{font-size:11px;color:var(--jade);opacity:.85;margin-bottom:6px}}
.cons-wrap{{display:flex;justify-content:center;margin:2px 0 10px}}
.cons{{width:100%;max-width:300px;height:auto}}
.card.big .cons{{max-width:460px}}
.hub-t{{fill:var(--cinnabar);font-family:'Instrument Serif',Georgia,serif;font-size:13px}}
.node-t{{fill:var(--parch);opacity:.82;font-size:8.5px;font-family:'IBM Plex Mono',ui-monospace,monospace}}
.chips{{display:flex;flex-wrap:wrap;gap:5px;margin-bottom:8px}}
.chip{{font-size:10.5px;padding:3px 8px;border-radius:20px;border:1px solid var(--line);
display:inline-flex;align-items:center;background:rgba(0,0,0,.18)}}
.chip b{{color:var(--mute);margin-left:4px;font-weight:400}}
.dropped{{font-size:11px;color:var(--mute);margin-bottom:8px}}
.dropped summary{{cursor:pointer;color:#e0b13e}}
.dropped ul{{margin:6px 0 0 14px}}.dropped s{{color:var(--parch)}}
.se{{font-size:11px;color:var(--mute);border-top:1px solid var(--line);padding-top:8px;margin-top:auto}}
.se-read{{color:var(--jade)}}.se-create{{color:#7d9bd2}}.se-mutate{{color:#e0b13e}}.se-irreversible{{color:var(--cinnabar)}}
#selfcheck{{position:fixed;bottom:10px;right:12px;z-index:9;font-size:10px;padding:4px 9px;border-radius:20px;
background:var(--glass);border:1px solid var(--line);backdrop-filter:blur(10px)}}
#selfcheck.ok{{color:var(--jade);border-color:#35A48155}}
#selfcheck.bad{{color:var(--cinnabar);border-color:#E64A2E88}}
footer{{text-align:center;color:var(--mute);font-size:11.5px;margin-top:60px;line-height:1.9}}
@media (max-width:520px){{.grid{{grid-template-columns:1fr}}.stats{{gap:18px}}}}
</style></head><body>
<div id="bg"><div class="orb o1"></div><div class="orb o2"></div><div class="orb o3"></div></div>
<div class="wrap">
  <header class="hero">
    <h1>Connector <em>Atlas</em></h1>
    <div class="hub">Claude</div>
    <p class="tagline">Claude is the brain in the centre. Take the connector directory, add Claude and
    two connectors, then more and more — and see which combinations form a real use case, and
    <em style="color:var(--cinnabar);font-style:normal">why</em>. Only the combos that work are shown.</p>
    <div class="stats">
      <span><b>{n_uc}</b>use cases</span>
      <span><b>{n_conn}</b>connectors composed</span>
      <span><b>{biggest}</b>in the biggest system</span>
      <span><b>12</b>functional domains</span>
    </div>
    <div class="legend">{legend}</div>
  </header>

  <h2 class="tier" id="small">Small — Claude + <em>2–5</em> connectors</h2>
  <p class="tier-sub">A source, something acted on, an output — the smallest workflows a person would actually want.</p>
  <div class="grid">{small}</div>

  <h2 class="tier" id="medium">Medium — Claude + a <em>whole domain desk</em></h2>
  <p class="tier-sub">Grow a small one until it runs an entire function: a Sales desk, a Finance back office.</p>
  <div class="grid">{medium}</div>

  <h2 class="tier" id="large">Large — Claude + a combination that can <em>run like a company</em></h2>
  <p class="tier-sub">Best connector per capability across the domains. Scale and coverage shown honestly —
  functional reach, never autonomy.</p>
  <div class="grid">{large}</div>

  <footer>
    Claude in the middle · a gallery of discovered use cases, small to huge.<br/>
    Coherence is judged on functional capabilities — no join keys, no popularity, no personal context.<br/>
    Generated by <code>engine/render.py</code> from <code>engine/discover.py</code>.
  </footer>
</div>
<div id="selfcheck">checking…</div>
<script>
(function(){{
  // minimal scaffolding self-check: the <!DOCTYPE> must trigger standards mode, and the
  // viewport meta must give a real device width (not the 980px quirks fallback).
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

    cat = load(os.path.basename(args.usecases))["usecases"] if os.path.dirname(args.usecases) == DATA \
        else json.load(open(args.usecases, encoding="utf-8"))["usecases"]
    caps_data = load("capabilities.json")
    doms_data = load("domains.json")
    out_html = build(cat, caps_data, doms_data)
    with open(args.out, "w", encoding="utf-8") as fh:
        fh.write(out_html)
    print(f"wrote {args.out}  ({len(out_html):,} bytes, {len(cat)} use cases)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
