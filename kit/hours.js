(function(){
  var H=[null, [540, 1050], [600, 780], [540, 1050], [540, 960], [540, 960], [600, 780]], L={"en": {"open": "Open now until %", "closed": "Closed now. Opens %", "today": "today", "tomorrow": "tomorrow", "none": "Hours vary"}, "es": {"open": "Abierto ahora hasta las %", "closed": "Cerrado ahora. Abre %", "today": "hoy", "tomorrow": "ma\u00f1ana", "none": "Horario variable"}};
  var lang=function(){return document.documentElement.getAttribute('data-lang')||'en'};
  var DN={en:['Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday'],es:['domingo','lunes','martes','miércoles','jueves','viernes','sábado']};
  function run(){
    var n=ctNow(),el=document.querySelectorAll('[data-status]'),txt,open=false,lg=lang(),T=L[lg]||L.en;
    var today=H[n.d];
    if(today&&n.m>=today[0]&&n.m<today[1]){open=true;txt=T.open.replace('%',fmtT(today[1]))}
    else{
      var k=null,dd=0;
      if(today&&n.m<today[0]){k=today;dd=0}
      else{for(var i=1;i<=7;i++){var x=H[(n.d+i)%7];if(x){k=x;dd=i;break}}}
      if(k){var when=dd===0?T.today:(dd===1?T.tomorrow:DN[lg][(n.d+dd)%7]);txt=T.closed.replace('%',when+' '+fmtT(k[0]))}
      else txt=T.none;
    }
    el.forEach(function(e){e.classList.toggle('open',open);e.querySelector('.st').textContent=txt});
    document.querySelectorAll('[data-day]').forEach(function(r){r.classList.toggle('today',+r.dataset.day===n.d)});
  }
  run();setInterval(run,60000);
  document.querySelectorAll('.langs button').forEach(function(b){b.addEventListener('click',function(){setTimeout(run,0)})});
})();
