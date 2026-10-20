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

## Open
- Safari (owner's iPad): the page did not load (before the fixes of 20 Oct: offline-helper page requests, no
  structuredClone/roundRect, errors shown in the hint line). Those fixes broke `sw.js` – the line's code sat after a `//`
  comment, so the helper returned nothing and the page failed after the first visit on every browser; fixed 20 Oct
  (e6f0e92). Await his report from the iPad: iPadOS version, what he sees.
- Live measurement on the devices (memory, storage per cache, frame times) – "later". Decided: the figures go to a shared
  online store the atlas reads live (not a committed file). Still open: measure inside Pult, on an atlas test page, or
  both. Safari limits: no page memory or per-cache size directly; frame times yes; storage per cache by adding up the
  stored files; overall storage only from Safari 17.
- Pult's unused code (22 declarations, 8 KB) – listed, not to be deleted yet.
