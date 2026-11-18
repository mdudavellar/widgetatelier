"""Expand the local font catalog from official Google Fonts files and notices."""
from pathlib import Path
import urllib.request,re,json,base64,concurrent.futures
root=Path(__file__).parent
assets=json.loads((root/'fonts.json').read_text())
names=['Inter','Roboto','Open Sans','Oswald','Rubik','Manrope','Outfit','Urbanist','Work Sans','DM Mono','Archivo','Barlow','Righteous','Bebas Neue','Pacifico','Dancing Script','Sacramento','Allura','Parisienne','Satisfy','Cinzel','Prata','Italiana','Marcellus','Forum','Abril Fatface','Alfa Slab One','Comfortaa','Amatic SC','Shadows Into Light','Patrick Hand','Indie Flower']
def fetch(url):
 return urllib.request.urlopen(urllib.request.Request(url,headers={'User-Agent':'Mozilla/5.0 AppleWebKit/537.36 Chrome/120.0.0.0 Safari/537.36'}),timeout=50).read()
def load(name):
 slug=name.lower().replace(' ','');license=None;license_path=None
 for folder,filename in [('ofl','OFL.txt'),('apache','LICENSE.txt'),('ofl','LICENSE.txt')]:
  try:license=fetch(f'https://raw.githubusercontent.com/google/fonts/main/{folder}/{slug}/{filename}').decode();license_path=filename;break
  except urllib.error.HTTPError as e:
   if e.code!=404:raise
 if not license:raise ValueError('No license for '+name)
 css=fetch('https://fonts.googleapis.com/css2?family='+name.replace(' ','+')+'&display=swap').decode()
 blocks=re.findall(r'/\* latin \*/\s*(@font-face\s*\{[^}]+\})',css) or re.findall(r'@font-face\s*\{[^}]+\}',css)[-1:]
 if not blocks:raise ValueError('No font face for '+name)
 urls={url for block in blocks for url in re.findall(r'url\(([^)]+)\)',block)}
 for url in urls:
  encoded='data:font/woff2;base64,'+base64.b64encode(fetch(url)).decode();blocks=[block.replace(url,encoded) for block in blocks]
 (root/'licenses'/f'{slug}-{license_path}').write_text(license)
 print(name,'ready',flush=True)
 return name,{'css':'\n'.join(blocks),'license':license,'source':'https://fonts.google.com/specimen/'+name.replace(' ','+')}
with concurrent.futures.ThreadPoolExecutor(max_workers=4) as ex:
 for name,asset in ex.map(load,[name for name in names if name not in assets]):assets[name]=asset
(root/'fonts.json').write_text(json.dumps(assets,ensure_ascii=False))
