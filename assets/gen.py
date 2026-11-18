# -*- coding: utf-8 -*-
"""Generate the GitHub profile README assets (light + dark SVGs) for Dr-Zero69."""
import os, html
OUT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LIGHT = {"bone": "#2B2B2B", "muted": "#7A7A7A", "dim": "#A3A3A3", "rule": "#C8C8C8", "ghost": "#D9D9D9", "accent": "#1F6F5F"}
DARK = {"bone": "#E6E6E6", "muted": "#8A8A8A", "dim": "#6A6A6A", "rule": "#3A3A3A", "ghost": "#262626", "accent": "#6FCFB5"}
MONO = '.mono{font-family:ui-monospace,"SFMono-Regular","SF Mono",Menlo,Consolas,"Liberation Mono",monospace;}'
ANIM = ('.rise{opacity:0;animation:rise .7s cubic-bezier(.2,.7,.2,1) forwards;}@keyframes rise{from{opacity:0;transform:translateY(8px)}to{opacity:1;transform:translateY(0)}}'
        '.draw{stroke-dasharray:1000;stroke-dashoffset:1000;animation:draw 1.4s cubic-bezier(.6,0,.2,1) forwards;}@keyframes draw{to{stroke-dashoffset:0}}'
        '.fade{opacity:0;animation:fade .7s ease forwards;}@keyframes fade{to{opacity:1}}'
        + "".join(f".a{i}{{animation-delay:{0.1*i:.2f}s}}" for i in range(1, 13)) +
        '@media (prefers-reduced-motion:reduce){.rise,.draw,.fade,.rot,.dot,.ring{animation:none}.draw{stroke-dashoffset:0}.rise,.fade{opacity:1}}')
E = html.escape
if os.environ.get("NOANIM"): ANIM = ""


def svg(name, h, body, label, extra_css=""):
    for folder, pal in (("", LIGHT), ("dark", DARK)):
        root = ":root{" + ";".join(f"--{k}:{v}" for k, v in pal.items()) + "}"
        doc = (f'<svg viewBox="0 0 1000 {h}" width="1000" height="{h}" fill="none" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="{E(label)}">'
               f'<style>{root}{MONO}{ANIM}{extra_css}</style>{body}</svg>')
        d = os.path.join(OUT, "assets", folder); os.makedirs(d, exist_ok=True)
        open(os.path.join(d, name + ".svg"), "w", encoding="utf-8").write(doc)


def T(x, y, s, size=15, fill="bone", cls="", anchor=None, ls=None, weight=None):
    size = size + 1
    a = f' text-anchor="{anchor}"' if anchor else ""
    l = f' letter-spacing="{ls}"' if ls is not None else ""
    w = f' font-weight="{weight}"' if weight else ""
    return f'<text class="mono {cls}" x="{x}" y="{y}" font-size="{size}" fill="var(--{fill})"{a}{l}{w}>{E(s)}</text>'


def section(num, title, idx):
    body = (f'<line class="draw" x1="48" y1="78" x2="952" y2="78" stroke="var(--rule)" stroke-width="1"/>'
            + T(48, 68, f"{num:02d}", 52, "ghost", "fade a1") + T(128, 58, title.upper(), 14, "accent", "fade a2", ls=6)
            + T(952, 58, f"SECTION {num:02d} / 06", 11, "muted", "fade a2", anchor="end", ls=2))
    svg(f"s{num:02d}", 92, body, f"Section {num:02d} — {title}")


# ---------------- header
rot = ["Predicting residential soil metals, and reporting honestly when they will not be predicted.",
       "PFAS mixtures and a liver enzyme that NHANES had never measured before 2021.",
       "Small-area stroke prevalence from soil, housing, roads and demographics.",
       "Teaching language models to read a urinary biomonitoring panel against a reference set."]
