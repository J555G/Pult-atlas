#!/bin/sh
# Pult Atlas: the inventory of every version of Pult, the parts joined to it, and the page.
#   tools/build.sh <Pult checkout> [--site]
# writes out/ (the page with model.json and history.json, e.g. for the private Claude copy); with --site also the web app
# at the root of this repository (what GitHub Pages serves).
set -e
A=$(cd "$(dirname "$0")/.." && pwd); P=$(cd "${1:?the Pult checkout}" && pwd)
mkdir -p "$A/out"
python3 "$A/tools/archgen.py" "$P" "$A/out"
python3 "$A/tools/startup.py" "$P" "$A/out/current.json" "$A/out/startup.json"
python3 "$A/tools/figures.py" "$P" "$A/out/figures.json"
python3 "$A/tools/merge.py" "$A/parts" "$A/out/current.json" "$A/out/model.json"
cp "$A/src/atlas.html" "$A/out/atlas.html"
if [ "$2" = "--site" ]; then python3 "$A/tools/site.py" "$A/out" "$P" "$A"; git -C "$P" rev-parse HEAD > "$A/.pult-head"; fi
