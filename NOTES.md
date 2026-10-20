# Working notes

- Decisions about the atlas are numbered A1, A2, … (Pult's own decisions keep their own numbers, 475 onward).
- Work on the atlas happens in its own conversation; Pult work in Pult's.
- The owner wants every request's options and their implications laid out, and the choices left to him.

## History before this repository (in Pult's repo, tools/arch, 20 Oct 2026)
- Built from seven readings of Pult's code (shell & reader; dictionary & export; library; settings, offline, storage &
  data; map; relief, sun & sky; online sources, engines & build tools).
- Choices made: figures – code and data sizes measured, loads estimated (live measurement on the devices later); one view
  in space (Web / Layers, Flat), cards facing the viewer that sway on their strings; colour by part or by load, four load
  bars per card; filter to what a part relies on / what relies on it / both, with whole chains; spacing slider; twirl with
  two fingers; back and forward through the parts looked at; full screen keeps the top bar; installable web app.

## Decided 21 Oct
- The offline-helper fix stays (the owner first asked to undo it, then chose to keep it once the consequence was laid out).
- The drawing fills the screen between a slim top bar and a slim version bar (the bars carry the safe areas); the
  full-screen button is gone.
- Filters as button rows that wrap, never drop-down menus.
- Cards far away show only their name in large letters with a bar of their colour; nearer (wider than 70–105 px on
  screen, crossfading) the full card. One tap slides the panel in over the drawing (bottom sheet on phones); ✕, Escape
  or a tap on the empty drawing closes it. The legend that used to fill the empty panel opens from ⓘ in the top bar.

## Decided 21 Oct (later)
- The selected part stays where it is until moved by hand – also when filters or the arrangement change (no refit then).
- Opening or closing a part keeps it in place: its parts start side by side where it was.
- All nine suggestions for understanding Pult approved and built: guided walks (8, in walks.json), start-up order
  (tools/startup.py), trace a function, follow the data (two flow steps each way), health (most relied on, circles,
  pairs, largest, code nothing calls), compare two versions, per part: GitHub links, inner call drawing, history and
  "how it came about", overview map. Lit parts never move the camera by themselves ("Show them" does, when tapped).
- Inventory: the offline helper's scripts (sw.js, reliefsw.js) are their own scope – names no longer link across.

## Decided 21 Oct (night)
- Pult's numbered decisions are not needed now (decisions.json hook stays unused).
- Distant names smaller (11–15 px). Phones: short labels (Lay, Sto, ↑ ↓ ↕, ✦).
- Touch screens: every control at least 44 px. The top bar then takes 2 rows on iPad, 4 on phones – kept as it is.
- 44 px was still too small on the owner's iPad: a Size setting (Options → Size: Normal 44 px, Large 55 px, Extra large
  66 px) scales bars, panel, menus, overview map and the names in the drawing; touch screens start at Large.

## Open
- Walks are hand-written: when Pult changes, the build reports functions they name that no longer exist.
- "First in vN" counts from where a function's file was created: code moved between files (v160 split of app.js) looks
  new there.
- Safari (owner's iPad): the page did not load (before the fixes of 20 Oct: offline-helper page requests, no
  structuredClone/roundRect, errors shown in the hint line). Those fixes broke `sw.js` – the line's code sat after a `//`
  comment, so the helper returned nothing and the page failed after the first visit on every browser; fixed 20 Oct
  (e6f0e92). Await his report from the iPad: iPadOS version, what he sees.
- Live measurement on the devices (memory, storage per cache, frame times) – "later". Decided: the figures go to a shared
  online store the atlas reads live (not a committed file). Still open: measure inside Pult, on an atlas test page, or
  both. Safari limits: no page memory or per-cache size directly; frame times yes; storage per cache by adding up the
  stored files; overall storage only from Safari 17.
- Pult's unused code (22 declarations, 8 KB) – listed, not to be deleted yet.
