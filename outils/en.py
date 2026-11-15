# Génère la version anglaise des pages intérieures à partir des pages françaises.
# Lancer après pages2.py :  python3 en.py
import os, re
OUT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
SITE = "https://manmbailikol.github.io/ccm-site/"
PAGES = ["institution", "chantiers", "observatoire", "annuaire", "actualites"]

T = {
# commun
"Aller au contenu": "Skip to content",
"Association à but non lucratif et apolitique · Membre du réseau du Conseil international de la musique": "Non-profit, non-political association · Member of the International Music Council network",
"Annuaire des professionnels": "Directory of professionals", "Langue": "Language",
"Conseil Camerounais de la Musique, accueil": "Cameroon Music Council, home",
"Logo du Conseil Camerounais de la Musique": "Cameroon Music Council logo",
"Navigation principale": "Main navigation", "L'institution": "The institution", "Chantiers musicaux": "Music Worksites",
"Observatoire": "Observatory", "Annuaire": "Directory", "Actualités": "News", "Devenir adhérent": "Become a member",
"Ouvrir le menu": "Open menu", "Accueil": "Home",
"Pour un environnement plus favorable à la musique camerounaise.": "For a better environment for Cameroonian music.",
"Douala, Cameroun": "Douala, Cameroon", "Mission et histoire": "Mission and history", "Gouvernance": "Governance",
"Les cinq droits de la musique": "The five music rights", "Agir": "Get involved", "Annuaire des membres": "Member directory",
"Adhésion": "Membership", "Lettre d'information": "Newsletter", "Recevez l'actualité du Conseil": "Get the Council's news",
"votre@adresse.cm": "you@example.com", "S'inscrire": "Subscribe",
"© 2026 Conseil Camerounais de la Musique. Tous droits réservés.": "© 2026 Cameroon Music Council (Conseil Camerounais de la Musique). All rights reserved.",
"Retour à l'accueil": "Back to home", "Écrire au CCM sur WhatsApp": "Message the CCM on WhatsApp", "Écrire au CCM": "Message the CCM",
"Chiffres clés": "Key figures",
# institution
"L'institution — Conseil Camerounais de la Musique": "The institution — Cameroon Music Council",
"Mission, histoire, gouvernance et valeurs du Conseil Camerounais de la Musique, association nationale membre du réseau du Conseil international de la musique.": "Mission, history, governance and values of the Cameroon Music Council, the national association in the International Music Council network.",
"› L'institution": "› The institution",
"Structurer la filière musicale, avec tous ses acteurs": "Structuring the music sector, with all its players",
"Association à but non lucratif et apolitique, le Conseil Camerounais de la Musique rassemble musiciens, arrangeurs, formateurs, chercheurs, musicologues, critiques, producteurs, sonorisateurs, diffuseurs, éditeurs, promoteurs et spécialistes des droits d'auteur.": "A non-profit, non-political association, the Cameroon Music Council brings together musicians, arrangers, trainers, researchers, musicologists, critics, producers, sound engineers, broadcasters, publishers, promoters and copyright specialists.",
"Notre mission": "Our mission",
"Une force de proposition auprès des institutions nationales et internationales": "A driving force with national and international institutions",
"Le CCM structure l'industrie musicale au Cameroun en veillant à l'épanouissement des acteurs. Il soutient la création, facilite la diffusion des œuvres, encourage l'éducation musicale des jeunes, documente et valorise le patrimoine, et veille au statut des musiciens comme à la protection de leurs droits.": "The CCM structures the music industry in Cameroon while ensuring that its players thrive. It supports creation, helps works reach audiences, encourages music education for young people, documents and promotes the heritage, and safeguards musicians' status and rights.",
"Sur le plan socio-économique, il contribue à la création de richesses et d'emplois, et plaide auprès du ministère de l'Économie, de la Planification et de l'Aménagement du territoire pour que la musique soit prise en compte dans la Stratégie nationale de développement 2020-2030 (SND30).": "On the socio-economic front, it contributes to wealth and job creation, and advocates with the Ministry of the Economy, Planning and Regional Development for music to be included in the National Development Strategy 2020-2030 (SND30).",
"Relier": "Connect", "Contribuer au renforcement des relations entre toutes les parties prenantes du secteur musical et à une meilleure structuration de l'industrie musicale au Cameroun.": "Strengthen relations between all stakeholders in the music sector and help structure the music industry in Cameroon.",
"Mailler": "Network", "Créer et structurer un réseau de professionnels sur tout le territoire.": "Build and structure a network of professionals across the country.",
"Rassembler": "Unite", "Renforcer les relations entre les associations et les entreprises musicales.": "Strengthen ties between music associations and companies.",
"Animer": "Engage", "Encourager l'organisation de séminaires, festivals, concerts, ateliers et réunions d'experts.": "Encourage seminars, festivals, concerts, workshops and expert meetings.",
"Former": "Train", "Contribuer à la formation et à la professionnalisation des acteurs camerounais de la musique.": "Help train and professionalise Cameroonian music professionals.",
"Structurer": "Structure", "Participer à l'élaboration d'une structuration de l'industrie musicale au Cameroun.": "Take part in designing the structure of the music industry in Cameroon.",
"Histoire": "History", "Né du Conseil international de la musique": "Born of the International Music Council",
"Le CCM est l'association nationale qui représente le Cameroun dans le réseau du Conseil international de la musique, fondé en 1949 à l'initiative de l'UNESCO.": "The CCM is the national association representing Cameroon in the network of the International Music Council, founded in 1949 at UNESCO's initiative.",
"Le Conseil international de la musique proclame, lors de son assemblée générale, les cinq droits de la musique.": "At its General Assembly, the International Music Council proclaims the five music rights.",
"Lors de la 30": "At the 30", "e": "th",
"assemblée générale du CIM, le Cameroun est admis comme membre, à la demande motivée de Luc Yatchokeu, alors président de l'association CIGALE. Le CIM demande la création d'une association nationale dédiée.": "IMC General Assembly, Cameroon is admitted as a member, following a reasoned application by Luc Yatchokeu, then president of the CIGALE association. The IMC asks for a dedicated national association to be created.",
"Fondation du Conseil Camerounais de la Musique sous l'égide du professeur Lupwishi Mbuyamba, coordonnateur régional du CIM en Afrique. Enregistrement à Douala le 14 septembre 2009 (n° 133/2009/RDDA/C19/BAPP).": "The Cameroon Music Council is founded under the aegis of Professor Lupwishi Mbuyamba, IMC regional coordinator for Africa. Registered in Douala on 14 September 2009 (no. 133/2009/RDDA/C19/BAPP).",
"Assemblées générales ordinaire et extraordinaire du 31 mars à Yaoundé : statuts amendés et nouveau bureau exécutif élu.": "Ordinary and extraordinary General Assemblies held in Yaoundé on 31 March: statutes amended and a new executive board elected.",
"Les Chantiers musicaux du Cameroun réunissent 64 professionnels des dix régions et aboutissent à l'": "The Cameroon Music Worksites bring together 64 professionals from all ten regions and lead to the ",
"Introduction au schéma de développement de l'industrie musicale camerounaise": "Introduction to the Development Plan of the Cameroonian Music Industry",
"Lancement de l'annuaire en ligne des membres titulaires de la carte du CCM.": "Launch of the online directory of CCM card-holding members.",
"Nos valeurs": "Our values", "Proclamés en 2001 par le Conseil international de la musique, ils guident l'action du CCM au Cameroun.": "Proclaimed in 2001 by the International Music Council, they guide the CCM's work in Cameroon.",
"Le droit pour les enfants et les adultes de s'exprimer musicalement en toute liberté.": "The right for all children and adults to express themselves musically in all freedom.",
"Le droit d'apprendre et d'étudier les langages et savoir-faire musicaux.": "The right to learn musical languages and skills.",
"Le droit d'accéder à la musique par la participation, l'écoute, la création et l'information.": "The right to have access to musical involvement through participation, listening, creation and information.",
"Le droit pour les artistes musicaux de développer leur art et de le communiquer à travers tous les médias, avec des outils et des structures appropriés.": "The right for musical artists to develop their artistry and communicate through all media, with proper facilities at their disposal.",
"Le droit pour les artistes musicaux d'obtenir une juste reconnaissance et une rémunération équitable pour leur travail.": "The right for musical artists to obtain just recognition and fair remuneration for their work.",
"Une association transparente et démocratique": "A transparent, democratic association",
"Les statuts du CCM ont été amendés et son bureau exécutif élu lors des assemblées générales du 31 mars 2021 à Yaoundé.": "The CCM's statutes were amended and its executive board elected at the General Assemblies held in Yaoundé on 31 March 2021.",
"Didier Ngadjui Toko, président du Conseil Camerounais de la Musique": "Didier Ngadjui Toko, President of the Cameroon Music Council",
"Président": "President", "Entrepreneur culturel, expert du secteur musical pour la zone Afrique-Caraïbes-Pacifique": "Cultural entrepreneur, music sector expert for the Africa-Caribbean-Pacific region",
"Les organes du Conseil": "The Council's bodies", "Assemblée générale": "General Assembly", "Constituée de tous les membres.": "Made up of all members.",
"Bureau exécutif": "Executive Board", "Un président, deux vice-présidents, un secrétaire général et son adjoint, un trésorier, un responsable de la communication et deux responsables des opérations, l'un à Douala, l'autre à Yaoundé.": "A president, two vice-presidents, a secretary general and deputy, a treasurer, a communications officer and two operations officers, one in Douala and one in Yaoundé.",
"Observatoire de la musique": "Music Observatory",
"Organe interne habilité à fournir des arguments techniques pour les relations du CCM avec le ministère des Arts et de la Culture, les collectivités territoriales décentralisées et les autres institutions. Il remet chaque année un rapport au bureau exécutif.": "Internal body providing technical evidence for the CCM's dealings with the Ministry of Arts and Culture, local authorities and other institutions. It submits an annual report to the executive board.",
"Commissions": "Committees", "Commission financière, commission juridique et commission chargée de l'appui aux initiatives musicales.": "Finance committee, legal committee and committee supporting music initiatives.",
"Comité consultatif": "Advisory committee", "Veille au bon fonctionnement du CCM selon la vision du Conseil international de la musique et les bonnes pratiques recommandées par les institutions nationales et internationales.": "Oversees the proper running of the CCM in line with the vision of the International Music Council and the good practices recommended by national and international institutions.",
"Représentants régionaux": "Regional representatives", "Personnes physiques ou morales membres du CCM, chargées de représenter l'association et de relayer ses activités dans leur région.": "Individual or corporate CCM members who represent the association and relay its activities in their region.",
"Rejoignez le réseau des professionnels de la musique au Cameroun.": "Join the network of music professionals in Cameroon.",
"Devenir membre": "Become a member", "Voir l'annuaire": "Browse the directory",
# chantiers
"Les Chantiers musicaux du Cameroun — Conseil Camerounais de la Musique": "The Cameroon Music Worksites — Cameroon Music Council",
"Les Chantiers musicaux du Cameroun : trois étapes à Douala et Yaoundé en 2024, 64 professionnels, des experts internationaux et un schéma de développement de l'industrie musicale.": "The Cameroon Music Worksites: three stages in Douala and Yaoundé in 2024, 64 professionals, international experts and a development plan for the music industry.",
"› Chantiers musicaux": "› Music Worksites", "Programme phare · 2024": "Flagship programme · 2024",
"Les Chantiers musicaux du Cameroun": "The Cameroon Music Worksites",
"Plus de six mois de concertation, en 2024, pour diagnostiquer la filière, renforcer ses acteurs et poser les bases d'un schéma de développement. Avec le soutien de l'Ambassade de France au Cameroun et de l'Institut français, dans le cadre du Fonds Équipe France.": "More than six months of consultation in 2024 to assess the sector, strengthen its players and lay the foundations of a development plan. Supported by the French Embassy in Cameroon and the Institut français, through the Team France Fund.",
"professionnels des dix régions": "professionals from all ten regions", "étapes à Douala et Yaoundé": "stages in Douala and Yaoundé",
"intervenants présentés pour la phase 2": "speakers featured in phase 2", "pages pour le schéma de développement": "pages in the development plan",
"Logo des Chantiers musicaux du Cameroun": "Cameroon Music Worksites logo", "Le déroulé": "How it unfolded",
"Trois étapes, de l'état des lieux à la stratégie": "Three stages, from assessment to strategy",
"Prise de parole lors de la première étape à Douala": "Speech during the first stage in Douala",
"Étape 01 · Douala · 8 au 10 février 2024": "Stage 01 · Douala · 8 to 10 February 2024", "L'état des lieux": "Assessing the situation",
"64 professionnels des dix régions, issus de la production, de la promotion et de la diffusion, ont travaillé en ateliers par grandes aires culturelles : septentrion, Grassfields, peuples de la forêt et Grand Sawa. Objectif : comprendre comment fonctionne le secteur et identifier ce qui l'empêche d'éclore.": "64 professionals from all ten regions, working in production, promotion and broadcasting, met in workshops by major cultural area: the North, the Grassfields, the forest peoples and the Greater Sawa. The goal: understand how the sector works and identify what is holding it back.",
"21 producteurs": "21 producers", "20 acteurs de la promotion": "20 promotion professionals", "23 acteurs de la diffusion": "23 broadcasting professionals",
"Atelier de renforcement de capacités à Yaoundé": "Capacity-building workshop in Yaoundé",
"Étape 02 · Yaoundé · 18 au 22 mars 2024": "Stage 02 · Yaoundé · 18 to 22 March 2024", "Le renforcement des capacités": "Capacity building",
"Lancée le 18 mars 2024 à la médiathèque de l'Institut français de Yaoundé, en marge du Yaoundé Music Expo, la deuxième étape a proposé plus de 16 ateliers : gestion de projets musicaux, marketing digital, distribution, droits d'auteur et droits voisins, entrepreneuriat, stratégies de diffusion.": "Launched on 18 March 2024 at the Institut français library in Yaoundé, alongside the Yaoundé Music Expo, the second stage offered more than 16 workshops: music project management, digital marketing, distribution, copyright and related rights, entrepreneurship, broadcasting strategies.",
"Plus de 16 ateliers": "More than 16 workshops", "12 experts internationaux": "12 international experts", "25 formateurs camerounais": "25 Cameroonian trainers",
"Table ronde de restitution": "Round table presenting the findings", "Étape 03 · Yaoundé · juin 2024": "Stage 03 · Yaoundé · June 2024", "La restitution": "Presenting the findings",
"L'": "The ",
"a été présentée aux pouvoirs publics, aux institutions et aux organisations professionnelles, en marge de la Zone by DOMAF, pour contribuer à une politique culturelle nationale.": "was presented to public authorities, institutions and professional organisations, alongside Zone by DOMAF, as a contribution to a national cultural policy.",
"Document de 144 pages": "144-page document", "Versions française et anglaise": "French and English editions", "Prochaine étape : un schéma stratégique complet": "Next step: a full strategic plan",
"Phase 2 · Yaoundé, 18 au 22 mars 2024": "Phase 2 · Yaoundé, 18 to 22 March 2024", "Les intervenants": "The speakers",
"Experts camerounais et internationaux, artistes, managers, juristes, journalistes et dirigeants d'entreprise ont partagé leur expérience avec les professionnels sélectionnés.": "Cameroonian and international experts, artists, managers, lawyers, journalists and business leaders shared their experience with the selected professionals.",
"Affiche du lancement officiel de la phase 2 le 18 mars 2024 à l'Institut français de Yaoundé, en marge du Yaoundé Music Expo": "Poster for the official launch of phase 2 on 18 March 2024 at the Institut français in Yaoundé, alongside the Yaoundé Music Expo",
"Lancement officiel de la phase 2, 18 mars 2024, Institut français de Yaoundé.": "Official launch of phase 2, 18 March 2024, Institut français, Yaoundé.",
"Cameroun": "Cameroon", "Côte d'Ivoire": "Côte d'Ivoire", "Nigéria": "Nigeria", "Guinée": "Guinea", "Sénégal": "Senegal",
"Directeur général de Keyzit Cameroun, fondateur d'Arise Entertainment": "Managing Director of Keyzit Cameroun, founder of Arise Entertainment",
"Directeur du sponsoring, Orange Cameroun": "Head of Sponsorship, Orange Cameroun", "Artiste, manager et consultant": "Artist, manager and consultant",
"Responsable chez FOCEP S.A.": "Manager at FOCEP S.A.", "Consultant spécialiste du marketing et de la publicité": "Marketing and advertising consultant",
"PDG du groupe ICONProd, fondateur du label ICON Fusion": "CEO of the ICONProd group, founder of the ICON Fusion label",
"Consultant marketing et go-to-market": "Marketing and go-to-market consultant", "Autrice-compositrice-interprète": "Singer-songwriter",
"Directrice artistique de Seize mètres carrés": "Artistic director of Seize mètres carrés", "Journaliste culturel, fondateur de Radio Afrika": "Cultural journalist, founder of Radio Afrika",
"Fondateur de Ckrowd.com, président de KAM Africa": "Founder of Ckrowd.com, president of KAM Africa", "Producteur, multi-instrumentiste et compositeur": "Producer, multi-instrumentalist and composer",
"Fondatrice de La Neuvième Muse": "Founder of La Neuvième Muse", "Directrice de la programmation, Trace Mboa": "Head of Programming, Trace Mboa",
"Auteur-compositeur-interprète": "Singer-songwriter", "Cofondateur d'Aftown Music": "Co-founder of Aftown Music", "Associé, HighTower Solicitors and Advocates": "Partner, HighTower Solicitors and Advocates",
"En vidéo": "On video", "Les Chantiers musicaux en quatre minutes": "The Music Worksites in four minutes",
"Votre navigateur ne lit pas cette vidéo.": "Your browser cannot play this video.", "Le document": "The document",
"Ils ont contribué au schéma de développement": "Contributors to the development plan",
"Avec l'appui de nombreux professionnels remerciés dans le document, ces contributeurs ont rédigé l'": "With support from many professionals thanked in the document, these contributors wrote the ",
"Télécharger le document (FR)": "Download (French)", "English version": "Download (English)",
"Expert en stratégie commerciale et marketing": "Sales and marketing strategy expert", "Analyste marketing senior": "Senior marketing analyst",
"Artiste musicien, manager, président du conseil d'administration de The Music Club": "Musician, manager, chairman of The Music Club",
"Auteur, spécialiste de la musique et du digital en Afrique francophone": "Author, specialist in music and digital in French-speaking Africa",
"Ingénieur culturel, fondateur d'Arise Entertainment": "Cultural engineer, founder of Arise Entertainment",
"Ingénieur culturel, fondateur et ancien président du CCM": "Cultural engineer, founder and former president of the CCM",
"Professionnel de la stratégie et du marketing": "Strategy and marketing professional", "Gestionnaire d'entreprise, spécialiste du marketing": "Business manager, marketing specialist",
"En images": "In pictures", "Galerie": "Gallery", "Photo de groupe des participants": "Group photo of the participants", "Salle plénière": "Plenary room",
"Intervention devant les participants à Yaoundé": "Presentation to participants in Yaoundé", "Participants attentifs lors d'un atelier": "Participants during a workshop",
"Échanges entre professionnels pendant un atelier": "Professionals talking during a workshop", "Affiche de l'atelier sur la promotion, phase 2": "Poster for the promotion workshop, phase 2",
"Experts et formateurs réunis": "Experts and trainers together", "Interview presse lors des Chantiers musicaux": "Press interview at the Music Worksites",
"Affiche de l'atelier sur l'entrepreneuriat, phase 2": "Poster for the entrepreneurship workshop, phase 2",
# observatoire
"Observatoire de la musique — Conseil Camerounais de la Musique": "Music Observatory — Cameroon Music Council",
"Les chiffres de la musique au Cameroun : cartographie des 3 199 professionnels, marché potentiel, habitudes d'écoute, plateformes et attentes des auditeurs, d'après le CCM (2024).": "Music in Cameroon in figures: mapping of 3,199 professionals, potential market, listening habits, platforms and listener expectations, from the CCM (2024).",
"› Observatoire": "› Observatory", "Comprendre la musique camerounaise, chiffres à l'appui": "Understanding Cameroonian music, with the figures to prove it",
"Les données de l'étude menée par le CCM au premier semestre 2024 à Douala, Yaoundé, Bafoussam et Garoua, et de la cartographie des professionnels de la filière.": "Data from the study carried out by the CCM in the first half of 2024 in Douala, Yaoundé, Bafoussam and Garoua, and from its mapping of the sector's professionals.",
"d'habitants au Cameroun, avec une croissance de 2,51 % par an": "people live in Cameroon, with 2.51% growth a year",
"de la population a entre 10 et 74 ans": "of the population is aged 10 to 74",
"de consommateurs potentiels de musique, compte tenu du taux de pauvreté (38,6 %)": "potential music consumers, allowing for the poverty rate (38.6%)",
"professionnels recensés dans la base de données du CCM": "professionals listed in the CCM database",
"Cartographie des professionnels": "Mapping the professionals", "Qui fait la musique au Cameroun ?": "Who makes music in Cameroon?",
"Thèmes de la cartographie": "Mapping topics", "Le marché potentiel": "The potential market",
"Combien vaut la vente directe de musique ?": "How much are direct music sales worth?",
"Simulation du CCM : 12 027 032 consommateurs potentiels achètent des chansons au prix pratiqué par les « téléchargeurs », 50 ou 100 FCFA. Choisissez un scénario pour voir le chiffre d'affaires par tranche d'âge.": "CCM simulation: 12,027,032 potential consumers buy songs at the price charged by local download vendors, 50 or 100 FCFA. Pick a scenario to see revenue by age group.",
"Chansons achetées par personne et par an": "Songs bought per person per year", "Chansons par an": "Songs per year", "Prix par chanson": "Price per song",
"Chiffre d'affaires par tranche d'âge": "Revenue by age group", "Tranche d'âge": "Age group", "Consommateurs": "Consumers", "Chiffre d'affaires (FCFA)": "Revenue (FCFA)",
"Scénario": "Scenario", "de chiffre d'affaires par an": "in revenue per year",
"Jeunes, 10 à 29 ans": "Young people, 10 to 29", "Adultes, 30 à 49 ans": "Adults, 30 to 49", "Seniors, 50 à 74 ans": "Seniors, 50 to 74",
"Le parcours d'écoute": "The listening journey", "Des réseaux sociaux au « téléchargeur »": "From social media to the download vendor",
"La découverte commence souvent sur TikTok et Instagram ; elle se termine le plus souvent par un fichier partagé via Xender par l'entourage, ou par l'achat d'une chanson à 50 ou 100 FCFA auprès d'un téléchargeur.": "Discovery often starts on TikTok and Instagram; it usually ends with a file shared by friends via Xender, or with a song bought for 50 or 100 FCFA from a download vendor.",
"Les audiences": "Audiences", "Téléspectateurs": "TV viewers", "Internautes": "Internet users", "Auditeurs de radio": "Radio listeners", "Utilisateurs des réseaux sociaux": "Social media users",
"bars et snack-bars sonorisés.": "bars and snack bars with sound systems.",
"Les lieux de consommation hors domicile, avec la télévision et la radio, restent les grands vecteurs de nouveautés. Pour retrouver un titre, on utilise Shazam ou l'on demande au DJ.": "Bars and other out-of-home venues, along with TV and radio, remain the main channels for new music. To find a song, people use Shazam or ask the DJ.",
"Les quatre routines d'écoute": "The four listening routines", "5 h – 9 h": "5 am – 9 am", "Le matin, à la maison": "Morning, at home",
"Les adultes préfèrent la douceur du gospel, souvent en guise de prière du matin. Les adolescents choisissent des musiques fortes et dansantes, comme le mbolé ou le rap, écoutées seuls dans la chambre ou pendant les travaux ménagers.": "Adults prefer gentle gospel, often as a morning prayer. Teenagers choose loud, danceable music such as mbolé or rap, played alone in their room or while doing chores.",
"Téléphone, enceinte Bluetooth, télévision, applications": "Phone, Bluetooth speaker, TV, apps", "10 h – 18 h": "10 am – 6 pm", "Tout au long de la journée": "Throughout the day",
"La plupart des adultes n'écoutent pas de musique, pris par leurs occupations. Une bonne journée finit en chanson festive ; une mauvaise, souvent sans musique. Les jeunes passent du rythmé au plus doux, puis reviennent au fort.": "Most adults do not listen to music, busy with work. A good day ends with a festive song; a bad one, often with no music. Young people move from upbeat to gentler music, then back to loud.",
"Téléphone, enceinte Bluetooth, télévision, radio": "Phone, Bluetooth speaker, TV, radio", "19 h – 22 h": "7 pm – 10 pm", "Le soir, à la maison": "Evening, at home",
"Quand ils ne sortent pas, les auditeurs choisissent des musiques qui leur parlent personnellement, loin des musiques d'ambiance faites pour danser.": "When they stay in, listeners choose music that speaks to them personally, away from party music made for dancing.",
"Téléphone, enceinte Bluetooth, télévision": "Phone, Bluetooth speaker, TV", "19 h – tard": "7 pm – late", "Le soir, en sortie": "Evening, going out",
"En groupe, chacun tait ses goûts : au bar, place à la musique très rythmée et au volume élevé. Plus tard, snack-bars et boîtes de nuit prennent le relais avec un son de meilleure qualité.": "In a group, personal tastes take a back seat: at the bar, it is upbeat music at high volume. Later, snack bars and nightclubs take over with better sound.",
"Sonorisation du bar, musique live, platines DJ": "Bar sound system, live music, DJ decks",
"Ce que veulent les auditeurs": "What listeners want", "Le moyen d'écoute idéal": "The ideal way to listen",
"Résultat d'un exercice projectif mené en avril 2024 auprès d'adolescents, de jeunes adultes et de quadragénaires à Yaoundé, Douala, Bafoussam et Maroua.": "Findings from a projective exercise carried out in April 2024 with teenagers, young adults and people in their forties in Yaoundé, Douala, Bafoussam and Maroua.",
"« Je paie déjà pour ma connexion, l'application devrait être gratuite ! »": "“I already pay for my data, the app should be free!”",
"Constant, quadragénaire, Yaoundé": "Constant, in his forties, Yaoundé",
"Idéalement être gratuit, ou ne pas multiplier les paiements": "Ideally be free, or avoid multiple payments", "Permettre d'acheter des chansons à l'unité, autour de 100 FCFA": "Let people buy single songs, for around 100 FCFA",
"Confirmer chaque achat par SMS, avec le montant et le titre": "Confirm each purchase by text message, with the amount and the title", "Proposer un large catalogue, par genre, artiste et pays": "Offer a broad catalogue, by genre, artist and country",
"Fonctionner sur iOS, Android et même sur les téléphones simples": "Work on iOS, Android and even basic phones", "Prévenir des nouveautés par SMS, même hors connexion": "Announce new releases by text message, even offline",
"Réduire les publicités": "Show fewer ads", "Permettre aux auditeurs de laisser un avis aux auteurs": "Let listeners leave feedback for the songwriters",
"Les moyens digitaux": "Digital channels", "Les plateformes utilisées au Cameroun": "Platforms used in Cameroon",
"Boomplay revendique 1,5 million d'utilisateurs camerounais, contre 4 700 comptes payants cumulés sur Spotify, Apple Music et Deezer. YouTube et Spotify, les plus utilisées au monde, ne permettent pas encore aux artistes camerounais de monétiser leurs écoutes.": "Boomplay claims 1.5 million Cameroonian users, against 4,700 paid accounts across Spotify, Apple Music and Deezer combined. YouTube and Spotify, the most used platforms in the world, do not yet let Cameroonian artists monetise their streams.",
"Sources : CCM,": "Sources: CCM,",
", 2024, d'après la base de données du CCM, l'ONU (World Population Prospects 2024), l'INS (ECAM5), GSMA, Statista, Datareportal et l'IFPI.": ", 2024, based on the CCM database, the UN (World Population Prospects 2024), the INS (ECAM5), GSMA, Statista, Datareportal and the IFPI.",
"Télécharger le rapport complet": "Download the full report",
# annuaire
"Annuaire des membres — Conseil Camerounais de la Musique": "Member directory — Cameroon Music Council",
"› Annuaire": "› Directory", "L'annuaire des membres du CCM": "The CCM member directory",
"Les professionnels de la musique titulaires de la carte de membre du Conseil Camerounais de la Musique. Trouvez un partenaire par région, par ville ou par métier, et contactez-le par l'intermédiaire du CCM.": "Music professionals holding a Cameroon Music Council membership card. Find a partner by region, city or profession, and contact them through the CCM.",
"Chiffres de l'annuaire": "Directory figures", "membres titulaires de la carte": "card-holding members", "régions représentées sur 10": "of the 10 regions represented",
"villes": "cities", "cartes valables jusqu'en janvier": "cards valid until January",
"Rechercher dans l'annuaire": "Search the directory", "Rechercher un nom, une ville, un métier": "Search for a name, city or profession",
"Ex. Douala, producteur…": "E.g. Douala, producer…", "Région": "Region", "Toutes les régions": "All regions", "Métier": "Profession", "Tous les métiers": "All professions",
"Réinitialiser": "Reset", "Les membres par région": "Members by region", "Extrême-Nord": "Far North", "Sud-Ouest": "South-West", "Nord": "North", "Sud": "South",
"Est": "East", "Ouest": "West", "Nord-Ouest": "North-West", "À propos de cet annuaire": "About this directory",
"Pour protéger la vie privée des membres, les numéros de téléphone et les nationalités ne sont pas publiés. Chaque demande de contact passe par le secrétariat du CCM, qui la transmet au membre concerné.": "To protect members' privacy, phone numbers and nationalities are not published. Every contact request goes through the CCM secretariat, which forwards it to the member.",
"Vous êtes membre et souhaitez modifier ou retirer votre fiche ?": "Are you a member and want to update or remove your listing?", "Écrivez-nous": "Write to us",
"Vous n'êtes pas encore membre ?": "Not a member yet?", "Demander ma carte de membre": "Apply for my membership card",
# actualites
"Actualités — Conseil Camerounais de la Musique": "News — Cameroon Music Council",
"Les actualités du Conseil Camerounais de la Musique : Chantiers musicaux, publications, formations et vie du réseau.": "News from the Cameroon Music Council: Music Worksites, publications, training and network life.",
"› Actualités": "› News", "La vie du Conseil": "Council news",
"Programmes, publications, formations : les dernières nouvelles du Conseil Camerounais de la Musique.": "Programmes, publications, training: the latest from the Cameroon Music Council.",
"Écran titre de la vidéo des Chantiers musicaux": "Title screen of the Music Worksites video", "2025 · Vidéo": "2025 · Video",
"Les Chantiers musicaux du Cameroun racontés en quatre minutes": "The Cameroon Music Worksites in four minutes",
"Le CCM publie une vidéo de synthèse des Chantiers musicaux : de l'héritage du makossa et de « Soul Makossa » à la métamorphose numérique de l'industrie, des chiffres de la cartographie aux pistes du schéma de développement.": "The CCM releases a summary video of the Music Worksites (in French): from the legacy of makossa and “Soul Makossa” to the industry's digital transformation, from the mapping figures to the development plan's proposals.",
"Voir la vidéo": "Watch the video", "Juin 2024 · Publications": "June 2024 · Publications",
"Le schéma de développement présenté aux pouvoirs publics à Yaoundé": "The development plan presented to public authorities in Yaoundé",
"Dernière étape des Chantiers musicaux, la restitution a permis de présenter l'": "The last stage of the Music Worksites presented the ",
"aux institutions et aux organisations professionnelles, en marge de la Zone by DOMAF. Le document dresse la cartographie de 3 199 professionnels, analyse les habitudes d'écoute et propose une stratégie globale : décentralisation, musique à l'école, application des lois, monétisation numérique, mobilité des artistes.": "to institutions and professional organisations, alongside Zone by DOMAF. The document maps 3,199 professionals, analyses listening habits and proposes a comprehensive strategy: decentralisation, music in schools, law enforcement, digital monetisation and artist mobility.",
"Télécharger le document": "Download the document", "Affiche du lancement de la phase 2": "Poster for the phase 2 launch",
"18 mars 2024 · Formation": "18 March 2024 · Training", "Lancement de la phase 2 en marge du Yaoundé Music Expo": "Phase 2 launched alongside the Yaoundé Music Expo",
"La deuxième étape des Chantiers musicaux a été officiellement lancée le 18 mars 2024 à l'Institut français de Yaoundé. Du 18 au 22 mars, des experts camerounais et internationaux venus du Nigéria, du Ghana, de Côte d'Ivoire, du Sénégal, de France et de Martinique ont animé plus de 16 ateliers sur la promotion, l'entrepreneuriat, la distribution et les droits.": "The second stage of the Music Worksites was officially launched on 18 March 2024 at the Institut français in Yaoundé. From 18 to 22 March, Cameroonian and international experts from Nigeria, Ghana, Côte d'Ivoire, Senegal, France and Martinique ran more than 16 workshops on promotion, entrepreneurship, distribution and rights.",
"Découvrir les intervenants": "Meet the speakers", "Ouverture des Chantiers musicaux à Douala": "Opening of the Music Worksites in Douala",
"8 février 2024 · Programmes": "8 February 2024 · Programmes", "Lancement des Chantiers musicaux du Cameroun à Douala": "Launch of the Cameroon Music Worksites in Douala",
"Du 8 au 10 février 2024, 64 professionnels des dix régions se sont réunis à Douala pour dresser l'état des lieux de la musique camerounaise. Producteurs, promoteurs et diffuseurs ont travaillé par aires culturelles pour identifier les freins qui empêchent la filière d'éclore.": "From 8 to 10 February 2024, 64 professionals from all ten regions met in Douala to assess the state of Cameroonian music. Producers, promoters and broadcasters worked by cultural area to identify what is holding the sector back.",
"Le programme complet": "The full programme",
}
METIERS = {
"Entrepreneur culturel": "Cultural entrepreneur", "Entrepreneure culturelle": "Cultural entrepreneur", "Promoteur culturel": "Cultural promoter",
"Promotrice culturelle": "Cultural promoter", "Journaliste culturelle": "Cultural journalist", "Journaliste": "Journalist", "Animatrice radio": "Radio host",
"Event organizer": "Event organiser", "Promoteur musical": "Music promoter", "Producteur et promoteur culturel": "Producer and cultural promoter",
"Distributeur / Éditeur": "Distributor / Publisher", "Producteur / Artiste": "Producer / Artist", "Promoteur de label": "Label promoter",
"Édition musicale": "Music publishing", "Technicien audiovisuel": "Audiovisual technician", "Producteur": "Producer", "Producteur / Manager": "Producer / Manager",
}
FAM = {"Médias": "Media", "Production": "Production", "Promotion et événementiel": "Promotion and events", "Édition et distribution": "Publishing and distribution",
       "Technique": "Technical", "Entrepreneuriat culturel": "Cultural entrepreneurship", "Autres métiers": "Other professions"}
