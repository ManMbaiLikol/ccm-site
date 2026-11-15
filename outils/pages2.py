import json, os, sys, re
sys.path.insert(0, os.path.dirname(__file__))
from commun import tete, entete_page, pied, esc
from pages import ecrire, P, ARROW, OUT

# ------------------------------------------------------------------ OBSERVATOIRE
home = open(os.path.join(OUT, "index.html")).read()
themes_js = re.search(r"var CCM_THEMES = \[.*?\n\];", home, re.S).group(0)

audiences = [("Téléspectateurs", 16257552), ("Internautes", 16000000), ("Auditeurs de radio", 12763728), ("Utilisateurs des réseaux sociaux", 5000000)]
amax = max(v for _, v in audiences)
routines = [
    ("5 h – 9 h", "Le matin, à la maison", "Les adultes préfèrent la douceur du gospel, souvent en guise de prière du matin. Les adolescents choisissent des musiques fortes et dansantes, comme le mbolé ou le rap, écoutées seuls dans la chambre ou pendant les travaux ménagers.", "Téléphone, enceinte Bluetooth, télévision, applications"),
    ("10 h – 18 h", "Tout au long de la journée", "La plupart des adultes n'écoutent pas de musique, pris par leurs occupations. Une bonne journée finit en chanson festive ; une mauvaise, souvent sans musique. Les jeunes passent du rythmé au plus doux, puis reviennent au fort.", "Téléphone, enceinte Bluetooth, télévision, radio"),
    ("19 h – 22 h", "Le soir, à la maison", "Quand ils ne sortent pas, les auditeurs choisissent des musiques qui leur parlent personnellement, loin des musiques d'ambiance faites pour danser.", "Téléphone, enceinte Bluetooth, télévision"),
    ("19 h – tard", "Le soir, en sortie", "En groupe, chacun tait ses goûts : au bar, place à la musique très rythmée et au volume élevé. Plus tard, snack-bars et boîtes de nuit prennent le relais avec un son de meilleure qualité.", "Sonorisation du bar, musique live, platines DJ"),
]
attentes = [
    "Idéalement être gratuit, ou ne pas multiplier les paiements",
    "Permettre d'acheter des chansons à l'unité, autour de 100 FCFA",
    "Confirmer chaque achat par SMS, avec le montant et le titre",
    "Proposer un large catalogue, par genre, artiste et pays",
    "Fonctionner sur iOS, Android et même sur les téléphones simples",
    "Prévenir des nouveautés par SMS, même hors connexion",
    "Réduire les publicités",
    "Permettre aux auditeurs de laisser un avis aux auteurs",
]
plateformes = ["Boomplay", "YouTube", "Audiomack", "VidMate", "Tubidy", "Ayoba (MTN)", "Spotify", "Deezer", "Digster", "Stillac Play", "Jengu"]

segments = [("Jeunes, 10 à 29 ans", 6938200, "40,1 %", 11300000), ("Adultes, 30 à 49 ans", 3577164, "20,7 %", 5826000), ("Seniors, 50 à 74 ans", 1511668, "8,7 %", 2462000)]

