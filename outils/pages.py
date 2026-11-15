import json, os, sys
sys.path.insert(0, os.path.dirname(__file__))
from commun import tete, entete_page, pied, esc

OUT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
P = "../"


def ecrire(slug, html):
    os.makedirs(f"{OUT}/{slug}", exist_ok=True)
    open(f"{OUT}/{slug}/index.html", "w").write(html)
    print("écrit", slug, len(html))


ARROW = '<svg aria-hidden="true" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12h14M13 6l6 6-6 6"></path></svg>'

# ------------------------------------------------------------------ INSTITUTION
objectifs = [
    ("Relier", "Contribuer au renforcement des relations entre toutes les parties prenantes du secteur musical et à une meilleure structuration de l'industrie musicale au Cameroun."),
    ("Mailler", "Créer et structurer un réseau de professionnels sur tout le territoire."),
    ("Rassembler", "Renforcer les relations entre les associations et les entreprises musicales."),
    ("Animer", "Encourager l'organisation de séminaires, festivals, concerts, ateliers et réunions d'experts."),
    ("Former", "Contribuer à la formation et à la professionnalisation des acteurs camerounais de la musique."),
    ("Structurer", "Participer à l'élaboration d'une structuration de l'industrie musicale au Cameroun."),
]
droits = [
    "Le droit pour les enfants et les adultes de s'exprimer musicalement en toute liberté.",
    "Le droit d'apprendre et d'étudier les langages et savoir-faire musicaux.",
    "Le droit d'accéder à la musique par la participation, l'écoute, la création et l'information.",
    "Le droit pour les artistes musicaux de développer leur art et de le communiquer à travers tous les médias, avec des outils et des structures appropriés.",
    "Le droit pour les artistes musicaux d'obtenir une juste reconnaissance et une rémunération équitable pour leur travail.",
]
frise = [
    ("2001", "Le Conseil international de la musique proclame, lors de son assemblée générale, les cinq droits de la musique."),
    ("2003", "Lors de la 30<sup>e</sup> assemblée générale du CIM, le Cameroun est admis comme membre, à la demande motivée de Luc Yatchokeu, alors président de l'association CIGALE. Le CIM demande la création d'une association nationale dédiée."),
    ("2009", "Fondation du Conseil Camerounais de la Musique sous l'égide du professeur Lupwishi Mbuyamba, coordonnateur régional du CIM en Afrique. Enregistrement à Douala le 14 septembre 2009 (n° 133/2009/RDDA/C19/BAPP)."),
    ("2021", "Assemblées générales ordinaire et extraordinaire du 31 mars à Yaoundé : statuts amendés et nouveau bureau exécutif élu."),
    ("2024", "Les Chantiers musicaux du Cameroun réunissent 64 professionnels des dix régions et aboutissent à l'<em>Introduction au schéma de développement de l'industrie musicale camerounaise</em>."),
    ("2026", "Lancement de l'annuaire en ligne des membres titulaires de la carte du CCM."),
]
organes = [
    ("Assemblée générale", "Constituée de tous les membres."),
    ("Bureau exécutif", "Un président, deux vice-présidents, un secrétaire général et son adjoint, un trésorier, un responsable de la communication et deux responsables des opérations, l'un à Douala, l'autre à Yaoundé."),
    ("Observatoire de la musique", "Organe interne habilité à fournir des arguments techniques pour les relations du CCM avec le ministère des Arts et de la Culture, les collectivités territoriales décentralisées et les autres institutions. Il remet chaque année un rapport au bureau exécutif."),
    ("Commissions", "Commission financière, commission juridique et commission chargée de l'appui aux initiatives musicales."),
    ("Comité consultatif", "Veille au bon fonctionnement du CCM selon la vision du Conseil international de la musique et les bonnes pratiques recommandées par les institutions nationales et internationales."),
    ("Représentants régionaux", "Personnes physiques ou morales membres du CCM, chargées de représenter l'association et de relayer ses activités dans leur région."),
]

