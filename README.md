# Conseil Camerounais de la Musique — site web

Site du Conseil Camerounais de la Musique (CCM), association à but non lucratif fondée à Douala en 2009.

Site statique (HTML, CSS, JavaScript sans dépendance), publié avec GitHub Pages : https://manmbailikol.github.io/ccm-site/

## Pages

| Adresse | Contenu |
| --- | --- |
| `/` | Accueil (FR) |
| `/en/` | Accueil (EN) |
| `/institution/` | Mission, objectifs, histoire, les cinq droits de la musique, gouvernance |
| `/chantiers/` | Chantiers musicaux du Cameroun : étapes, intervenants de la phase 2, vidéo, contributeurs, galerie |
| `/observatoire/` | Cartographie des professionnels, marché potentiel, habitudes d'écoute, plateformes |
| `/annuaire/` | Annuaire des membres titulaires de la carte, avec recherche et filtres |
| `/actualites/` | Actualités du Conseil |

## Fichiers

- `assets/css/site.css` : feuille de style commune à toutes les pages
- `assets/js/site.js` : menu mobile, compteurs, lettre d'information (pages intérieures)
- `assets/membres/` : photos des membres (une par numéro de carte)
- `assets/intervenants/` : portraits des intervenants de la phase 2
- `docs/` : *Introduction au schéma de développement de l'industrie musicale camerounaise* (FR et EN, PDF compressés)
- `media/` : vidéo des Chantiers musicaux
- `sitemap.xml`, `robots.txt` : référencement

## Modifier les pages intérieures

Les pages intérieures sont générées par les scripts de `outils/` (Python 3, sans dépendance) :

```
cd outils
python3 pages2.py
```

- Ajouter ou modifier un membre de l'annuaire : éditer `outils/donnees/membres.json` (numéro, nom, métier, région, ville, validité, photo), déposer la photo dans `assets/membres/<numéro>.jpg`, puis relancer le script.
- Les textes des pages se trouvent dans `outils/pages.py` (institution, chantiers, actualités) et `outils/pages2.py` (observatoire, annuaire).

L'annuaire ne publie ni téléphone ni nationalité : les demandes de contact passent par infos@ccm-cmc.org.

## Statistiques de visite

Chaque page contient un repère `<!-- STATS -->` dans son en-tête. Une fois le compte GoatCounter créé, le remplacer par :

```html
<script data-goatcounter="https://NOM.goatcounter.com/count" async src="//gc.zgo.at/count.js"></script>
```

## Sources

Chiffres : CCM, *Introduction au schéma de développement de l'industrie musicale camerounaise*, 2024.
