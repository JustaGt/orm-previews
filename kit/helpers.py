"""ORM sample site helpers. Import these in a spec file next to build.py."""
import os, sys, html
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from build import build

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'out')
os.makedirs(OUT, exist_ok=True)

def P(x):
    """Unsplash photo id like '1551024601-bec78aea704b' -> spec value."""
    return 'photo-' + x

DAYS = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']

def hour_rows(H, labels):
    """H is [Sun..Sat] of [open_minute, close_minute] or None. labels maps weekday index to text."""
    order = [1, 2, 3, 4, 5, 6, 0]
    return [(d, DAYS[d], labels.get(d, 'Closed')) for d in order]

def nav4(first=('Menu', '#menu')):
    return [first, ('About', '#about'), ('Hours', '#hours'), ('Visit', '#visit')]

MORT_PANEL = '''<form class="panel rise" id="mort" onsubmit="return false">
<h3>What would the payment be?</h3>
<div class="fields">
<label class="field">Down payment<select name="dp"><option value="3.5">3.5%</option><option value="5">5%</option><option value="10">10%</option><option value="20" selected>20%</option><option value="25">25%</option></select></label>
<label class="field">Rate you were quoted<input name="rate" inputmode="decimal" value="6.25" size="5" aria-label="Interest rate in percent"></label>
<label class="field">Term<select name="term"><option value="30" selected>30 years</option><option value="15">15 years</option></select></label>
</div>
<p class="note" id="mort-s" style="margin-top:16px"></p>
</form>'''

MORT_JS = '''
(function(){
  var f=document.getElementById('mort');if(!f)return;
  function calc(){
    var dp=parseFloat(f.dp.value)/100,r=parseFloat(String(f.rate.value).replace(',','.'))/100/12,n=parseInt(f.term.value,10)*12;
    document.querySelectorAll('[data-price]').forEach(function(el){
      var P=parseFloat(el.dataset.price)*(1-dp),m=r>0?P*r/(1-Math.pow(1+r,-n)):P/n;
      el.textContent=isFinite(m)&&m>0?'About $'+Math.round(m).toLocaleString('en-US')+' a month':'';
    });
    var s=document.getElementById('mort-s');
    if(s)s.textContent=Math.round(dp*100)+'% down, '+f.rate.value+'% for '+f.term.value+' years. Principal and interest only. Taxes, insurance and any HOA are extra.';
  }
  f.addEventListener('input',calc);f.addEventListener('change',calc);calc();
})();
'''

def listing(addr, town, price, detail=''):
    p = int(price.replace('$', '').replace(',', ''))
    small = f'{town}' + (f' · {detail}' if detail else '')
    val = f'{price}<small style="display:block;font-weight:400;color:var(--muted);font-size:var(--step-small)" data-price="{p}"></small>'
    return (addr, val, small)

def areas(h2, towns, facts):
    t = ''.join(f'<span class="">{html.escape(x)}</span>' for x in towns)
    rows = ''.join(f'<div class="row"><span class="n">{a}</span><span class="v">{b}</span></div>' for a, b in facts)
    return f'''<section class="sec" id="areas" data-k="s2a">
<h2 class="d rise">{h2}</h2>
<p class="towns d rise">{t}</p>
<div style="margin-top:72px"><div class="rows"><div class="g rise">{rows}</div></div></div>
</section>'''


def broker(slug, s, h1):
    """Real estate broker or agent site with the live mortgage payment estimate."""
    s['h1_html'] = h1
    s['dot_style'] = ' style="background:var(--accent)"'
    s['extra_js'] = MORT_JS
    s['services']['panel'] = MORT_PANEL
    return slug, s

def broker_nav():
    return [('Listings', '#listings'), ('About', '#about'), ('Areas', '#areas'), ('Contact', '#contact')]

def write_all(specs, only=None):
    for slug, s in specs.items():
        if only and slug not in only:
            continue
        out = build(s)
        open(os.path.join(OUT, slug + '.html'), 'w').write(out)
        print(slug, len(out))