html = tete("institution", "L'institution", "Mission, histoire, gouvernance et valeurs du Conseil Camerounais de la Musique, association nationale membre du réseau du Conseil international de la musique.")
html += entete_page("L'institution", "Structurer la filière musicale, avec tous ses acteurs", "Association à but non lucratif et apolitique, le Conseil Camerounais de la Musique rassemble musiciens, arrangeurs, formateurs, chercheurs, musicologues, critiques, producteurs, sonorisateurs, diffuseurs, éditeurs, promoteurs et spécialistes des droits d'auteur.", "L'institution")
html += f'''
<section id="mission" class="section">
<div class="wrap grid2">
<div class="rv">
<p class="eyebrow">Notre mission</p>
<h2 class="h2">Une force de proposition auprès des institutions nationales et internationales</h2>
<p class="lead">Le CCM structure l'industrie musicale au Cameroun en veillant à l'épanouissement des acteurs. Il soutient la création, facilite la diffusion des œuvres, encourage l'éducation musicale des jeunes, documente et valorise le patrimoine, et veille au statut des musiciens comme à la protection de leurs droits.</p>
<p style="margin: 20px 0 0">Sur le plan socio-économique, il contribue à la création de richesses et d'emplois, et plaide auprès du ministère de l'Économie, de la Planification et de l'Aménagement du territoire pour que la musique soit prise en compte dans la Stratégie nationale de développement 2020-2030 (SND30).</p>
</div>
<div class="grid2 rv" style="gap: 16px">
''' + "".join(f'''<article class="carte" style="padding: 24px"><p class="serif" style="margin: 0; font-size: 20px; color: var(--vert)">{t}</p><p style="margin: 0; font-size: 15px; color: var(--gris)">{d}</p></article>
''' for t, d in objectifs) + '''</div>
</div>
</section>

<section id="histoire" class="section" style="background: #fff; border-top: 1px solid var(--filet)">
<div class="wrap grid2">
<div class="rv">
<p class="eyebrow">Histoire</p>
<h2 class="h2">Né du Conseil international de la musique</h2>
<p class="lead">Le CCM est l'association nationale qui représente le Cameroun dans le réseau du Conseil international de la musique, fondé en 1949 à l'initiative de l'UNESCO.</p>
</div>
<ol class="frise rv">
''' + "".join(f'<li><span class="annee">{a}</span><p style="margin: 0">{t}</p></li>\n' for a, t in frise) + '''</ol>
</div>
</section>

<section id="droits" style="background: var(--vert); color: var(--papier); padding: 104px 0; position: relative; overflow: hidden">
<div class="anneaux" aria-hidden="true"><i></i><i></i><i></i><i></i></div>
<div class="wrap grid2" style="position: relative">
<div class="rv">
<p style="margin: 0 0 16px; font-size: 13px; font-weight: 600; letter-spacing: .12em; text-transform: uppercase; color: var(--ambre)">Nos valeurs</p>
<h2 class="serif" style="margin: 0; font-size: 44px; line-height: 1.1">Les cinq droits de la musique</h2>
<p style="margin: 20px 0 0; font-size: 18px; color: #d6e2d9">Proclamés en 2001 par le Conseil international de la musique, ils guident l'action du CCM au Cameroun.</p>
</div>
<ol style="list-style: none; margin: 0; padding: 0">
''' + "".join(f'<li class="droit rv-g" style="border-color: #3d7a52"><span>{i}</span><p style="margin: 0; font-size: 17px">{d}</p></li>\n' for i, d in enumerate(droits, 1)) + f'''</ol>
</div>
</section>

<section id="gouvernance" class="section">
<div class="wrap grid2">
<div class="rv">
<p class="eyebrow">Gouvernance</p>
<h2 class="h2">Une association transparente et démocratique</h2>
<p class="lead">Les statuts du CCM ont été amendés et son bureau exécutif élu lors des assemblées générales du 31 mars 2021 à Yaoundé.</p>
<div style="display: flex; gap: 24px; align-items: center; margin-top: 36px; padding: 24px; background: #fff; border: 1px solid var(--filet); border-radius: 8px">
<img src="{P}assets/president-didier-ngadjui-toko.jpg" alt="Didier Ngadjui Toko, président du Conseil Camerounais de la Musique" width="128" height="128" style="width: 128px; height: 128px; border-radius: 50%; object-fit: cover; flex-shrink: 0; border: 3px solid var(--ambre)">
<div>
<p style="margin: 0; font-size: 13px; font-weight: 600; letter-spacing: .08em; text-transform: uppercase; color: var(--bordeaux)">Président</p>
<p class="serif" style="margin: 4px 0 0; font-size: 26px; color: var(--vert)">Didier Ngadjui Toko</p>
<p style="margin: 2px 0 0; font-size: 14px; color: var(--gris)">Entrepreneur culturel, expert du secteur musical pour la zone Afrique-Caraïbes-Pacifique</p>
</div>
</div>
</div>
<div class="rv">
<h3 class="serif" style="margin: 0 0 20px; font-size: 24px; color: var(--vert)">Les organes du Conseil</h3>
<dl style="margin: 0; border-top: 1px solid var(--filet)">
''' + "".join(f'<div style="padding: 16px 0; border-bottom: 1px solid var(--filet)"><dt style="font-weight: 600">{t}</dt><dd style="margin: 4px 0 0; font-size: 15px; color: var(--gris)">{d}</dd></div>\n' for t, d in organes) + f'''</dl>
</div>
</div>
</section>

<section style="background: var(--bordeaux); color: var(--papier); padding: 72px 0">
<div class="wrap" style="display: flex; justify-content: space-between; align-items: center; gap: 32px; flex-wrap: wrap">
<h2 class="serif" style="margin: 0; font-size: 34px; line-height: 1.15; max-width: 640px">Rejoignez le réseau des professionnels de la musique au Cameroun.</h2>
<div style="display: flex; gap: 16px; flex-wrap: wrap">
<a class="btn btn-ambre" href="{P}#adhesion">Devenir membre {ARROW}</a>
<a class="btn btn-ligne" href="{P}annuaire/">Voir l'annuaire</a>
</div>
</div>
</section>
'''
html += pied()
ecrire("institution", html)

