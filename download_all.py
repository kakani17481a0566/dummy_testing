import os
import re
import urllib.request
from urllib.parse import urljoin

base_url = 'https://logartis.info/'
target_dir = r'c:\Users\MO\Downloads\New folder (2)'

downloaded = set()

def download_file(rel_path):
    rel_path = rel_path.strip().lstrip('/')
    if not rel_path or rel_path in downloaded:
        return
    downloaded.add(rel_path)
    
    url = urljoin(base_url, rel_path)
    local_path = os.path.join(target_dir, rel_path.replace('/', os.sep))
    os.makedirs(os.path.dirname(local_path), exist_ok=True)
    
    if os.path.exists(local_path) and os.path.getsize(local_path) > 0:
        print(f"[EXISTS] {rel_path}", flush=True)
        return True
        
    try:
        print(f"[DOWNLOADING] {url} ...", flush=True)
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, timeout=15) as resp, open(local_path, 'wb') as out:
            out.write(resp.read())
        print(f"[OK] {rel_path} ({os.path.getsize(local_path)} bytes)", flush=True)
        return True
    except Exception as e:
        print(f"[FAILED] {rel_path}: {e}", flush=True)
        return False

# Core files
download_file('index.html')
download_file('manifest.webmanifest')
download_file('styles.8c9e672140f150fba930.css')
download_file('runtime.d4905fc349c3942af5be.js')
download_file('polyfills.3785b940a5ff94175efb.js')
download_file('polyfills-es5.97728994a8f4007b99ec.js')
download_file('main.be139ff41f386a5b9c64.js')

# Icons
icons = [
    'assets/thumbnail.jpg',
    'assets/cloud.png',
    'assets/lensflare2.png',
    'assets/lensflare3.png',
    'assets/lensflare4.png',
    'assets/prev.jpg',
    'assets/prev.mp4',
    'assets/icon/apple-icon-57x57.png',
    'assets/icon/apple-icon-60x60.png',
    'assets/icon/apple-icon-72x72.png',
    'assets/icon/apple-icon-76x76.png',
    'assets/icon/apple-icon-114x114.png',
    'assets/icon/apple-icon-120x120.png',
    'assets/icon/apple-icon-144x144.png',
    'assets/icon/apple-icon-152x152.png',
    'assets/icon/apple-icon-180x180.png',
    'assets/icon/android-icon-192x192.png',
    'assets/icon/favicon-32x32.png',
    'assets/icon/favicon-96x96.png',
    'assets/icon/favicon-16x16.png',
]
for i in icons:
    download_file(i)

# Sounds
sounds = [
    'assets/sounds/bg.mp3',
    'assets/sounds/chapel.mp3',
    'assets/sounds/chimes.mp3',
    'assets/sounds/electric.mp3',
    'assets/sounds/forest.mp3',
    'assets/sounds/night.mp3',
    'assets/sounds/thunder2.mp3',
    'assets/sounds/village.mp3',
    'assets/sounds/wind.mp3',
]
for s in sounds:
    download_file(s)

# Models
models = [
    'assets/models/cat_animated/cat.gltf',
    'assets/models/cat_animated/cat.bin',
    'assets/models/cat_animated/cat.png',
    'assets/models/house/house.FBX',
    'assets/models/chapel/chapel.obj',
    'assets/models/chapel/chapel.mtl',
    'assets/models/converted/tr.obj',
    'assets/models/converted/fo.obj',
    'assets/models/converted/fo_diff1.png',
    'assets/models/village/1.obj',
    'assets/models/village/2.obj',
    'assets/models/village/3.obj',
    'assets/models/converted/rock/Rock_1.obj',
    'assets/models/converted/rock/Rock_2.obj',
    'assets/models/converted/rock/Rock_3.obj',
    'assets/models/converted/rock/Rock_4.obj',
    'assets/models/converted/rock/Rock_5.obj',
    'assets/models/man/man_tshirt_jeans.FBX',
]
for m in models:
    download_file(m)

# JSON Data
download_file('assets/works/data.json')
data_json_path = os.path.join(target_dir, 'assets', 'works', 'data.json')
if os.path.exists(data_json_path):
    with open(data_json_path, 'r', encoding='utf-8', errors='ignore') as f:
        text = f.read()
        paths = re.findall(r'assets/[a-zA-Z0-9_\-./]+\.[a-zA-Z0-9]+', text)
        for p in paths:
            download_file(p)

print("=== Finished Downloader Script ===", flush=True)