rot_css = ('.rot{opacity:0;animation:rot 16s linear infinite;}' + "".join(f".r{i+1}{{animation-delay:{1.6+4*i}s}}" for i in range(4)) +
           '@keyframes rot{0%{opacity:0}1.5%{opacity:1}22%{opacity:1}25%{opacity:0}100%{opacity:0}}@media (prefers-reduced-motion:reduce){.rot{opacity:0}.rot.r1{opacity:1}}')
hdr = (f'<line class="draw a1" x1="48" y1="58" x2="952" y2="58" stroke="var(--rule)" stroke-width="1"/>'
       + T(48, 44, "PROFILE — INDEX Nº 001", 11, "muted", "fade a1", ls=3.5)
       + T(952, 44, "GREENSBORO, NC — 36.07° N & 79.79° W", 11, "muted", "fade a1", anchor="end", ls=3.5)
       + T(46, 176, "ANURODH JHA", 72, "bone", "rise a2", ls=-1, weight=700)
       + T(48, 224, "Environmental Epidemiology · Machine Learning · Geospatial Analysis", 20, "accent", "rise a3")
       + T(48, 262, "PhD Candidate, Applied Science & Technology · North Carolina A&T State University", 15, "muted", "rise a4")
       + f'<line class="draw a4" x1="48" y1="296" x2="952" y2="296" stroke="var(--rule)" stroke-width="1"/>'
       + "".join(T(48, 334, s, 15, "bone", f"rot r{i+1}") for i, s in enumerate(rot))
       + T(48, 372, "CURRENTLY ▸ dissertation on pollutant distribution, exposure risk and health outcomes · May 2027", 12, "muted", "fade a6", ls=1))
svg("header", 400, hdr, "Anurodh Jha — Environmental Epidemiology, Machine Learning, Geospatial Analysis", rot_css)

# ---------------- 01 whoami
who = (T(48, 32, "PhD candidate, North Carolina A&T State University, Greensboro, NC. Environmental Health & Disease Lab.", 15, "bone", "rise a1")
       + T(48, 60, "I work where environmental measurements, biomonitoring data and predictive models meet,", 15, "bone", "rise a2")
       + T(48, 84, "and I care whether a model survives honest validation: blocked, nested, weighted, uncertain.", 15, "bone", "rise a2")
       + f'<line class="rise a3" x1="48" y1="112" x2="952" y2="112" stroke="var(--rule)" stroke-width="1" opacity=".6"/>'
       + T(48, 146, "FOCUS  ▸", 11, "muted", "rise a4", ls=2.5) + T(164, 146, "Exposure science · Mixture epidemiology · Spatial ML · Agentic AI · LLMs · RAG", 15, "bone", "rise a4")
       + T(48, 180, "DATA  ▸", 11, "muted", "rise a5", ls=2.5) + T(164, 180, "Soil metals · Serum PFAS · Urinary biomonitoring · CDC PLACES · Census & TIGER", 15, "bone", "rise a5")
       + T(48, 214, "STATUS  ▸", 11, "muted", "rise a6", ls=2.5) + T(164, 214, "Prelims submitted · one paper accepted, two under review · open to collaboration", 15, "accent", "rise a6"))
svg("whoami", 236, who, "About Anurodh")

# ---------------- rows (research / projects)
def rows(name, items, label):
    h = 20 + 104 * len(items)
    body = ""
    for i, (title, l1, l2, meta) in enumerate(items):
        y = 20 + 104 * i
        body += (f'<g transform="translate(0 {y})"><g class="rise a{min(i+1,12)}">' + T(48, 24, title, 17, "bone", weight=700, ls=0.8)
                 + T(48, 49, l1, 12, "bone") + T(48, 68, l2, 12, "muted") + T(48, 87, meta, 11, "accent", ls=0.4)
                 + f'<line x1="48" y1="104" x2="952" y2="104" stroke="var(--rule)" stroke-width="1"/></g></g>')
    svg(name, h, body, label)

