#!/usr/bin/env python3
"""Figures for the Data view, counted from a Pult checkout at every build (so they never go stale):
   tools/figures.py <Pult checkout> <out/figures.json>
datamap.json names them in braces, e.g. "{editions} editions"; merge.py fills them in and reports any it does not know."""
import gzip, json, os, sys
P, out = sys.argv[1], sys.argv[2]
f = {}
def fmt(n): return f'{n:,}'
try:
    cat = json.load(open(os.path.join(P, 'texts', 'catalog.json')))
    f['editions'] = fmt(sum(len(a.get('works', [])) for a in cat['authors'])); f['authors'] = fmt(len(cat['authors']))
except Exception as e: print('figures: no catalogue –', e)
try:
    pk = json.load(open(os.path.join(P, 'packages', 'packages.json')))['packages']
    ENC = {'people', 'encyclopedia'}
    f['dict_packages'] = fmt(sum(1 for p in pk if p['kind'] in ('dictionary', 'morph', 'morphhints', 'latmorph') and p['id'] != 'suda'))
    f['enc_packages'] = fmt(sum(1 for p in pk if p['kind'] in ENC or p['id'] == 'suda'))
    f['packages'] = fmt(len(pk))
except Exception as e: print('figures: no package list –', e)
try:
    d = json.loads(gzip.open(os.path.join(P, 'packages', 'tempora-persons.gdpkg.gz')).read())
    per, st = set(), 0
    for k, v in d['buckets'].items():
        if k.startswith('p:'):
            for pid, L in v['e'].items(): per.add(pid); st += len(L)
    f['persons'] = fmt(len(per)); f['statements'] = fmt(st)
except Exception as e: print('figures: no Tempora persons –', e)
json.dump(f, open(out, 'w'), indent=1)
print('figures:', ', '.join(f'{k} {v}' for k, v in f.items()))
