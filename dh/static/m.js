/* TREE Deal Hunter — telefoonpagina.
   Zelfde bron als het dashboard (/api/...), zodat de bedragen overal gelijk zijn.
   Alles wat uit een bron komt wordt ontsmet vóór het in de pagina staat (esc / safeUrl). */
'use strict';

const S = {
  items: [], zones: [], auctions: [], companies: [], boards: [], sum: null, alerts: [], dossiers: {klaar: [], aanbevolen: []},
  klasse: null, loss: false, nieuw: false, alleenMakelaar: false, reno: false, zone: null, sort: 'maand',
  tab: 'kansen', view: 'kansen', map: null, layers: {}, markers: null, zoneLayer: null,
  detailSeq: 0, wiSeq: 0, open: null
};

/* ---------- hulpjes ---------- */
const $ = (s) => document.querySelector(s);
const esc = (v) => String(v == null ? '' : v).replace(/[&<>"']/g, (c) =>
  ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c]));
function safeUrl(u) {
  if (u == null || u === '' || u === 'undefined' || u === 'null') return null;
  try {
    const x = new URL(String(u), location.origin);
    return (x.protocol === 'http:' || x.protocol === 'https:') ? x.href : null;
  } catch (e) { return null; }
}
const num = (v) => (v == null || isNaN(v)) ? '—' : Math.round(v).toLocaleString('nl-NL');
const eur = (v) => (v == null || isNaN(v)) ? '—' : '\u20ac\u00a0' + num(v);   // vaste spatie: het euroteken mag niet op een eigen regel vallen
const pct = (v, d) => (v == null || isNaN(v)) ? '—' : (v * 100).toFixed(d == null ? 0 : d) + ' %';
const maxeur = (v) => (v == null || v <= 0) ? '<span class="v nul">niet haalbaar</span>' : `<span class="v">${eur(v)}</span>`;
/* Wijknamen ook zonder de samenvatting: die komt een seconde later binnen, en tot dan stonden
   hier ruwe sleutels als "granadella_balcon" op het scherm. */
const ZONE_NL = {
  montgo_ermita: 'Montgó – Ermita', centro: 'Centrum', puerto_arenal: 'Puerto – Arenal',
  tosalet_adsubia: 'Tosalet – Adsubia', granadella_balcon: 'Granadella – Balcón al Mar',
  rafalet_pinosol: 'Rafalet – Pinosol', benitachell: 'Benitachell', moraira: 'Moraira'
};
const zoneLabel = (z) => (S.sum && S.sum.zone_labels && S.sum.zone_labels[z]) || ZONE_NL[z] || z || '';
const sgn = (v) => (v == null || isNaN(v)) ? '—' : (v > 0 ? '+' : '') + (v * 100).toFixed(0) + ' %';
async function api(path, opts) {
  const r = await fetch(path, opts);
  if (!r.ok) throw new Error(path + ': ' + r.status);
  return r.json();
}
const KLASSE = ['groen', 'blauw', 'oranje', 'grijs', 'onzeker'];
const TYPE = {
  Land: 'perceel', Plot: 'perceel', Villa: 'villa', Apartment: 'appartement', Penthouse: 'penthouse',
  Townhouse: 'rijwoning', Bungalow: 'bungalow', 'Country House': 'finca', Finca: 'finca',
  Commercial: 'bedrijfsruimte', Duplex: 'maisonnette', Studio: 'studio'
};
const soort = (t) => TYPE[t] || (t ? String(t).toLowerCase() : '');
const KLEUR = { groen: '#2f7a55', blauw: '#2f6386', oranje: '#b86e12', grijs: '#8c918e', onzeker: '#7d6a9c', geen: '#c3c0b8' };

/* ---------- laden ---------- */
async function load() {
  // De lijst eerst en meteen tonen. De samenvatting rekent alle 1.600 objecten door en duurt
  // seconden; daarop wachten betekende een leeg scherm op de telefoon.
  const zacht = (p, leeg) => p.catch(() => leeg);
  S.items = await api('/api/listings?tab=kansen,teduur,later,buiten');
  renderBar(); renderChips(); renderList();
  const [sum, auctions, zones, alerts, companies, tablones, dossiers] = await Promise.all([
    zacht(api('/api/summary'), null), zacht(api('/api/auctions'), []), zacht(api('/api/zones'), []),
    zacht(api('/api/alerts?days=14'), []), zacht(api('/api/companies?days=30'), []),
    zacht(api('/api/tablones'), {boards: []}), zacht(api('/api/dossiers'), {klaar: [], aanbevolen: []})
  ]);
  if (sum) S.sum = sum;
  S.auctions = auctions; S.zones = zones;
  S.alerts = alerts; S.companies = companies; S.boards = tablones.boards || []; S.dossiers = dossiers;
  renderBar(); renderChips(); renderList(); renderAuctions(); renderCompanies(); renderBoards(); renderZones(); renderDossiers();
  if (S.map) {
    $('#legend').innerHTML = KLASSE.map((k) => `<span><i style="background:${KLEUR[k]}"></i>${esc(((S.sum && S.sum.class_labels) || {})[k] || k)}</span>`).join('');
    syncMarkers();
  }
}

function renderBar() {
  const inBeeldNu = S.items.filter((x) => x.tab === S.tab && x.merk !== 'weg').length;
  const waar = S.tab === 'kansen' ? 'in Jávea' : S.tab === 'teduur' ? 'te duur' : S.tab === 'later' ? 'misschien later' : 'buiten Jávea';
  if (!S.sum) {                       // de samenvatting komt erachteraan
    $('#runinfo').innerHTML = `<b>${esc(inBeeldNu)}</b> ${esc(waar)}`;
    return;
  }
  const s = S.sum;
  const last = (s.runs || []).find((r) => r.finished_at) || {};
  const fout = (s.sources || []).filter((x) => x.last_status !== 'ok').map((x) => x.key);
  const t = last.finished_at ? new Date(last.finished_at).toLocaleString('nl-NL', { day: 'numeric', month: 'short', hour: '2-digit', minute: '2-digit' }) : 'nog geen ronde';
  const nxt = s.next_run ? new Date(s.next_run).toLocaleTimeString('nl-NL', { hour: '2-digit', minute: '2-digit' }) : '—';
  const inBeeld = S.items.filter((x) => x.tab === S.tab && x.merk !== 'weg').length;
  $('#runinfo').innerHTML = `<b>${esc(inBeeld)}</b> ${S.tab === 'kansen' ? 'in Jávea' : S.tab === 'teduur' ? 'te duur' : S.tab === 'later' ? 'misschien later' : 'buiten Jávea'} · ronde ${esc(t)} · volgende ${esc(nxt)}` +
    (fout.length ? ` · <span class="fout">bron ${esc(fout.join(', '))} niet gelukt</span>` : '');
}