research = [
    ("01 / SOIL METALS → SMALL-AREA STROKE PREVALENCE", "Can household soil metals, soil properties, housing, roads and demographics predict modeled stroke prevalence by census tract?",
     "Tree ensembles and Ridge under nested leave-one-tract-out and spatially blocked validation; SHAP; honest about 36 tracts.",
     "PYTHON · SCIKIT-LEARN · SHAP · ARCGIS PRO · KRIGING · MORAN'S I  —  IJERPH, REVISED AFTER REVIEW"),
    ("02 / PFAS MIXTURES × BUTYRYLCHOLINESTERASE", "Serum PFAS and circulating BChE in U.S. adults, using the NHANES 2021–2023 cycle that measured the enzyme for the first time.",
     "Survey-weighted quantile g-computation and single-PFAS models; WQS and BKMR sensitivity analyses.",
     "R · SURVEY · QGCOMP · GWQS · BKMR  —  TOXICS, ACCEPTED NOVEMBER 2026"),
    ("03 / ELEMENT-SPECIFIC PREDICTABILITY OF RESIDENTIAL SOIL METALS", "Multi-output machine learning for Pb, Cd, Zn, Se and Cu from covariates alone, tested with spatial blocking and an external city.",
     "Shows which elements carry covariate signal and which do not, and why random CV overstates all of them.",
     "PYTHON · RANDOM FOREST · SPATIAL CV · GEOPANDAS  —  ENVIRONMENTS, REVISED AFTER REVIEW"),
    ("04 / LANGUAGE MODELS × URINARY BIOMONITORING", "An NHANES-based reference set so that LLMs interpreting urinary biomonitoring results can be scored against truth.",
     "Phase 0 complete: analyte and cycle selection, detection audit, joint cohort. Phase 1: weighted percentiles.",
     "NHANES 2011–2018 · PYTHON · DESIGN-BASED ESTIMATION · LLM EVALUATION  —  IN PROGRESS"),
]
rows("research", research, "Research: four studies")
projects = [
    ("05 / VALORANT WIN-RATE PREDICTION", "Player performance statistics (K/D, kills, deaths, assists, maps, agents) as predictors of win rate.",
     "Feature engineering and model comparison in a notebook, because epidemiologists also play games.", "JUPYTER · PYTHON · SCIKIT-LEARN  —  github.com/Dr-Zero69/Valorant-Win-Rate-Prediction"),
    ("06 / FIREBRAND TRAJECTORY PREDICTOR", "Predicting where wind-borne embers land, an input to wildfire spread and structure-ignition risk.",
     "Physics-informed features with a learned trajectory model.", "PYTHON · SIMULATION  —  github.com/Dr-Zero69/Firebrand-Trajectory-Predictor"),
    ("07 / BATTERY HEATING AND HEATER SIGNAL", "Thermal behaviour of a battery pack and the control signal that keeps it in its operating window.",
     "Signal processing and modelling of heater response.", "PYTHON  —  github.com/Dr-Zero69/Battery-heating-and-heater-signal"),
]
rows("projects", projects, "Side projects")

# ---------------- stack
stack = [("LANGUAGES", "Python · R · SQL · PowerShell · C#"), ("MODELLING", "scikit-learn · Random Forest / Extra Trees · Ridge · SHAP · nested & spatial CV"),
         ("MIXTURES", "survey · qgcomp · gWQS · bkmr · design-based inference, domain analysis, FDR control"),
         ("GEOSPATIAL", "ArcGIS Pro · geopandas · ordinary kriging · Moran's I · spatial folds · TIGER/Line"),
         ("DATA", "NHANES · CDC PLACES / 500 Cities · Census & ACS · county GIS · XRF soil campaigns"),
         ("WRITING", "Word & Zotero automation (lxml, CSL) · reproducible, script-verified manuscripts"),
         ("AI", "Agentic AI workflows · LLM evaluation · RAG pipelines · Claude API & Code · Azure AI"),
         ("TOOLING", "Jupyter · Git · VS Code · PowerShell")]
