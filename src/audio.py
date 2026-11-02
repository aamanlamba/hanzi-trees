import sys, os, hashlib, time
sys.path.insert(0,'.')
from concurrent.futures import ThreadPoolExecutor
from gtts import gTTS
from data import *
texts=set()
for r,br in TREES:
  texts.add(r)
  for c,ch,leaves in br:
    texts.add(ch)
    for w in [c]+leaves: texts.add(w[0]); texts.add(w[3])
for w,parts in SPLITS:
  texts.add(w[0]); texts.add(w[3])
  for ch,leaves in parts:
    texts.add(ch)
    for l in leaves: texts.add(l[0]); texts.add(l[3])
for c in CHARS: texts.add(c)
os.makedirs('audio',exist_ok=True)
def fn(t): return 'audio/hz_'+hashlib.md5(t.encode()).hexdigest()[:12]+'.mp3'
def go(t):
  p=fn(t)
  if os.path.exists(p) and os.path.getsize(p)>500: return 0
  for i in range(5):
    try: gTTS(t,lang='zh-CN').save(p); return 0
    except Exception as e: time.sleep(2*(i+1))
  return 1
with ThreadPoolExecutor(6) as ex: fails=sum(ex.map(go,sorted(texts)))
print(len(texts),'texts, fails',fails)