const TABLABEL = { kansen: 'Jávea', teduur: 'Te duur', later: 'Misschien later', buiten: 'Buiten Jávea' };

function renderSeg() {
  const tel = (t) => S.items.filter((x) => x.tab === t && x.merk !== 'weg').length;
  $('#tabseg').innerHTML = ['kansen', 'teduur', 'later', 'buiten'].map((t) =>
    `<button role="tab" class="sg${S.tab === t ? ' on' : ''}" data-tab="${t}" aria-selected="${S.tab === t}">${esc(TABLABEL[t])}<span class="n">${tel(t)}</span></button>`).join('');
}

function renderChips() {
  // Binnen één tabblad zijn gemeenteknoppen zinloos; dan filter je op wijk.
  const basis = S.items.filter((x) => x.tab === S.tab && x.merk !== 'weg');
  const tel = (f) => basis.filter(f).length;
  const wijken = [...new Set(basis.map((x) => x.zone).filter(Boolean))]
    .map((z) => [z, zoneLabel(z)]).sort((a, b) => a[1].localeCompare(b[1]));
  $('#areachips').innerHTML = [`<button class="chip${S.zone ? '' : ' on'}" data-zone="">Alle wijken <span class="n">${basis.length}</span></button>`]
    .concat(wijken.map(([z, l]) => `<button class="chip${S.zone === z ? ' on' : ''}" data-zone="${esc(z)}">${esc(l)} <span class="n">${tel((x) => x.zone === z)}</span></button>`)).join('');
  $('#classchips').innerHTML = [`<button class="chip${S.klasse ? '' : ' on'}" data-klasse="">Alle kansen</button>`]
    .concat(KLASSE.filter((k) => tel((x) => x['class'] === k)).map((k) =>
      `<button class="chip${S.klasse === k ? ' on' : ''}" data-klasse="${k}"><i style="width:.55rem;height:.55rem;border-radius:50%;background:${KLEUR[k]};display:inline-block"></i> ${esc(((S.sum && S.sum.class_labels) || {})[k] || k)} <span class="n">${tel((x) => x['class'] === k)}</span></button>`)).join('');
}

/* ---------- lijst ---------- */
function filtered() {
  let out = S.items.filter((x) => {
    if (x.tab !== S.tab) return false;
    if (x.merk === 'weg') return false;                 // weggeklikt komt niet terug in de lijst
    if (S.zone && x.zone !== S.zone) return false;
    if (S.klasse && x.class !== S.klasse) return false;
    if (S.nieuw && !(x.events_7d || []).length) return false;
    if (S.alleenMakelaar && !x.alleen_bij_makelaar) return false;
    if (S.reno && !(x.renovatie && x.renovatie.punten >= 2)) return false;
    if (!S.loss && x.calc && x.calc.result < 0) return false;
    return true;
  });
  const key = {
    maand: (x) => -(x.per_maand == null ? -1e12 : x.per_maand),
    room: (x) => -(x.room == null ? -9 : x.room),
    result: (x) => -((x.calc && x.calc.result) || -1e12),
    price: (x) => (x.price == null ? 1e12 : x.price),
    new: (x) => -(new Date(x.first_seen || 0).getTime())
  }[S.sort];
  // onbetrouwbaar gerekende objecten altijd achteraan: ze zijn geen vergelijking waard
  out.sort((a, b) => (a.reliable === false) - (b.reliable === false) || key(a) - key(b));
  return out;
}

function sumBlock(x) {
  if (!x.calc) return '';
  const c = x.calc;
  return `<div class="sums">
    <div><span class="k">Aankoop</span><span class="v">${eur(c.acquisition)}</span></div>
    <div><span class="k">Bouw</span><span class="v">${eur(c.build)}</span></div>
    <div><span class="k">Verkoop</span><span class="v">${eur(c.sale)}</span></div>
    <div><span class="k">Resultaat</span><span class="v ${c.result >= 0 ? 'pos' : 'neg'}">${eur(c.result)}</span></div>
  </div>
  <div class="sub">${esc(c.months)} maanden · marge ${pct(c.margin)} · rendement op kosten ${pct(c.roi_on_costs)} · verkoop ${num(c.eur_m2_sale)} €/m²</div>`;
}

function vlaggen(x) {
  // Hoogstens twee vlaggetjes: meer maakt het kaartje weer een lap tekst.
  const v = [];
  if (x.water && x.water.waarschuwing) v.push(`<span class="flag let">${esc(x.water.waarschuwing.split('.')[0])}</span>`);
  if (x.opknapper) v.push(`<span class="flag ok">${esc(x.opknapper.reden)}</span>`);
  const kp = x.koper;
  if (kp && kp.punten) v.push(`<span class="flag">${esc(kp.redenen.slice(0, 2).join(' · '))}</span>`);
  if ((x.tegenspraak || []).length) v.push(`<span class="flag let">${esc(x.tegenspraak[0])}</span>`);
  if (x.bestemming && x.bestemming !== 'stedelijk') v.push(`<span class="flag let">${esc(x.bestemming)}</span>`);
  else if (x.bestemming_wonen === 'onbekend') v.push('<span class="flag">bestemming onbekend</span>');
  if (x.fiscaal) v.push(`<span class="flag let">fiscale waarde + ${eur(x.fiscaal.verschil)}</span>`);
  else if (x.price_drop) v.push(`<span class="flag ok">prijs ${sgn(x.price_drop)}</span>`);
  else if ((x.events_7d || []).includes('NIEUW')) v.push('<span class="flag ok">nieuw</span>');
  else if (x.alleen_bij_makelaar) v.push('<span class="flag">niet op de portalen gezien</span>');
  return v.slice(0, 2).join('');
}

