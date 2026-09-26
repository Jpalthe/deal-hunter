/* TREE Deal Hunter — dashboard. Alle tekst uit bronnen wordt ge-escaped voordat hij in de pagina komt. */
(() => {
  "use strict";

  // ---------------------------------------------------------------- helpers
  const $ = (s, el = document) => el.querySelector(s);
  const $$ = (s, el = document) => [...el.querySelectorAll(s)];
  const esc = (v) => String(v ?? "").replace(/[&<>"']/g, (c) => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c]));
  const safeUrl = (u) => (typeof u === "string" && /^https?:\/\//i.test(u) ? u : null);
  const nf = new Intl.NumberFormat("nl-NL", { maximumFractionDigits: 0 });
  const eur = (v) => (v === null || v === undefined || Number.isNaN(v) ? "—" : nf.format(Math.round(v)) + " €");
  const keur = (v) => (v === null || v === undefined ? "—" : v >= 1e6 ? (v / 1e6).toFixed(2).replace(".", ",") + " M" : nf.format(Math.round(v / 1000)) + "k");
  const pct = (v, d = 0) => (v === null || v === undefined ? "—" : (v * 100).toFixed(d).replace(".", ",") + " %");
  const signed = (v) => (v === null || v === undefined ? "—" : (v > 0 ? "+" : v < 0 ? "−" : "") + Math.abs(v * 100).toFixed(0) + " %");
  const m2 = (v) => (v ? nf.format(Math.round(v)) : "—");
  const api = async (path, opts) => {
    const r = await fetch(path, opts);
    if (!r.ok) throw new Error(`${r.status} ${await r.text()}`);
    return r.json();
  };
  const CLASS_ORDER = ["groen", "blauw", "oranje", "grijs", "onzeker", "geen"];
  const CLASS_COLOR = { groen: "#2f7a55", blauw: "#2f6386", oranje: "#b86e12", grijs: "#8c918e", onzeker: "#7d6a9c", geen: "#b9bdb9" };
  const CAT_LABEL = { renovatie: "Renovatie", perceel: "Perceel", "appartement-renovatie": "Appartement", appartement: "Appartement", bijzonder: "Bijzonder", overig: "Overig" };
  const EVENT_LABEL = { NIEUW: "Nieuw", "PRIJS GEWIJZIGD": "Prijs gewijzigd", GEWIJZIGD: "Gewijzigd", "OPNIEUW AANGEBODEN": "Opnieuw aangeboden", "NIET MEER GEVONDEN": "Verdwenen" };

  const state = {
    summary: null, listings: [], auctions: [], zones: [],
    f: { q: "", area: "alle", cat: "alle", cls: new Set(), onlyNew: false, onlyOpen: false, onlyIdeal: false, showLoss: false, alles: false, sort: "room" },
    selected: null, detail: null, overrides: {}, scenarioKey: null,
  };

  // ---------------------------------------------------------------- map
  const map = L.map("map", { zoomControl: true, preferCanvas: false }).setView([38.765, 0.16], 12);
  const ignBase = L.tileLayer(
    "https://www.ign.es/wmts/ign-base?layer=IGNBaseTodo&style=default&tilematrixset=GoogleMapsCompatible&Service=WMTS&Request=GetTile&Version=1.0.0&Format=image/jpeg&TileMatrix={z}&TileCol={x}&TileRow={y}",
    { maxZoom: 19, attribution: "Kaart © IGN España (CC BY 4.0)" }
  ).addTo(map);
  const pnoa = L.tileLayer(
    "https://www.ign.es/wmts/pnoa-ma?layer=OI.OrthoimageCoverage&style=default&tilematrixset=GoogleMapsCompatible&Service=WMTS&Request=GetTile&Version=1.0.0&Format=image/jpeg&TileMatrix={z}&TileCol={x}&TileRow={y}",
    { maxZoom: 20, attribution: "Luchtfoto PNOA © IGN España (CC BY 4.0)" }
  );
  const catastro = L.tileLayer.wms("https://ovc.catastro.meh.es/Cartografia/WMS/ServidorWMS.aspx", {
    layers: "Catastro", format: "image/png", transparent: true, version: "1.1.1", minZoom: 15, maxZoom: 21,
    attribution: "Percelen © Dirección General del Catastro",
  });
  const lyrListings = L.layerGroup().addTo(map);
  const lyrIdeal = L.layerGroup().addTo(map);
  const lyrAuctions = L.layerGroup().addTo(map);
  const lyrZones = L.layerGroup().addTo(map);
  L.control.layers(
    { "Kaart (IGN)": ignBase, "Luchtfoto (PNOA)": pnoa },
    { "Objecten (feed)": lyrListings, "Kandidaten Idealista": lyrIdeal, "Veilingen": lyrAuctions, "Wijkprijzen per m²": lyrZones, "Kadastrale percelen (vanaf zoom 15)": catastro },
    { collapsed: window.innerWidth < 900, position: "topright" }
  ).addTo(map);
  L.control.scale({ imperial: false }).addTo(map);
  const markers = new Map();

  map.on("click", async (e) => {
    if (!map.hasLayer(catastro)) return;
    const pop = L.popup().setLatLng(e.latlng).setContent("Kadastrale referentie opzoeken…").openOn(map);
    try {
      const d = await api(`/api/catastro?lat=${e.latlng.lat.toFixed(6)}&lon=${e.latlng.lng.toFixed(6)}`);
      if (!d.parcels.length) { pop.setContent(`Geen perceel gevonden. ${esc(d.error || "")}`); return; }
      pop.setContent(
        `<b>Kadastrale percelen bij dit punt</b><br>` +
        d.parcels.map((p) => `<span style="font-family:var(--font-mono)">${esc(p.rc)}</span>${p.distance_m ? ` · ${esc(p.distance_m)} m` : ""}<br>${esc(p.address)}<br><a href="${esc(p.sede_url)}" target="_blank" rel="noopener">Open in Sede Catastro</a>`).join("<hr style='border:0;border-top:1px solid #ddd'>") +
        `<br><span class="note">${esc(d.note)}</span>`
      );
    } catch (err) { pop.setContent(`Catastro niet bereikbaar: ${esc(err.message.slice(0, 120))}`); }
  });

  function legend() {
    const labels = state.summary?.class_labels || {};
    $("#legend").innerHTML = CLASS_ORDER.filter((c) => c !== "geen").map((c) => `<div><span class="dot ${c}"></span>${esc(labels[c] || c)}</div>`).join("") +
      `<div><span class="dot veiling"></span>Veiling</div><div><span class="k-label">K07</span>&nbsp;Kandidaat Idealista (pin benaderend)</div>`;
  }

  // ---------------------------------------------------------------- data
  async function loadAll() {
    // De telefoon haalde de vijf tabbladen op, dit scherm alles wat actief is.
    // Daardoor stonden hier 3.757 objecten waaronder goedkope woningen buiten de
    // focus, en verscheen dezelfde woning uit twee bronnen twee keer — de
    // ontdubbeling zit namelijk op het tabblad. Nu halen beide hetzelfde op.
    // Het vinkje "Ook buiten de focus" zet het oude gedrag terug.
    const pad = state.f.alles ? "/api/listings" : "/api/listings?tab=kansen,teduur,later,buiten,onvolledig";
    const [summary, listings, auctions, zones] = await Promise.all([api("/api/summary"), api(pad), api("/api/auctions"), api("/api/zones")]);
    Object.assign(state, { summary, listings, auctions, zones });
    renderTop(); renderFilters(); renderList(); renderMap(); renderAuctions(); renderZones(); legend();
    const busy = Object.keys(state.overrides).length || document.activeElement?.id === "rv-note" || document.activeElement?.type === "range";
    if (state.selected && !$("#drawer").hidden && !busy) openDetail(state.selected, false, true);
  }

  // ---------------------------------------------------------------- top + KPI
  function renderTop() {
    const s = state.summary;
    const last = s.runs.find((r) => r.status) || null;
    const t = (iso) => (iso ? new Date(iso).toLocaleString("nl-NL", { weekday: "short", hour: "2-digit", minute: "2-digit" }) : "—");
    const lastTxt = !last ? "nog geen ronde" : `<b>${esc(t(last.started_at))}</b>${last.status === "ok" ? "" : last.status === "running" ? " · <b>loopt</b>" : " · <b>fout</b>"}`;
    $("#runinfo").innerHTML = `Laatste ronde ${lastTxt} · volgende <b>${esc(t(s.next_run))}</b> · marge-eis <b>${pct(s.kader.margin)}</b> op verkoop`;
    const names = { bp: "BP-feed", boe: "BOE", aeat: "AEAT" };
    $("#sources").innerHTML = s.sources.map((x) => `<span class="src ${x.last_status === "ok" ? "" : "fout"}" title="${esc(x.last_error || "laatst gelukt " + (x.last_success_at || "—"))}">${esc(names[x.key] || x.key)} ${x.last_count ?? ""}</span>`).join("") +
      `<span class="src" title="AI-kosten deze maand">AI ${esc(s.ai_cost_month.toFixed(2).replace(".", ","))} €</span>`;
    const c = s.counts, bc = c.by_class;
    const kpi = (value, label, cls, filt) => `<${filt ? "button" : "div"} class="kpi${filt && state.f.cls.has(filt) && state.f.cls.size === 1 ? " on" : ""}" ${filt ? `data-kpi="${filt}"` : ""}><span class="kpi-value">${cls ? `<span class="dot ${cls}"></span>` : ""}${esc(value)}</span><span class="kpi-label">${esc(label)}</span></${filt ? "button" : "div"}>`;
    $("#kpis").innerHTML = [
      kpi(c.active, `objecten in werkgebied · ${c.idealista} kandidaten Idealista`),
      kpi(bc.groen || 0, "haalt marge, ook voorzichtig", "groen", "groen"),
      kpi(bc.blauw || 0, "haalt marge in basis", "blauw", "blauw"),
      kpi(bc.oranje || 0, "onderhandelbaar tot 30 %", "oranje", "oranje"),
      kpi(c.new_7d, "nieuw in 7 dagen"),
      kpi(c.price_changes_7d, "prijswijzigingen in 7 dagen"),
      kpi(c.auctions_in_area, "veilingen in werkgebied", "veiling"),
      kpi(`${c.reviewed}/${c.active}`, "door jou beoordeeld"),
    ].join("");
    $$("#kpis [data-kpi]").forEach((b) => b.addEventListener("click", () => {
      const k = b.dataset.kpi;
      state.f.cls = state.f.cls.size === 1 && state.f.cls.has(k) ? new Set() : new Set([k]);
      renderTop(); renderFilters(); renderList(); renderMap();
    }));
  }

  // ---------------------------------------------------------------- filters + list
  function renderFilters() {
    const L0 = state.listings;
    const chip = (group, value, label, count, on) => `<button class="chip${on ? " on" : ""}" data-g="${group}" data-v="${esc(value)}">${label}${count !== undefined ? ` <span class="n">${count}</span>` : ""}</button>`;
    const areas = [["alle", "Alle gebieden"], ["javea", "Jávea"], ["benitachell", "Benitachell"], ["moraira", "Moraira"]];
    $("#f-area").innerHTML = areas.map(([v, l]) => chip("area", v, esc(l), v === "alle" ? L0.length : L0.filter((x) => x.area === v).length, state.f.area === v)).join("");
    const cats = [["alle", "Alles"], ["renovatie", "Renovatie"], ["perceel", "Percelen"], ["appartement", "Appartementen"]];
    $("#f-cat").innerHTML = cats.map(([v, l]) => chip("cat", v, esc(l), v === "alle" ? undefined : L0.filter((x) => (x.category || "").startsWith(v)).length, state.f.cat === v)).join("");
    const labels = state.summary.class_labels;
    $("#f-class").innerHTML = CLASS_ORDER.map((c) => chip("cls", c, `<span class="dot ${c}"></span>${esc(labels[c])}`, L0.filter((x) => x.class === c).length, state.f.cls.has(c))).join("");
    $$(".filters .chip").forEach((b) => b.addEventListener("click", () => {
      const { g, v } = b.dataset;
      if (g === "cls") { state.f.cls.has(v) ? state.f.cls.delete(v) : state.f.cls.add(v); }
      else state.f[g] = v;
      renderTop(); renderFilters(); renderList(); renderMap();
    }));
  }

  function filtered() {
    const f = state.f, q = f.q.trim().toLowerCase();
    let items = state.listings.filter((x) =>
      (f.area === "alle" || x.area === f.area) &&
      (f.cat === "alle" || (x.category || "").startsWith(f.cat)) &&
      (!f.cls.size || f.cls.has(x.class)) &&
      (!f.onlyNew || x.events_7d.length) &&
      (!f.onlyOpen || !x.review) &&
      (!f.onlyIdeal || x.source === "idealista") &&
      (f.showLoss || !(x.calc && x.calc.result < 0)) &&
      (!q || [x.ref, x.kandidaat, x.location, x.zone_label, x.area_label, x.type, x.scenario, ...(x.signals || [])].join(" ").toLowerCase().includes(q))
    );
    const rank = (x) => (x.room ?? -9) - (x.reliable === false ? 100 : 0);   // onbetrouwbare uitkomsten onderaan
    if (f.sort === "room") items.sort((a, b) => rank(b) - rank(a) || (a.price || 0) - (b.price || 0));
    if (f.sort === "price") items.sort((a, b) => (a.price || 0) - (b.price || 0));
    if (f.sort === "new") items.sort((a, b) => String(b.first_seen).localeCompare(String(a.first_seen)));
    return items;
  }

  function sumBlock(x) {
    const c = x.calc;
    if (!c) return "";
    const m2s = x.result_m2 ? nf.format(x.result_m2) + " m²" : "";
    return `<div class="sum">
      <div><span>Aankoop + kosten</span><b>${keur(c.acquisition)}</b></div>
      <div><span>Bouw ${esc(m2s)}</span><b>${keur(c.build)}</b></div>
      <div><span>Verkoop ${esc(m2s)} × ${nf.format(c.eur_m2_sale)}</span><b>${keur(c.sale)}</b></div>
      <div><span>Resultaat</span><b class="${c.result >= 0 ? "pos" : "neg"}">${c.result >= 0 ? "+" : "−"}${keur(Math.abs(c.result))}</b></div>
    </div><p class="sumline">marge ${pct(c.margin)} · rendement op kosten ${pct(c.roi_on_costs)} · ${esc(c.months)} mnd · basisscenario bij vraagprijs</p>`;
  }

  function card(x) {
    const mp = x.max_price;
    const ev = x.events_7d.map((e) => `<span class="badge ${e === "NIEUW" ? "groen" : e === "PRIJS GEWIJZIGD" ? "oranje" : ""}">${esc(EVENT_LABEL[e] || e)}</span>`).join("");
    const rv = x.review ? `<span class="badge ${x.review.verdict === "interessant" ? "groen" : x.review.verdict === "afwijzen" ? "bad" : "oranje"}">${esc(x.review.verdict)}</span>` : "";
    return `<button class="card${state.selected === x.id ? " sel" : ""}" data-id="${x.id}">
      <div class="card-top"><span class="dot ${x.class}" title="${esc(x.class_label)}"></span><span class="card-ref">${esc(x.kandidaat ? x.kandidaat + " · " : "")}${esc(x.ref)}</span>
        ${x.source === "idealista" ? '<span class="badge src-ideal">Idealista</span>' : ""}<span class="card-where">${esc(x.zone_label || x.area_label)}</span></div>
      <div class="card-main"><span class="card-price">${eur(x.price)}</span><span class="card-m2">${m2(x.built_m2)} m² · perceel ${m2(x.plot_m2)} m² · ${esc(CAT_LABEL[x.category] || x.category || "")}</span></div>
      ${mp ? `<p class="triple-cap">Maximale koopprijs bij ${pct(state.summary.kader.margin)} marge</p><div class="triple"><div><span>Voorzichtig</span><b>${keur(mp.conservative)}</b></div><div><span>Basis</span><b>${keur(mp.base)}</b></div><div><span>Gunstig</span><b>${keur(mp.upside)}</b></div></div>${sumBlock(x)}` : `<div class="note">${esc(x.reason || "Geen indicatie")}</div>`}
      <div class="badges"><span class="badge ${x.class}">${x.room !== null && x.room !== undefined ? "Ruimte " + signed(x.room) : esc(x.class_label)}</span>${x.reliable === false ? '<span class="badge onzeker">onzeker</span>' : ""}${ev}${rv}</div>
    </button>`;
  }

  function renderList() {
    const items = filtered();
    const loss = state.listings.filter((x) => x.calc && x.calc.result < 0).length;
    $("#listmeta").textContent = `${items.length} van ${state.listings.length} objecten · maximale koopprijs voorzichtig / basis / gunstig bij ${pct(state.summary.kader.margin)} marge`
      + (!state.f.showLoss && loss ? ` · ${loss} met verlies verborgen` : "");
    $("#cards").innerHTML = items.length ? items.map(card).join("") : `<div class="empty">Geen objecten met deze filters.</div>`;
    $$("#cards .card").forEach((b) => b.addEventListener("click", () => openDetail(Number(b.dataset.id), true)));
  }

  // ---------------------------------------------------------------- map render
  function renderMap() {
    lyrListings.clearLayers(); lyrIdeal.clearLayers(); lyrAuctions.clearLayers(); lyrZones.clearLayers(); markers.clear();
    const ids = new Set(filtered().map((x) => x.id));
    for (const x of state.listings) {
      if (x.lat == null || x.lon == null || !ids.has(x.id)) continue;
      const color = CLASS_COLOR[x.class];
      const sel = state.selected === x.id;
      const mk = L.circleMarker([x.lat, x.lon], {
        radius: x.source === "idealista" ? 9 : 7, color: x.source === "idealista" ? "#1c2220" : "#fff", weight: sel ? 4 : 2,
        fillColor: color, fillOpacity: x.class === "geen" ? 0.35 : 0.9, dashArray: x.class === "onzeker" ? "3 2" : null,
      });
      mk.bindTooltip(`<b>${esc(x.kandidaat || x.ref)}</b> · ${eur(x.price)}<br>${esc(x.class_label)}${x.max_price ? `<br>basis ${keur(x.max_price.base)}` : ""}`, { direction: "top" });
      mk.on("click", () => openDetail(x.id, false));
      (x.source === "idealista" ? lyrIdeal : lyrListings).addLayer(mk);
      if (x.kandidaat) lyrIdeal.addLayer(L.marker([x.lat, x.lon], { icon: L.divIcon({ className: "", html: `<span class="k-label">${esc(x.kandidaat)}</span>`, iconAnchor: [-8, 18] }), interactive: false }));
      markers.set(x.id, mk);
    }
    for (const a of state.auctions) {
      if (a.lat == null) continue;
      const mk = L.marker([a.lat, a.lon], { icon: L.divIcon({ className: "", html: '<div class="auction-icon"></div>', iconSize: [14, 14] }) });
      mk.bindPopup(`<b>Veiling ${esc(a.sub)}</b><br>${esc(a.town || "")} · taxatie ${eur(a.valuation)}<br>sluit ${esc(a.end_date || "—")}<br>${a.blockers.map(esc).join("<br>")}${safeUrl(a.url) ? `<br><a href="${esc(a.url)}" target="_blank" rel="noopener">Portaal</a>` : ""}`);
      lyrAuctions.addLayer(mk);
    }
    renderZoneLabels();
  }

  function renderZoneLabels() {
    lyrZones.clearLayers();
    const compact = map.getZoom() < 13;
    for (const z of state.zones) {
      const vr = z.villa_renovated?.median, vn = z.villa_new?.median;
      const html = compact
        ? `<div class="zone-label compact"><b>${esc(z.label)}</b> ${vr ? nf.format(vr) : "—"}</div>`
        : `<div class="zone-label"><b>${esc(z.label)}</b><br><span>gerenoveerd</span> ${vr ? nf.format(vr) : "—"} · <span>nieuw</span> ${vn ? nf.format(vn) : "—"} €/m²</div>`;
      lyrZones.addLayer(L.marker([z.lat, z.lon], { icon: L.divIcon({ className: "", html, iconAnchor: compact ? [30, -10] : [60, -12] }), interactive: false }));
    }
  }
  map.on("zoomend", () => { if (state.zones.length) renderZoneLabels(); });

  // ---------------------------------------------------------------- detail drawer
  let wiTimer = null, wiSeq = 0, detailSeq = 0;

  async function openDetail(id, fly, keep) {
    clearTimeout(wiTimer); wiSeq++;
    const my = ++detailSeq;
    state.selected = id;
    renderList();
    $("#drawer").hidden = false; $(".mapwrap").classList.add("drawer-open");
    if (!keep) $("#drawer-body").innerHTML = `<div class="dz"><div class="note">Dossier laden…</div></div>`;
    let d;
    try { d = await api(`/api/listing/${id}`); }
    catch (e) { if (my === detailSeq) $("#drawer-body").innerHTML = `<div class="dz"><div class="warnbox">Dossier kon niet laden: ${esc(e.message.slice(0, 160))}</div></div>`; return; }
    if (my !== detailSeq) return;                       // intussen een ander object geopend
    const prevScenario = keep ? state.scenarioKey : null;
    state.detail = d;
    if (!keep) { state.overrides = {}; }
    state.scenarioKey = prevScenario && (d.feasibility?.scenarios || []).some((x) => x.key === prevScenario) ? prevScenario : (d.feasibility?.best_key || null);
    state.lastFeas = d.feasibility;
    renderMap();
    if (fly && d.lat != null) map.flyTo([d.lat, d.lon], Math.max(map.getZoom(), 15), { duration: 0.6 });
    renderDetail();
    if (keep && Object.keys(state.overrides).length) whatIf();
  }

  function scaleBar(price, mp) {
    const vals = [price, mp.conservative, mp.base, mp.upside].filter((v) => v !== null && v !== undefined);
    const max = Math.max(...vals) * 1.08 || 1;
    const x = (v) => Math.max(0, Math.min(100, (v / max) * 100));
    return `<div class="scale">
      <div class="scale-track"></div>
      <div class="scale-band" style="left:${x(mp.conservative)}%;width:${Math.max(x(mp.upside) - x(mp.conservative), 0.5)}%"></div>
      <div class="scale-mark" style="left:${x(mp.base)}%"></div>
      <div class="scale-ask" style="left:${x(price)}%"></div>
      <span class="scale-lbl ask" style="left:${x(price)}%">${state.overrides.price !== undefined ? "koopprijs" : "vraagprijs"}</span>
      <span class="scale-lbl" style="left:${x(mp.conservative)}%">${keur(mp.conservative)}</span>
      <span class="scale-lbl" style="left:${x(mp.base)}%">${keur(mp.base)}</span>
      <span class="scale-lbl" style="left:${x(mp.upside)}%">${keur(mp.upside)}</span>
    </div>`;
  }

  function sparkline(hist) {
    if (!hist || hist.length < 2) return `<div class="note">${hist && hist.length ? "Eén prijs gezien: " + eur(hist[0][1]) + " sinds " + esc(String(hist[0][0]).slice(0, 10)) : "Geen prijshistorie."}</div>`;
    const ps = hist.map((h) => h[1]); const lo = Math.min(...ps), hi = Math.max(...ps); const W = 300, H = 44;
    const pts = hist.map((h, i) => [(i / (hist.length - 1)) * (W - 8) + 4, hi === lo ? H / 2 : H - 6 - ((h[1] - lo) / (hi - lo)) * (H - 12)]);
    return `<svg class="spark" viewBox="0 0 ${W} ${H}" role="img" aria-label="Prijsverloop"><polyline fill="none" stroke="#1c2220" stroke-width="1.5" points="${pts.map((p) => p.join(",")).join(" ")}"/>${pts.map((p) => `<circle cx="${p[0]}" cy="${p[1]}" r="2.5" fill="#b8a07a"/>`).join("")}</svg>
      <div class="note">${hist.map((h) => `${eur(h[1])} (${esc(String(h[0]).slice(0, 10))})`).join(" → ")}</div>`;
  }

  function currentScenario(feas) {
    const scen = (feas?.scenarios || []).filter((x) => x.available);
    return { scen, cur: scen.find((x) => x.key === state.scenarioKey) || scen[0] || null };
  }

  function baseScenario(key) {
    return (state.detail?.feasibility?.scenarios || []).find((x) => x.key === key) || null;
  }

  // Volledige opbouw van het dossier: kop, object, schuiven en lege resultaatcontainers.
  function renderDetail() {
    const d = state.detail, s = state.summary, feas = state.lastFeas;
    const { scen, cur } = currentScenario(feas);
    const head = `<div class="dz-head">
      <div class="eyebrow"><span>${esc(d.kandidaat ? d.kandidaat + " · " : "")}${esc(d.source === "idealista" ? "Idealista " : "BP ")}${esc(d.ref)}</span><span>${esc(d.area_label)}${d.zone_label ? " · " + esc(d.zone_label) : ""}</span><span>${esc(d.type || "")}</span></div>
      <h2>${eur(d.price)} · ${esc(CAT_LABEL[d.category] || d.category || "")} ${d.location ? "in " + esc(d.location) : ""}</h2>
      <div class="badges"><span class="badge ${d.class}">${esc(d.class_label)}</span>${d.events_7d.map((e) => `<span class="badge">${esc(EVENT_LABEL[e] || e)}</span>`).join("")}
      ${safeUrl(d.url) ? `<a class="badge" href="${esc(d.url)}" target="_blank" rel="noopener">bronadvertentie ↗</a>` : ""}</div></div>`;
    const facts = `<div class="block"><h3>Object</h3><div class="stats">
      <div class="stat"><span>Vraagprijs</span><b>${eur(d.price)}</b></div>
      <div class="stat"><span>Gebouwd</span><b>${m2(d.built_m2)} m²</b>${d.built_m2 && d.price ? `<small>${nf.format(Math.round(d.price / d.built_m2))} €/m²</small>` : ""}</div>
      <div class="stat"><span>Perceel</span><b>${m2(d.plot_m2)} m²</b>${d.plot_m2 && d.price && !d.built_m2 ? `<small>${nf.format(Math.round(d.price / d.plot_m2))} €/m²</small>` : ""}</div>
    </div>${d.kandidaat_info?.pin_note ? `<p class="note">${esc(d.kandidaat_info.pin_note)}</p>` : ""}</div>`;

    if (!cur) {
      $("#drawer-body").innerHTML = `<div class="dz">${head}${facts}<div class="warnbox">${esc(feas?.reason || "Geen haalbaarheid te berekenen.")}</div><div id="res-extra">${extraBlocks(d)}</div></div>`;
      bindReview(d); return;
    }
    const a = s.kader, ov = state.overrides;
    const val = (k, dflt) => (ov[k] !== undefined ? ov[k] : dflt);
    const base = baseScenario(cur.key) || cur;
    const baseM2 = base.base_result_m2 || base.result_m2;
    const tabs = scen.length > 1 ? `<div class="scen-tabs">${scen.map((x) => `<button class="chip${x.key === cur.key ? " on" : ""}" data-scen="${esc(x.key)}">${esc(x.label)}</button>`).join("")}</div>` : `<p class="note" style="margin:0 0 .5rem">${esc(cur.label)}</p>`;

    const fmts = {};
    const sl = (key, label, min, max, step, value, fmt) => { fmts[key] = fmt; const v = Math.min(max, Math.max(min, value)); return `<label class="slider"><span>${label}</span><input type="range" data-ov="${key}" min="${min}" max="${max}" step="${step}" value="${v}"><output>${fmt(v)}</output></label>`; };
    const priceMin = Math.max(1000, Math.round((d.price || 100000) * 0.4 / 1000) * 1000), priceMax = Math.round((d.price || 100000) * 1.2 / 1000) * 1000;
    const m2Min = Math.max(20, Math.round(baseM2 * 0.5)), m2Max = Math.min(5000, Math.max(m2Min + 10, Math.round(baseM2 * 1.6)));
    const sliders = `<div class="block"><h3><span>Wat als</span><span id="wi-status">live herberekend</span></h3><div class="sliders">
      ${sl("margin", "Marge-eis op verkoop", 0.05, 0.4, 0.01, val("margin", a.margin), (v) => pct(+v))}
      ${sl("price", "Koopprijs", priceMin, priceMax, 1000, val("price", d.price), (v) => keur(+v))}
      ${sl("sale_adj", "Verkoopprijs wijk", -0.3, 0.3, 0.01, val("sale_adj", 0), (v) => signed(+v))}
      ${cur.kind === "nieuwbouw" ? "" : sl("reno_rate", "Renovatie €/m²", 400, 2200, 50, val("reno_rate", a.reno_rate), (v) => nf.format(+v))}
      ${sl("new_rate", cur.kind === "nieuwbouw" ? "Nieuwbouw €/m²" : "Uitbreiding €/m²", 1200, 3500, 50, val("new_rate", a.new_rate), (v) => nf.format(+v))}
      ${sl("fees_pct", "Honoraria", 0, 0.2, 0.005, val("fees_pct", a.fees_pct), (v) => pct(+v, 1))}
      ${sl("commission_pct", "Courtage verkoop", 0, 0.07, 0.005, val("commission_pct", a.commission_pct), (v) => pct(+v, 1))}
      ${sl("result_m2", "Verkoopbaar m²", m2Min, m2Max, 5, val("result_m2", cur.result_m2), (v) => nf.format(+v) + " m²")}
    </div><div class="slider-actions"><span>${cur.kind === "nieuwbouw" ? "Meer m² betekent meer nieuwbouw." : "Boven het bestaande oppervlak rekent het model uitbreiding tegen het uitbreidingstarief."}</span><button class="btn" id="reset-ov">Terug naar kader</button></div></div>`;

    $("#drawer-body").innerHTML = `<div class="dz">${head}${facts}<div id="res-max"></div>${sliders}<div id="res-costs"></div><div id="res-comps"></div><div id="res-extra">${extraBlocks(d)}</div></div>`;
    $("#res-max").dataset.tabs = "1";
    renderResults(feas, tabs);

    $$("#drawer-body input[type=range]").forEach((inp) => inp.addEventListener("input", () => {
      const k = inp.dataset.ov; state.overrides[k] = Number(inp.value);
      inp.nextElementSibling.textContent = fmts[k] ? fmts[k](Number(inp.value)) : inp.value;
      clearTimeout(wiTimer); wiTimer = setTimeout(whatIf, 220);
    }));
    $("#reset-ov")?.addEventListener("click", () => { state.overrides = {}; state.lastFeas = state.detail.feasibility; renderDetail(); });
    bindReview(d);
  }

  // Alleen de resultaatblokken; de schuiven blijven staan zodat slepen niet wordt onderbroken.
  function renderResults(feas, tabsHtml) {
    const d = state.detail;
    const { scen, cur } = currentScenario(feas);
    if (!cur) return;
    const mp = cur.max_price, mg = cur.margin_at_asking, ov = state.overrides;
    const at = ov.price !== undefined ? `bij koopprijs ${keur(ov.price)}` : "bij vraagprijs";
    const mpClass = (m) => (m >= feas.margin_required ? "pos" : "neg");
    const tabs = tabsHtml ?? (scen.length > 1 ? `<div class="scen-tabs">${scen.map((x) => `<button class="chip${x.key === cur.key ? " on" : ""}" data-scen="${esc(x.key)}">${esc(x.label)}</button>`).join("")}</div>` : `<p class="note" style="margin:0 0 .5rem">${esc(cur.label)}</p>`);
    const warn = cur.warnings.length ? `<div class="warnbox">${cur.warnings.map(esc).join("<br>")}</div>` : "";
    const build = cur.kind === "nieuwbouw" ? `${nf.format(cur.newbuild_m2)} m² nieuwbouw` : `${nf.format(cur.renovation_m2)} m² renovatie${cur.newbuild_m2 ? " + " + nf.format(cur.newbuild_m2) + " m² uitbreiding" : ""}`;
    $("#res-max").innerHTML = `<div class="block"><h3><span>Maximale koopprijs bij ${pct(feas.margin_required)} marge</span><span>${esc(cur.months)} mnd · ${esc(build)}</span></h3>${tabs}
      <div class="stats">
        <div class="stat"><span>Voorzichtig</span><b>${eur(mp.conservative)}</b><small>verkoop ${keur(cur.sale.conservative)}</small></div>
        <div class="stat hl"><span>Basis</span><b>${eur(mp.base)}</b><small>verkoop ${keur(cur.sale.base)}</small></div>
        <div class="stat"><span>Gunstig</span><b>${eur(mp.upside)}</b><small>verkoop ${keur(cur.sale.upside)}</small></div>
      </div>${scaleBar(feas.price, mp)}
      <div class="stats" style="margin-top:.6rem">
        <div class="stat"><span>Marge ${esc(at)}, voorzichtig</span><b class="${mpClass(mg.conservative)}">${pct(mg.conservative)}</b></div>
        <div class="stat"><span>Basis</span><b class="${mpClass(mg.base)}">${pct(mg.base)}</b></div>
        <div class="stat"><span>Gunstig</span><b class="${mpClass(mg.upside)}">${pct(mg.upside)}</b></div>
      </div>
      ${cur.sum ? `<p class="sumline" style="margin-top:.5rem">Rekening bij ${esc(at)} (basis): aankoop en kosten ${eur(cur.sum.acquisition)} + bouw ${eur(cur.sum.build)} + overige ${eur(cur.sum.other)} = <b>${eur(cur.sum.total_costs)}</b>; verkoop ${nf.format(cur.result_m2)} m² × ${nf.format(cur.sum.eur_m2_sale)} €/m² = <b>${eur(cur.sum.sale)}</b>; resultaat <b class="${cur.sum.result >= 0 ? "pos" : "neg"}">${eur(cur.sum.result)}</b> · marge ${pct(cur.sum.margin)} · rendement op kosten ${pct(cur.sum.roi_on_costs)}. Bouw komt neer op ${nf.format(cur.sum.eur_m2_build)} €/m² inclusief honoraria, leges, reserve en niet-terugvorderbare btw.</p>` : ""}
      <p class="note">Onderhandelingsruimte ten opzichte van de vraagprijs (basis): <b>${d.price ? signed(mp.base / d.price - 1) : "—"}</b>. Verkoop = vraagprijs per m² van gerenoveerde of nieuwe woningen in de wijk: voorzichtig p25, basis mediaan, gunstig p75 (n=${esc(cur.comps.n)}). Vraagprijzen, geen transacties.</p>${warn}</div>`;

    const bmax = Math.max(...cur.breakdown.map((b) => b.eur), cur.sale.base, 1);
    $("#res-costs").innerHTML = `<div class="block"><h3><span>Kostenopbouw ${esc(at)} (basis)</span><span>excl. terugvorderbare btw</span></h3><div class="costs">
      ${cur.breakdown.map((b) => `<div class="cost"><span>${esc(b.label)}</span><div class="cost-bar${b.label === "Koopprijs" ? " buy" : ""}" style="width:${Math.max((b.eur / bmax) * 100, 0.8)}%"></div><b>${eur(b.eur)}</b></div>`).join("")}
      <div class="cost total"><span>Totale kosten</span><span></span><b>${eur(cur.total_costs_base)}</b></div>
      <div class="cost"><span>Verkoop basis</span><div class="cost-bar" style="background:#2f6386;width:${(cur.sale.base / bmax) * 100}%"></div><b>${eur(cur.sale.base)}</b></div>
      <div class="cost total"><span>Resultaat</span><span></span><b class="${mpClass(mg.base)}">${eur(cur.result_at_asking.base)}</b></div>
    </div></div>`;

    const comp = d.comps?.[cur.comps.series];
    $("#res-comps").innerHTML = comp ? `<div class="block"><h3><span>Wijkprijzen: ${esc(comp.zone)}</span><span>${esc((comp.verification || "").split(":")[0])}</span></h3>
      <div class="stats"><div class="stat"><span>p25</span><b>${nf.format(comp.p25 || 0)}</b><small>€/m²</small></div><div class="stat"><span>Mediaan</span><b>${nf.format(comp.median || 0)}</b><small>€/m² · n=${esc(comp.n)}</small></div><div class="stat"><span>p75</span><b>${nf.format(comp.p75 || 0)}</b><small>€/m²</small></div></div>
      ${comp.examples?.length ? `<table class="mini" style="margin-top:.6rem"><thead><tr><th>Voorbeeld</th><th class="num">Prijs</th><th class="num">m²</th><th class="num">€/m²</th></tr></thead><tbody>${comp.examples.map((e) => `<tr><td><a href="https://www.idealista.com/es/inmueble/${encodeURIComponent(e.code)}/" target="_blank" rel="noopener">${esc(e.code)}</a><br><span class="note">${esc((e.label || "").slice(0, 90))}</span></td><td class="num">${keur(e.price)}</td><td class="num">${m2(e.m2)}</td><td class="num">${e.eur_m2 ? nf.format(e.eur_m2) : "—"}</td></tr>`).join("")}</tbody></table>` : ""}</div>` : "";

    $$("#res-max [data-scen]").forEach((b) => b.addEventListener("click", () => {
      if (b.dataset.scen === state.scenarioKey) return;
      state.scenarioKey = b.dataset.scen;
      delete state.overrides.result_m2;                 // m² hoort bij één scenario
      renderDetail();
      if (Object.keys(state.overrides).length) whatIf();
    }));
  }

  async function whatIf() {
    const d = state.detail, my = ++wiSeq;
    const status = $("#wi-status");
    if (status) status.textContent = "rekenen…";
    try {
      const feas = await api(`/api/listing/${d.id}/wat-als`, { method: "POST", headers: { "Content-Type": "application/json" }, body: JSON.stringify({ ...state.overrides, scenario_key: state.scenarioKey }) });
      if (my !== wiSeq || state.detail !== d) return;   // verouderd antwoord of ander dossier
      state.lastFeas = feas;
      renderResults(feas);
      const st = $("#wi-status"); if (st) st.textContent = "live herberekend";
    } catch (e) {
      if (my !== wiSeq || state.detail !== d) return;
      const st = $("#wi-status"); if (st) st.textContent = "berekening mislukt: " + e.message.slice(0, 80);
    }
  }

  function extraBlocks(d) {
    const sig = d.signals_full || {};
    const claims = d.kandidaat_info?.claims || [...(sig.licence_claims || []), ...(sig.extension_claims || [])];
    const blockers = d.kandidaat_info?.blockers || d.blockers || [];
    const signals = [...(sig.renovation_signals || []), ...(sig.plot_signals || []).slice(0, 2), ...(sig.special_signals || [])];
    const rv = d.reviews?.[0];
    return `
      ${blockers.length ? `<div class="block"><h3>Blokkades en open punten</h3><ul class="plain">${blockers.map((b) => `<li>${esc(b)}</li>`).join("")}</ul></div>` : ""}
      <div class="block"><h3>Signalen en claims van de aanbieder</h3>
        ${signals.length ? `<p class="note" style="margin:0 0 .3rem">Signalen: ${signals.map(esc).join(", ")}</p>` : ""}
        ${claims.length ? `<ul class="plain">${claims.map((c) => `<li>${esc(c)}</li>`).join("")}</ul>` : `<p class="note" style="margin:0">Geen claims herkend.</p>`}
        ${d.desc ? `<p class="note" style="margin:.5rem 0 0">${esc(d.desc.slice(0, 500))}</p>` : ""}</div>
      <div class="block"><h3>Prijsverloop</h3>${sparkline(d.price_history)}</div>
      <div class="block"><h3><span>Jouw oordeel</span><span>${rv ? esc(rv.verdict + " · " + String(rv.at).slice(0, 16).replace("T", " ")) : "nog niet beoordeeld"}</span></h3>
        <div class="review-row"><button class="btn good" data-rv="interessant">Interessant</button><button class="btn warn" data-rv="watchlist">Watchlist</button><button class="btn bad" data-rv="afwijzen">Afwijzen</button>
        <input id="rv-note" placeholder="Reden, kort" value="${esc(rv?.note || "")}"></div>
        <p class="note" id="rv-status">Oordelen worden opgeslagen met datum; het systeem leert ervan. Er gaat niets naar buiten.</p></div>`;
  }

  function bindReview(d) {
    $$("#drawer-body [data-rv]").forEach((b) => b.addEventListener("click", async () => {
      const note = $("#rv-note").value;
      try {
        await api("/api/review", { method: "POST", headers: { "Content-Type": "application/json" }, body: JSON.stringify({ listing_id: d.id, verdict: b.dataset.rv, note }) });
      } catch (e) { const st = $("#rv-status"); if (st) st.textContent = "Opslaan mislukt: " + e.message.slice(0, 100); return; }
      if (state.detail !== d) return;
      const x = state.listings.find((l) => l.id === d.id); if (x) x.review = { verdict: b.dataset.rv, note };
      d.reviews = [{ verdict: b.dataset.rv, note, at: new Date().toISOString() }, ...(d.reviews || [])];
      state.summary.counts.reviewed = state.listings.filter((l) => l.review).length;
      renderList(); renderTop();
      $("#res-extra").innerHTML = extraBlocks(d); bindReview(d);
    }));
  }

  // ---------------------------------------------------------------- other tabs
  function renderAuctions() {
    const rows = state.auctions;
    const days = (s) => { if (!s) return null; const t = new Date(s + "T18:00:00"); return Math.ceil((t - new Date()) / 864e5); };
    $("#auctions").innerHTML = `<div class="list-simple">${rows.length ? rows.map((a) => {
      const dd = days(a.end_date);
      return `<div class="card" style="cursor:default"><div class="card-top"><span class="dot veiling"></span><span class="card-ref">${esc(a.sub)}</span><span class="badge veiling">${esc(a.source)}</span><span class="card-where">${esc(a.town || "ligging onbekend")}</span></div>
        <div class="card-main"><span class="card-price">${eur(a.valuation)}</span><span class="card-m2">${a.end_date ? "sluit " + esc(a.end_date) + (dd !== null ? ` · ${dd} dagen` : "") : "sluitdatum onbekend"}</span></div>
        <div class="note">${esc(a.title || "")}</div>
        <div class="badges">${a.area ? '<span class="badge groen">in werkgebied</span>' : '<span class="badge">buiten werkgebied</span>'}${a.blockers.map((b) => `<span class="badge bad">${esc(b)}</span>`).join("")}</div>
        ${safeUrl(a.url) ? `<a href="${esc(a.url)}" target="_blank" rel="noopener" class="note">Open op het veilingportaal ↗</a>` : ""}</div>`;
    }).join("") : '<div class="empty">Geen lopende veilingen in Alicante met bekende ligging.</div>'}
    <p class="note">AEAT-lijst onder CC BY 4.0. BOE-aankondigingen noemen de ligging niet; bevestiging gaat handmatig via het portaal. Bieden, storten en registreren gebeurt nooit vanuit dit systeem.</p></div>`;
  }

  function renderZones() {
    const cell = (s) => (s ? `${nf.format(s.median)}<br><span class="note">n=${esc(s.n)}</span>` : "—");
    $("#zones").innerHTML = `<div class="list-simple"><table class="mini"><thead><tr><th>Wijk</th><th class="num">Gerenoveerd</th><th class="num">Nieuwbouw</th><th class="num">Appartement</th></tr></thead><tbody>
      ${state.zones.map((z) => `<tr data-z="${esc(z.zone)}" style="cursor:pointer"><td><b>${esc(z.label)}</b></td><td class="num">${cell(z.villa_renovated)}</td><td class="num">${cell(z.villa_new)}</td><td class="num">${cell(z.apartment_renovated)}</td></tr>`).join("")}
      </tbody></table><p class="note">Mediaan vraagprijs per m² gebouwd, 15 september 2026, na controle. Klik om naar de wijk te gaan.</p></div>`;
    $$("#zones tr[data-z]").forEach((tr) => tr.addEventListener("click", () => { const z = state.zones.find((x) => x.zone === tr.dataset.z); if (z) map.flyTo([z.lat, z.lon], 14); }));
  }

  async function renderReports() {
    const r = await api("/api/reports");
    $("#reports").innerHTML = `<div class="list-simple">
      ${r.haalbaarheid ? `<a class="card" href="/rapporten/haalbaarheid.html" target="_blank" rel="noopener"><div class="card-top"><span class="card-ref">Haalbaarheid Jávea</span><span class="card-where">rapport</span></div><div class="note">Doorrekening van de veertien kandidaten en de wijkprijzen.</div></a>` : ""}
      ${r.daily.map((f) => `<a class="card" href="/rapporten/${encodeURIComponent(f)}" target="_blank" rel="noopener"><div class="card-top"><span class="card-ref">${esc(f.replace(".html", ""))}</span><span class="card-where">dagrapport</span></div></a>`).join("")}</div>`;
  }

  // ---------------------------------------------------------------- wiring
  $$(".tab").forEach((t) => t.addEventListener("click", () => {
    $$(".tab").forEach((x) => x.classList.toggle("active", x === t));
    $$(".tabpanel").forEach((p) => (p.hidden = p.dataset.panel !== t.dataset.tab));
    if (t.dataset.tab === "rapporten") renderReports();
  }));
  $("#q").addEventListener("input", (e) => { state.f.q = e.target.value; renderList(); renderMap(); });
  $("#f-new").addEventListener("change", (e) => { state.f.onlyNew = e.target.checked; renderList(); renderMap(); });
  $("#f-open").addEventListener("change", (e) => { state.f.onlyOpen = e.target.checked; renderList(); renderMap(); });
  $("#f-ideal").addEventListener("change", (e) => { state.f.onlyIdeal = e.target.checked; renderList(); renderMap(); });
  $("#f-loss").addEventListener("change", (e) => { state.f.showLoss = e.target.checked; renderList(); renderMap(); });
  // Dit vinkje haalt een ándere verzameling op, dus het is een herlaadactie en
  // geen filter. Daarom loadAll en niet renderList.
  $("#f-alles").addEventListener("change", (e) => { state.f.alles = e.target.checked; loadAll(); });
  $("#sort").addEventListener("change", (e) => { state.f.sort = e.target.value; renderList(); });
  $("#drawer-close").addEventListener("click", () => { clearTimeout(wiTimer); wiSeq++; detailSeq++; state.detail = null; state.overrides = {}; $("#drawer").hidden = true; $(".mapwrap").classList.remove("drawer-open"); state.selected = null; renderList(); renderMap(); });
  document.addEventListener("keydown", (e) => { if (e.key === "Escape" && !$("#drawer").hidden) $("#drawer-close").click(); });
  // Kleine schermen: schakelen tussen lijst en kaart
  document.body.classList.add("view-lijst");
  $$(".vs").forEach((b) => b.addEventListener("click", () => {
    $$(".vs").forEach((x) => { const on = x === b; x.classList.toggle("on", on); x.setAttribute("aria-selected", String(on)); });
    document.body.classList.toggle("view-kaart", b.dataset.view === "kaart");
    document.body.classList.toggle("view-lijst", b.dataset.view === "lijst");
    if (b.dataset.view === "kaart") setTimeout(() => map.invalidateSize(), 60);
  }));
  const showMapOnMobile = () => { if (window.innerWidth <= 900) { $('.vs[data-view="kaart"]').click(); } };
  if (location.hash === "#rapporten") $('.tab[data-tab="rapporten"]').click();

  loadAll().catch((e) => { $("#runinfo").textContent = "Dashboard kon niet laden: " + e.message; });
  setInterval(() => loadAll().catch(() => {}), 5 * 60 * 1000);
})();
