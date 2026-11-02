import sys, re, io, contextlib, os
sys.path.insert(0,'.')
with contextlib.redirect_stdout(io.StringIO()):
    import build
from playwright.sync_api import sync_playwright
PLAY='<svg width="34" height="34" viewBox="0 0 34 34" style="margin:6px;vertical-align:middle"><circle cx="17" cy="17" r="17" fill="#2f7de1"/><path d="M13 10 L25 17 L13 24 Z" fill="#fff"/></svg>'
def fill(model, note, tmpl, side):
    f=dict(zip([x['name'] for x in model.fields], note.fields))
    q=model.templates[tmpl]['qfmt']; a=model.templates[tmpl]['afmt']
    t=q if side=='q' else a.replace('{{FrontSide}}',q)
    t=re.sub(r'\{\{#(\w+)\}\}(.*?)\{\{/\1\}\}',lambda m:m.group(2) if f.get(m.group(1)) else '',t,flags=re.S)
    def cz(m):
        txt=f['Text']
        if side=='q': return re.sub(r'\{\{c1::(.*?)::(.*?)\}\}',r'<span class="cloze">[…]</span>',txt)
        return re.sub(r'\{\{c1::(.*?)::(.*?)\}\}',r'<span class="cloze">\1</span>',txt)
    t=re.sub(r'\{\{cloze:Text\}\}',cz,t)
    t=re.sub(r'\{\{(\w+)\}\}',lambda m:f.get(m.group(1),''),t)
    return re.sub(r'\[sound:[^\]]+\]',PLAY,t)
def find(model,key):
    for d in build.decks:
        for n in d.notes:
            if n.model is model and n.fields[0]==key: return n
    for d in build.decks:
        for n in d.notes:
            if n.model is model and key in n.fields[0]: return n
shots=[
 ('01_root_character', build.CHAR_MODEL,'火',0,'a'),
 ('02_compound_word', build.WORD_MODEL,'火山',0,'a'),
 ('03_built_word', build.WORD_MODEL,'星期',0,'a'),
 ('04_split_tree', build.WORD_MODEL,'老板',0,'a'),
 ('05_cloze_front', build.CLOZE_MODEL,'车站',0,'q'),
 ('06_cloze_back', build.CLOZE_MODEL,'车站',0,'a'),
 ('07_recall_front', build.WORD_MODEL,'银行',1,'q'),
 ('08_polyphone', build.CHAR_MODEL,'行',0,'a'),
]
with sync_playwright() as p:
    b=p.chromium.launch()
    for name,model,key,tmpl,side in shots:
        n=find(model,key)
        if model is build.CLOZE_MODEL:
            n=[x for d in build.decks for x in d.notes if x.model is model and '{{c1::'+key+'::' in x.fields[0]][0]
        h=fill(model,n,tmpl,side)
        pg=b.new_page(viewport={'width':860,'height':600},device_scale_factor=2)
        pg.set_content(f'<html><head><meta charset=utf-8><style>{build.CSS} body{{margin:0;padding:24px 20px}}</style></head><body class="card">{h}</body></html>')
        pg.screenshot(path=f'shots/{name}.png',full_page=True); pg.close()
    b.close()
print(os.listdir('shots'))
