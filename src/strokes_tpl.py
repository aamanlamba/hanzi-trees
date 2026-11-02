# Stroke-pad templates (Hanzi Writer). Imported by build.py.
import json, os

HW_DIR = os.path.join(os.path.dirname(__file__), 'hw', 'node_modules', 'hanzi-writer-data')
HW_JS = '_hanzi-writer.min.js'

def strokes_json(text):
    data = {}
    for c in dict.fromkeys(text):
        p = os.path.join(HW_DIR, c + '.json')
        if os.path.exists(p):
            d = json.load(open(p, encoding='utf-8'))
            data[c] = {'strokes': d['strokes'], 'medians': d['medians']}
    # keep it compact; escape "</" so the JSON can't close the script tag
    return json.dumps(data, ensure_ascii=False, separators=(',', ':')).replace('</', '<\\/')

PAD_CSS = """
.pad{display:flex;justify-content:center;gap:10px;flex-wrap:wrap;margin:16px auto 6px}
.pad .cell{position:relative;border:2px solid #d8d3c7;border-radius:12px;background:#fff;touch-action:none}
.nightMode .pad .cell{background:#23262c;border-color:#444}
.pad .cell svg.grid{position:absolute;inset:0;pointer-events:none}
.pad .cell.active{border-color:#2f7de1;box-shadow:0 0 0 3px rgba(47,125,225,.18)}
.pad .cell.done{border-color:#5cb85c}
.padbar{display:flex;justify-content:center;gap:8px;margin:6px 0}
.padbar button{font:inherit;font-size:14px;padding:5px 12px;border-radius:999px;border:1px solid #ccc;background:#f4f2ec;color:inherit;cursor:pointer}
.nightMode .padbar button{background:#2a2d33;border-color:#555}
.padmsg{font-size:15px;color:#888;min-height:20px}
.padmsg.ok{color:#3c9a3c;font-weight:600}
"""

# Shared JS: load the library once from media, then call fn.
_LOADER = """
function hzLoad(fn){
  if (window.HanziWriter) { fn(); return; }
  var s = document.getElementById('hz-lib');
  if (!s) { s = document.createElement('script'); s.id = 'hz-lib'; s.src = '%s'; document.head.appendChild(s); }
  s.addEventListener('load', fn);
}
function hzNight(){ return document.body.classList.contains('nightMode') || document.documentElement.classList.contains('night-mode') || document.body.classList.contains('night_mode'); }
function hzSize(n){ var w = Math.min(document.documentElement.clientWidth || 360, 720) - 72; return Math.max(80, Math.min(170, Math.floor((w - 14*(n-1)) / n))); }
function hzGrid(cell, s){
  var g = document.createElementNS('http://www.w3.org/2000/svg','svg'); g.setAttribute('class','grid'); g.setAttribute('width',s); g.setAttribute('height',s);
  var c = hzNight() ? '#3a3d44' : '#ece7dc';
  g.innerHTML = '<line x1="0" y1="0" x2="'+s+'" y2="'+s+'" stroke="'+c+'" stroke-dasharray="4"/><line x1="'+s+'" y1="0" x2="0" y2="'+s+'" stroke="'+c+'" stroke-dasharray="4"/>'
    + '<line x1="'+s/2+'" y1="0" x2="'+s/2+'" y2="'+s+'" stroke="'+c+'" stroke-dasharray="4"/><line x1="0" y1="'+s/2+'" x2="'+s+'" y2="'+s/2+'" stroke="'+c+'" stroke-dasharray="4"/>';
  cell.appendChild(g);
}
""" % HW_JS