# ------------------------------------------------------------------ CHANTIERS
intervenants = [
    ("Freddy Tchala", "Country Manager, Activa Assurance", "Cameroun"),
    ("Walter Ebelle Eboumbou", "Directeur général de Keyzit Cameroun, fondateur d'Arise Entertainment", "Cameroun"),
    ("Robert Ekotto", "Directeur du sponsoring, Orange Cameroun", "Cameroun"),
    ("Richard Eboa", "Artiste, manager et consultant", "Cameroun"),
    ("Daniel Ndiewan", "Responsable chez FOCEP S.A.", "Cameroun"),
    ("Mike Epaka", "Consultant spécialiste du marketing et de la publicité", "Cameroun"),
    ("Lionel Tousse", "PDG du groupe ICONProd, fondateur du label ICON Fusion", "Cameroun"),
    ("Jean Eudes Biem", "Cerdotola", "Cameroun"),
    ("Jacques Mouen", "Strategic Marketing Leader", "Cameroun"),
    ("Inès Abichou", "Abidjan", "Côte d'Ivoire"),
    ("Charles Elame", "Consultant marketing et go-to-market", "Cameroun"),
    ("Ruby Gyang", "Autrice-compositrice-interprète", "Nigéria"),
    ("Mylène Emica", "Directrice artistique de Seize mètres carrés", "Martinique"),
    ("Mory Touré", "Journaliste culturel, fondateur de Radio Afrika", "Guinée"),
    ("Kayode Adebayo", "Fondateur de Ckrowd.com, président de KAM Africa", "Nigéria"),
    ("Ibaaku", "Producteur, multi-instrumentiste et compositeur", "Sénégal"),
    ("Céline Bakond", "Fondatrice de La Neuvième Muse", "France"),
    ("Carole Tchameni", "Directrice de la programmation, Trace Mboa", "Cameroun"),
    ("Blick Bassy", "Auteur-compositeur-interprète", "Cameroun"),
    ("Antoine Mensah", "Cofondateur d'Aftown Music", "Ghana"),
    ("Akinyemi Ayinoluwa", "Associé, HighTower Solicitors and Advocates", "Nigéria"),
]
contributeurs = [
    ("Charles Elamé", "Expert en stratégie commerciale et marketing"),
    ("Hans Sanama", "Analyste marketing senior"),
    ("Richard Eboa (Jabar)", "Artiste musicien, manager, président du conseil d'administration de The Music Club"),
    ("Davy Lessouga", "Auteur, spécialiste de la musique et du digital en Afrique francophone"),
    ("Walter Ebelle Eboumbou", "Ingénieur culturel, fondateur d'Arise Entertainment"),
    ("Luc Yatchokeu", "Ingénieur culturel, fondateur et ancien président du CCM"),
    ("Jean Pierre Boep", "Professionnel de la stratégie et du marketing"),
    ("Jacques Derse Mouen", "Gestionnaire d'entreprise, spécialiste du marketing"),
]
etapes = [
    ("01", "L'état des lieux", "Douala · 8 au 10 février 2024", "douala-phase1.jpg", "Prise de parole lors de la première étape à Douala",
     "64 professionnels des dix régions, issus de la production, de la promotion et de la diffusion, ont travaillé en ateliers par grandes aires culturelles : septentrion, Grassfields, peuples de la forêt et Grand Sawa. Objectif : comprendre comment fonctionne le secteur et identifier ce qui l'empêche d'éclore.",
     ["21 producteurs", "20 acteurs de la promotion", "23 acteurs de la diffusion"]),
    ("02", "Le renforcement des capacités", "Yaoundé · 18 au 22 mars 2024", "yaounde-phase2.jpg", "Atelier de renforcement de capacités à Yaoundé",
     "Lancée le 18 mars 2024 à la médiathèque de l'Institut français de Yaoundé, en marge du Yaoundé Music Expo, la deuxième étape a proposé plus de 16 ateliers : gestion de projets musicaux, marketing digital, distribution, droits d'auteur et droits voisins, entrepreneuriat, stratégies de diffusion.",
     ["Plus de 16 ateliers", "12 experts internationaux", "25 formateurs camerounais"]),
    ("03", "La restitution", "Yaoundé · juin 2024", "yaounde-panel.jpg", "Table ronde de restitution",
     "L'<em>Introduction au schéma de développement de l'industrie musicale camerounaise</em> a été présentée aux pouvoirs publics, aux institutions et aux organisations professionnelles, en marge de la Zone by DOMAF, pour contribuer à une politique culturelle nationale.",
     ["Document de 144 pages", "Versions française et anglaise", "Prochaine étape : un schéma stratégique complet"]),
]