REG = {"Extrême-Nord": "Far North", "Sud-Ouest": "South-West", "Nord-Ouest": "North-West", "Nord": "North", "Sud": "South", "Est": "East", "Ouest": "West"}

SCRIPT = [
    ("toLocaleString('fr-FR')", "toLocaleString('en-US')"), (".replace('.', ',')", ""),
    ("' membres' : ' membre')", "' members' : ' member')"), ("' sur ' + CCM_MEMBRES.length", "' of ' + CCM_MEMBRES.length"),
    ("Aucun membre ne correspond à cette recherche.", "No member matches this search."), ("'Photo de '", "'Photo of '"),
    (">Contacter</a>", ">Contact</a>"), ("'Annuaire : mise en relation avec '", "'Directory: introduction request for '"),
    ("'Total'", "'Total'"), ("<td>Total</td>", "<td>Total</td>"),
    ("'milliards de FCFA'", "'billion FCFA'"), ("'millions de FCFA'", "'million FCFA'"),
    ("label:'1 chanson',nom:'ultra pessimiste'", "label:'1 song',nom:'very pessimistic'"), ("label:'10 chansons',nom:'pessimiste'", "label:'10 songs',nom:'pessimistic'"),
    ("label:'30 chansons',nom:'réaliste'", "label:'30 songs',nom:'realistic'"), ("label:'100 chansons',nom:'optimiste'", "label:'100 songs',nom:'optimistic'"),
    ("' %</strong>", "'%</strong>"),
]