sb = f'<line x1="150" y1="8" x2="150" y2="{32*len(stack)+6}" stroke="var(--rule)" stroke-width="1" opacity=".5"/>'
for i, (k, v) in enumerate(stack):
    sb += T(48, 32 + 32 * i, k, 12, "muted", f"rise a{i+1}", ls=2) + T(166, 32 + 32 * i, v, 15, "bone", f"rise a{i+1}")
svg("stack", 32 * len(stack) + 20, sb, "Technical stack")

# ---------------- timeline
tl = [("2022", "Joined GitHub. First notebooks.", False), ("2024", "Firebrand trajectory predictor · Azure AI Vision labs · first spatial models.", False),
      ("2025", "Battery heater-signal modelling · Valorant win-rate prediction · soil metal analyses begin.", False),
      ("2026", "Three manuscripts submitted and revised · Toxics paper accepted · prelims · LLM Phase 0.", True),
      ("2027", "Phase 1 reference percentiles · full dissertation draft · defense · graduation (May).", False)]
tb = f'<line class="draw" x1="110" y1="10" x2="110" y2="{40*len(tl)+10}" stroke="var(--rule)" stroke-width="1"/>'
for i, (yr, s, now) in enumerate(tl):
    y = 34 + 40 * i
    tb += T(48, y + 4, yr, 13, "accent" if now else "muted", f"rise a{i+1}", ls=1)
    tb += f'<circle class="rise a{i+1}" cx="110" cy="{y}" r="{5 if now else 3.5}" fill="var(--{"accent" if now else "dim"})"/>'
    tb += T(132, y + 5, s, 14, "bone", f"rise a{i+1}")
svg("timeline", 40 * len(tl) + 20, tb, "Route: 2022 to 2027")

# ---------------- footer
fcss = '.dot{animation:p 2.4s ease-in-out infinite}.ring{animation:r 2.4s ease-out infinite;transform-origin:60px 64px}@keyframes p{0%,100%{opacity:1}50%{opacity:.35}}@keyframes r{0%{transform:scale(.4);opacity:.8}80%,100%{transform:scale(2.6);opacity:0}}'
fb = (f'<line class="draw" x1="48" y1="24" x2="952" y2="24" stroke="var(--rule)" stroke-width="1"/>'
      f'<circle class="ring" cx="60" cy="64" r="5" stroke="var(--accent)" stroke-width="1" fill="none"/><circle class="dot" cx="60" cy="64" r="4" fill="var(--accent)"/>'
      + T(82, 62, "STATUS — RESEARCH, COOK, WORKOUT AND WORK ON MY 1000 HOBBIES :D", 12, "bone", ls=3)
      + T(82, 82, "\"If the held-out error is good, check the folds.\" — Dr. Zero", 11, "muted", ls=2)
      + T(952, 66, "Greensboro, NC   ·   © 2026", 15, "muted", anchor="end"))
svg("footer", 110, fb, "Status", fcss)

for i, t in enumerate(["who am i", "research", "side projects", "telemetry", "the route", "stack"], 1):
    section(i, t, i)


def pic(name, alt, width=None):
    w = f' width="{width}"' if width else ""
    return f'<picture><source media="(prefers-color-scheme: dark)" srcset="assets/dark/{name}.svg"/><img src="assets/{name}.svg"{w} alt="{alt}"/></picture>'


