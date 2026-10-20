# Pult Atlas

Every part of **Pult** (the reader for Greek and Latin texts, https://github.com/J555G/lesepult) in three levels – what
each part does, what it relies on, how data moves between them, whether it works offline, and an estimate of what it costs
the device (memory, storage, CPU, GPU) – drawn in space as cards on strings, with a slider through every version of Pult.

**Web app:** https://j555g.github.io/pult-atlas/ – installable (Add to Home Screen), works offline.

## How it is made
- `parts/*.json` – the hand-written description of Pult's parts: id (`map.relief.contours`), name, what it does, how it
  works, the functions (`file.js|name`) and files it consists of, network needs, load estimates 0–5 with notes; and the
  data flows between parts. `fixups.json` sharpens flows that name only a whole part.
- `tools/archgen.py` – reads every commit of Pult: files and sizes, every top-level declaration of every script, and which
  declarations use which (history.json delta-encoded; current.json).
- `tools/merge.py` – joins the parts with the inventory into model.json; new functions not yet placed in `parts/` go to
  the main part of their file and are listed in its report.
- `src/atlas.html` – the page (one view in space; Web or Layers, optionally Flat).
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