function oordeelRegel(x) {
  const b = x.bod;
  if (!b || !x.price) return '<p class="oordeel grijs">Nog niet betrouwbaar te rekenen.</p>';
  if (b.serieus_mogelijk === false && b.serieus_tekst) {
    return `<p class="oordeel let"><b>! Vraagprijs moet eerst zakken</b>
      <span>${esc(b.serieus_tekst)}</span></p>`;
  }
  if (b.kloof) {
    return `<p class="oordeel let"><b>! Te duur om te rekenen</b>
      <span>De deal draagt ${eur(b.plafond)} van de ${eur(x.price)}</span></p>`;
  }
  const v = b.voorzichtig || 0;
  const klasse = v >= x.price ? 'ok' : (b.plafond >= x.price ? '' : 'let');
  const merk = v >= x.price ? '✓' : (b.plafond >= x.price ? '·' : '!');
  return `<p class="oordeel ${klasse}"><b>${esc(merk)} Openen op ${eur(b.opening)}</b>
    <span>Niet hoger dan ${eur(b.walk)}</span></p>`;
}

/* Bij welke aanbieder de advertentie staat. Liefst de naam van het kantoor; anders het webadres
   zonder www en zonder .com, want dat herken je ook. */
function aanbieder(x) {
  if (x.kantoor) return x.kantoor;
  const u = safeUrl(x.url);
  if (!u) return null;
  try {
    const host = new URL(u).hostname.replace(/^www\./, '');
    if (/idealista/.test(host)) return 'Idealista';
    return host.replace(/\.(com|es|net|nl|eu)$/, '');
  } catch (e) { return null; }
}

function card(x) {
  const waar = x.zone_label || x.area_label || '—';
  const soortmerk = x.appartement ? 'appartement' : (String(x.category || '').startsWith('perceel') ? 'perceel' : soort(x.type));
  const maten = [x.built_m2 ? num(x.built_m2) + ' m²' : null, x.plot_m2 ? 'perceel ' + num(x.plot_m2) + ' m²' : null]
    .filter(Boolean).join(' · ');
  const c = x.calc;
  const haalt = x['class'] === 'groen' || x['class'] === 'blauw';
  const som = c ? `<div class="sums">
      <div><span class="k">Aankoop</span><span class="v">${eur(c.acquisition)}</span></div>
      <div><span class="k">Bouw</span><span class="v">${eur(c.build)}</span></div>
      <div><span class="k">Verkoop</span><span class="v">${eur(c.sale)}</span></div>
      <div><span class="k">Resultaat</span><span class="v ${c.result < 0 ? 'neg' : (haalt ? 'pos' : '')}">${eur(c.result)}${c.roi_on_costs != null ? `<i class="rend">${pct(c.roi_on_costs)} op kosten</i>` : ''}</span></div>
    </div>
    ${c.financing_per_5pct ? `<span class="rente">Gerekend met ${pct(c.financing_rate, 0)} rente.
      Elke 5 % meer kost ${eur(c.financing_per_5pct)} van het resultaat.</span>` : ''}` : '';
  const merk = x.merk || '';
  const adv = safeUrl(x.url);          // Jan 26-09-2026: geen foto's, wel een duidelijke weg naar de bron
  const bij = aanbieder(x);
  return `<article class="card ${esc(x['class'])}${merk ? ' gemerkt' : ''}" data-card="${esc(x.id)}">
    <button class="card-open" data-id="${esc(x.id)}">
      <span class="head"><span class="where">${esc(waar)}</span><span class="price">${eur(x.price)}</span></span>
      <span class="maten">${maten && maten.startsWith(soortmerk) ? '' : esc(soortmerk) + (maten ? ' · ' : '')}${esc(maten || x.ref)}</span>
      ${x.bronnen > 1 ? `<span class="bronnen">Staat bij ${esc(x.bronnen)} aanbieders: ${esc((x.ook_bij || []).map((o) => o.bron).join(', '))}${x.prijsverschil_tussen_bronnen ? ' · ' + eur(x.prijsverschil_tussen_bronnen) + ' verschil in vraagprijs' : ''}</span>` : ''}
      ${oordeelRegel(x)}
      ${som}
      <span class="flags">${vlaggen(x)}</span>
    </button>
    ${adv ? `<a class="adv" href="${esc(adv)}" target="_blank" rel="noopener noreferrer">
      Advertentie openen${bij ? ' bij ' + esc(bij) : ''} <span class="pijl">↗</span></a>` : ''}
    <div class="acts">
      <button class="act${merk === 'boeiend' ? ' on' : ''}" data-mark="boeiend" data-mid="${esc(x.id)}">♥ Boeiend</button>
      <button class="act${merk === 'gebeld' ? ' on' : ''}" data-mark="gebeld" data-mid="${esc(x.id)}">☎ Gebeld</button>
      <button class="act${merk === 'bod' ? ' on' : ''}" data-mark="bod" data-mid="${esc(x.id)}">€ Bod uit</button>
      <button class="act weg" data-mark="weg" data-mid="${esc(x.id)}">✕ Weg</button>
    </div>
    ${(merk === 'gebeld' || merk === 'bod') ? notitieblok(x) : ''}
  </article>`;
}

/* Wat je na een telefoontje wilt onthouden, en wanneer je eraan herinnerd wilt worden. De
   herinnering komt mee in het ochtendbericht van 08:00 (Jan, 26-09-2026). */
function notitieblok(x) {
  return `<div class="notitie" data-nid="${esc(x.id)}">
    <textarea rows="2" placeholder="Wat is er gezegd?">${esc(x.notitie || '')}</textarea>
    <div class="nrij">
      <label>Terugbellen op <input type="date" value="${esc(x.volgende_stap || '')}"></label>
      <button data-bewaar="${esc(x.id)}">Bewaren</button>
    </div>
    <p class="nuit"></p>
  </div>`;
}

