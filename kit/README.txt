ORM sample site kit (Onyx Rise Media)

Download every file in this folder into one working folder:
  base=https://justagt.github.io/orm-previews/kit
  for f in build.py base.css base.js hours.js helpers.py example_local.py example_broker.py check.js photos.txt; do curl -sSO $base/$f; done

Make a site:
  1. Copy example_local.py (local businesses, open now sign, optional live panel) or example_broker.py (brokers and agents, listings with a live payment estimate) to a new file.
  2. Replace EVERY value with facts verified on the business's own Facebook page, Google listing or chamber listing. Real prices, hours and reviews only. If a fact is unknown, leave that row out.
  3. Pick photos only from photos.txt (all checked). Same photo may repeat.
  4. python3 yourfile.py  -> writes out/<slug>.html
  5. Phone check: npm i playwright is preinstalled in Claude sessions; run  node check.js http://localhost:PORT/<slug>.html  after  (cd out && python3 -m http.server PORT &)
     Must show sw equal to cw (no sideways scroll), broken [], ribbon true, dashes [], free 0.
  6. Upload out/<slug>.html at https://github.com/JustaGt/orm-previews/upload/main , commit, wait about a minute, then confirm
     https://justagt.github.io/orm-previews/<slug>.html returns 200.

Spec keys (see build.py): name, short, title, desc, theme{bg,surface,ink,muted,accent,accent_ink,band,band_ink,ok}, font (gambarino, clash, zodiak, cabinet, sentient),
photos{h,menu,about,strip[3],s2a,visit,foot}, nav, primary, secondary, status_default, lead, facts, services{id,h2,sub,panel,groups,note},
about{h2,ps}, band{fig,bx,small,word}, hours{H,rows,note} OR areas_html, visit{rows,go}, footer{nav,contact,follow,legal}, dock, extra_js.
Rows are tuples (name, value, small_note, soft). hours H is a list Sunday..Saturday of [open_minute, close_minute] or None.
Use band word=True when the big figure is wider than 3 characters (like 100%).

Writing rules for everything: never use dashes (hyphens, en or em dashes) in visible text, never the word free, never mention Sandro's family.
