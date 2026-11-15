# Gabarit commun des pages intérieures (FR)
import json

SITE = "https://manmbailikol.github.io/ccm-site/"
WA = "237690939633"

NAV = [
    ("institution", "L'institution"),
    ("chantiers", "Chantiers musicaux"),
    ("observatoire", "Observatoire"),
    ("annuaire", "Annuaire"),
    ("actualites", "Actualités"),
]


def tete(slug, titre, description, p="../"):
    return f'''<!doctype html>
<html lang="fr">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{titre} — Conseil Camerounais de la Musique</title>
<meta name="description" content="{description}">
<link rel="canonical" href="{SITE}{slug}/">
<link rel="alternate" hreflang="fr" href="{SITE}{slug}/">
<link rel="alternate" hreflang="en" href="{SITE}en/{slug}/">
<meta property="og:title" content="{titre} — Conseil Camerounais de la Musique">
<meta property="og:description" content="{description}">
<meta property="og:image" content="{SITE}assets/partage-ccm.jpg">
<meta property="og:type" content="website">
<meta property="og:locale" content="fr_FR">
<meta name="twitter:card" content="summary_large_image">
<meta name="theme-color" content="#106938">
<link rel="icon" href="{p}assets/logo-ccm.webp" type="image/webp">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,400;9..144,500;9..144,600&amp;family=Inter:wght@400;500;600;700&amp;family=Montserrat:ital,wght@0,500;0,700;0,800;1,500&amp;display=swap" rel="stylesheet">
<link rel="stylesheet" href="{p}assets/css/site.css">
<!-- STATS -->
</head>
<body>
<a class="evitement" href="#contenu">Aller au contenu</a>
<div class="ccm">
<div style="background: var(--vert-nuit); color: #d6e2d9; font-size: 13px">
<div class="wrap" style="display: flex; justify-content: space-between; align-items: center; min-height: 40px; gap: 16px; flex-wrap: wrap">
<span>Association à but non lucratif et apolitique · Membre du réseau du Conseil international de la musique</span>
<div style="display: flex; gap: 20px; align-items: center">
<a href="{p}annuaire/" style="color: #d6e2d9; text-decoration: none">Annuaire des professionnels</a>
<div role="group" aria-label="Langue" style="display: flex; gap: 4px">
<a href="./" aria-current="true" style="color: var(--ambre); font-weight: 700; text-decoration: none; padding: 4px 6px">FR</a>
<a href="{p}en/{slug}/" hreflang="en" lang="en" style="color: #d6e2d9; text-decoration: none; padding: 4px 6px">EN</a>
</div>
</div>
</div>
</div>
<header style="position: sticky; top: 0; z-index: 20; background: rgba(239,245,240,.94); backdrop-filter: blur(8px); border-bottom: 1px solid var(--filet)">
<div class="wrap" style="display: flex; align-items: center; justify-content: space-between; min-height: 88px; gap: 32px; position: relative">
<a href="{p}" aria-label="Conseil Camerounais de la Musique, accueil" style="display: flex; align-items: center">
<img src="{p}assets/logo-ccm.webp" alt="Logo du Conseil Camerounais de la Musique" style="height: 64px; width: auto; display: block">
</a>
<nav class="nav" id="nav-principale" aria-label="Navigation principale">
''' + "\n".join(
        f'<a href="{p}{s}/"' + (' aria-current="page"' if s == slug else '') + f'>{l}</a>' for s, l in NAV
    ) + f'''
<a href="#contact">Contact</a>
</nav>
<div style="display: flex; gap: 12px; align-items: center">
<a class="btn btn-vert entete-cta" href="{p}#adhesion">Devenir adhérent</a>
<button type="button" id="menu-btn" class="menu-btn" aria-expanded="false" aria-controls="nav-principale" aria-label="Ouvrir le menu"><svg aria-hidden="true" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><path d="M4 7h16M4 12h16M4 17h16"></path></svg></button>
</div>
</div>
</header>
<main id="contenu">
'''


def entete_page(fil, titre, intro, surtitre=""):
    eq = "".join("<span></span>" for _ in range(12))
    sur = f'<p style="margin: 0 0 16px; font-size: 13px; font-weight: 600; letter-spacing: .12em; text-transform: uppercase; color: var(--ambre)">{surtitre}</p>' if surtitre else ""
    return f'''<section class="page-tete">
<div class="wrap">
<p class="fil entree"><a href="../">Accueil</a> › {fil}</p>
{sur}
<h1 class="entree d1">{titre}</h1>
<p class="intro entree d2">{intro}</p>
</div>
<div class="eq" aria-hidden="true">{eq}</div>
</section>
'''