async function bewaarNotitie(id) {
  const blok = document.querySelector(`.notitie[data-nid="${id}"]`);
  if (!blok) return;
  const uit = blok.querySelector('.nuit');
  const x = S.items.find((i) => i.id === id);
  uit.className = 'nuit'; uit.textContent = 'Bewaren…';
  try {
    const r = await api('/api/markeer', { method: 'POST', headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ id: id, merk: (x && x.merk) || 'gebeld',
                             notitie: blok.querySelector('textarea').value,
                             volgende_stap: blok.querySelector('input[type=date]').value || null }) });
    if (x) { x.notitie = r.notitie; x.volgende_stap = r.volgende_stap; }
    uit.className = 'nuit ok';
    uit.textContent = r.volgende_stap ? 'Bewaard. Je krijgt er bericht over op ' + r.volgende_stap + '.' : 'Bewaard.';
  } catch (e) { uit.className = 'nuit fout'; uit.textContent = 'Bewaren mislukt.'; }
}

function renderList() {
  renderSeg();
  const rows = filtered();
  const verborgen = S.items.filter((x) => x.tab === S.tab && x.merk !== 'weg' && x.calc && x.calc.result < 0).length;
  const totaal = S.items.filter((x) => x.tab === S.tab && x.merk !== 'weg').length;
  $('#listmeta').textContent = `${rows.length} van ${totaal}` +
    (S.loss ? '' : verborgen ? ` · ${verborgen} met verlies verborgen` : '');
  $('#cards').innerHTML = rows.length ? rows.map(card).join('')
    : '<p class="empty">Niets gevonden met deze filters.</p>';
  for (const m of ['boeiend', 'gebeld']) {
    const eigen = S.items.filter((x) => x.merk === m)
      .sort((a, b) => -((a.per_maand || -1e12) - (b.per_maand || -1e12)));
    const el = document.getElementById('cards-' + m);
    if (el) el.innerHTML = eigen.length ? eigen.map(card).join('')
      : `<p class="empty">Nog niets als ${m} aangemerkt.</p>`;
    const teller = document.getElementById('n-' + m);
    if (teller) teller.textContent = eigen.length || '';
  }
  renderAlerts();
}

function renderDossiers() {
  const el = document.getElementById('dossierbox');
  if (!el) return;
  const klaar = (S.dossiers.aanbevolen || []).filter((x) => x.heeft_dossier);
  if (!klaar.length) { el.innerHTML = ''; return; }
  el.innerHTML = `<div class="dossiers"><div class="dtop"><b>${klaar.length} volledige dossiers</b>
    <a href="/dossiers/index.html" target="_blank" rel="noopener noreferrer">besluitpagina</a></div>
    ${klaar.map((x) => `<a class="drow" href="/dossiers/${encodeURIComponent(x.ref)}.html" target="_blank" rel="noopener noreferrer">
      <span class="dot ${esc(x['class'])}"></span><span class="dw">${esc(x.zone || '')}</span>
      <span class="dp">${eur(x.price)}</span><span class="dr">${eur(x.result)}</span><span class="dm">${esc(x.months)} mnd</span></a>`).join('')}</div>`;
}

function renderAlerts() {
  // Alleen melden over objecten die ook in de lijst staan; anders wijst de banner naar iets wat je
  // niet kunt openen.
  const zichtbaar = new Set(S.items.filter((x) => x.tab === S.tab && x.merk !== 'weg').map((x) => x.id));
  const mee = (a) => zichtbaar.has(a.listing_id);
  const direct = S.alerts.filter((a) => a.tier === 'direct' && mee(a));
  const verz = S.alerts.filter((a) => a.tier === 'verzamel' && mee(a));
  // een nulmeting is geen nieuws: die objecten stonden er al toen de meldingen aangingen
  const wanneer = (rij) => rij.every((a) => a.baseline)
    ? 'stond er al toen de meldingen aangingen'
    : 'nieuw sinds een van de vorige rondes';
  const delen = [];
  if (direct.length) delen.push(`<b>${direct.length} sterke kans${direct.length === 1 ? '' : 'en'}</b>`);
  if (verz.length) delen.push(`${verz.length} onderhandelbaar`);
  const h = delen.length
    ? `<p class="alertline">${delen.join(' · ')} — ${esc(wanneer(direct.concat(verz)))}.</p>` : '';
  $('#alertbox').innerHTML = h;
}

/* ---------- veilingen, vennootschappen, borden, wijken ---------- */
function renderAuctions() {
  const a = S.auctions;
  $('#auctionmeta').textContent = `${a.length} lopende veilingen in de provincie. Een BOE-aankondiging noemt nooit de ligging; die moet je zelf bevestigen.`;
  $('#auctions').innerHTML = a.length ? a.map((x) => {
    const u = safeUrl(x.url);
    const end = x.end_date ? new Date(x.end_date) : null;
    const days = end ? Math.ceil((end - Date.now()) / 86400000) : null;
    return `<div class="row veiling"><div class="t">${esc(x.title || x.sub || '—')}</div>
      <div class="d">${esc(x.source)} · ${esc(x.town || x.area || 'ligging onbekend')} ${x.valuation ? '· waarde ' + eur(x.valuation) : ''}
      ${end ? '· sluit ' + esc(end.toLocaleDateString('nl-NL')) + (days != null ? ` (${days} dagen)` : '') : ''}</div>
      ${(x.blockers || []).length ? `<div class="d">⚠ ${esc(x.blockers.join(' · '))}</div>` : ''}
      ${u ? `<div class="d"><a href="${esc(u)}" target="_blank" rel="noopener noreferrer">aankondiging openen</a></div>` : ''}</div>`;
  }).join('') : '<p class="empty">Geen lopende veilingen in beeld.</p>';
}

function renderCompanies() {
  $('#companies').innerHTML = S.companies.length ? S.companies.slice(0, 40).map((c) => {
    const u = safeUrl(c.url);
    return `<div class="row ${c.priority >= 2 ? 'prio2' : ''}"><div class="t">${esc(c.name)}</div>
      <div class="d">${esc((c.acts || []).join(' · '))}${c.sector ? ' · ' + esc(c.sector) : ''}${c.place ? ' · ' + esc(c.place) : ''} · ${esc(c.published_on || '')}</div>
      ${u ? `<div class="d"><a href="${esc(u)}" target="_blank" rel="noopener noreferrer">BORME openen</a></div>` : ''}</div>`;
  }).join('') : '<p class="empty">Nog geen signalen. De eerste ronde vult deze lijst.</p>';
}