U = "Dr-Zero69"
stats_l = f"https://github-readme-stats.vercel.app/api?username={U}&show_icons=true&hide_border=true&bg_color=00000000&title_color=1F6F5F&icon_color=1F6F5F&text_color=2B2B2B&hide_title=false"
stats_d = f"https://github-readme-stats.vercel.app/api?username={U}&show_icons=true&hide_border=true&bg_color=00000000&title_color=6FCFB5&icon_color=6FCFB5&text_color=E6E6E6"
langs_l = f"https://github-readme-stats.vercel.app/api/top-langs/?username={U}&layout=compact&hide_border=true&bg_color=00000000&title_color=1F6F5F&text_color=2B2B2B"
langs_d = f"https://github-readme-stats.vercel.app/api/top-langs/?username={U}&layout=compact&hide_border=true&bg_color=00000000&title_color=6FCFB5&text_color=E6E6E6"
graph_l = f"https://github-readme-activity-graph.vercel.app/graph?username={U}&bg_color=ffffff00&color=2B2B2B&line=1F6F5F&point=1F6F5F&area=true&area_color=1F6F5F&hide_border=true"
graph_d = f"https://github-readme-activity-graph.vercel.app/graph?username={U}&bg_color=00000000&color=E6E6E6&line=6FCFB5&point=6FCFB5&area=true&area_color=6FCFB5&hide_border=true"
readme = f"""<div align="center">

{pic("header", "Anurodh Jha")}

<a href="https://github.com/{U}?tab=repositories"><picture><source media="(prefers-color-scheme: dark)" srcset="https://img.shields.io/badge/REPOSITORIES-0d1117?style=flat-square&logo=github&logoColor=ffffff"/><img src="https://img.shields.io/badge/REPOSITORIES-ffffff?style=flat-square&logo=github&logoColor=000000" alt="Repositories"/></picture></a>
<a href="https://www.ncat.edu/"><picture><source media="(prefers-color-scheme: dark)" srcset="https://img.shields.io/badge/NC%20A%26T-0d1117?style=flat-square&logo=academia&logoColor=ffffff"/><img src="https://img.shields.io/badge/NC%20A%26T-ffffff?style=flat-square&logo=academia&logoColor=000000" alt="North Carolina A&T State University"/></picture></a>
<a href="https://www.linkedin.com/in/anurodh-jha-690105145/"><picture><source media="(prefers-color-scheme: dark)" srcset="https://img.shields.io/badge/LINKEDIN-0d1117?style=flat-square&logo=linkedin&logoColor=ffffff"/><img src="https://img.shields.io/badge/LINKEDIN-ffffff?style=flat-square&logo=linkedin&logoColor=000000" alt="LinkedIn"/></picture></a>
<a href="https://www.cdc.gov/nchs/nhanes/"><picture><source media="(prefers-color-scheme: dark)" srcset="https://img.shields.io/badge/NHANES-0d1117?style=flat-square&logo=databricks&logoColor=ffffff"/><img src="https://img.shields.io/badge/NHANES-ffffff?style=flat-square&logo=databricks&logoColor=000000" alt="NHANES"/></picture></a>
<a href="https://www.cdc.gov/"><picture><source media="(prefers-color-scheme: dark)" srcset="https://img.shields.io/badge/CDC-0d1117?style=flat-square&logo=cdc&logoColor=ffffff"/><img src="https://img.shields.io/badge/CDC-ffffff?style=flat-square&logo=cdc&logoColor=000000" alt="CDC"/></picture></a>

</div>

{pic("s01", "01 — who am i")}
{pic("whoami", "About Anurodh")}
{pic("s02", "02 — research")}
{pic("research", "Four studies")}
{pic("s03", "03 — side projects")}
{pic("projects", "Side projects")}
{pic("s04", "04 — telemetry")}

<div align="center">

<picture><source media="(prefers-color-scheme: dark)" srcset="{stats_d}"/><img src="{stats_l}" width="48%" alt="GitHub statistics"/></picture>
<picture><source media="(prefers-color-scheme: dark)" srcset="{langs_d}"/><img src="{langs_l}" width="48%" alt="Repository languages"/></picture>

<picture><source media="(prefers-color-scheme: dark)" srcset="{graph_d}"/><img src="{graph_l}" width="97%" alt="Contribution activity"/></picture>

</div>

{pic("s05", "05 — the route")}
{pic("timeline", "Route: 2022 to 2027")}
{pic("s06", "06 — stack")}
{pic("stack", "Technical stack")}
{pic("footer", "Current status")}
"""
open(os.path.join(OUT, "README.md"), "w", encoding="utf-8").write(readme)
print("written", OUT)