html = tete("chantiers", "Les Chantiers musicaux du Cameroun", "Les Chantiers musicaux du Cameroun : trois étapes à Douala et Yaoundé en 2024, 64 professionnels, des experts internationaux et un schéma de développement de l'industrie musicale.")
html += entete_page("Chantiers musicaux", "Les Chantiers musicaux du Cameroun", "Plus de six mois de concertation, en 2024, pour diagnostiquer la filière, renforcer ses acteurs et poser les bases d'un schéma de développement. Avec le soutien de l'Ambassade de France au Cameroun et de l'Institut français, dans le cadre du Fonds Équipe France.", "Programme phare · 2024")
html += f'''
<section aria-label="Chiffres clés" style="background: var(--vert-nuit); color: var(--papier)">
<div class="wrap bandeau" style="display: grid; grid-template-columns: repeat(4, minmax(0, 1fr)); gap: 32px; padding-top: 52px; padding-bottom: 52px">
<div><p class="chiffre"><span data-compte="64" data-dec="0">64</span></p><p style="margin: 10px 0 0; color: #d6e2d9; font-size: 15px">professionnels des dix régions</p></div>
<div><p class="chiffre"><span data-compte="3" data-dec="0">3</span></p><p style="margin: 10px 0 0; color: #d6e2d9; font-size: 15px">étapes à Douala et Yaoundé</p></div>
<div><p class="chiffre"><span data-compte="21" data-dec="0">21</span></p><p style="margin: 10px 0 0; color: #d6e2d9; font-size: 15px">intervenants présentés pour la phase 2</p></div>
<div><p class="chiffre"><span data-compte="144" data-dec="0">144</span></p><p style="margin: 10px 0 0; color: #d6e2d9; font-size: 15px">pages pour le schéma de développement</p></div>
</div>
</section>

<section class="section">
<div class="wrap">
<div class="rv" style="display: flex; gap: 32px; align-items: center; flex-wrap: wrap; margin-bottom: 48px">
<img src="{P}assets/chantiers.png" alt="Logo des Chantiers musicaux du Cameroun" style="height: 120px; width: auto">
<div style="max-width: 680px">
<p class="eyebrow">Le déroulé</p>
<h2 class="h2">Trois étapes, de l'état des lieux à la stratégie</h2>
</div>
</div>
<div style="display: flex; flex-direction: column; gap: 32px">
''' + "".join(f'''<article class="phase-ligne rv" style="display: grid; grid-template-columns: minmax(0, 1fr) minmax(0, 1.1fr); gap: 40px; align-items: stretch; background: #fff; border: 1px solid var(--filet); border-radius: 12px; overflow: hidden">
<img src="{P}assets/{img}" alt="{alt}" loading="lazy" style="width: 100%; height: 100%; min-height: 300px; object-fit: cover; display: block">
<div style="padding: 36px 40px 36px 0">
<p style="margin: 0; font-size: 13px; font-weight: 600; letter-spacing: .1em; text-transform: uppercase; color: var(--bordeaux)">Étape {n} · {lieu}</p>
<h3 class="serif" style="margin: 10px 0 14px; font-size: 30px; color: var(--vert)">{titre}</h3>
<p style="margin: 0; font-size: 17px">{texte}</p>
<ul style="list-style: none; margin: 18px 0 0; padding: 0; display: flex; gap: 8px; flex-wrap: wrap">''' + "".join(f'<li class="tag">{c}</li>' for c in chiffres) + '''</ul>
</div>
</article>
''' for n, titre, lieu, img, alt, texte, chiffres in etapes) + f'''</div>
</div>
</section>

<section id="intervenants" class="section" style="background: var(--lilas)">
<div class="wrap">
<div class="rv grid2" style="align-items: end; margin-bottom: 40px">
<div>
<p class="eyebrow">Phase 2 · Yaoundé, 18 au 22 mars 2024</p>
<h2 class="h2" style="color: var(--encre)">Les intervenants</h2>
<p style="font-size: 18px; margin: 16px 0 0">Experts camerounais et internationaux, artistes, managers, juristes, journalistes et dirigeants d'entreprise ont partagé leur expérience avec les professionnels sélectionnés.</p>
</div>
<figure style="margin: 0; justify-self: end; max-width: 300px">
<img src="{P}assets/affiche-lancement-phase2.jpg" alt="Affiche du lancement officiel de la phase 2 le 18 mars 2024 à l'Institut français de Yaoundé, en marge du Yaoundé Music Expo" loading="lazy" style="width: 100%; border-radius: 8px; box-shadow: 0 18px 40px rgba(0,0,0,.18)">
<figcaption style="font-size: 13px; margin-top: 8px">Lancement officiel de la phase 2, 18 mars 2024, Institut français de Yaoundé.</figcaption>
</figure>
</div>
<div class="grid4" style="gap: 16px">
''' + "".join(f'''<article class="carte personne rv"><img src="{P}assets/intervenants/intervenant-{i:02d}.jpg" alt="Portrait de {esc(n)}" loading="lazy" width="132" height="132"><span class="pays">{pays}</span><h3>{n}</h3><p>{role}</p></article>
''' for i, (n, role, pays) in enumerate(intervenants)) + f'''</div>
</div>
</section>

<section id="video" aria-labelledby="video-titre" style="background: var(--vert-nuit); color: var(--papier); padding: 104px 0">
<div class="wrap">
<div class="rv" style="max-width: 760px; margin-bottom: 36px">
<p style="margin: 0 0 16px; font-size: 13px; font-weight: 600; letter-spacing: .12em; text-transform: uppercase; color: var(--ambre)">En vidéo</p>
<h2 id="video-titre" class="serif" style="margin: 0; font-size: 44px; line-height: 1.1">Les Chantiers musicaux en quatre minutes</h2>
</div>
<figure class="rv video-cadre" style="margin: 0">
<video controls preload="none" playsinline poster="{P}assets/video-chantiers-poster.jpg" style="display: block; width: 100%; aspect-ratio: 1280 / 690; background: #000; border-radius: 12px">
<source src="{P}media/chantiers-ccm-2025.mp4" type="video/mp4">
Votre navigateur ne lit pas cette vidéo.
</video>
</figure>
</div>
</section>

<section id="contributeurs" class="section">
<div class="wrap grid2">
<div class="rv">
<p class="eyebrow">Le document</p>
<h2 class="h2">Ils ont contribué au schéma de développement</h2>
<p class="lead">Avec l'appui de nombreux professionnels remerciés dans le document, ces contributeurs ont rédigé l'<em>Introduction au schéma de développement de l'industrie musicale camerounaise</em>.</p>
<div style="display: flex; gap: 16px; margin-top: 32px; flex-wrap: wrap">
<a class="btn btn-vert" href="{P}docs/introduction-schema-developpement-industrie-musicale-camerounaise.pdf" download>Télécharger le document (FR)</a>
<a class="btn btn-contour" href="{P}docs/introduction-development-plan-cameroonian-music-industry.pdf" download lang="en">English version</a>
</div>
</div>
<dl class="rv" style="margin: 0; border-top: 1px solid var(--filet)">
''' + "".join(f'<div style="padding: 14px 0; border-bottom: 1px solid var(--filet)"><dt style="font-weight: 600">{n}</dt><dd style="margin: 2px 0 0; font-size: 15px; color: var(--gris)">{r}</dd></div>\n' for n, r in contributeurs) + f'''</dl>
</div>
</section>

<section id="galerie" aria-labelledby="galerie-titre" style="padding: 0 0 104px">
<div class="wrap">
<div class="rv" style="margin-bottom: 32px">
<p class="eyebrow">En images</p>
<h2 id="galerie-titre" class="serif" style="margin: 0; font-size: 34px; color: var(--vert)">Galerie</h2>
</div>
<div class="galerie rv" style="display: grid; grid-template-columns: repeat(4, minmax(0, 1fr)); grid-auto-rows: 210px; gap: 12px">
''' + "".join(f'<a href="{P}assets/{f}" style="{st}"><img class="photo" src="{P}assets/{f}" alt="{a}" loading="lazy" style="height: 100%; border-radius: 0"></a>\n' for f, a, st in [
    ("groupe-chantiers.jpg", "Photo de groupe des participants", "grid-column: span 2; grid-row: span 2"),
    ("salle-pleniere.jpg", "Salle plénière", ""),
    ("yaounde-intervention.jpg", "Intervention devant les participants à Yaoundé", ""),
    ("yaounde-public.jpg", "Participants attentifs lors d'un atelier", ""),
    ("atelier-echanges.jpg", "Échanges entre professionnels pendant un atelier", ""),
    ("atelier-promotion-phase2.jpg", "Affiche de l'atelier sur la promotion, phase 2", "grid-column: span 2"),
    ("experts.jpg", "Experts et formateurs réunis", ""),
    ("presse.jpg", "Interview presse lors des Chantiers musicaux", ""),
    ("atelier-entrepreneuriat-phase2.jpg", "Affiche de l'atelier sur l'entrepreneuriat, phase 2", "grid-column: span 2"),
]) + '''</div>
</div>
</section>
'''
html += pied()
ecrire("chantiers", html)