function renderBoards() {
  $('#boards').innerHTML = S.boards.map((b) => {
    const u = safeUrl(b.url);
    return `<div class="row"><div class="t">${esc(b.town)}</div>
      <div class="d">${u ? `<a href="${esc(u)}" target="_blank" rel="noopener noreferrer">bord openen</a>` : esc(b.url)}</div></div>`;
  }).join('');
}

function renderZones() {
  const rows = S.zones.map((z) => `<tr><td>${esc(z.label)}</td>
    <td class="num">${z.villa_renovated ? num(z.villa_renovated.median) : '—'}</td>
    <td class="num">${z.villa_new ? num(z.villa_new.median) : '—'}</td>
    <td class="num">${z.apartment_renovated ? num(z.apartment_renovated.median) : '—'}</td></tr>`).join('');
  $('#zones').innerHTML = `<table><thead><tr><th>Wijk</th><th class="num">Gerenoveerd</th><th class="num">Nieuwbouw</th><th class="num">Appartement</th></tr></thead><tbody>${rows}</tbody></table>
    <p class="meta">Mediaan vraagprijs per m² gebouwd. Voorzichtig rekent met het laagste kwart, gunstig met het hoogste kwart van dezelfde reeks.</p>`;
}

/* ---------- kaart ---------- */
function initMap() {
  if (S.map) { setTimeout(() => S.map.invalidateSize(), 60); return; }
  S.map = L.map('map', { zoomControl: false, attributionControl: true }).setView([38.789, 0.166], 12);
  L.control.zoom({ position: 'bottomright' }).addTo(S.map);
  S.layers.ign = L.tileLayer('https://www.ign.es/wmts/ign-base?layer=IGNBaseTodo&style=default&tilematrixset=GoogleMapsCompatible&Service=WMTS&Request=GetTile&Version=1.0.0&Format=image/jpeg&TileMatrix={z}&TileCol={x}&TileRow={y}',
    { maxZoom: 19, attribution: 'IGN España' });
  S.layers.pnoa = L.tileLayer('https://www.ign.es/wmts/pnoa-ma?layer=OI.OrthoimageCoverage&style=default&tilematrixset=GoogleMapsCompatible&Service=WMTS&Request=GetTile&Version=1.0.0&Format=image/jpeg&TileMatrix={z}&TileCol={x}&TileRow={y}',
    { maxZoom: 19, attribution: 'PNOA, IGN España' });
  S.layers.cad = L.tileLayer.wms('https://ovc.catastro.meh.es/Cartografia/WMS/ServidorWMS.aspx', {
    layers: 'Catastro', format: 'image/png', transparent: true, attribution: 'Dirección General del Catastro'
  });
  S.layers.ign.addTo(S.map);
  S.markers = L.layerGroup().addTo(S.map);
  S.zoneLayer = L.layerGroup();
  // De samenvatting kan nog onderweg zijn; zonder deze vangnetten brak de legenda de hele
  // kaartopbouw af en bleef de kaart zonder spelden staan.
  $('#legend').innerHTML = KLASSE.map((k) => `<span><i style="background:${KLEUR[k]}"></i>${esc(((S.sum && S.sum.class_labels) || {})[k] || k)}</span>`).join('');
  syncMarkers();
  setTimeout(() => S.map.invalidateSize(), 60);
}

function syncMarkers() {
  if (!S.markers) return;
  S.markers.clearLayers();
  filtered().forEach((x) => {
    if (x.lat == null || x.lon == null) return;
    L.circleMarker([x.lat, x.lon], {
      radius: 8, color: '#fff', weight: 2, fillColor: KLEUR[x.class] || KLEUR.geen, fillOpacity: 0.95
    }).addTo(S.markers).on('click', () => openDetail(x.id));
  });
  S.zoneLayer.clearLayers();
  S.zones.forEach((z) => {
    const v = z.villa_renovated && z.villa_renovated.median;
    if (!v) return;
    L.marker([z.lat, z.lon], {
      icon: L.divIcon({ className: '', html: `<div style="background:#fffefb;border:1px solid rgba(43,51,49,.3);border-radius:6px;padding:2px 5px;font:500 11px/1.2 system-ui;white-space:nowrap">${esc(z.label)} ${num(v)} €/m²</div>`, iconSize: null })
    }).addTo(S.zoneLayer);
  });
}

/* ---------- dossier ---------- */
async function openDetail(id) {
  const seq = ++S.detailSeq;
  $('#sheet').hidden = false;
  document.body.style.overflow = 'hidden';
  $('#sheet-body').innerHTML = '<p class="empty">Laden…</p>';
  let d;
  try { d = await api('/api/listing/' + encodeURIComponent(id)); } catch (e) {
    if (seq === S.detailSeq) $('#sheet-body').innerHTML = '<p class="empty">Kon dit dossier niet laden.</p>';
    return;
  }
  if (seq !== S.detailSeq) return;                      // een ander object is intussen geopend
  S.open = { id: id, data: d, scenario: d.feasibility && d.feasibility.best_key, ov: {} };
  renderSheet();
}

function scenarioOf() {
  const f = S.open.data.feasibility || {};
  return (f.scenarios || []).find((s) => s.key === S.open.scenario) || null;
}