QUIZ_HTML = """
<div class="pad" id="hz-pad"></div>
<div class="padbar"><button type="button" id="hz-hint">Show outline</button><button type="button" id="hz-redo">Start over</button></div>
<div class="padmsg" id="hz-msg">Draw each character, stroke by stroke. A hint appears after 3 misses.</div>
<script type="application/json" id="hz-data">{{Strokes}}</script>
<script>
(function(){
%s
  var pad = document.getElementById('hz-pad'); if (!pad) return;
  var data = {}; try { data = JSON.parse(document.getElementById('hz-data').textContent || '{}'); } catch(e) {}
  var chars = Object.keys(data);
  if (!chars.length) { document.getElementById('hz-msg').textContent = ''; return; }
  var word = '{{text:Word}}'; chars = Array.from(word).filter(function(c){ return data[c]; });
  hzLoad(function(){
    pad.innerHTML = '';
    var night = hzNight(), s = hzSize(chars.length), writers = [], cells = [], cur = 0, outline = false;
    var msg = document.getElementById('hz-msg');
    chars.forEach(function(c){
      var cell = document.createElement('div'); cell.className = 'cell'; cell.style.width = s+'px'; cell.style.height = s+'px';
      hzGrid(cell, s); pad.appendChild(cell); cells.push(cell);
      var holder = document.createElement('div'); cell.appendChild(holder);
      writers.push(HanziWriter.create(holder, c, {
        width: s, height: s, padding: 6, showCharacter: false, showOutline: false,
        strokeColor: night ? '#e8e6e1' : '#1d2433', outlineColor: night ? '#3f434b' : '#e3ded2',
        drawingColor: night ? '#7fb4ff' : '#2f7de1', highlightColor: '#f0a43a',
        drawingWidth: Math.max(14, s/9), showHintAfterMisses: 3, highlightOnComplete: true,
        charDataLoader: function(ch, done){ done(data[ch]); }
      }));
    });
    function start(i){
      cur = i;
      cells.forEach(function(c, k){ c.classList.toggle('active', k === i); });
      if (i >= writers.length) {
        msg.textContent = 'Well done! Now check the answer.'; msg.className = 'padmsg ok'; return;
      }
      msg.className = 'padmsg';
      msg.textContent = chars.length > 1 ? 'Character ' + (i+1) + ' of ' + chars.length : 'Draw the character';
      var misses = 0;
      writers[i].quiz({
        onMistake: function(){ misses++; },
        onComplete: function(r){ cells[i].classList.add('done'); start(i+1); }
      });
    }
    document.getElementById('hz-hint').onclick = function(){
      outline = !outline; writers.forEach(function(w){ outline ? w.showOutline() : w.hideOutline(); });
      this.textContent = outline ? 'Hide outline' : 'Show outline';
    };
    document.getElementById('hz-redo').onclick = function(){
      writers.forEach(function(w){ w.cancelQuiz(); w.hideCharacter(); });
      cells.forEach(function(c){ c.classList.remove('done'); }); start(0);
    };
    start(0);
  });
})();
</script>
""" % _LOADER

ANIM_HTML = """
<div class="pad" id="hz-anim"></div>
<div class="padmsg">Stroke order: tap a character to replay</div>
<script type="application/json" id="hz-adata">{{Strokes}}</script>
<script>
(function(){
%s
  var pad = document.getElementById('hz-anim'); if (!pad) return;
  var data = {}; try { data = JSON.parse(document.getElementById('hz-adata').textContent || '{}'); } catch(e) {}
  var chars = Array.from('{{text:%s}}').filter(function(c){ return data[c]; });
  if (!chars.length) { pad.nextElementSibling.style.display = 'none'; return; }
  hzLoad(function(){
    pad.innerHTML = '';
    var night = hzNight(), s = Math.min(hzSize(chars.length), 130), ws = [];
    chars.forEach(function(c){
      var cell = document.createElement('div'); cell.className = 'cell'; cell.style.width = s+'px'; cell.style.height = s+'px'; cell.style.cursor = 'pointer';
      hzGrid(cell, s); pad.appendChild(cell);
      var holder = document.createElement('div'); cell.appendChild(holder);
      var w = HanziWriter.create(holder, c, {
        width: s, height: s, padding: 6, showOutline: true, strokeAnimationSpeed: 1.4, delayBetweenStrokes: 180,
        strokeColor: night ? '#e8e6e1' : '#1d2433', outlineColor: night ? '#3f434b' : '#e3ded2', radicalColor: '#c0392b',
        charDataLoader: function(ch, done){ done(data[ch]); }
      });
      cell.onclick = function(){ w.animateCharacter(); };
      ws.push(w);
    });
    (function play(i){ if (i < ws.length) ws[i].animateCharacter({ onComplete: function(){ play(i+1); } }); })(0);
  });
})();
</script>
"""

def anim_html(field):
    return ANIM_HTML % (_LOADER, field)