# ------------------------------------------------------------------ ACTUALITES
articles = [
    ("video", "2025 · Vidéo", "Les Chantiers musicaux du Cameroun racontés en quatre minutes", "video-chantiers-poster.jpg", "Écran titre de la vidéo des Chantiers musicaux",
     "Le CCM publie une vidéo de synthèse des Chantiers musicaux : de l'héritage du makossa et de « Soul Makossa » à la métamorphose numérique de l'industrie, des chiffres de la cartographie aux pistes du schéma de développement.",
     f'<a class="lien" href="{P}chantiers/#video">Voir la vidéo</a>'),
    ("restitution", "Juin 2024 · Publications", "Le schéma de développement présenté aux pouvoirs publics à Yaoundé", "yaounde-panel.jpg", "Table ronde de restitution",
     "Dernière étape des Chantiers musicaux, la restitution a permis de présenter l'<em>Introduction au schéma de développement de l'industrie musicale camerounaise</em> aux institutions et aux organisations professionnelles, en marge de la Zone by DOMAF. Le document dresse la cartographie de 3 199 professionnels, analyse les habitudes d'écoute et propose une stratégie globale : décentralisation, musique à l'école, application des lois, monétisation numérique, mobilité des artistes.",
     f'<a class="lien" href="{P}docs/introduction-schema-developpement-industrie-musicale-camerounaise.pdf" download>Télécharger le document</a>'),
    ("phase2", "18 mars 2024 · Formation", "Lancement de la phase 2 en marge du Yaoundé Music Expo", "affiche-lancement-phase2.jpg", "Affiche du lancement de la phase 2",
     "La deuxième étape des Chantiers musicaux a été officiellement lancée le 18 mars 2024 à l'Institut français de Yaoundé. Du 18 au 22 mars, des experts camerounais et internationaux venus du Nigéria, du Ghana, de Côte d'Ivoire, du Sénégal, de France et de Martinique ont animé plus de 16 ateliers sur la promotion, l'entrepreneuriat, la distribution et les droits.",
     f'<a class="lien" href="{P}chantiers/#intervenants">Découvrir les intervenants</a>'),
    ("lancement", "8 février 2024 · Programmes", "Lancement des Chantiers musicaux du Cameroun à Douala", "douala-phase1.jpg", "Ouverture des Chantiers musicaux à Douala",
     "Du 8 au 10 février 2024, 64 professionnels des dix régions se sont réunis à Douala pour dresser l'état des lieux de la musique camerounaise. Producteurs, promoteurs et diffuseurs ont travaillé par aires culturelles pour identifier les freins qui empêchent la filière d'éclore.",
     f'<a class="lien" href="{P}chantiers/">Le programme complet</a>'),
]
html = tete("actualites", "Actualités", "Les actualités du Conseil Camerounais de la Musique : Chantiers musicaux, publications, formations et vie du réseau.")
html += entete_page("Actualités", "La vie du Conseil", "Programmes, publications, formations : les dernières nouvelles du Conseil Camerounais de la Musique.", "Actualités")
html += '<section class="section" style="padding-top: 56px"><div class="wrap">\n' + "".join(f'''<article id="{i}" class="article rv">
<img src="{P}assets/{img}" alt="{alt}" loading="lazy">
<div>
<p class="date">{d}</p>
<h2>{t}</h2>
<p style="margin: 0 0 18px; font-size: 17px">{txt}</p>
{lien}
</div>
</article>
''' for i, d, t, img, alt, txt, lien in articles) + '</div></section>\n'
html += pied()
ecrire("actualites", html)
