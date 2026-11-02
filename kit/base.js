
document.documentElement.classList.add('js');
(function(){
  var io=new IntersectionObserver(function(es){es.forEach(function(e){if(e.isIntersecting){e.target.classList.add('in');io.unobserve(e.target)}})},{rootMargin:'0px 0px -8% 0px'});
  document.querySelectorAll('.rise').forEach(function(el){io.observe(el)});
  document.querySelectorAll('.stage').forEach(function(st){
    var imgs=st.querySelectorAll('.frame img');if(imgs.length<2||window.matchMedia('(max-width:900px)').matches)return;
    var o=new IntersectionObserver(function(es){es.forEach(function(e){if(e.isIntersecting){var k=e.target.getAttribute('data-k');imgs.forEach(function(im){im.classList.toggle('on',im.getAttribute('data-k')===k)})}})},{rootMargin:'-45% 0px -45% 0px'});
    st.querySelectorAll('[data-k]').forEach(function(s){if(s.tagName!=='IMG')o.observe(s)});
  });
  var dock=document.querySelector('.dock'),hero=document.querySelector('.hero');
  if(dock&&hero){new IntersectionObserver(function(es){dock.classList.toggle('show',!es[0].isIntersecting)}).observe(hero)}
  document.querySelectorAll('.langs button').forEach(function(b){b.addEventListener('click',function(){
    document.documentElement.setAttribute('data-lang',b.dataset.l);
    document.documentElement.lang=b.dataset.l;
    document.querySelectorAll('.langs button').forEach(function(x){x.setAttribute('aria-pressed',String(x.dataset.l===b.dataset.l))});
  })});
})();
function ctNow(){
  var f=new Intl.DateTimeFormat('en-US',{timeZone:'America/Chicago',weekday:'short',hour:'numeric',minute:'numeric',hour12:false});
  var p={};f.formatToParts(new Date()).forEach(function(x){p[x.type]=x.value});
  var days=['Sun','Mon','Tue','Wed','Thu','Fri','Sat'];
  return {d:days.indexOf(p.weekday),m:(parseInt(p.hour,10)%24)*60+parseInt(p.minute,10)};
}
function fmtT(m){var h=Math.floor(m/60),mi=m%60,ap=h>=12?'PM':'AM';h=h%12||12;return h+(mi?':'+String(mi).padStart(2,'0'):'')+' '+ap}

