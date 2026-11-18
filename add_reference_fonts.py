"""Vendor identifiable open reference fonts; keep unknown/commercial references explicit."""
from pathlib import Path
import urllib.request,re,json,base64,concurrent.futures
root=Path(__file__).parent
assets=json.loads((root/'fonts.json').read_text())
styles={
 'Montserrat':':ital,wght@0,200..700;1,200..700',
 'Raleway':':ital,wght@0,200..700;1,200..700',
 'League Spartan':':wght@200..700',
 'Poppins':':ital,wght@0,200;0,300;0,400;0,700;1,400;1,700',
 'Lato':':ital,wght@0,300;0,400;0,700;1,400;1,700',
 'Great Vibes':'', 'Anton':'',
 'Josefin Sans':':ital,wght@0,200..700;1,200..700',
 'Lora':':ital,wght@0,400..700;1,400..700',
 'Averia Sans Libre':':ital,wght@0,300;0,400;0,700;1,400;1,700',
 'EB Garamond':':ital,wght@0,400..700;1,400..700',
 'GFS Didot':''
}
def fetch(url):
 return urllib.request.urlopen(urllib.request.Request(url,headers={'User-Agent':'Mozilla/5.0 AppleWebKit/537.36 Chrome/120.0.0.0 Safari/537.36'}),timeout=50).read()
def load(entry):
 name,spec=entry;slug=name.lower().replace(' ','')
 if name=='Montserrat':license=assets[name]['license']
 else:
  try:license=fetch(f'https://raw.githubusercontent.com/google/fonts/main/ofl/{slug}/OFL.txt').decode()
  except Exception:license=fetch(f'https://raw.githubusercontent.com/google/fonts/main/ofl/{slug}/LICENSE.txt').decode()
 css=fetch('https://fonts.googleapis.com/css2?family='+name.replace(' ','+')+spec+'&display=swap').decode()
 blocks=re.findall(r'/\* latin \*/\s*(@font-face\s*\{[^}]+\})',css)
 if not blocks:blocks=re.findall(r'@font-face\s*\{[^}]+\}',css)
 urls={url for block in blocks for url in re.findall(r'url\(([^)]+)\)',block)}
 data={url:'data:font/woff2;base64,'+base64.b64encode(fetch(url)).decode() for url in urls}
 for url,value in data.items():blocks=[block.replace(url,value) for block in blocks]
 (root/'licenses'/f'{slug}-OFL.txt').write_text(license)
 print(name,'ready',len(blocks),'faces',flush=True)
 return name,{'css':'\n'.join(blocks),'license':license,'source':'https://fonts.google.com/specimen/'+name.replace(' ','+')}
with concurrent.futures.ThreadPoolExecutor(max_workers=4) as ex:
 for name,asset in ex.map(load,styles.items()):assets[name]=asset
(root/'fonts.json').write_text(json.dumps(assets,ensure_ascii=False))