html = tete("observatoire", "Observatoire de la musique", "Les chiffres de la musique au Cameroun : cartographie des 3 199 professionnels, marché potentiel, habitudes d'écoute, plateformes et attentes des auditeurs, d'après le CCM (2024).")
html += entete_page("Observatoire", "Comprendre la musique camerounaise, chiffres à l'appui", "Les données de l'étude menée par le CCM au premier semestre 2024 à Douala, Yaoundé, Bafoussam et Garoua, et de la cartographie des professionnels de la filière.", "Observatoire de la musique")
html += f'''
<section aria-label="Chiffres clés" style="background: var(--vert-nuit); color: var(--papier)">
<div class="wrap bandeau" style="display: grid; grid-template-columns: repeat(4, minmax(0, 1fr)); gap: 32px; padding-top: 52px; padding-bottom: 52px">
<div><p class="chiffre"><span data-compte="28.2" data-dec="1">28,2</span> M</p><p style="margin: 10px 0 0; color: #d6e2d9; font-size: 15px">d'habitants au Cameroun, avec une croissance de 2,51 % par an</p></div>
<div><p class="chiffre"><span data-compte="70" data-dec="0">70</span> %</p><p style="margin: 10px 0 0; color: #d6e2d9; font-size: 15px">de la population a entre 10 et 74 ans</p></div>
<div><p class="chiffre"><span data-compte="12" data-dec="0">12</span> M</p><p style="margin: 10px 0 0; color: #d6e2d9; font-size: 15px">de consommateurs potentiels de musique, compte tenu du taux de pauvreté (38,6 %)</p></div>
<div><p class="chiffre"><span data-compte="3199" data-dec="0">3 199</span></p><p style="margin: 10px 0 0; color: #d6e2d9; font-size: 15px">professionnels recensés dans la base de données du CCM</p></div>
</div>
</section>

<section id="cartographie" class="section">
<div class="wrap">
<div class="rv">
<p class="eyebrow">Cartographie des professionnels</p>
<h2 class="h2">Qui fait la musique au Cameroun ?</h2>
</div>
<div role="tablist" aria-label="Thèmes de la cartographie" id="themes-onglets" style="display: flex; gap: 10px; flex-wrap: wrap; margin-top: 32px"></div>
<div class="grid2" style="margin-top: 28px; gap: 32px; align-items: stretch">
<article class="carte" style="padding: 36px">
<h3 id="theme-titre" class="serif" style="margin: 0; font-size: 26px"></h3>
<p id="theme-sous" style="margin: 0; font-size: 15px; color: var(--gris)"></p>
<div id="theme-lignes" style="display: grid; gap: 18px; margin-top: 12px"></div>
</article>
<article class="carte" style="padding: 36px; background: var(--vert); border-color: var(--vert); color: var(--papier); justify-content: center">
<p id="theme-cle" class="serif" style="margin: 0; font-size: 88px; line-height: 1; color: var(--ambre)"></p>
<p id="theme-cletexte" class="serif" style="margin: 8px 0 0; font-size: 26px; line-height: 1.25"></p>
<p id="theme-lecture" style="margin: 16px 0 0; font-size: 16px; color: #d6e2d9"></p>
</article>
</div>
</div>
</section>

<section id="marche" class="section" style="background: #fff; border-top: 1px solid var(--filet)">
<div class="wrap">
<div class="rv grid2" style="align-items: end">
<div>
<p class="eyebrow">Le marché potentiel</p>
<h2 class="h2">Combien vaut la vente directe de musique ?</h2>
</div>
<p style="margin: 0; color: var(--gris)">Simulation du CCM : 12 027 032 consommateurs potentiels achètent des chansons au prix pratiqué par les « téléchargeurs », 50 ou 100 FCFA. Choisissez un scénario pour voir le chiffre d'affaires par tranche d'âge.</p>
</div>
<div class="filtres" style="margin-top: 32px">
<div><p style="margin: 0 0 8px; font-weight: 600; font-size: 15px">Chansons achetées par personne et par an</p><div role="radiogroup" aria-label="Chansons par an" id="scen-onglets" style="display: flex; gap: 8px; flex-wrap: wrap"></div></div>
<div><p style="margin: 0 0 8px; font-weight: 600; font-size: 15px">Prix par chanson</p><div role="radiogroup" aria-label="Prix par chanson" id="prix-onglets" style="display: flex; gap: 8px"></div></div>
</div>
<div class="grid2" style="margin-top: 28px; gap: 32px; align-items: stretch">
<div class="boite-tableau"><table class="tableau"><caption class="sr" style="position:absolute;left:-9999px">Chiffre d'affaires par tranche d'âge</caption><thead><tr><th scope="col">Tranche d'âge</th><th scope="col">Consommateurs</th><th scope="col">Chiffre d'affaires (FCFA)</th></tr></thead><tbody id="simu-lignes"></tbody></table></div>
<div style="background: var(--vert-nuit); color: var(--papier); border-radius: 12px; padding: 40px; text-align: center; display: flex; flex-direction: column; justify-content: center">
<p style="margin: 0; font-size: 13px; font-weight: 600; letter-spacing: .12em; text-transform: uppercase; color: var(--ambre)">Scénario <span id="simu-nom"></span></p>
<p id="simu-montant" class="serif" style="margin: 16px 0 0; font-size: 76px; line-height: 1; color: var(--ambre); font-variant-numeric: tabular-nums"></p>
<p style="margin: 10px 0 0; font-size: 18px"><span id="simu-unite"></span> de chiffre d'affaires par an</p>
</div>
</div>
<div class="grid3" style="margin-top: 32px">
''' + "".join(f'<div class="carte rv"><p class="chiffre-vert">{pct}</p><p style="margin: 0; font-size: 15px"><strong>{n}</strong> : {tot:,} personnes dans la population totale</p></div>\n'.replace(",", " ") for n, _, pct, tot in segments) + f'''</div>
</div>
</section>

<section id="ecoute" class="section">
<div class="wrap">
<div class="rv grid2">
<div>
<p class="eyebrow">Le parcours d'écoute</p>
<h2 class="h2">Des réseaux sociaux au « téléchargeur »</h2>
</div>
<p class="lead" style="margin: 0">La découverte commence souvent sur TikTok et Instagram ; elle se termine le plus souvent par un fichier partagé via Xender par l'entourage, ou par l'achat d'une chanson à 50 ou 100 FCFA auprès d'un téléchargeur.</p>
</div>
<div class="grid2" style="margin-top: 48px; gap: 32px; align-items: stretch">
<article class="carte rv" style="padding: 36px">
<h3 class="serif" style="margin: 0; font-size: 24px">Les audiences</h3>
<div style="display: grid; gap: 18px; margin-top: 8px">
''' + "".join(f'<div><div style="display: flex; justify-content: space-between; font-size: 15px; margin-bottom: 6px"><span>{l}</span><strong>{v:,}</strong></div><div class="barre"><span style="width: {v/amax*100:.0f}%; background: var(--vert)"></span></div></div>\n'.replace(",", " ") for l, v in audiences) + f'''</div>
</article>
<article class="carte rv" style="padding: 36px; background: var(--bordeaux); border-color: var(--bordeaux); color: var(--papier); justify-content: center">
<p class="serif" style="margin: 0; font-size: 80px; line-height: 1; color: var(--ambre)"><span data-compte="26996" data-dec="0">26 996</span></p>
<p class="serif" style="margin: 8px 0 0; font-size: 26px; line-height: 1.25">bars et snack-bars sonorisés.</p>
<p style="margin: 16px 0 0; color: #f6dde2">Les lieux de consommation hors domicile, avec la télévision et la radio, restent les grands vecteurs de nouveautés. Pour retrouver un titre, on utilise Shazam ou l'on demande au DJ.</p>
</article>
</div>

<h3 class="serif rv" style="margin: 72px 0 24px; font-size: 30px; color: var(--vert)">Les quatre routines d'écoute</h3>
<div class="grid4">
''' + "".join(f'<article class="routine rv"><p class="heure">{h}</p><h4 style="margin: 6px 0 10px; font-size: 17px">{t}</h4><p style="margin: 0; font-size: 15px">{d}</p><p style="margin: 12px 0 0; font-size: 13px; color: var(--gris)">{e}</p></article>\n' for h, t, d, e in routines) + f'''</div>
</div>
</section>

<section id="attentes" style="background: var(--lilas); padding: 104px 0">
<div class="wrap grid2">
<div class="rv">
<p class="eyebrow">Ce que veulent les auditeurs</p>
<h2 class="h2" style="color: var(--encre)">Le moyen d'écoute idéal</h2>
<p style="font-size: 18px; margin: 16px 0 0">Résultat d'un exercice projectif mené en avril 2024 auprès d'adolescents, de jeunes adultes et de quadragénaires à Yaoundé, Douala, Bafoussam et Maroua.</p>
<blockquote style="margin: 32px 0 0; padding: 24px; background: var(--papier); border-radius: 10px">
<p class="serif" style="margin: 0; font-size: 22px; line-height: 1.35">« Je paie déjà pour ma connexion, l'application devrait être gratuite ! »</p>
<footer style="margin-top: 10px; font-size: 14px; color: var(--gris)">Constant, quadragénaire, Yaoundé</footer>
</blockquote>
</div>
<ul class="rv" style="list-style: none; margin: 0; padding: 0">
''' + "".join(f'<li style="display: flex; gap: 14px; align-items: flex-start; padding: 14px 0; border-top: 1px solid rgba(15,25,18,.18)"><svg aria-hidden="true" width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="#a10b2b" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round" style="flex-shrink: 0; margin-top: 2px"><path d="M5 12l5 5L20 7"></path></svg><span>{a}</span></li>\n' for a in attentes) + f'''</ul>
</div>
</section>

<section id="plateformes" class="section">
<div class="wrap">
<div class="rv grid2" style="align-items: end">
<div>
<p class="eyebrow">Les moyens digitaux</p>
<h2 class="h2">Les plateformes utilisées au Cameroun</h2>
</div>
<p style="margin: 0; color: var(--gris)">Boomplay revendique 1,5 million d'utilisateurs camerounais, contre 4 700 comptes payants cumulés sur Spotify, Apple Music et Deezer. YouTube et Spotify, les plus utilisées au monde, ne permettent pas encore aux artistes camerounais de monétiser leurs écoutes.</p>
</div>
<ul class="rv" style="list-style: none; margin: 40px 0 0; padding: 0; display: flex; gap: 10px; flex-wrap: wrap">
''' + "".join(f'<li class="onglet" style="cursor: default">{p}</li>' for p in plateformes) + f'''
</ul>
<div style="display: flex; gap: 16px; flex-wrap: wrap; margin-top: 56px; padding-top: 32px; border-top: 1px solid var(--filet); align-items: center; justify-content: space-between">
<p class="source" style="max-width: 720px">Sources : CCM, <em>Introduction au schéma de développement de l'industrie musicale camerounaise</em>, 2024, d'après la base de données du CCM, l'ONU (World Population Prospects 2024), l'INS (ECAM5), GSMA, Statista, Datareportal et l'IFPI.</p>
<a class="btn btn-vert" href="{P}docs/introduction-schema-developpement-industrie-musicale-camerounaise.pdf" download>Télécharger le rapport complet</a>
</div>
</div>
</section>
'''
SEG = json.dumps([[n, v] for n, v, _, _ in segments], ensure_ascii=False)
js = f'''<script>
{themes_js}
var CCM_SEGMENTS = {SEG};
var CCM_SCENARIOS = [{{n:1,label:'1 chanson',nom:'ultra pessimiste'}},{{n:10,label:'10 chansons',nom:'pessimiste'}},{{n:30,label:'30 chansons',nom:'réaliste'}},{{n:100,label:'100 chansons',nom:'optimiste'}}];
(function () {{
  function $(i) {{ return document.getElementById(i); }}
  var theme = 0;
  function rendreTheme() {{
    $('themes-onglets').innerHTML = CCM_THEMES.map(function (t, i) {{ return '<button type="button" role="tab" aria-selected="' + (i === theme) + '" data-i="' + i + '" class="onglet' + (i === theme ? ' onglet-actif' : '') + '">' + t.label + '</button>'; }}).join('');
    var t = CCM_THEMES[theme];
    $('theme-titre').textContent = t.titre; $('theme-sous').textContent = t.sous; $('theme-cle').textContent = t.cle; $('theme-cletexte').textContent = t.cleTexte; $('theme-lecture').textContent = t.lecture;
    $('theme-lignes').innerHTML = t.lignes.map(function (l) {{ return '<div><div style="display:flex;justify-content:space-between;font-size:15px;margin-bottom:6px"><span>' + l[0] + '</span><strong>' + l[1] + ' %</strong></div><div class="barre"><span style="width:' + l[1] + '%;background:' + t.couleur + '"></span></div></div>'; }}).join('');
  }}
  $('themes-onglets').addEventListener('click', function (e) {{ var b = e.target.closest('button'); if (b) {{ theme = +b.dataset.i; rendreTheme(); }} }});
  rendreTheme();
  var scen = 2, prix = 0, PRIX = [50, 100];
  function f(n) {{ return Math.round(n).toLocaleString('fr-FR'); }}
  function pastilles(l, a) {{ return l.map(function (x, i) {{ return '<button type="button" role="radio" aria-checked="' + (i === a) + '" data-i="' + i + '" class="onglet' + (i === a ? ' onglet-actif' : '') + '">' + x + '</button>'; }}).join(''); }}
  function rendreSimu() {{
    $('scen-onglets').innerHTML = pastilles(CCM_SCENARIOS.map(function (s) {{ return s.label; }}), scen);
    $('prix-onglets').innerHTML = pastilles(PRIX.map(function (p) {{ return p + ' FCFA'; }}), prix);
    var sc = CCM_SCENARIOS[scen], k = sc.n * PRIX[prix], tot = 0, rows = '';
    CCM_SEGMENTS.forEach(function (s) {{ var v = s[1] * k; tot += v; rows += '<tr><td>' + s[0] + '</td><td>' + f(s[1]) + '</td><td>' + f(v) + '</td></tr>'; }});
    rows += '<tr class="total"><td>Total</td><td>' + f(12027032) + '</td><td>' + f(tot) + '</td></tr>';
    $('simu-lignes').innerHTML = rows; $('simu-nom').textContent = sc.nom;
    if (tot >= 1e9) {{ $('simu-montant').textContent = (tot / 1e9).toFixed(1).replace('.', ','); $('simu-unite').textContent = 'milliards de FCFA'; }}
    else {{ $('simu-montant').textContent = f(tot / 1e6); $('simu-unite').textContent = 'millions de FCFA'; }}
  }}
  $('scen-onglets').addEventListener('click', function (e) {{ var b = e.target.closest('button'); if (b) {{ scen = +b.dataset.i; rendreSimu(); }} }});
  $('prix-onglets').addEventListener('click', function (e) {{ var b = e.target.closest('button'); if (b) {{ prix = +b.dataset.i; rendreSimu(); }} }});
  rendreSimu();
}})();
</script>'''
html += pied(js_page=js)
ecrire("observatoire", html)

