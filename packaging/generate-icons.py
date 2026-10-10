#!/usr/bin/env python3
"""Regenerate TabDocs icons from its original PNG. Requires Pillow (pip install Pillow)."""
from pathlib import Path
from PIL import Image
from base64 import b64encode
root=Path(__file__).resolve().parent.parent/'assets/app-icon'
src=root/'tabdocs-source.png'
im=Image.open(src).convert('RGBA')
im.resize((1024,1024),Image.Resampling.LANCZOS).save(root/'tabdocs-1024.png')
im.resize((512,512),Image.Resampling.LANCZOS).save(root/'tabdocs-macos-512.png')
im.save(root/'tabdocs.ico',format='ICO',sizes=[(16,16),(20,20),(24,24),(32,32),(40,40),(48,48),(64,64),(128,128),(256,256)])
im.resize((1024,1024),Image.Resampling.LANCZOS).save(root/'tabdocs.icns',format='ICNS')
for size in (16,24,32,48,64,128,256,512):
    f=root/'hicolor'/f'{size}x{size}'/'apps'/'org.tabdocs.TabDocs.png'
    f.parent.mkdir(parents=True,exist_ok=True)
    im.resize((size,size),Image.Resampling.LANCZOS).save(f)
svg='<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" width="512" height="512" viewBox="0 0 512 512"><image width="512" height="512" xlink:href="data:image/png;base64,'+b64encode(src.read_bytes()).decode()+'"/></svg>\n'
(root/'tabdocs.svg').write_text(svg)
(root/'hicolor/scalable/apps/org.tabdocs.TabDocs.svg').write_text(svg)
print('TabDocs icons regenerated')
