const { chromium } = require('playwright');
(async () => {
  const urls = process.argv.slice(2);
  const browser = await chromium.launch();
  for (const u of urls) {
    const ctx = await browser.newContext({ viewport: { width: 390, height: 844 }, deviceScaleFactor: 1, isMobile: true, hasTouch: true });
    const page = await ctx.newPage();
    const errs = [];
    page.on('pageerror', e => errs.push('JS:' + e.message));
    page.on('requestfailed', r => errs.push('FAIL:' + r.url().slice(0, 90)));
    let status = 0;
    try { const r = await page.goto(u, { waitUntil: 'networkidle', timeout: 45000 }); status = r.status(); } catch (e) { errs.push('NAV:' + e.message.slice(0, 80)); }
    await page.evaluate(async () => { for (let y = 0; y < document.body.scrollHeight; y += 600) { window.scrollTo(0, y); await new Promise(r => setTimeout(r, 120)); } });
    await page.waitForTimeout(1500);
    const info = await page.evaluate(() => {
      const sw = document.documentElement.scrollWidth, cw = document.documentElement.clientWidth;
      const wide = [...document.querySelectorAll('body *')].filter(e => { const r = e.getBoundingClientRect(); return r.right > cw + 2 && r.width > 0 && getComputedStyle(e).position !== 'fixed'; }).slice(0, 4).map(e => e.tagName + '.' + (e.className || '').toString().slice(0, 30));
      const imgs = [...document.images];
      const broken = imgs.filter(i => i.complete && i.naturalWidth === 0).map(i => i.src.slice(0, 80));
      const bg = [...document.querySelectorAll('*')].map(e => getComputedStyle(e).backgroundImage).filter(b => b && b.includes('url(')).length;
      const txt = document.body.innerText;
      const dashes = (txt.match(/[^\n]{0,25}[–—][^\n]{0,25}/g) || []).slice(0, 5);
      return { title: document.title, sw, cw, wide, imgs: imgs.length, broken, bg, ribbon: /Sample website by Onyx Rise Media/i.test(txt), placeholder: /placeholder/i.test(txt), dashes, free: (txt.match(/\bfree\b/gi) || []).length };
    });
    console.log(JSON.stringify({ u: u.split('/').pop(), status, ...info, errs: errs.slice(0, 5) }));
    await page.evaluate(()=>window.scrollTo(0,0)); await page.waitForTimeout(1200); if (process.env.SHOT) await page.screenshot({ path: process.env.SHOT + '/' + u.split('/').pop().replace('.html', '') + '.png', fullPage: false });
    await ctx.close();
  }
  await browser.close();
})();
