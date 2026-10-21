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

## Decided 21 Oct (01:22)
- Four views of the same parts, switchable, the selection kept between them: Flow (default; columns sources → stored and
  behind the scenes → engines → screen, order untangled by barycentres, a main part's opened parts framed together),
  Map (a region per main part with its parts, regions of a floor wrapping, ribbons between regions until a part is
  selected), Focus (selected part in the middle: data in left, data out right, calls above, callers below), Space (the
  3D cards, now settled before shown, distant names never overlap – a dot instead). The matrix view (D) was not chosen.
- Lines: Data, Code, Selected only – independent switches, any combination; flow labels only with Options → Flow labels.
- Flow tidied (01:44, the owner chose 1–3 of six): lines within one column only for the selected part (↕ n on the card
  otherwise); an opened group's lines bundled into one ribbon per partner until a part is selected; zoomed out, cards show
  only their name, large. Not chosen: accordion opening, sticky column heads, quiet colours.
- Map: inside a region its own parts first, then each opened part as a framed group (▾ name · n parts, bar on the
  left, one step in per level); with a part selected only its own lines are drawn.
- Flow: an opened group has a header band (▾ name · n parts) and a bar down its left; its parts indented one step per
  level (right edges in line), a part opened inside it under its own ▾ sub-heading, its parts kept together.

## Decided 21 Oct (01:49)
- Space rebuilt from scratch as a tower of four floors (the owner chose it over 'flow in depth' and 'ring of floors'):
  sources at the bottom, then engines, stored and behind the scenes, the screen on top; every main part a plot in its
  colour, its parts upright cards (facing the viewer) in rows, opened parts as dashed areas with ▾ names; lines between
  floors straight up or down a shaft and across at the half-floor; same-floor lines as arches only for the selection;
  with nothing selected one bundle per pair of main parts; a selected plot shows its links in blue / orange.
  Nothing moves but the camera: no physics, no pulling parts. Snaps Front / Top / Corner; Floors sets the floor height.
  Far parts are chips, nearer their names, near the whole card; plot names drawn last with a halo.
- The old physics web (draw3d, frame3d, tick3d …) is no longer used – still in the code, to be removed when the tower
  has proved itself.

## Decided 21 Oct (07:54)
- Compact bar on touch screens (phones and iPad) and in windows under 1100 px: one row (‹ › ⌂, search, Controls,
  overview strip – not on phones –, Explore, ⓘ); Controls drops a tray with the views, lines, colours, filters and
  options over the drawing, closing when the drawing is tapped. Tray buttons 44 px. Wide mouse screens keep the full bar.
- The standing gesture note is gone; its line only shows short messages and errors.
- Bug fixed: the drawing could not shrink below its canvas size, so a taller pane (dragged divider, phones) slid under
  the version bar – the canvas is now absolute inside its area.
- Lines on phones: same as elsewhere (the owner declined 'Selected only' by default).

## Decided 21 Oct (08:08)
- Opening or closing a part keeps its top edge where it was on the screen (Flow, Map, Space; the view moves by what the
  layout moved). Map and Space now also open parts inside a main part that is itself closed.

## Decided 21 Oct (08:24)
- ‹ › go back and forward through everything looked at: each stop is the selected part (or none) together with the
  Explore page that was open (walk and step, trace, data, health, comparison …). Also at the top of the pane beside ✕
  (hidden when there is nowhere to go), and the browser's / phone's back gesture.

## Decided 21 Oct (09:49)
- Space controls calmed (owner chose 1 and 3 of four; not chosen: speed work, focus helpers): one finger turns with a
  little glide, the tilt kept above the floors (pitch −1.48 … −0.08), no twisting; two fingers slide and zoom towards
  the fingers; mouse: shift/right-drag slides, wheel zooms at the pointer; a tap stays a tap up to 8 px.
- Space labels never overlap: placed by priority – selected part, plot names, floor names (now in the left margin at
  their floor's height), opened-group names, then cards from the nearest back; whatever would cover something already
  placed is left out and its card becomes a small chip. Floors spaced by their depth so they do not cover each other.
- Measured, not yet acted on: 200–600 style look-ups per frame in Space (3–5 ms a frame on a desktop, more on phones).

## Decided 21 Oct (09:58)
- The divider can be pulled all the way to the edge (the pane closes, the drawing takes the whole width; on phones
  down to the bottom). A ⅓ button on the divider brings the pane back to the right third (phones: the bottom third).

## Decided 21 Oct (10:10)
- Space steered like a map app (owner's choice over a freed turntable or walking through): one finger slides the floors
  so the spot touched stays under the finger (with a glide); two fingers pinch to zoom towards the floor spot between
  them and twist to turn round it; both fingers up or down together tilt (from nearly level to straight down). Mouse:
  drag slides, right/shift-drag turns and tilts, wheel zooms at the pointer. What two fingers do is decided once per
  touch from both fingers' movement (touch events arrive one finger at a time – judged per event, a twist looked like a
  tilt and the halves cancelled out).
- Bug found and fixed: the tower had been seen from below all along (the tilt's sign was reversed, so the limit meant
  to keep the camera above the floors kept it underneath). The camera is now always above.
- Measured: slide, pinch and wheel keep the touched spot exactly in place; twist turns the floors the fingers' way.

## Decided 21 Oct (10:12)
- Map-app steering was wrong for a tower (measured: nothing followed the finger – each floor drifted at its own speed –,
  a swipe up flew 4,230 units sideways instead of climbing, the pivot floated between floors). Replaced, by the owner's
  choice, with 'scroll the tower': swipe up/down rides through the floors (the part touched follows the finger),
  left/right turns the tower round its axis (the part touched follows), the swipe keeps the direction it began in;
  pinch closer/further towards the floor under the fingers; two fingers up/down together tilt; tap a floor's name in
  the margin to glide there. The pivot always stays on the tower's axis. Mouse: drag the same, shift-drag tilts.
- Floors about half as far apart (420 base, grown by 0.21 × floor depth); names still never overlap.

## Decided 21 Oct (10:40)
- Space, two fingers: sliding moves the tower in the plane of the screen (the plane facing the viewer, whatever the tilt),
  pinch zooms towards the fingers, twist turns the tower round its axis the fingers' way – all at once. The pivot may now
  leave the axis by up to about one floor's width (and half a floor-width above or below the tower); one-finger turning
  still turns round the tower's axis, so a tower slid aside turns in place.
- Tilt moved from 'two fingers up/down' to a Tilt slider in the Controls tray (Space only); Front / Top / Corner stay.
- Measured: a two-finger slide moves a part by the fingers' distance (within ~10 %, parts nearer than the pivot a little
  more); twist turns the parts the fingers' way; a one-finger turn after sliding aside keeps the axis in place.

## Decided 21 Oct (11:58)
- Two fingers: the spot between them when they touch down (the part there, else the tower's axis at that floor) now
  follows them exactly – slid with them, spread or drawn in with the pinch like a photo (measured: offset to the fingers
  unchanged by a slide, scaled exactly by the pinch). Other parts, nearer or further, move by their own perspective.

## Decided 21 Oct (12:10)
- Space steered like a globe (owner's choices): one finger sideways turns the tower round its axis, up or down tips it
  over round the spot touched (that spot stays put) – without limit, right over and upside down if wanted –, diagonal
  swipes do both at once. Riding up and down the floors now with two fingers (slide) or by tapping a floor's name.
- The Tilt slider is gone again (one finger tilts). Front / Top / Corner glide back the short way round.
- Two fingers: twirling turns the picture in the plane of the screen (measured: 0.5 rad of fingers → 0.51 rad), the
  spot between them staying under them; slide and pinch as before.

## Open
- Android: installing from Chrome failed (21 Oct); the owner installed the atlas via Brave instead. Chrome's own check
  finds the atlas installable (no errors). If Chrome is wanted later: harden the manifest (fixed id and start_url,
  separate 'any' and 'maskable' icons with safe margins). Never advise clearing site data for j555g.github.io – Pult's
  offline data lives there too.
- Walks are hand-written: when Pult changes, the build reports functions they name that no longer exist.
- "First in vN" counts from where a function's file was created: code moved between files (v160 split of app.js) looks
  new there.
- Live measurement on the devices (memory, storage per cache, frame times) – "later". Decided: the figures go to a shared
  online store the atlas reads live (not a committed file). Still open: measure inside Pult, on an atlas test page, or
  both. Safari limits: no page memory or per-cache size directly; frame times yes; storage per cache by adding up the
  stored files; overall storage only from Safari 17.
- Pult's unused code (22 declarations, 8 KB) – listed, not to be deleted yet.
