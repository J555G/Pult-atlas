#!/usr/bin/env python3
"""Pult Atlas · how Pult starts, read from its code: the scripts in the order index.html loads them, the handlers that run
when the page is ready, and the steps of app.js's main() in order – which ones it waits for, which run later on a timer.

    python3 tools/startup.py <Pult checkout> <inventory current.json> <out startup.json>

Each step names a declaration (file|name) where it can; merge.py joins it to its part.
"""
import json, re, sys, os

def main(repo, inv_path, out):
    inv = json.load(open(inv_path)); decls = {d['k']: d for d in inv['decls']}
    defs = {}
    for k in decls:
        f, n = k.split('|'); defs.setdefault(n, k)
    html = open(os.path.join(repo, 'index.html'), encoding='utf-8').read()
    scripts = re.findall(r'<script\s+src="([^"?]+)', html)
    steps = []
    for s in scripts:
        if '/' in s: continue
        size = inv['files'].get(s, 0)
        steps.append({'kind': 'script', 'file': s, 'bytes': size, 'decl': f'{s}|(top level)' if f'{s}|(top level)' in decls else None})
    # handlers that wait for the page to be ready (DOMContentLoaded), script by script
    ready = []
    for s in scripts:
        p = os.path.join(repo, s)
        if not os.path.exists(p): continue
        t = open(p, encoding='utf-8').read()
        if re.search(r"addEventListener\(\s*'DOMContentLoaded'", t) and s != 'app.js': ready.append(s)
    if ready: steps.append({'kind': 'ready', 'files': ready})
    # main() in app.js: the calls in order
    app = open(os.path.join(repo, 'app.js'), encoding='utf-8').read()
    m = re.search(r'^\(async function main\(\) \{\n(.*?)^\}\)\(\);', app, re.S | re.M)
    if m:
        body = m.group(1); line0 = app[:m.start(1)].count('\n') + 1; seen = set()
        for li, ln in enumerate(body.split('\n')):
            code = re.sub(r'//.*$', '', ln)
            if 'addEventListener(' in code: code = code[:code.index('addEventListener(')]   # (what runs on a tap later is not start-up)
            if 'serviceWorker.register' in code and 'sw' not in seen:
                seen.add('sw'); steps.append({'kind': 'call', 'name': 'register the offline helper', 'decl': 'sw.js|(top level)' if 'sw.js|(top level)' in decls else None, 'wait': False, 'line': line0 + li}); continue
            later = {}
            for tm in re.finditer(r'setTimeout\((.*?),\s*(\d+)\)', code):
                for n in re.findall(r'([A-Za-z_$][\w$]*)\s*\(', tm.group(1)): later[n] = int(tm.group(2))
            for cm in re.finditer(r'(await\s+)?([A-Za-z_$][\w$]*)\s*\(', code):
                n = cm.group(2)
                if n not in defs or n in seen or n in ('setting', 'getAll', '$'): continue
                seen.add(n)
                st = {'kind': 'call', 'name': n, 'decl': defs[n], 'wait': bool(cm.group(1)), 'line': line0 + li}
                if n in later: st['later'] = later[n]
                if re.match(r'\s*if\s*\(', code): st['cond'] = True   # (only when something is there, e.g. a text open last time)
                steps.append(st)
    json.dump({'steps': steps}, open(out, 'w'), separators=(',', ':'))
    print(len([s for s in steps if s['kind'] == 'script']), 'scripts,', len([s for s in steps if s['kind'] == 'call']), 'start-up steps')

main(*sys.argv[1:4])
