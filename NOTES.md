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

## Decided 21 Oct (12:20)
- One finger up/down tips the tower round the screen's horizontal line through the spot touched, also after a twirl
  (measured: after a 0.5 rad twirl a swipe down moves a far part straight down the screen; a full turn returns exactly).
- Parts near the tower's axis barely move on a sideways swipe – kept as it is for now (owner).

## Decided 21 Oct (13:26)
- The globe rules conflicted (sideways turned round the tower's own axis, up/down round the screen's line, each swipe
  round a different spot – tipped or twirled, sideways went slanted or backwards and the tower wandered). Replaced, by
  the owner's choice, with a trackball: one finger rolls the tower whichever way it moves, round the screen's own lines,
  pivoting on the selected part (else the middle of the tower), which stays put. Speed set so the tower's near edge
  keeps up with the finger. Measured: parts move the finger's way upright, twirled and upside down; the pivot does not
  move; right-down-up-left returns exactly. Front / Top / Corner set the tower straight again.

## Decided 21 Oct (13:51)
- Space: only what is in direct view can be tapped (owner's choices). Names drawn on top come first; otherwise the
  nearest thing along the line of sight wins – card, floor, plot or opened-group area –, even where the thing in front
  is see-through. A tap on a plot selects its main part, on a group area that opened part, on bare floor clears the
  selection. Measured (Corner): 81 of 109 card centres tappable, the rest behind a floor (13), a name (8) or a nearer
  card (7); from below none (the floors are in front).
- Questions to the owner go in writing in the reply, not as tappable choices (he wants to comment on every point).

## Decided 21 Oct (18:20)
- Bug fixed: in Space every card was drawn after all floors, plots and group areas, so see-through surfaces in front
  never tinted the cards behind them. Now drawn back to front: the floors are parallel, so from the camera's height
  outwards – floors below it bottom-up, above it top-down, each floor before or after the cards standing on it, the
  camera's own storey last. Lines are drawn after the farthest step, so nearer floors tint them too.

## Decided 21 Oct (18:34)
- Space: the cards lie flat on their plot (no longer upright facing the camera), each turned on the spot so its
  writing faces the viewer; from below read the right way round (never mirrored). Spaced by their diagonal (230 × 230)
  so that, turning, they never touch – opened parts' cards never overlap their group's. Seen nearly edge-on: a sliver
  in its colour with the name written above it; far: the outline in its colour.
- A card is never hidden by its own floor, plot or group – neither in the drawing (each floor drawn just before its
  own cards) nor for tapping; other floors hide it (above the camera drawn top-down, below it bottom-up). Measured:
  from below 74 of 109 card centres now tappable (before: none), from the corner 90.
- Floors keep their spacing (the owner: the point is seeing how the parts relate, not a flat stack).
- Lines start and end on the flat cards.

## Decided 21 Oct (18:47)
- The owner: keep everything tidy and readable – the point is understanding Pult's architecture. So the flat cards became
  flat tiles in tight rows on their plot (200 × 92, fixed like squares on a map), each name written upright over its
  tile on the screen – never squashed, mirrored or upside down, from any side –, nearest first; a name that would cover
  one already written is left out, its tile stays. Tapping a name = tapping its tile. (Replaces the turning flat cards.)

## Decided 21 Oct (20:56)
- A part's name is written flat on its tile and fixed to it, like writing on a table: it turns only with the tower
  (from the far side it reads upside down); from below flipped across the tile's long side so it is not mirrored
  (owner, 20:59: "the name should be fixed to the tile" – a first version that turned the writing was wrong). Up to two
  lines as large as fits (15–22 units), cut short with … beyond that. Names too small to read on the screen (under about 6.5 px) are left out; the tile stays.

## Decided 21 Oct (21:39)
- Every name in Space is written on what it names and fixed to it (owner): plot names in a heading band along the plot's
  top edge, opened parts' names (▾) in a band at the top of their dashed area, floor names along the floor plate's front
  edge (the margin labels and their tap-to-glide are gone, owner's choice 3a). From below flipped, never mirrored.
- Far away, like a map: three levels by the tiles' width on the screen – far (< ~55 px): plain tiles and the main
  part's name large across its whole plot, over the tiles; middle: the parts' names in one large line; near (> ~127 px):
  up to two lines. Short crossfades between them.
- Writing on a surface is drawn at its true size on the screen and laid on with a near-unit transform (a huge font
  shrunk by the transform comes out garbled in the browser).

## Decided 22 Oct (00:45)
- Bug fixed (owner's screenshot): lines above the plots were dimmed – all lines were drawn in one go before the nearer
  floors and plots. Now each line is cut at the floor heights and each piece drawn in its place among the floors, back
  to front (floors above the camera top-down: the pieces above a floor before it; below the camera bottom-up: after it).

## Decided 31 Oct (13:35) – the owner approved all fourteen proposals
- Data Map integrated as a fifth view, Data (datamap.json; each box's parts are tappable, the selection carries over to
  the other views, a selected part marks its rows). The build checks the parts it names; its figures stay hand-written.
  The old Pult Data Map artifact is left as it is (no choice made about it).
- Found while doing it: the atlas did not know Pult's later files (tempora.js, people.js, mapcam.js, crash.js,
  astronomy.min.js – about 370 KB of code, 414 declarations). Added (parts/H.json): Suda tab and Tempora as main parts on
  the On screen floor, map.camera, shell.crash, engine.astronomy, data.people, data.chrono. All 1,608 declarations placed.
- Pult's own colours (lesepult/style.css: paper #faf8f3, ink #211f1b, burgundy #7a2e2e for the selection, Pult's blue for
  "uses", ochre for "used by") and fonts (Source Sans 3 for the interface and part names, Gentium Book Plus for headings).
- One muted colour family per floor (on screen red-brown, behind the scenes green-grey, engines slate, sources ochre);
  each main part's own hue only as the thin edge of its plot in Space.
- Light or dark as set in Pult on this device (read from Pult's database 'greekreader', store 'settings', key 'theme' –
  only if the database already exists: opening a missing one would create it empty and break Pult's first start); else
  the device; Options → Theme overrides (As in Pult / Light / Dark).
- Top bar like Pult's: ‹ › ⌂, the views as tabs (Flow · Map · Focus · Space · Data), search, Controls, Explore, ⓘ;
  everything else in the Controls tray on every screen. Phones: the tabs on a second row. The overview strip is gone.
- The version bar shows only with Explore → Versions open, or while an older version is shown.
- Flow with nothing selected or lit: one ribbon per pair of main parts (Map already did this).
- A part's page folds into sections like Pult's dictionary sources (the first open; the others as last left).
- Start page on opening (⌂ returns to it): what the atlas is, Data · Flow · Space · Guided walks, the four floors with
  their main parts.
- The old physics web (draw3d, tick3d, frame3d, fit3d, pan3d, Web/Layers/Flat) removed: 18 KB less.

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
