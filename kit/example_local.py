"""Example local business specs. Copy one, replace every value with verified facts, run: python3 example_local.py"""
import sys
from helpers import P, nav4, hour_rows, write_all

specs = {}

# ---------- Susie's Deli, Abilene ----------
SD_MAP = 'https://www.google.com/maps/search/?api=1&query=102+N+Buckeye+Ave+Abilene+KS+67410'
SD_FB = 'https://www.facebook.com/profile.php?id=61560385928358'
soup_panel = """<form class="panel rise" id="soup" onsubmit="return false">
<h3>Soup for the whole crew</h3>
<div class="fields">
<label class="field">Bowls, $8.99<select name="bowl">""" + ''.join(f'<option value="{i}"{" selected" if i == 2 else ""}>{i}</option>' for i in range(0, 21)) + """</select></label>
<label class="field">Cups, $4.99<select name="cup">""" + ''.join(f'<option value="{i}"{" selected" if i == 1 else ""}>{i}</option>' for i in range(0, 21)) + """</select></label>
</div>
<div class="out"><span class="big d" id="soup-t">$0</span><p id="soup-s">Before tax. Call ahead and it will be ready.</p></div>
</form>"""
soup_js = """
(function(){
  var f=document.getElementById('soup');if(!f)return;
  function calc(){
    var b=parseInt(f.bowl.value,10)||0,c=parseInt(f.cup.value,10)||0,t=b*8.99+c*4.99;
    document.getElementById('soup-t').textContent='$'+t.toFixed(2);
    document.getElementById('soup-s').textContent=(b+c===0?'Pick a few bowls or cups.':b+(b===1?' bowl':' bowls')+' and '+c+(c===1?' cup':' cups')+', before tax. Call ahead and it will be ready.');
  }
  f.addEventListener('change',calc);calc();
})();
"""
sd_visit = """<section class="sec" id="hours" data-k="s2a">
<h2 class="d rise">Stop in</h2>
<p class="sub rise">Dine in, grab takeout or order ahead for pickup.</p>
<div class="rows"><div class="g rise">
<div class="row"><span class="n">Dine in</span><span class="v soft">Big tables, cozy rooms</span></div>
<div class="row"><span class="n">Takeout</span><span class="v soft">Call ahead</span></div>
<div class="row"><span class="n">In store pickup</span><span class="v soft">Order online</span></div>
<div class="row"><span class="n">Art on the walls<small>Landscape photographs are $65 each. Pat Little’s Trails End art is priced on each piece.</small></span><span class="v soft">All for sale</span></div>
</div></div>
<p class="note rise">The soup of the day and hours go up on Facebook first.</p>
</section>"""
specs['susies-deli-abilene'] = dict(
    name="Susie's Deli", short="Susie's Deli",
    title="Susie's Deli | Breakfast, sandwiches and soup in Abilene, KS",
    desc="Everything Bagel BLTs, chicken salad hoagies, biscuits and gravy, soup of the day and creamery malts on N Buckeye in Abilene, Kansas.",
    theme=dict(bg='#fbf6ec', surface='#f0e6d3', ink='#23201a', muted='#6d6556', accent='#3d6b4f', accent_ink='#fbf6ec', band='#3d6b4f', band_ink='#fbf6ec', ok='#2f9e5b'),
    font='sentient',
    photos=dict(h=P('1528735602780-2552fd46c7af'), menu=P('1553909489-cd47e0907980'), about=P('1525351484163-7529414344d8'),
                strip=[P('1567620905732-2d1ec7ab7445'), P('1546793665-c74683f339c1'), P('1509365465985-25d11c17e812')],
                s2a=P('1533089860892-a7c6f0a88666'), visit=P('1565958011703-44f9829ba187'), foot=P('1504754524776-8f4f37790ca0')),
    nav=[('Menu', '#menu'), ('About', '#about'), ('Stop in', '#hours'), ('Visit', '#visit')],
    primary=('Call (785) 571 0564', 'tel:+17855710564'), secondary=('Get directions', SD_MAP),
    status_default='Breakfast, lunch and soup of the day',
    lead='Good food made by someone who loves to feed people.',
    facts=['<b>100%</b> recommend on Facebook', 'Soup of the day', 'Malts from the creamery inside'],
    services=dict(id='menu', h2='On the menu', sub='Breakfast, sandwiches, a soup of the day and a creamery right inside.',
                  panel=soup_panel,
                  groups=[dict(h3='Soup of the day', rows=[('Bowl', '$8.99', 'Like the vegetable beef'), ('Cup', '$4.99')]),
                          dict(h3='Breakfast', rows=[('Biscuits and gravy', 'With hash browns', '', True), ('Sausage bagel', 'Mornings', '', True), ('Breakfast bowl', 'With bacon', '', True), ('Cinnamon rolls', 'While they last', '', True)]),
                          dict(h3='Sandwiches', rows=[('Everything Bagel BLT', 'The favorite', '', True), ('Chicken salad hoagie', 'Lunch', '', True), ('Italian', 'Lunch', '', True), ('Turkey', 'Your way', '', True), ('Chicken wrap', 'Lunch', '', True)]),
                          dict(h3='On the side', rows=[('Taco salad', 'Ask for Dorothy Lynch', '', True), ('Macaroni salad', 'Floy’s recipe', '', True), ('Fresh fruit', 'Side', '', True)]),
                          dict(h3='Creamery', rows=[('Malts and ice cream', 'Chocolate is a must', '', True)])],
                  note='Feeding a crowd? Call (785) 571 0564.'),
    about=dict(h2='Tucked inside an old home', ps=["Susie's Deli opened in June 2024 on North Buckeye in Abilene, in a cozy old home with big tables that fit the whole family.", 'Regulars come back for the Everything Bagel BLT, the chicken salad hoagies, the biscuits and gravy and whatever soup is on that day.', 'Save room: there is a creamery right inside, and every piece of art on the walls is for sale.']),
    band=dict(fig='100%', bx="of Facebook reviewers recommend Susie's.", small='Good food made by someone who loves to feed people.', word=True),
    areas_html=sd_visit,
    visit=dict(rows=[('Deli', '102 N Buckeye Avenue', SD_MAP), ('Town', 'Abilene, Kansas 67410', None), ('Phone', '(785) 571 0564', 'tel:+17855710564')],
               go=('Call ahead', 'tel:+17855710564')),
    footer=dict(nav=[('Menu', '#menu'), ('About', '#about'), ('Stop in', '#hours'), ('Visit', '#visit')], contact='102 N Buckeye Avenue<br>Abilene, KS 67410<a href="tel:+17855710564">(785) 571 0564</a>',
                follow=[('Facebook', SD_FB)],
                legal="Every price and detail comes from Susie's Facebook page, Visit Abilene and public reviews."),
    dock=[('Call', 'tel:+17855710564'), ('Directions', SD_MAP)],
    extra_js=soup_js,
)

