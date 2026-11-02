import sys, hashlib, html, re
sys.path.insert(0, '.')
import genanki, jieba
from pypinyin import pinyin, Style
from data import TREES, SPLITS, CHARS, READINGS
from strokes_tpl import strokes_json, PAD_CSS, QUIZ_HTML, anim_html, HW_JS

jieba.setLogLevel(60)

def afile(t): return 'hz_' + hashlib.md5(t.encode()).hexdigest()[:12] + '.mp3'
def snd(t): return f'[sound:{afile(t)}]'
E = html.escape

# ---------- vocabulary index ----------
VOCAB = {}
def reg(w):
    VOCAB.setdefault(w[0], w)
for r, br in TREES:
    for c, ch, leaves in br:
        for w in [c] + leaves: reg(w)
for w, parts in SPLITS:
    reg(w)
    for ch, leaves in parts:
        for l in leaves: reg(l)
for w in VOCAB: jieba.add_word(w, freq=200000)

PUNCT = set('，。？！、；：“”（）')
NEUTRAL = {'个': 'ge'}
FIX = {  # neutral tones, proper nouns and readings the converter gets wrong
 'rènshí':'rènshi','shūfú':'shūfu','gàosù':'gàosu','xiāoxī':'xiāoxi','zhīshí':'zhīshi','xiūxī':'xiūxi',
 'ēnài':"ēn'ài",'xínglǐ':'xíngli','bàbà':'bàba','māmā':'māma','wǎnshàng':'wǎnshang','zǎoshàng':'zǎoshang',
 'yéyé':'yéye','dìdi':'dìdi','xīān':"Xī'ān",'shànghǎi':'Shànghǎi','yúnnán':'Yúnnán','chéngdū':'Chéngdū',
 'kūnmíng':'Kūnmíng','sìchuān':'Sìchuān','zhōngqiūjié':'Zhōngqiūjié','wànshèngjié':'Wànshèngjié',
 'làxià':'luòxià','hěnzhǎng':'hěn cháng','wǒliàng':'wǒ liáng','shuí':'shéi','chángchéng':'Chángchéng',
 'rénmínbì':'Rénmínbì','nuǎnhuo':'nuǎnhuo','shēnfènzhèng':'shēnfènzhèng','dǎbùkāi':'dǎ bu kāi','hěn de rénxīn':'hěn dé rénxīn','yīlùshàng':'yílù shang',
 'búdàochángchéngfēihǎohàn':'bú dào Chángchéng fēi hǎohàn','zhídeyíkàn':'zhíde yí kàn','xièxiè':'xièxie',
 'bāolǐ':'bāo li','dàyòuyuán':'dà yòu yuán','sìjìrúchūn':'sìjì rú chūn',
}
TONE_MARKS = {'ā':1,'á':2,'ǎ':3,'à':4,'ē':1,'é':2,'ě':3,'è':4,'ī':1,'í':2,'ǐ':3,'ì':4,'ō':1,'ó':2,'ǒ':3,'ò':4,
              'ū':1,'ú':2,'ǔ':3,'ù':4,'ǖ':1,'ǘ':2,'ǚ':3,'ǜ':4}
def tone(syl):
    for ch in syl:
        if ch in TONE_MARKS: return TONE_MARKS[ch]
    return 5