def pied(p="../", js_page=""):
    return f'''</main>
<footer id="contact" class="pied" style="background: var(--vert-nuit); color: #d6e2d9; font-size: 15px">
<div class="wrap pied-grille" style="display: grid; grid-template-columns: 1.4fr 1fr 1fr 1.4fr; gap: 48px; padding-top: 72px; padding-bottom: 56px">
<div>
<p class="serif" style="margin: 0 0 12px; font-size: 24px; color: var(--papier)">Conseil Camerounais de la Musique</p>
<p style="margin: 0">Pour un environnement plus favorable à la musique camerounaise.</p>
<address style="font-style: normal; margin-top: 24px; line-height: 1.8">
Bonamoussadi, Antenne Kotto<br>Douala, Cameroun<br>
<a href="tel:+237690939633">+237 690 939 633</a> · <a href="tel:+237653807653">653 807 653</a><br>
<a href="mailto:infos@ccm-cmc.org">infos@ccm-cmc.org</a>
</address>
</div>
<nav aria-label="L'institution">
<p style="margin: 0 0 16px; color: var(--papier); font-weight: 600">L'institution</p>
<ul style="list-style: none; margin: 0; padding: 0; display: grid; gap: 10px">
<li><a href="{p}institution/">Mission et histoire</a></li><li><a href="{p}institution/#gouvernance">Gouvernance</a></li><li><a href="{p}institution/#droits">Les cinq droits de la musique</a></li><li><a href="{p}actualites/">Actualités</a></li>
</ul>
</nav>
<nav aria-label="Agir">
<p style="margin: 0 0 16px; color: var(--papier); font-weight: 600">Agir</p>
<ul style="list-style: none; margin: 0; padding: 0; display: grid; gap: 10px">
<li><a href="{p}chantiers/">Chantiers musicaux</a></li><li><a href="{p}observatoire/">Observatoire</a></li><li><a href="{p}annuaire/">Annuaire des membres</a></li><li><a href="{p}#adhesion">Adhésion</a></li>
</ul>
</nav>
<form id="form-lettre" aria-label="Lettre d'information" style="display: flex; flex-direction: column; gap: 12px">
<p style="margin: 0 0 4px; color: var(--papier); font-weight: 600">Lettre d'information</p>
<label for="courriel" style="font-size: 14px">Recevez l'actualité du Conseil</label>
<div style="display: flex; gap: 8px">
<input id="courriel" type="email" autocomplete="email" placeholder="votre@adresse.cm" style="flex: 1; min-width: 0; min-height: 48px; padding: 0 14px; border-radius: 4px; border: 1px solid #3d5a46; background: #0b3a1d; color: var(--papier)">
<button type="submit" class="btn btn-ambre">S'inscrire</button>
</div>
</form>
</div>
<div style="border-top: 1px solid #1d4a2c">
<div class="wrap" style="display: flex; justify-content: space-between; gap: 16px; flex-wrap: wrap; padding-top: 20px; padding-bottom: 20px; font-size: 13px">
<span>© 2026 Conseil Camerounais de la Musique. Tous droits réservés.</span>
<a href="{p}">Retour à l'accueil</a>
</div>
</div>
</footer>
</div>
<a class="whatsapp" href="https://wa.me/{WA}" target="_blank" rel="noopener" aria-label="Écrire au CCM sur WhatsApp"><svg aria-hidden="true" width="22" height="22" viewBox="0 0 24 24" fill="currentColor"><path d="M12 2a10 10 0 0 0-8.6 15.1L2 22l5-1.3A10 10 0 1 0 12 2zm0 18.2a8.2 8.2 0 0 1-4.2-1.2l-.3-.2-3 .8.8-2.9-.2-.3A8.2 8.2 0 1 1 12 20.2zm4.5-6.1c-.2-.1-1.5-.7-1.7-.8s-.4-.1-.6.1-.7.8-.8 1-.3.2-.5.1a6.7 6.7 0 0 1-3.3-2.9c-.3-.4.2-.4.7-1.3a.4.4 0 0 0 0-.4l-.8-1.8c-.2-.5-.4-.4-.6-.4h-.5a1 1 0 0 0-.7.3 3 3 0 0 0-.9 2.2 5.2 5.2 0 0 0 1.1 2.7 11.8 11.8 0 0 0 4.5 4c1.7.7 2.3.8 3.2.6a2.7 2.7 0 0 0 1.8-1.3 2.2 2.2 0 0 0 .1-1.3c0-.1-.2-.2-.5-.3z"/></svg><span>Écrire au CCM</span></a>
<script src="{p}assets/js/site.js"></script>
{js_page}
</body>
</html>
'''


def esc(s):
    return (s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;").replace('"', "&quot;"))