# ---------- 56 Donuts, Council Grove ----------
fd_H = [None, None, [300, 660], [300, 660], [300, 660], [300, 660], [300, 660]]
FD_MAP = 'https://www.google.com/maps/search/?api=1&query=617+E+Main+St+Council+Grove+KS+66846'
specs['56-donuts-council-grove'] = dict(
    name='56 Donuts', short='56 Donuts',
    title='56 Donuts | Donuts and kolaches in Council Grove, KS',
    desc='Donuts, kolaches, cinnamon rolls, apple fritters and biscuits and gravy on E Main St in Council Grove, Kansas, from 5 AM until they sell out.',
    theme=dict(bg='#f4f6fb', surface='#e3e8f3', ink='#14213d', muted='#58627a', accent='#1d3a8a', accent_ink='#f4f6fb', band='#1d3a8a', band_ink='#f4f6fb', ok='#2f9e5b'),
    font='cabinet',
    photos=dict(h=P('1551024601-bec78aea704b'), menu=P('1533910534207-90f31029a78e'), about=P('1509365465985-25d11c17e812'),
                strip=[P('1533910534207-90f31029a78e'), P('1509042239860-f550ce710b93'), P('1555507036-ab1f4038808a')],
                s2a=P('1495474472287-4d71bcdd2085'), visit=P('1551024601-bec78aea704b'), foot=P('1509365465985-25d11c17e812')),
    nav=nav4(),
    primary=('Call (620) 767 5551', 'tel:+16207675551'), secondary=('Get directions', FD_MAP),
    status_default='Tue to Sat from 5 AM',
    lead='Donuts, kolaches, cinnamon rolls and biscuits and gravy on East Main in Council Grove, from 5 AM until they sell out.',
    facts=['<b>3 years</b> on East Main', '<b>100%</b> recommend on Facebook', 'Open until sold out'],
    services=dict(id='menu', h2='In the case', sub='Get there early. When it is gone, it is gone.',
                  groups=[dict(h3='Donuts', rows=[('Glazed donuts', 'Fresh daily', '', True), ('Cake donuts', 'Fresh daily', '', True), ('Donut sticks', 'Fresh daily', '', True), ('Bag of donut holes', 'Fresh daily', '', True)]),
                          dict(h3='The big bakers', rows=[('Cinnamon rolls', 'Fresh daily', '', True), ('Apple fritters', 'Fresh daily', '', True), ('Kolaches', 'Fresh daily', '', True)]),
                          dict(h3='Biscuits and gravy', rows=[('1 biscuit with gravy', '$2.50'), ('2 biscuits with gravy', '$5.00')]),
                          dict(h3='To drink', rows=[('Coffee', 'Hot', '', True), ('Fountain drinks', 'Cold', '', True)])],
                  note='Biscuits and gravy runs on select days while supplies last. Facebook says when.'),
    about=dict(h2='Three years on East Main', ps=['56 Donuts opened its doors on East Main Street in Council Grove on October 3, 2023, from 5 AM until the case is empty.', 'The case fills with glazed, cake donuts and donut sticks, plus cinnamon rolls, apple fritters, kolaches and bags of donut holes.', 'This October the shop turned three and threw a $3 for 3 Years special to say thanks to everyone who walks through the door.']),
    band=dict(fig='3', bx='years of donuts on East Main Street.', small='100% of Facebook reviewers recommend 56 Donuts.'),
    hours=dict(H=fd_H, rows=hour_rows(fd_H, {2: '5 AM to 11 AM', 3: '5 AM to 11 AM', 4: '5 AM to 11 AM', 5: '5 AM to 11 AM', 6: '5 AM to 11 AM'}), note='Or until sold out. Facebook posts the minute the case is empty.'),
    visit=dict(rows=[('Shop', '617 E Main Street', FD_MAP), ('Town', 'Council Grove, Kansas 66846', None), ('Phone', '(620) 767 5551', 'tel:+16207675551')],
               go=('Get directions', FD_MAP)),
    footer=dict(nav=nav4(), contact='617 E Main Street<br>Council Grove, KS 66846<a href="tel:+16207675551">(620) 767 5551</a>',
                follow=[('Facebook', 'https://www.facebook.com/p/56-Donuts-61551670814483/')],
                legal='Every price, hour and detail comes from the 56 Donuts Facebook page and Council Grove listings.'),
    dock=[('Call', 'tel:+16207675551'), ('Directions', FD_MAP)],
)


if __name__ == '__main__':
    write_all(specs, sys.argv[1:])
