# Pult Atlas

Every part of **Pult** (the reader for Greek and Latin texts, https://github.com/J555G/lesepult) in three levels – what
each part does, what it relies on, how data moves between them, whether it works offline, and an estimate of what it costs
the device (memory, storage, CPU, GPU) – drawn in space as cards on strings, with a slider through every version of Pult.

**Web app:** https://j555g.github.io/Pult-atlas/ – installable (Add to Home Screen), works offline.

## How it is made
- `parts/*.json` – the hand-written description of Pult's parts: id (`map.relief.contours`), name, what it does, how it
  works, the functions (`file.js|name`) and files it consists of, network needs, load estimates 0–5 with notes; and the
  data flows between parts. `fixups.json` sharpens flows that name only a whole part.
- `tools/archgen.py` – reads every commit of Pult: files and sizes, every top-level declaration of every script, and which
  declarations use which (history.json delta-encoded; current.json).
- `tools/startup.py` – how Pult starts, read from its code: script order, page-ready handlers, the steps of app.js's main().
- `walks.json` – the guided walks, written by hand from Pult's code (each step: parts, functions, a sentence), and captions for
  the start-up steps. `decisions.json` (optional, not yet written) – Pult's numbered decisions with the parts they concern.
- `datamap.json` – the Data view (from the Pult Data Map, 31 Oct 2026): one row per stream of data, source → toolkit →
  package → in Pult, each box with the atlas parts it names; written by hand, the build reports any part it names that
  no longer exists. Figures in braces ({editions}, {persons}, {statements}, {dict_packages}, {enc_packages}) are
  counted from Pult at every build by `tools/figures.py`.
- `parts/H.json` – the parts for Pult's later files: the Suda tab (people.js), Tempora (tempora.js), the map's camera,
  crash reports, astronomy-engine, the encyclopaedia and chronology packages.
- `tools/merge.py` – joins the parts with the inventory into model.json; new functions not yet placed in `parts/` go to
  the main part of their file and are listed in its report.
- `src/atlas.html` – the page (one view in space; Web or Layers, optionally Flat; Explore: walks, start-up, trace, data,
  health, compare; per part: functions with GitHub links, its inner call drawing, history; an overview map).
- `tools/site.py` – the web app at the root: the page with its own head, d3, Pult's fonts, an offline helper (`sw.js`),
  manifest, icons, the data.
- `tools/build.sh <Pult checkout> [--site]` – all of it. Without `--site` only `out/` (for the private Claude copy).

## Updates
GitHub rebuilds the atlas by itself (`.github/workflows/build.yml`): every 30 minutes it checks whether Pult has a new
commit, and on every push here. Its commits touch only the generated files at the root – pull before pushing.

When Pult changes shape (new parts, parts renamed or removed), edit `parts/` – the build report lists functions that were
placed automatically.

Private Claude copy of the page: https://claude.ai/artifact/8hfEfcfQKD6mHoAYwuiyps (republish `out/atlas.html` with
`model.json` and `history.json`; from a new conversation pass this URL as `url`).