def sentence_pinyin(s):
    toks = [t for t in jieba.cut(s)]
    # per-character base readings (phrase-aware), used for sandhi look-ahead
    base = [x[0] for x in pinyin(s, style=Style.TONE)]
    chars = list(s)
    out, pos = [], 0
    for ti, tok in enumerate(toks):
        n = len(tok)
        if tok in PUNCT or not tok.strip():
            if out: out[-1] += tok
            else: out.append(tok)
            pos += n; continue
        if tok in VOCAB:
            out.append(VOCAB[tok][1].replace(' ', '')); pos += n; continue
        syls = [x[0] for x in pinyin(tok, style=Style.TONE)]
        for k, c in enumerate(tok):
            gi = pos + k
            nxt = chars[gi + 1] if gi + 1 < len(chars) else ''
            nxt_tone = tone(base[gi + 1]) if gi + 1 < len(base) and nxt not in PUNCT else 0
            prev = chars[gi - 1] if gi > 0 else ''
            if c == '一':
                if prev in '第十' or nxt in '月号' or nxt_tone == 0 or nxt in PUNCT: syls[k] = 'yī'
                elif nxt == '个' or nxt_tone == 4: syls[k] = 'yí'
                else: syls[k] = 'yì'
            elif c == '不':
                syls[k] = 'bú' if (nxt == '个' or nxt_tone == 4) else 'bù'
            elif c in NEUTRAL and n > 1 or (c == '个' and n == 1):
                syls[k] = 'ge'
        if tok in ('得', '地'): syls = ['de']
        if len(tok) > 1 and tok.endswith('儿') and tok not in ('女儿', '婴儿', '儿子', '儿童'):
            syls = syls[:-2] + [syls[-2] + 'r']
        word = ''.join(syls)
        out.append(FIX.get(word, word))
        pos += n
    res = ' '.join(out)
    for a, b in FIX.items():
        res = re.sub(r'(?<![a-zāáǎàēéěèīíǐìōóǒòūúǔùǖǘǚǜü])' + re.escape(a) + r'(?![a-zāáǎàēéěèīíǐìōóǒòūúǔùǖǘǚǜü])', b, res)
    return res

def gloss(c):
    return CHARS[c][1].split(';')[0].split(',')[0].split(' / ')[0].strip()

def breakdown(word):
    return ' + '.join(f'{c} <span class="g">({E(gloss(c))})</span>' for c in word)

# ---------- mini tree rendering ----------
PALETTE = ['blue', 'green', 'purple']

def node(hz, py, en, cls, cur, small=False):
    on = ' cur' if hz == cur else ''
    sz = ' sm' if small else ''
    return (f'<div class="n {cls}{on}{sz}"><div class="h">{E(hz)}</div>'
            f'<div class="p">{E(py)}</div><div class="e">{E(en)}</div></div>')

def char_py(c): return CHARS[c][0].split('/')[0]

def root_tree_html(root, branches, cur):
    cols = []
    for i, (comp, ch, leaves) in enumerate(branches):
        col = PALETTE[i]
        leaf_html = ''.join(node(l[0], l[1], l[2], col, cur, True) for l in leaves)
        cols.append(f'<div class="col">{node(comp[0], comp[1], comp[2], col, cur)}'
                    f'<div class="ln {col}"></div>{node(ch, char_py(ch), gloss(ch), col, cur)}'
                    f'<div class="ln {col}"></div><div class="leaves">{leaf_html}</div></div>')
    return (f'<div class="tree"><div class="top">{node(root, char_py(root), gloss(root), "orange", cur)}</div>'
            f'<div class="ln orange"></div><div class="cols">{"".join(cols)}</div></div>')

def split_tree_html(word, parts, cur):
    cols = []
    for i, (ch, leaves) in enumerate(parts):
        col = ['blue', 'orange'][i]
        leaf_html = ''.join(node(l[0], l[1], l[2], col, cur, True) for l in leaves)
        cols.append(f'<div class="col">{node(ch, char_py(ch), gloss(ch), col, cur)}'
                    f'<div class="ln {col}"></div><div class="leaves">{leaf_html}</div></div>')
    return (f'<div class="tree"><div class="top">{node(word[0], word[1], word[2], "pink", cur)}</div>'
            f'<div class="ln pink"></div><div class="cols two">{"".join(cols)}</div></div>')

