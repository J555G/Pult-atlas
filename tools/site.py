#!/usr/bin/env python3
"""Pult Atlas · the web app: the page (src/atlas.html) with its own head, d3 and Pult's fonts served from here, an offline
helper, the manifest and icons, and the data – written to the root of this repository (GitHub Pages serves it).

    python3 tools/site.py <out dir with model.json, history.json> <Pult checkout> <site dir>
"""
import os, re, shutil, sys
R = os.path.dirname(os.path.dirname(os.path.abspath(__file__))); out, pult, site = sys.argv[1:4]
S = os.path.join(R, 'src')
page = open(os.path.join(S, 'atlas.html'), encoding='utf-8').read()
page = re.sub(r'<meta name="claude:[^>]*>\n?', '', page)
page = re.sub(r'<link rel="preconnect"[^>]*>\n?|<link rel="stylesheet" href="https://fonts\.googleapis\.com[^>]*>\n?', '', page)
page = re.sub(r'<script src="https://cdnjs\.cloudflare\.com/ajax/libs/d3/[^"]+"></script>', '<script src="d3.min.js"></script>', page)
i = page.index('</style>') + len('</style>')
head = open(os.path.join(S, 'site', 'head.html'), encoding='utf-8').read()
html = head + page[:i] + '\n</head>\n<body>\n' + page[i:] + """
<script>if ('serviceWorker' in navigator) addEventListener('load', () => navigator.serviceWorker.register('sw.js').catch(() => {}));</script>
</body>
</html>
"""
open(os.path.join(site, 'index.html'), 'w', encoding='utf-8').write(html)
for f in ['sw.js', 'manifest.webmanifest', 'd3.min.js', 'LICENSE-d3.txt', 'icon-180.png', 'icon-192.png', 'icon-512.png']:
    shutil.copy(os.path.join(S, 'site', f), os.path.join(site, f))
for f in ['model.json', 'history.json']:
    shutil.copy(os.path.join(out, f), os.path.join(site, f))
# Pult's own fonts (SIL Open Font License): Gentium Book Plus and Source Sans 3
fd = os.path.join(site, 'fonts'); os.makedirs(fd, exist_ok=True)
for f in os.listdir(os.path.join(pult, 'fonts')):
    if f.startswith(('gentium-book-plus', 'source-sans-3')) or f.upper().startswith('OFL') or f.lower().startswith('license'):
        shutil.copy(os.path.join(pult, 'fonts', f), os.path.join(fd, f))
css = open(os.path.join(pult, 'fonts.css'), encoding='utf-8').read()
blocks = [b for b in re.split(r'(?=/\*)', css) if 'gentium-book-plus' in b or 'source-sans-3' in b]
open(os.path.join(site, 'fonts.css'), 'w', encoding='utf-8').write(''.join(blocks))
print('atlas web app written to', site)