# ------------------------------------------------------------------ ANNUAIRE
membres = json.load(open(os.path.join(os.path.dirname(__file__), "donnees", "membres.json")))


def famille(m):
    x = m.lower()
    if "journal" in x or "radio" in x: return "Médias"
    if "produc" in x: return "Production"
    if "promot" in x or "event" in x: return "Promotion et événementiel"
    if "édit" in x or "edit" in x or "distrib" in x: return "Édition et distribution"
    if "technic" in x: return "Technique"
    if "entrepreneur" in x: return "Entrepreneuriat culturel"
    return "Autres métiers"


data = [dict(n=m["num"], nom=m["nom"], metier=m["metier"], fam=famille(m["metier"]), region=m["region"], ville=m["ville"], photo=m["photo"], valide=m["valide"].capitalize()) for m in membres]
regions = {}
for d in data: regions[d["region"]] = regions.get(d["region"], 0) + 1
rmax = max(regions.values())
reg_bars = "".join(f'<div><div style="display: flex; justify-content: space-between; font-size: 15px; margin-bottom: 6px"><span>{r}</span><strong>{c}</strong></div><div class="barre"><span style="width: {c/rmax*100:.0f}%; background: var(--vert)"></span></div></div>\n' for r, c in sorted(regions.items(), key=lambda x: -x[1]))
n_villes = len({d["ville"] for d in data})