# ---------- models ----------
CSS = """
.card{font-family:-apple-system,"Segoe UI","PingFang SC","Noto Sans CJK SC","Microsoft YaHei",sans-serif;
 background:#fbfaf7;color:#1d2433;text-align:center;font-size:18px;padding:12px}
.nightMode.card,.night_mode .card{background:#1b1d22;color:#e8e6e1}
.big{font-size:84px;line-height:1.15;font-weight:500}
.mid{font-size:56px;font-weight:500}
.py{font-size:26px;color:#c0392b;margin-top:4px}
.nightMode .py{color:#ff8a7a}
.mean{font-size:22px;margin:6px 0 2px}
.bd{font-size:18px;margin:8px auto;padding-top:8px;border-top:1px solid #ddd;max-width:520px}
.g{color:#777;font-size:15px}
.read{font-size:15px;color:#555;background:#f1eee6;border-radius:8px;padding:6px 10px;display:inline-block;margin:6px}
.nightMode .read{background:#2a2d33;color:#cfcac0}
.ex{margin:14px auto 4px;max-width:560px;text-align:left;border-left:3px solid #e2a03f;padding:4px 12px 4px 16px}
.ex .zh{font-size:22px}.ex .pz{color:#c0392b;font-size:15px}.ex .en{color:#666;font-size:15px}
.nightMode .ex .en{color:#aaa}
.lvl{font-size:12px;letter-spacing:.08em;text-transform:uppercase;color:#999}
.prompt{font-size:26px;margin-top:20px}
.cloze{font-weight:600;color:#2f7de1}
.nightMode .cloze{color:#7fb4ff}
.hint{color:#999;font-size:15px}
/* tree */
.tree{margin:18px auto 0;max-width:760px;font-size:12px}
.top{display:flex;justify-content:center}
.cols{display:flex;gap:6px;justify-content:center}
.col{flex:1;display:flex;flex-direction:column;align-items:center;min-width:0}
.leaves{display:flex;gap:3px;width:100%}
.leaves .n{flex:1}
.n{border:2px solid;border-radius:10px;padding:3px 4px;min-width:64px;background:#fff}
.nightMode .n{background:#23262c}
.n .h{font-size:22px;line-height:1.2}.n .p{font-size:11px;font-weight:600}.n .e{font-size:10px;color:#666;line-height:1.15}
.n.sm .h{font-size:17px}
.n.cur{box-shadow:0 0 0 3px #e74c3c;transform:scale(1.04)}
.ln{width:2px;height:10px;margin:0 auto}
.orange{border-color:#f0a43a}.n.orange{background:#fff5e2}.ln.orange{background:#f0a43a}
.blue{border-color:#3b8de8}.n.blue{background:#e9f3ff}.ln.blue{background:#3b8de8}
.green{border-color:#5cb85c}.n.green{background:#ecf8e8}.ln.green{background:#5cb85c}
.purple{border-color:#9b59d0}.n.purple{background:#f3eafc}.ln.purple{background:#9b59d0}
.pink{border-color:#e8679b}.n.pink{background:#fdeaf2}.ln.pink{background:#e8679b}
.nightMode .n.orange,.nightMode .n.blue,.nightMode .n.green,.nightMode .n.purple,.nightMode .n.pink{background:#23262c}
@media (max-width:520px){.n .e{display:none}.n .h{font-size:17px}.n.sm .h{font-size:14px}.n{min-width:0}}
""" + PAD_CSS

CHAR_MODEL = genanki.Model(
    1607392611, 'Hanzi Tree · Character',
    fields=[{'name': n} for n in ['Hanzi', 'Pinyin', 'Meaning', 'Readings', 'Builds', 'Audio', 'Tree', 'Role', 'Strokes']],
    templates=[
        {'name': 'Character → Sound & Meaning',
         'qfmt': '<div class="lvl">{{Role}}</div><div class="big">{{Hanzi}}</div>',
         'afmt': '{{FrontSide}}<div class="py">{{Pinyin}}</div><div class="mean">{{Meaning}}</div>{{Audio}}'
                 '{{#Readings}}<div class="read">{{Readings}}</div>{{/Readings}}'
                 '<div class="bd">Builds: {{Builds}}</div>' + anim_html('Hanzi') + '{{Tree}}'},
    ], css=CSS)

WORD_MODEL = genanki.Model(
    1607392612, 'Hanzi Tree · Word',
    fields=[{'name': n} for n in ['Word', 'Pinyin', 'Meaning', 'Breakdown', 'Audio', 'Sentence',
                                   'SentencePinyin', 'SentenceEnglish', 'SentenceAudio', 'Tree', 'Role',
                                   'Hint', 'Strokes']],
    templates=[
        {'name': 'Read: Word → Sound & Meaning',
         'qfmt': '<div class="lvl">{{Role}}</div><div class="mid">{{Word}}</div>',
         'afmt': '{{FrontSide}}<div class="py">{{Pinyin}}</div><div class="mean">{{Meaning}}</div>{{Audio}}'
                 '<div class="bd">{{Breakdown}}</div>'
                 '<div class="ex"><div class="zh">{{Sentence}}</div><div class="pz">{{SentencePinyin}}</div>'
                 '<div class="en">{{SentenceEnglish}}</div>{{SentenceAudio}}</div>{{Tree}}'},
        {'name': 'Recall: Meaning → Word',
         'qfmt': '<div class="lvl">{{Role}} · write it</div><div class="prompt">{{Meaning}}</div>'
                 '<div class="hint">{{Hint}}</div>' + QUIZ_HTML,
         'afmt': '<div class="lvl">{{Role}} · write it</div><div class="prompt">{{Meaning}}</div><hr>'
                 '<div class="mid">{{Word}}</div><div class="py">{{Pinyin}}</div>{{Audio}}'
                 '<div class="bd">{{Breakdown}}</div>' + anim_html('Word') + '{{Tree}}'},
        {'name': 'Listen: Sound → Word',
         'qfmt': '<div class="lvl">{{Role}} · listen</div><div class="prompt">🔊</div>{{Audio}}',
         'afmt': '{{FrontSide}}<hr><div class="mid">{{Word}}</div><div class="py">{{Pinyin}}</div>'
                 '<div class="mean">{{Meaning}}</div>'},
    ], css=CSS)

