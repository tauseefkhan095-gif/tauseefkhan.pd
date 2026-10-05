#!/usr/bin/env python3
"""Optional, run once on your computer:  python3 download-images.py

Some project pictures still load from the server of the old Framer portfolio. This saves each of them
into images/projects/ and points index.html at the local copies, so the site no longer depends on that server.
Pictures that cannot be downloaded are left exactly as they are."""
import re, sys, pathlib, urllib.request

root = pathlib.Path(__file__).resolve().parent
page = root / 'index.html'
html = page.read_text(encoding='utf-8')
urls = set(re.findall(r'https://framerusercontent\.com/images/[A-Za-z0-9_-]+\.(?:png|jpe?g|webp)(?:\?scale-down-to=\d+)?', html))
if not urls:
    sys.exit('Nothing to do: index.html has no pictures on framerusercontent.com.')
dest = root / 'images' / 'projects'
dest.mkdir(parents=True, exist_ok=True)
done = 0
for u in sorted(urls, key=len, reverse=True):          # longest first, so one address is never part of another
    m = re.match(r'.*/([A-Za-z0-9_-]+)\.(png|jpe?g|webp)(?:\?scale-down-to=(\d+))?$', u)
    name = m.group(1) + ('-' + m.group(3) if m.group(3) else '') + '.' + m.group(2)
    try:
        data = urllib.request.urlopen(urllib.request.Request(u, headers={'User-Agent': 'Mozilla/5.0'}), timeout=60).read()
        if len(data) < 500:
            raise ValueError('empty file')
        (dest / name).write_bytes(data)
        html = html.replace(u, 'images/projects/' + name)
        done += 1
        print('saved  ', name)
    except Exception as e:
        print('SKIPPED', u, '-', e)
page.write_text(html, encoding='utf-8')
print('%d of %d pictures saved; index.html now uses the local copies.' % (done, len(urls)))