function renderSheet() {
  const d = S.open.data, s = scenarioOf();
  const where = [d.zone_label || d.area_label, d.location].filter(Boolean).join(' · ');
  const u = safeUrl(d.url);
  const scen = (d.feasibility && d.feasibility.scenarios || []).filter((x) => x.available);
  let h = `<h1>${esc(where || d.ref)}</h1>
    ${d.kantoor ? `<p class="meta">Via ${esc(d.kantoor)}${d.alleen_bij_makelaar ? ' · niet gezien op de portalen die wij volgen' : d.portaal ? ' · ook gezien bij ' + esc(d.portaal) : ''}</p>` : ''}
    <p class="meta"><span class="ref">${esc(d.ref)}</span> · ${esc(soort(d.type))} ${d.built_m2 ? '· ' + num(d.built_m2) + ' m² gebouwd' : ''} ${d.plot_m2 ? '· ' + num(d.plot_m2) + ' m² perceel' : ''} · vraagprijs ${eur(d.price)}</p>`;

  if (scen.length > 1) {
    h += `<div class="scroller">${scen.map((x) => `<button class="chip${x.key === S.open.scenario ? ' on' : ''}" data-scen="${esc(x.key)}">${esc(x.label)}</button>`).join('')}</div>`;
  }
  if (!s) {
    h += `<p class="warn blok">${esc((d.feasibility && d.feasibility.reason) || 'Niet te rekenen.')}</p>`;
  } else {
    h += `<p class="meta" style="margin-bottom:.2rem">Maximale koopprijs bij jouw marge</p>
    <div class="three" id="three">
      <div><span class="k">Voorzichtig</span>${maxeur(s.max_price.conservative)}<span class="m">${num(s.comps.eur_m2.conservative)} €/m² verkoop</span></div>
      <div><span class="k">Basis</span>${maxeur(s.max_price.base)}<span class="m">${num(s.comps.eur_m2.base)} €/m² verkoop</span></div>
      <div><span class="k">Gunstig</span>${maxeur(s.max_price.upside)}<span class="m">${num(s.comps.eur_m2.upside)} €/m² verkoop</span></div>
    </div>
    <p class="meta">Hoogste koopprijs waarbij de marge nog gehaald wordt. Drie kolommen: laagste kwart, mediaan en hoogste kwart van de wijkprijzen.</p>
    <p class="meta" style="margin-bottom:.2rem">De rekensom bij de huidige vraagprijs</p>
    <div id="sums">${sumBlock({ calc: s.sum })}</div>
    <dl class="kv" id="kv">
      <dt>Scenario</dt><dd>${esc(s.label)}</dd>
      <dt>Verkoopbaar</dt><dd>${num(s.result_m2)} m²</dd>
      <dt>Bouwkosten</dt><dd>${num(s.sum.eur_m2_build)} €/m²</dd>
      <dt>Vergelijking</dt><dd>${esc(zoneLabel(s.comps.zone))} · ${esc(s.comps.n)} objecten</dd>
    </dl>`;

    const a = (d.feasibility && d.feasibility.assumptions) || {};
    h += `<h2>Wat als</h2>
    ${slider('price', 'Koopprijs', Math.round((d.price || 200000) * 0.5), Math.round((d.price || 200000) * 1.2), 5000, S.open.ov.price != null ? S.open.ov.price : d.price, eur)}
    ${slider('margin', 'Winstmarge', 0.10, 0.40, 0.01, S.open.ov.margin != null ? S.open.ov.margin : a.margin, (v) => pct(v))}
    ${slider('reno_rate', 'Renovatie €/m²', 500, 2500, 50, S.open.ov.reno_rate != null ? S.open.ov.reno_rate : a.reno_rate, num)}
    ${slider('new_rate', 'Nieuwbouw €/m²', 1200, 4000, 50, S.open.ov.new_rate != null ? S.open.ov.new_rate : a.new_rate, num)}
    ${slider('result_m2', 'Verkoopbaar m²', Math.max(20, Math.round(s.base_result_m2 * 0.6)), Math.min(5000, Math.round(s.base_result_m2 * 1.6)), 5, S.open.ov.result_m2 != null ? S.open.ov.result_m2 : s.result_m2, num)}
    ${slider('sale_adj', 'Verkoopprijs bijstellen', -0.25, 0.25, 0.01, S.open.ov.sale_adj != null ? S.open.ov.sale_adj : 0, (v) => sgn(v))}
    ${slider('finance_rate', 'Rente van de investeerder', 0, 0.25, 0.005, S.open.ov.finance_rate != null ? S.open.ov.finance_rate : (a.finance_rate != null ? a.finance_rate : 0.15), (v) => pct(v, 1))}
    <p class="meta" id="wistatus"></p>`;

    (s.warnings || []).forEach((w) => { h += `<p class="warn">${esc(w)}</p>`; });
    if (s.over_max_duration) h += `<p class="warn">Looptijd ${esc(s.months)} maanden ligt boven jouw maximum.</p>`;
  }
  (d.blockers || []).forEach((b) => { h += `<p class="warn blok">${esc(b)}</p>`; });
  if (d.kandidaat_info) {
    (d.kandidaat_info.claims || []).forEach((c) => { h += `<p class="meta">Claim van de aanbieder: ${esc(c)}</p>`; });
  }
  const heeftDossier = (S.dossiers.klaar || []).indexOf(String(d.ref)) >= 0;
  h += `<div class="actions">
      ${heeftDossier ? `<a class="primary" href="/dossiers/${encodeURIComponent(d.ref)}.html" target="_blank" rel="noopener noreferrer">Volledig dossier</a>` : ''}
      ${u ? `<a href="${esc(u)}" target="_blank" rel="noopener noreferrer">Advertentie</a>` : ''}
      ${(d.lat != null && d.lon != null) ? `<a href="https://www.google.com/maps/search/?api=1&query=${encodeURIComponent(d.lat + ',' + d.lon)}" target="_blank" rel="noopener noreferrer">Kaart</a>
      <button data-cat="1">Kadaster</button>` : ''}
    </div>
    <div id="catout"></div>
    <h2>Beoordeling</h2>
    <div class="actions">
      <button class="primary" data-review="interessant">Interessant</button>
      <button data-review="watchlist">Volglijst</button>
      <button data-review="afwijzen">Afwijzen</button>
    </div>
    <p class="meta" id="reviewstatus">${d.review ? 'Laatste oordeel: ' + esc(d.review.verdict) + (d.review.note ? ' — ' + esc(d.review.note) : '') : 'Nog niet beoordeeld.'}</p>
    <p class="foot">Vraagprijzen uit vergelijkbare woningen in dezelfde wijk, geen transactieprijzen. Dit is een indicatie, geen taxatie en geen biedadvies. Percelen en vergunningen moeten per object bevestigd worden met nota simple en informe urbanístico.</p>`;
  $('#sheet-body').innerHTML = h;
  $('#sheet-body').scrollTop = 0;
}