CLOZE_MODEL = genanki.Model(
    1607392613, 'Hanzi Tree · Cloze', model_type=genanki.Model.CLOZE,
    fields=[{'name': n} for n in ['Text', 'Pinyin', 'English', 'Audio', 'Word', 'Tree']],
    templates=[{'name': 'Cloze',
                'qfmt': '<div class="lvl">fill the gap</div><div class="prompt">{{cloze:Text}}</div>'
                        '<div class="hint">{{English}}</div>',
                'afmt': '<div class="lvl">fill the gap</div><div class="prompt">{{cloze:Text}}</div>'
                        '<div class="py" style="font-size:18px">{{Pinyin}}</div><div class="hint">{{English}}</div>'
                        '{{Audio}}<div class="bd">{{Word}}</div>{{Tree}}'}],
    css=CSS)

# ---------- assemble ----------
ROOT = 'Chinese · Hanzi Trees'

DESC_STYLE = '<div style="text-align:left;max-width:640px;margin:0 auto;line-height:1.5">'
MAIN_DESC = DESC_STYLE + """
<h3 style="margin:0 0 6px">Chinese · Hanzi Trees</h3>
<p>Learn Chinese through <b>word families</b>. One character opens a set of words, and each word brings in the next character.</p>
<p><b>Root trees (01–31):</b> root character → 3 compounds → the new character each compound introduces → 3 everyday words built on it.<br>
<span style="color:#888">火 fire → 火车 train → 车 vehicle → 汽车 · 车站 · 车票</span></p>
<p><b>Splits (01–08):</b> a common word splits into its two characters, and each character branches into 3 words.<br>
<span style="color:#888">你好 → 你 (你们 · 你的 · 你家) + 好 (好吃 · 好看 · 好朋友)</span></p>
<p><b>Card types:</b> Character · Read · Recall (write it on a stroke pad) · Listen · Cloze. Character and Recall answers animate the stroke order. Every word has audio, an example sentence with pinyin and English, and a "+" breakdown. Every card shows its tree, with the current item outlined in red.</p>
<p><b>Tip:</b> study one tree at a time by clicking into its subdeck. To lighten the load, suspend <code>card:Listen*</code> or <code>card:Recall*</code> in the Browser.</p>
<p style="color:#888;font-size:90%">136 characters · 423 words · 1,828 cards · Simplified · HSK 1–3 (some HSK 4)</p>
</div>"""

def root_desc(root, branches):
    rows = ''.join(
        f'<li><b>{comp[0]}</b> {comp[1]} <span style="color:#888">({E(comp[2])})</span> → '
        f'<b>{ch}</b> {char_py(ch)} <span style="color:#888">({E(gloss(ch))})</span> → '
        + ' · '.join(l[0] for l in leaves) + '</li>'
        for comp, ch, leaves in branches)
    return (DESC_STYLE + f'<p><b style="font-size:150%">{root}</b> {char_py(root)} — {E(CHARS[root][1])}</p>'
            f'<ul style="padding-left:18px">{rows}</ul>'
            '<p style="color:#888;font-size:90%">Order: root → compound → linked character → its words. '
            'You meet each new character just before the words that use it.</p></div>')

