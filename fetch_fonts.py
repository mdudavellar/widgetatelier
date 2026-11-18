"""Development-time vendor of open fonts and SIL OFL notices. Never runs in editor."""
import urllib.request,re,json,base64,concurrent.futures
from pathlib import Path
families=['DM Sans','Playfair Display','Fraunces','Nunito','Libre Baskerville','Cormorant Garamond','Montserrat','Quicksand','DM Serif Display','Bodoni Moda','Space Grotesk','Syne','Caveat']
italics={'DM Sans','Playfair Display','Fraunces','Nunito','Libre Baskerville','Cormorant Garamond','Montserrat','DM Serif Display','Bodoni Moda'}
root=Path(__file__).parent
(root/'licenses').mkdir(exist_ok=True)
def fetch(url):
    req=urllib.request.Request(url,headers={'User-Agent':'Mozilla/5.0 AppleWebKit/537.36 Chrome/120.0.0.0 Safari/537.36'})
    return urllib.request.urlopen(req,timeout=50).read()
def family(name):
    slug=name.lower().replace(' ','')
    license=fetch('https://raw.githubusercontent.com/google/fonts/main/ofl/'+slug+'/OFL.txt').decode()
    (root/'licenses'/f'{slug}-OFL.txt').write_text(license)
    faces=[]
    for style in (['normal','italic'] if name in italics else ['normal']):
        spec=name.replace(' ','+')+(':ital@1' if style=='italic' else '')
        css=fetch('https://fonts.googleapis.com/css2?family='+spec+'&display=swap').decode()
        # Last subset returned by Google Fonts is Latin, including Portuguese glyphs.
        blocks=re.findall(r'@font-face\s*\{[^}]+\}',css)
        if not blocks: raise ValueError(name+' missing CSS')
        block=blocks[-1]
        url=re.search(r'url\(([^)]+)\)',block).group(1)
        font=fetch(url)
        block=block.replace(url,'data:font/woff2;base64,'+base64.b64encode(font).decode())
        # Some Google responses are variable fonts; this states the shipped face only.
        faces.append(block)
    print(name,'ready',flush=True)
    return name,{'css':'\n'.join(faces),'license':license,'source':'https://fonts.google.com/specimen/'+name.replace(' ','+')}
with concurrent.futures.ThreadPoolExecutor(max_workers=5) as ex:
    assets=dict(ex.map(family,families))
(root/'fonts.json').write_text(json.dumps(assets,ensure_ascii=False))

# Reference additions and their weight/style variants are part of the full catalog.
import runpy
runpy.run_path(str(root/"add_reference_fonts.py"), run_name="__main__")

runpy.run_path(str(root/"add_open_fonts.py"), run_name="__main__")