html = tete("annuaire", "Annuaire des membres", f"Annuaire des {len(data)} professionnels de la musique titulaires de la carte de membre du Conseil Camerounais de la Musique : promoteurs, producteurs, journalistes, éditeurs, dans {len(regions)} régions.")
html += entete_page("Annuaire", "L'annuaire des membres du CCM", "Les professionnels de la musique titulaires de la carte de membre du Conseil Camerounais de la Musique. Trouvez un partenaire par région, par ville ou par métier, et contactez-le par l'intermédiaire du CCM.", "Annuaire des professionnels")
html += f'''
<section aria-label="Chiffres de l'annuaire" style="background: var(--vert-nuit); color: var(--papier)">
<div class="wrap bandeau" style="display: grid; grid-template-columns: repeat(4, minmax(0, 1fr)); gap: 32px; padding-top: 44px; padding-bottom: 44px">
<div><p class="chiffre"><span data-compte="{len(data)}" data-dec="0">{len(data)}</span></p><p style="margin: 10px 0 0; color: #d6e2d9; font-size: 15px">membres titulaires de la carte</p></div>
<div><p class="chiffre"><span data-compte="{len(regions)}" data-dec="0">{len(regions)}</span></p><p style="margin: 10px 0 0; color: #d6e2d9; font-size: 15px">régions représentées sur 10</p></div>
<div><p class="chiffre"><span data-compte="{n_villes}" data-dec="0">{n_villes}</span></p><p style="margin: 10px 0 0; color: #d6e2d9; font-size: 15px">villes</p></div>
<div><p class="chiffre">2027</p><p style="margin: 10px 0 0; color: #d6e2d9; font-size: 15px">cartes valables jusqu'en janvier</p></div>
</div>
</section>

<section class="section" style="padding-top: 64px">
<div class="wrap">
<form class="filtres" role="search" aria-label="Rechercher dans l'annuaire" onsubmit="return false">
<label>Rechercher un nom, une ville, un métier<input type="search" id="q" placeholder="Ex. Douala, producteur…" autocomplete="off"></label>
<label>Région<select id="f-region"><option value="">Toutes les régions</option></select></label>
<label>Métier<select id="f-fam"><option value="">Tous les métiers</option></select></label>
<button type="button" id="f-raz" class="btn btn-contour">Réinitialiser</button>
</form>
<p id="resultat" aria-live="polite" style="margin: 24px 0 20px; font-weight: 600"></p>
<div id="liste" class="membres"></div>
<div class="grid2" style="margin-top: 80px; gap: 32px; align-items: start">
<article class="carte rv" style="padding: 36px">
<h2 class="serif" style="margin: 0; font-size: 26px">Les membres par région</h2>
<div style="display: grid; gap: 16px; margin-top: 8px">
{reg_bars}</div>
</article>
<article class="carte rv" style="padding: 36px; background: #f7f1e5; border-color: #e8dfcc">
<h2 class="serif" style="margin: 0; font-size: 26px; color: var(--vert)">À propos de cet annuaire</h2>
<p style="margin: 0">Pour protéger la vie privée des membres, les numéros de téléphone et les nationalités ne sont pas publiés. Chaque demande de contact passe par le secrétariat du CCM, qui la transmet au membre concerné.</p>
<p style="margin: 0">Vous êtes membre et souhaitez modifier ou retirer votre fiche ? <a href="mailto:infos@ccm-cmc.org?subject=Annuaire%20%3A%20modification%20de%20ma%20fiche">Écrivez-nous</a>.</p>
<p style="margin: 0">Vous n'êtes pas encore membre ?</p>
<a class="btn btn-vert" href="{P}#adhesion" style="align-self: flex-start">Demander ma carte de membre</a>
</article>
</div>
</div>
</section>
'''
js = '''<script>
var CCM_MEMBRES = ''' + json.dumps(data, ensure_ascii=False) + ''';
(function () {
  function $(i) { return document.getElementById(i); }
  function norm(s) { return s.normalize('NFD').replace(/[\\u0300-\\u036f]/g, '').toLowerCase(); }
  function esc(s) { return s.replace(/[&<>"]/g, function (c) { return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c]; }); }
  var regs = {}, fams = {};
  CCM_MEMBRES.forEach(function (m) { regs[m.region] = 1; fams[m.fam] = 1; });
  Object.keys(regs).sort().forEach(function (r) { $('f-region').insertAdjacentHTML('beforeend', '<option>' + esc(r) + '</option>'); });
  Object.keys(fams).sort().forEach(function (f) { $('f-fam').insertAdjacentHTML('beforeend', '<option>' + esc(f) + '</option>'); });
  var params = new URLSearchParams(location.search);
  if (params.get('region')) $('f-region').value = params.get('region');
  function rendre() {
    var q = norm($('q').value.trim()), r = $('f-region').value, f = $('f-fam').value;
    var l = CCM_MEMBRES.filter(function (m) {
      return (!r || m.region === r) && (!f || m.fam === f) && (!q || norm(m.nom + ' ' + m.metier + ' ' + m.ville + ' ' + m.region + ' ' + m.n).indexOf(q) > -1);
    });
    $('resultat').textContent = l.length + (l.length > 1 ? ' membres' : ' membre') + (l.length === CCM_MEMBRES.length ? '' : ' sur ' + CCM_MEMBRES.length);
    $('liste').innerHTML = l.length ? l.map(function (m) {
      var sujet = encodeURIComponent('Annuaire : mise en relation avec le membre n° ' + m.n + ' (' + m.nom + ')');
      return '<article class="membre">' +
        '<div class="membre-haut"><img src="../assets/membres/' + m.photo + '" alt="Photo de ' + esc(m.nom) + '" loading="lazy" width="86" height="106">' +
        '<div><h3>' + esc(m.nom) + '</h3><p class="metier">' + esc(m.metier) + '</p><p class="num">N° ' + m.n + '</p></div></div>' +
        '<div class="filet-tri" aria-hidden="true" style="padding:0 18px"><i></i><b style="background:#106938"></b><b style="background:#e21b19"></b><b style="background:#f2ea18"></b><i></i></div>' +
        '<div class="membre-bas"><span>' + esc(m.ville) + ' · ' + esc(m.region) + '</span><a href="mailto:infos@ccm-cmc.org?subject=' + sujet + '">Contacter</a></div></article>';
    }).join('') : '<p class="vide">Aucun membre ne correspond à cette recherche.</p>';
  }
  ['q', 'f-region', 'f-fam'].forEach(function (i) { $(i).addEventListener('input', rendre); });
  $('f-raz').addEventListener('click', function () { $('q').value = ''; $('f-region').value = ''; $('f-fam').value = ''; rendre(); $('q').focus(); });
  rendre();
})();
</script>'''
html += pied(js_page=js)
ecrire("annuaire", html)