def split_desc(w, parts):
    rows = ''.join(
        f'<li><b>{ch}</b> {char_py(ch)} <span style="color:#888">({E(gloss(ch))})</span> → '
        + ' · '.join(l[0] for l in leaves) + '</li>' for ch, leaves in parts)
    return (DESC_STYLE + f'<p><b style="font-size:150%">{w[0]}</b> {w[1]} — {E(w[2])}</p>'
            f'<p>{breakdown(w[0])}</p><ul style="padding-left:18px">{rows}</ul></div>')

decks, media = [], set()
main = genanki.Deck(2059399999, ROOT, description=MAIN_DESC)
splits_parent = genanki.Deck(2059409999, f'{ROOT}::Splits', description=DESC_STYLE + '<p><b>Splits</b>: common two-character words broken into their characters, each branching into three more words.</p></div>')
decks += [main, splits_parent]
seen_chars, seen_words = set(), set()
due = [0]

def guid(*a): return genanki.guid_for('hanzitree', *a)

def add(deck, model, fields, key, tags):
    due[0] += 1
    deck.add_note(genanki.Note(model=model, fields=fields, guid=guid(key), tags=tags, due=due[0]))

def builds_for(c):
    return ' · '.join(f'{w}' for w in VOCAB if c in w and len(w) > 1)

def add_char(deck, c, role, tree, tags):
    if c in seen_chars: return
    seen_chars.add(c)
    media.add(afile(c))
    py, en = CHARS[c]
    add(deck, CHAR_MODEL, [c, py, E(en), E(READINGS.get(c, '')), builds_for(c), snd(c), tree, role, strokes_json(c)],
        'char:' + c, tags + ['character'])

def hint_for(word, py):
    return f'{E(py)} · ' + ' + '.join(E(gloss(c)) for c in word)

def add_word(deck, w, role, tree, tags):
    word, py, en, sent, sen_en = w
    if word in seen_words: return
    seen_words.add(word)
    media.update([afile(word), afile(sent)])
    spy = sentence_pinyin(sent)
    add(deck, WORD_MODEL, [word, py, E(en), breakdown(word), snd(word), sent, spy, E(sen_en), snd(sent), tree, role,
                           hint_for(word, py), strokes_json(word)],
        'word:' + word, tags + ['word'])
    assert word in sent, (word, sent)
    cloze = sent.replace(word, '{{c1::' + word + '::' + E(en) + '}}', 1)
    add(deck, CLOZE_MODEL, [cloze, spy, E(sen_en), snd(sent), f'{word} · {py} · {E(en)}', tree],
        'cloze:' + word, tags + ['cloze'])

for i, (root, branches) in enumerate(TREES, 1):
    d = genanki.Deck(2059400000 + i, f'{ROOT}::{i:02d} {root} {char_py(root)} — {gloss(root)}', description=root_desc(root, branches))
    tag = [f'tree_{root}']
    add_char(d, root, 'root character', root_tree_html(root, branches, root), tag)
    for comp, ch, leaves in branches:
        add_word(d, comp, 'compound', root_tree_html(root, branches, comp[0]), tag)
        add_char(d, ch, 'linked character', root_tree_html(root, branches, ch), tag)
        for l in leaves:
            add_word(d, l, 'built word', root_tree_html(root, branches, l[0]), tag)
    decks.append(d)

for j, (w, parts) in enumerate(SPLITS, 1):
    d = genanki.Deck(2059410000 + j, f'{ROOT}::Splits::{j:02d} {w[0]} {w[1]} — {w[2]}', description=split_desc(w, parts))
    tag = [f'split_{w[0]}']
    add_word(d, w, 'word split', split_tree_html(w, parts, w[0]), tag)
    for ch, leaves in parts:
        add_char(d, ch, 'component character', split_tree_html(w, parts, ch), tag)
        for l in leaves:
            add_word(d, l, 'built word', split_tree_html(w, parts, l[0]), tag)
    decks.append(d)

pkg = genanki.Package(decks)
pkg.media_files = [f'audio/{m}' for m in sorted(media)] + [HW_JS]
pkg.write_to_file('Chinese_Hanzi_Trees.apkg')
n = sum(len(d.notes) for d in decks)
print('decks', len(decks), 'notes', n, 'chars', len(seen_chars), 'words', len(seen_words), 'audio', len(media))

# dump a sample for checking
import json
json.dump({w: sentence_pinyin(VOCAB[w][3]) for w in list(VOCAB)}, open('pinyin_check.json', 'w'), ensure_ascii=False, indent=0)