function slider(key, label, min, max, step, val, fmt) {
  const v = val == null ? min : val;
  return `<div class="sl"><label for="sl-${key}">${esc(label)}<output id="out-${key}">${fmt(v)}</output></label>
    <input type="range" id="sl-${key}" data-key="${key}" min="${min}" max="${max}" step="${step}" value="${v}"></div>`;
}

const FMT = { price: eur, margin: (v) => pct(v), reno_rate: num, new_rate: num, result_m2: num,
             sale_adj: (v) => sgn(v), finance_rate: (v) => pct(v, 1) };

async function whatIf() {
  const seq = ++S.wiSeq;
  const id = S.open.id;
  $('#wistatus').textContent = 'Rekenen…';
  let res;
  try {
    res = await api('/api/listing/' + encodeURIComponent(id) + '/wat-als', {
      method: 'POST', headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(Object.assign({ scenario_key: S.open.scenario }, S.open.ov))
    });
  } catch (e) {
    if (seq === S.wiSeq) $('#wistatus').textContent = 'Kon niet rekenen.';
    return;
  }
  if (seq !== S.wiSeq || !S.open || S.open.id !== id) return;   // antwoord hoort bij een ander object
  const s = (res.scenarios || []).find((x) => x.key === S.open.scenario) || (res.scenarios || [])[0];
  if (!s || !s.available) { $('#wistatus').textContent = 'Geen uitkomst voor deze waarden.'; return; }
  $('#three').innerHTML = `
    <div><span class="k">Voorzichtig</span>${maxeur(s.max_price.conservative)}<span class="m">${num(s.comps.eur_m2.conservative)} €/m² verkoop</span></div>
    <div><span class="k">Basis</span>${maxeur(s.max_price.base)}<span class="m">${num(s.comps.eur_m2.base)} €/m² verkoop</span></div>
    <div><span class="k">Gunstig</span>${maxeur(s.max_price.upside)}<span class="m">${num(s.comps.eur_m2.upside)} €/m² verkoop</span></div>`;
  $('#sums').innerHTML = sumBlock({ calc: s.sum });
  $('#kv').innerHTML = `<dt>Scenario</dt><dd>${esc(s.label)}</dd>
    <dt>Verkoopbaar</dt><dd>${num(s.result_m2)} m²</dd>
    <dt>Bouwkosten</dt><dd>${num(s.sum.eur_m2_build)} €/m²</dd>
    <dt>Vergelijking</dt><dd>${esc(zoneLabel(s.comps.zone))} · ${esc(s.comps.n)} objecten</dd>`;
  const changed = Object.keys(S.open.ov).length;
  $('#wistatus').textContent = changed
    ? 'Aangepaste aannames; het vergelijk met de vraagprijs klopt alleen als je de koopprijs niet hebt verschoven.'
    : '';
}

function closeSheet() {
  $('#sheet').hidden = true;
  document.body.style.overflow = '';
  S.open = null;
  S.detailSeq++; S.wiSeq++;
}

/* ---------- markeren: boeiend, gebeld, weg ---------- */
let toastTimer = null;
function toast(tekst) {
  const el = $('#toast');
  el.textContent = tekst; el.hidden = false;
  clearTimeout(toastTimer);
  toastTimer = setTimeout(() => { el.hidden = true; }, 2600);
}

async function markeer(id, merk) {
  const x = S.items.find((i) => i.id === id);
  if (!x) return;
  const nieuw = x.merk === merk ? 'geen' : merk;      // nog eens tikken maakt het merkje ongedaan
  const vorig = x.merk;
  x.merk = nieuw === 'geen' ? null : nieuw;           // meteen laten zien, ook op een trage lijn
  renderBar(); renderChips(); renderList(); syncMarkers();
  try {
    await api('/api/markeer', { method: 'POST', headers: { 'Content-Type': 'application/json' },
                                body: JSON.stringify({ id: id, merk: nieuw }) });
    toast(nieuw === 'geen' ? 'Merkje weggehaald' :
      nieuw === 'weg' ? 'Weggeklikt. Staat niet meer in de lijst.' :
      nieuw === 'boeiend' ? 'Op de lijst Boeiend gezet' :
      nieuw === 'bod' ? 'Bod uitgebracht' : 'Op de lijst Gebeld gezet');
  } catch (e) {
    x.merk = vorig;                                   // server wees het af: terugdraaien
    renderBar(); renderChips(); renderList();
    toast('Opslaan mislukt. Probeer het nog eens.');
  }
}

/* ---------- bediening ---------- */
function show(view) {
  S.view = view;
  document.querySelectorAll('.view').forEach((v) => { v.hidden = v.dataset.view !== view; });
  document.querySelectorAll('.tb').forEach((b) => {
    const on = b.dataset.go === view;
    b.classList.toggle('on', on);
    b.setAttribute('aria-selected', on ? 'true' : 'false');
  });
  if (view === 'kaart') initMap();
  $('#main').scrollTop = 0;
}

document.addEventListener('click', (e) => {
  const tb = e.target.closest('.tb'); if (tb) return show(tb.dataset.go);
  const sg = e.target.closest('[data-tab]');
  if (sg) { S.tab = sg.dataset.tab; S.zone = null; renderBar(); renderChips(); renderList(); syncMarkers(); return; }
  const mk = e.target.closest('[data-mark]');
  if (mk) { markeer(Number(mk.dataset.mid), mk.dataset.mark); return; }
  const bw = e.target.closest('[data-bewaar]');
  if (bw) { bewaarNotitie(Number(bw.dataset.bewaar)); return; }
  const zo = e.target.closest('[data-zone]'); if (zo) { S.zone = zo.dataset.zone || null; renderChips(); renderList(); syncMarkers(); return; }
  const kl = e.target.closest('[data-klasse]'); if (kl) { S.klasse = kl.dataset.klasse || null; renderChips(); renderList(); syncMarkers(); return; }
  const c = e.target.closest('.card-open'); if (c) return openDetail(Number(c.dataset.id));
  if (e.target.closest('#sheet-close')) return closeSheet();
  const sc = e.target.closest('[data-scen]');
  if (sc) { S.open.scenario = sc.dataset.scen; S.open.ov = {}; renderSheet(); return; }
  const rv = e.target.closest('[data-review]'); if (rv) return sendReview(rv.dataset.review);
  if (e.target.closest('[data-cat]')) return lookupCatastro();
});