def traduire(html, slug):
    head, rest = html.split("<body>", 1)
    body, scripts = (rest.split("<script", 1) + [""])[:2]
    scripts = "<script" + scripts if scripts else ""

    def tt(m):
        t = m.group(2).strip()
        return m.group(1) + m.group(2).replace(t, T[t]) + m.group(3) if t in T else m.group(0)

    def ta(m):
        return m.group(1) + '="' + T.get(m.group(2), m.group(2)) + '"'

    body = re.sub(r"(>)([^<>]+)(<)", tt, body)
    body = re.sub(r'\b(alt|aria-label|placeholder|title)="([^"]*)"', ta, body)
    body = re.sub(r'(<img src="[^"]*" alt=")Portrait de ([^"]+)"', r'\1Portrait of \2"', body)
    body = re.sub(r'(<img src="[^"]*" alt=")Didier', r'\1Didier', body)
    body = re.sub(r": ([0-9\u202f]+) personnes dans la population totale", lambda m: ": " + m.group(1).replace("\u202f", ",") + " people in the total population", body)
    head = re.sub(r"<title>(.*?)</title>", lambda m: "<title>" + T.get(m.group(1), m.group(1)) + "</title>", head)
    head = re.sub(r'(content)="([^"]*)"', ta, head)
    # données et textes des scripts
    for a, b in SCRIPT: scripts = scripts.replace(a, b)
    for fr, en in sorted(METIERS.items(), key=lambda x: -len(x[0])): scripts = scripts.replace(f'"metier": "{fr}"', f'"metier": "{en}"')
    for fr, en in FAM.items(): scripts = scripts.replace(f'"fam": "{fr}"', f'"fam": "{en}"')
    for fr, en in REG.items(): scripts = scripts.replace(f'"region": "{fr}"', f'"region": "{en}"')
    for fr, en in [("Jeunes, 10 à 29 ans", "Young people, 10 to 29"), ("Adultes, 30 à 49 ans", "Adults, 30 to 49"), ("Seniors, 50 à 74 ans", "Seniors, 50 to 74")]:
        scripts = scripts.replace(fr, en)
    if slug == "observatoire":
        en_home = open(os.path.join(OUT, "en", "index.html")).read()
        th_en = re.search(r"var CCM_THEMES = \[.*?\n\];", en_home, re.S).group(0)
        scripts = re.sub(r"var CCM_THEMES = \[.*?\n\];", lambda m: th_en, scripts, count=1, flags=re.S)
    scripts = scripts.replace("'Fermer le menu' : 'Ouvrir le menu'", "'Close menu' : 'Open menu'")
    out = head + "<body>" + body + scripts
    # langue, chemins, liens de langue
    out = out.replace('<html lang="fr">', '<html lang="en">').replace('content="fr_FR"', 'content="en_GB"')
    out = out.replace(f'<link rel="canonical" href="{SITE}{slug}/">', f'<link rel="canonical" href="{SITE}en/{slug}/">')
    for d in ("assets/", "docs/", "media/"):
        out = out.replace(f'"../{d}', f'"../../{d}')
    out = out.replace(f'<a href="./" aria-current="true" style="color: var(--ambre); font-weight: 700; text-decoration: none; padding: 4px 6px">FR</a>',
                      f'<a href="../../{slug}/" hreflang="fr" lang="fr" style="color: #d6e2d9; text-decoration: none; padding: 4px 6px">FR</a>')
    out = out.replace(f'<a href="../en/{slug}/" hreflang="en" lang="en" style="color: #d6e2d9; text-decoration: none; padding: 4px 6px">EN</a>',
                      '<a href="./" aria-current="true" style="color: var(--ambre); font-weight: 700; text-decoration: none; padding: 4px 6px">EN</a>')
    out = out.replace('<script src="../../assets/js/site.js"></script>', '<script>window.CCM_LANGUE="en";</script>\n<script src="../../assets/js/site.js"></script>')
    out = out.replace("?subject=Annuaire%20%3A%20modification%20de%20ma%20fiche", "?subject=Directory%3A%20update%20my%20listing")
    return out


if __name__ == "__main__":
    for slug in PAGES:
        fr = open(os.path.join(OUT, slug, "index.html")).read()
        en = traduire(fr, slug)
        os.makedirs(os.path.join(OUT, "en", slug), exist_ok=True)
        open(os.path.join(OUT, "en", slug, "index.html"), "w").write(en)
        # reste de français visible ?
        body = re.sub(r"<script.*?</script>", "", en.split("<body>", 1)[1], flags=re.S)
        restes = [t.strip() for t in re.findall(r">([^<>]+)<", body) if re.search(r"[éèêàçù]|\b(le|la|les|des|du|et)\b", t.strip()) and t.strip() not in T.values()]
        print("en/" + slug, len(en), "restes FR :", restes[:12])
