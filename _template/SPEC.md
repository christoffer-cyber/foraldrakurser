# Bygg-spec: en föräldrakurs (slide-innehåll)

Du författar **en** kurs i samma format som de befintliga. Du skriver INTE CSS, `<head>`,
navigation eller `<script>` — bara slide-innehållet. En förälder-vänlig, lugn, icke-dömande
svensk kurs. Allt är **utkast som granskas av barnmorska** — påstå aldrig något som verifierad
fakta; lägg `Marie: ...`-noteringar där rutiner/siffror varierar.

## Läs först (obligatoriskt)
- `~/Projects/foraldrakurser/amning/index.html` — den KANONISKA förlagan. Härma dess markup-mönster exakt.

## Filer du skriver (under din kursmapp `~/Projects/foraldrakurser/<slug>/`)
1. `<slug>/_hero.html` — hero-sliden:
   ```
   <section class="slide hero">
     <div class="col-text pad"><div class="inner">
       <div class="eyebrow">KURSNAMN</div>
       <h1>Kort<br>titel</h1>
       <div class="sub">En lugn rad om kursen</div>
       <div class="names"><span class="for">För</span><span class="who">Felicia &amp; Joakim</span><span class="leader">Tillsammans med Marie</span></div>
     </div></div>
     <div class="col-media"><img src="images/cover.png" alt="..."></div>
   </section>
   ```
2. `<slug>/_slides.html` — alla övriga slides i ordning (ren HTML, inga wrappers runt om).
3. `~/Projects/foraldrakurser/narration/<slug>.sv.json` — `{"1":"...","2":"...",...}` — en **talad** version (2–4 meningar, naturligt tal) per slide, inklusive hero=1. Lika många nycklar som antal slides.
4. `<slug>/_images.json` — `[{"name":"cover","prompt":"<engelsk bildprompt>"}, ...]` — **cover obligatorisk**, max 3 bilder totalt.

## Hårda regler
- **INGA EMOJIS.** Använd linje-SVG (se nedan), numrerade cirklar, eller färgprickar — som i amning.
- **Variera layouten.** Max ~3 rena punktlist-slides. Använd mixen nedan så det inte blir enformigt.
- Använd **bara befintliga CSS-klasser** (nedan). Hitta inte på nya klasser.
- ~12–14 slides totalt (inkl hero + avslutning). Sista sliden = `closing` (se amning slide 15).
- Bilder: `src="images/<name>.png"`. Cover används i hero. Interiör-split-bilder valfritt, håll totalen ≤3.
- Svenska, andra person ("du/ni"), varmt och tryggt. Matcha amnings ton.

## Tillgängliga layout-block (kopiera mönstren från amning/index.html)
- `layout-split` (text + bild): text-kolumn med `eyebrow`,`h2`,`lead`,`ul.clean`,`note`,(ev `partner`-kort) + `col-media` bild.
- `layout-default` med `ul.clean` (punktlista) — använd sparsamt.
- **stats** (ikon-statkort, 3–4 st): `.stats > .stat > .ic(svg)+b+span`.
- **cards / problem→lösning** (2×2): `.ps > .pscard(.p + .s)` (vänster terrakotta-kant).
- **triage** (grön/gul/röd eskalering): `.triage > .tri.green|.amber|.red > .dot + div(b+span)`.
- **storage / stor-siffra-trio**: `.storage > .store > .ic(svg)+.num+.unit+.where`.
- **cycle / numrerade steg**: `.cycle > .node(.ic[1/2/3]+b+span)` separerade av `.arrow`→, ev `.loopback`.
- **highlight** (lugnande nyckelmening): `.highlight > .tag + p`.
- **roles** (3 kort): `.roles > .role(.who+h3+p)`.
- **featured-audio** (för ljudledd övning, t.ex. andning/knip): `.featured-audio > button.play[data-src="audio/ovning.mp3"] + .fa-text(b+span)`. (Ljudfilen genereras separat — lägg bara knappen.)
- **closing**: `<section class="slide closing layout-center">` med `eyebrow`,`h1`,`.ask`,`.calm`.

## SVG-ikoner (klistra in i `.ic`, stroke ärver färgen)
- Droppe: `<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"><path d="M12 3.6c2.9 3.7 5.3 6.4 5.3 9.4a5.3 5.3 0 0 1-10.6 0c0-3 2.4-5.7 5.3-9.4z"/></svg>`
- Hjärta: `<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"><path d="M12 20S5 15.6 5 10.6A3.6 3.6 0 0 1 12 8a3.6 3.6 0 0 1 7 2.6C19 15.6 12 20 12 20z"/></svg>`
- Klocka: `<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="8.2"/><path d="M12 7.5v4.8l3.2 1.9"/></svg>`
- Sköld/säkerhet: `<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"><path d="M12 3l7 2.5v5c0 4.5-3 7.8-7 9.5-4-1.7-7-5-7-9.5v-5z"/><path d="M9 12l2 2 4-4"/></svg>`
- Måne/sömn: `<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"><path d="M20 14.5A8 8 0 1 1 9.5 4a6.5 6.5 0 0 0 10.5 10.5z"/></svg>`
- Prat/stöd: `<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"><path d="M20 12a7 7 0 0 1-9.5 6.5L5 20l1.5-4.5A7 7 0 1 1 20 12z"/></svg>`
- Trendlinje: `<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"><path d="M4 18h16"/><path d="M6 15l4-4 3 2 5-6"/><path d="M16 7h2.6v2.6"/></svg>`
- Plus/vård: `<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="8.2"/><path d="M12 8.5v7M8.5 12h7"/></svg>`

## Bildstil (för _images.json promptar)
Alltid prefixa varje prompt med:
"Soft, tender hand-painted gouache-style illustration, warm calm reassuring mood, limited palette of warm cream, terracotta, soft blush pink, sage green, muted gold ochre, gentle rounded organic shapes, soft edges, painterly, generous negative space, tasteful and non-clinical. NO text, no letters, no numbers. Scene: ..."

När du är klar: skriv de fyra filerna och returnera en kort rad med antal slides + bildnamn.