$('#t-loss').addEventListener('click', (e) => {
  S.loss = !S.loss;
  e.currentTarget.setAttribute('aria-pressed', String(S.loss));
  renderList(); syncMarkers();
});
$('#t-reno').addEventListener('click', (e) => {
  S.reno = !S.reno;
  e.currentTarget.setAttribute('aria-pressed', String(S.reno));
  renderList(); syncMarkers();
});
$('#t-mak').addEventListener('click', (e) => {
  S.alleenMakelaar = !S.alleenMakelaar;
  e.currentTarget.setAttribute('aria-pressed', String(S.alleenMakelaar));
  renderList(); syncMarkers();
});
$('#t-new').addEventListener('click', (e) => {
  S.nieuw = !S.nieuw;
  e.currentTarget.setAttribute('aria-pressed', String(S.nieuw));
  renderList(); syncMarkers();
});
$('#sort').addEventListener('change', (e) => { S.sort = e.target.value; renderList(); });
$('#layer').addEventListener('change', (e) => {
  if (!S.map) return;
  ['ign', 'pnoa'].forEach((k) => { if (S.map.hasLayer(S.layers[k])) S.map.removeLayer(S.layers[k]); });
  S.layers[e.target.value].addTo(S.map);
  if (S.map.hasLayer(S.layers.cad)) S.layers.cad.bringToFront();
});
$('#t-cad').addEventListener('click', (e) => {
  if (!S.map) return;
  const on = !S.map.hasLayer(S.layers.cad);
  if (on) S.layers.cad.addTo(S.map); else S.map.removeLayer(S.layers.cad);
  e.currentTarget.setAttribute('aria-pressed', String(on));
});
$('#t-zones').addEventListener('click', (e) => {
  if (!S.map) return;
  const on = !S.map.hasLayer(S.zoneLayer);
  if (on) S.zoneLayer.addTo(S.map); else S.map.removeLayer(S.zoneLayer);
  e.currentTarget.setAttribute('aria-pressed', String(on));
});

/* schuiven: tijdens het slepen alleen het label bijwerken, rekenen pas bij loslaten */
let wiTimer = null;
document.addEventListener('input', (e) => {
  const sl = e.target.closest('input[type=range][data-key]');
  if (!sl || !S.open) return;
  const k = sl.dataset.key, v = Number(sl.value);
  const out = document.getElementById('out-' + k);
  if (out) out.textContent = (FMT[k] || num)(v);
});
document.addEventListener('change', (e) => {
  const sl = e.target.closest('input[type=range][data-key]');
  if (!sl || !S.open) return;
  S.open.ov[sl.dataset.key] = Number(sl.value);
  clearTimeout(wiTimer);
  wiTimer = setTimeout(whatIf, 120);
});

async function sendReview(verdict) {
  if (!S.open) return;
  const st = $('#reviewstatus');
  st.textContent = 'Opslaan…';
  try {
    await api('/api/review', {
      method: 'POST', headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ listing_id: S.open.id, verdict: verdict })
    });
    st.textContent = 'Opgeslagen: ' + verdict + '. Er gaat niets naar buiten; dit blijft binnen het systeem.';
  } catch (e) { st.textContent = 'Opslaan mislukt.'; }
}

async function lookupCatastro() {
  if (!S.open) return;
  const d = S.open.data, out = $('#catout');
  out.innerHTML = '<p class="meta">Kadaster raadplegen…</p>';
  try {
    const r = await api(`/api/catastro?lat=${encodeURIComponent(d.lat)}&lon=${encodeURIComponent(d.lon)}`);
    out.innerHTML = (r.parcels || []).length
      ? `<div class="kv">${r.parcels.map((p) => `<dt>${esc(p.rc)}</dt><dd>${esc(p.address || '')}${p.distance_m ? ' · ' + esc(p.distance_m) + ' m' : ''} · <a href="${esc(safeUrl(p.sede_url) || '#')}" target="_blank" rel="noopener noreferrer">kaart</a></dd>`).join('')}</div>
        <p class="meta">${esc(r.note)}</p>`
      : `<p class="meta">Geen perceel gevonden op dit punt. ${esc(r.error || '')}</p>`;
  } catch (e) { out.innerHTML = '<p class="meta">Kadaster niet bereikbaar.</p>'; }
}

/* verversen alleen als er geen dossier openstaat, zodat werk niet wordt weggegooid */
setInterval(() => { if (!S.open && document.visibilityState === 'visible') load().catch(() => {}); }, 300000);

load().catch((e) => { $('#runinfo').innerHTML = '<span class="fout">Geen verbinding met de server.</span>'; });
laadBezorgstand();

// ── Bezorging van meldingen ─────────────────────────────────────────────────
// Tot 26-09-2026 mislukte het versturen geruisloos: veertien kansen zijn nooit
// bezorgd omdat er geen webhook stond, en nergens was dat te zien. Deze balk
// maakt dat zichtbaar zodra het weer gebeurt.
async function laadBezorgstand() {
  const balk = document.getElementById('bezorgbalk');
  if (!balk) return;
  try {
    const d = await api('/api/bezorgstand');
    if (!d || !d.gemist) { balk.hidden = true; return; }
    const reden = (d.laatste_fout || '').includes('DISCORD_WEBHOOK_URL')
      ? 'er staat geen Discord-webhook ingesteld'
      : (d.laatste_fout || 'onbekende reden');
    balk.innerHTML =
      `<b>${d.gemist} melding${d.gemist === 1 ? '' : 'en'} niet bezorgd.</b> ` +
      `Reden: ${esc(reden)}. Zet het kanaal goed bij Meer → Instellingen; ` +
      `daarna kun je de gemiste kansen alsnog laten nasturen.`;
    balk.hidden = false;
  } catch (err) {
    balk.hidden = true;   // liever geen balk dan een balk die zelf stuk is
  }
}
