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
- Safari: the atlas loads on the owner's iPad (seen 21 Oct, 00:54) – the loading problem is solved.
- Pult's numbered decisions are not needed now (decisions.json hook stays unused).
- Distant names smaller (11–15 px). Phones: short labels (Lay, Sto, ↑ ↓ ↕, ✦).
- Touch screens: every control at least 44 px. The top bar then takes 2 rows on iPad, 4 on phones – kept as it is.
- 44 px was still too small on the owner's iPad: a Size setting (Options → Size: Normal 44 px, Large 55 px, Extra large
  66 px) scales bars, panel, menus, overview map and the names in the drawing; touch screens start at Large.
- The owner's Safari draws the page ~1,280 px wide on a ~1,030 pt screen (Request Desktop Website or page zoom < 100 %),
  shrinking everything to ~80 %: the atlas measures innerWidth against screen.width and enlarges itself to make up for it.

## Decided 21 Oct (01:09)
- The information has a fixed pane on the right (below the drawing on phones), the web the pane to its left; nothing
  slides over the drawing any more. Without a selection the pane shows the overview and how to read the drawing; ✕
  returns to it. The pane grows with Size but leaves the drawing at least about half the width.
- Safari's page zoom was the cause of the tiny page (80 %, shared by all of j555g.github.io); recommended: 100 % or the
  Home Screen app. The compensation for shrinking stays until the owner decides.
- 21 Oct 01:14: the owner reset Safari's settings (page zoom back to 100 %).

## Decided 21 Oct (01:17)
- Top bar fixed at 44 px buttons whatever the Size (Size scales pane, menus and the writing in the drawing).
- Version bar slim (about 38 px).
- Divider between drawing and pane, draggable (remembered on the device; double-tap for the usual width).
- The overview moved from the drawing into the top bar: one strip of the main parts, floor by floor (hidden on phones).
- The app never zooms as a whole: no pinch, double-tap or ctrl+wheel page zoom (Safari gestures stopped, touch-action,
  viewport maximum-scale=1); the drawing keeps its own pinch zoom.

## Open
- Walks are hand-written: when Pult changes, the build reports functions they name that no longer exist.
- "First in vN" counts from where a function's file was created: code moved between files (v160 split of app.js) looks
  new there.
- Live measurement on the devices (memory, storage per cache, frame times) – "later". Decided: the figures go to a shared
  online store the atlas reads live (not a committed file). Still open: measure inside Pult, on an atlas test page, or
  both. Safari limits: no page memory or per-cache size directly; frame times yes; storage per cache by adding up the
  stored files; overall storage only from Safari 17.
- Pult's unused code (22 declarations, 8 KB) – listed, not to be deleted yet.
