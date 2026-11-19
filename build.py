"""Generates the static pages of reverse.tecknologiks.com (EN at the root, FR in fr/)."""
import pathlib, sys

OUT = pathlib.Path(sys.argv[1])
APP_ID = "1638978439"
STORE = f"https://apps.apple.com/app/id{APP_ID}"
MAIL = "support@tecknologiks.com"
DOMAIN = "https://reverse.tecknologiks.com/"
UPDATED = {"en": "November 20, 2026", "fr": "20 novembre 2026"}

PAGES = {
    "en": {"home": "index.html", "privacy": "privacy.html", "support": "support.html", "legal": "legal.html"},
    "fr": {"home": "index.html", "privacy": "confidentialite.html", "support": "support.html", "legal": "mentions-legales.html"},
}
LABELS = {
    "en": {"home": "Home", "privacy": "Privacy", "support": "Support", "legal": "Legal notice", "privacy_long": "Privacy policy"},
    "fr": {"home": "Accueil", "privacy": "Confidentialité", "support": "Support", "legal": "Mentions légales", "privacy_long": "Politique de confidentialité"},
}


def href(lang, page, from_lang):
    """Link from a page in from_lang to page in lang."""
    if lang == from_lang:
        return PAGES[lang][page] if page != "home" else "./"
    if lang == "fr":
        return "fr/" + (PAGES["fr"][page] if page != "home" else "")
    return "../" + (PAGES["en"][page] if page != "home" else "")


def render(lang, page, title, description, body):
    pre = "" if lang == "en" else "../"
    other = "fr" if lang == "en" else "en"
    L = LABELS[lang]
    current = ' aria-current="page"'
    nav = "\n".join(
        f'        <a href="{href(lang, p, lang)}"{current if p == page else ""}>{L[p]}</a>'
        for p in ("support", "privacy"))
    foot = "\n".join(f'        <a href="{href(lang, p, lang)}">{L["privacy_long"] if p == "privacy" else L[p]}</a>'
                     for p in ("home", "support", "privacy", "legal"))
    alt_en = DOMAIN + (PAGES["en"][page] if page != "home" else "")
    alt_fr = DOMAIN + "fr/" + (PAGES["fr"][page] if page != "home" else "")
    trademarks = ("App Store, iPhone, iPad and Live Photos are trademarks of Apple Inc. Google AdMob is a trademark of Google LLC."
                  if lang == "en" else
                  "App Store, iPhone, iPad et Live Photos sont des marques d’Apple Inc. Google AdMob est une marque de Google LLC.")
    return f"""<!doctype html>
<html lang="{lang}">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
  <title>{title}</title>
  <meta name="description" content="{description}">
  <meta name="color-scheme" content="light dark">
  <meta name="theme-color" content="#faf8f5" media="(prefers-color-scheme: light)">
  <meta name="theme-color" content="#0e0e10" media="(prefers-color-scheme: dark)">
  <meta name="apple-itunes-app" content="app-id={APP_ID}">
  <link rel="icon" href="{pre}assets/icon-64.png" type="image/png">
  <link rel="apple-touch-icon" href="{pre}assets/icon-180.png">
  <link rel="alternate" hreflang="en" href="{alt_en}">
  <link rel="alternate" hreflang="fr" href="{alt_fr}">
  <link rel="alternate" hreflang="x-default" href="{alt_en}">
  <link rel="stylesheet" href="{pre}assets/style.css">
</head>
<body>
  <div class="wrap">
    <header class="site">
      <a class="brand" href="./"><img src="{pre}assets/icon-64.png" width="32" height="32" alt=""><span>Reverse Clips</span></a>
      <nav class="site" aria-label="Navigation">
{nav}
        <a href="{href(other, page, lang)}" hreflang="{other}" lang="{other}">{other.upper()}</a>
      </nav>
    </header>

{body}

    <footer class="site">
      <nav aria-label="{'Legal links' if lang == 'en' else 'Liens légaux'}">
{foot}
      </nav>
      <p>{trademarks}</p>
      <p>© 2026 <a href="https://tecknologiks.com/">TecKnologikS</a></p>
    </footer>
  </div>
</body>
</html>
"""


SHOTS = {
    "en": [
        ("01-home", "Home screen of Reverse Clips: the orange rewind logo, the app name and the “Choose a video” button."),
        ("02-preview", "Preview of a cat video, with the trim strip, the “Reversed sound” switch turned on and the “Reverse” button."),
        ("03-processing", "Reversing in progress: 62%, about 4 seconds left, with a strip of frames and a Cancel button."),
        ("04-result", "The reversed video, looping, with the Reversed / Original switch, loops 1×, 2× or 3×, and the Save and Share buttons."),
    ],
    "fr": [
        ("01-home", "Accueil de Reverse Clips : le logo orange de retour arrière, le nom de l’app et le bouton « Choisir une vidéo »."),
        ("02-preview", "Aperçu d’une vidéo de chat, avec la bande de découpe, l’interrupteur « Son inversé » activé et le bouton « Inverser »."),
        ("03-processing", "Inversion en cours : 62 %, encore environ 4 secondes, avec une bande d’images et un bouton Annuler."),
        ("04-result", "La vidéo inversée, en boucle, avec le choix Inversée / Originale, les boucles 1×, 2× ou 3×, et les boutons Enregistrer et Partager."),
    ],
}


def gallery(lang):
    pre = "" if lang == "en" else "../"
    label = "Screenshots" if lang == "en" else "Captures d’écran"
    items = "\n".join(
        f'          <li><img src="{pre}assets/shots/{lang}/{name}.webp" width="600" height="1304" decoding="async" alt="{alt}"></li>'
        for name, alt in SHOTS[lang])
    return f"""      <section class="shots" aria-label="{label}">
        <ul>
{items}
        </ul>
      </section>"""


def store_button(lang):
    return f'<a class="button" href="{STORE}">{"Download on the App Store" if lang == "en" else "Télécharger sur l’App Store"}</a>'


HOME = {
    "en": f"""    <main>
      <section class="hero">
        <img class="app-icon" src="assets/icon-512.png" width="144" height="144" alt="">
        <h1 class="wordmark">Reverse Clips</h1>
        <p class="tagline">Your video, played backwards. Sound included.</p>
        <p class="lead">Reverse Clips plays any video from your library in reverse, in a few taps. Trim it, loop it, then save it to Photos or share it right away.</p>
        {store_button('en')}
        <p class="note">For iPhone and iPad, iOS 26 or later. Free with ads.</p>
      </section>

{gallery('en')}

      <section class="features" aria-label="Features">
        <div class="feature"><h2>A video or a Live Photo</h2><p>Choose a video or a Live Photo from your library, then trim the part you want to reverse.</p></div>
        <div class="feature"><h2>Reversed sound</h2><p>The sound is reversed too. Prefer silence? Turn it off for this video, or by default in Settings.</p></div>
        <div class="feature"><h2>Loop it</h2><p>Play the result once, twice or three times in a row, and compare it with the original.</p></div>
        <div class="feature"><h2>Save or share</h2><p>Save the reversed video to Photos or share it right away.</p></div>
        <div class="feature"><h2>No length limit</h2><p>Long videos are reversed piece by piece, with real progress and the time left.</p></div>
        <div class="feature"><h2>From Photos and Shortcuts</h2><p>Reverse straight from the Photos share sheet, or from the Shortcuts app with the “Reverse a video” action.</p></div>
        <div class="feature"><h2>Your privacy first</h2><p>Reverse Clips only asks to add videos to your library, never to read all of it. Videos are reversed on your device.</p></div>
        <div class="feature"><h2>For everyone</h2><p>Dynamic Type, VoiceOver, light and dark modes.</p></div>
      </section>

      <section class="pricing" aria-labelledby="pricing-title">
        <h2 id="pricing-title">Free, or ad-free</h2>
        <ul>
          <li><strong>Free:</strong> the whole app, with a banner on the home screen and a full-screen ad while a video is being reversed.</li>
          <li><strong>Premium:</strong> a one-time purchase through the App Store, no subscription. It removes the ads for good, and also reverses straight from the share sheet and Shortcuts without opening the app.</li>
          <li>Already bought it? It is still yours: tap “Restore purchase” in Settings.</li>
        </ul>
      </section>
    </main>""",
    "fr": f"""    <main>
      <section class="hero">
        <img class="app-icon" src="../assets/icon-512.png" width="144" height="144" alt="">
        <h1 class="wordmark">Reverse Clips</h1>
        <p class="tagline">Ta vidéo, lue à l’envers. Son compris.</p>
        <p class="lead">Reverse Clips lit à l’envers n’importe quelle vidéo de ta photothèque, en quelques touches. Découpe-la, mets-la en boucle, puis enregistre-la dans Photos ou partage-la tout de suite.</p>
        {store_button('fr')}
        <p class="note">Pour iPhone et iPad, iOS 26 ou plus récent. Gratuite avec des pubs.</p>
      </section>

{gallery('fr')}

      <section class="features" aria-label="Fonctionnalités">
        <div class="feature"><h2>Une vidéo ou une Live Photo</h2><p>Choisis une vidéo ou une Live Photo dans ta photothèque, puis découpe le passage à inverser.</p></div>
        <div class="feature"><h2>Son inversé</h2><p>Le son est inversé lui aussi. Tu préfères le silence ? Coupe-le pour cette vidéo, ou par défaut dans les Réglages.</p></div>
        <div class="feature"><h2>En boucle</h2><p>Lis le résultat une, deux ou trois fois de suite, et compare-le avec l’original.</p></div>
        <div class="feature"><h2>Enregistre ou partage</h2><p>Enregistre la vidéo inversée dans Photos ou partage-la tout de suite.</p></div>
        <div class="feature"><h2>Aucune limite de durée</h2><p>Les longues vidéos sont inversées par morceaux, avec une vraie progression et le temps restant.</p></div>
        <div class="feature"><h2>Depuis Photos et Raccourcis</h2><p>Inverse directement depuis la feuille de partage de Photos, ou depuis l’app Raccourcis avec l’action « Inverser une vidéo ».</p></div>
        <div class="feature"><h2>Ta vie privée d’abord</h2><p>Reverse Clips demande seulement à ajouter des vidéos à ta photothèque, jamais à la lire en entier. Les vidéos sont inversées sur ton appareil.</p></div>
        <div class="feature"><h2>Pour tout le monde</h2><p>Dynamic Type, VoiceOver, modes clair et sombre.</p></div>
      </section>

      <section class="pricing" aria-labelledby="pricing-title">
        <h2 id="pricing-title">Gratuite, ou sans pub</h2>
        <ul>
          <li><strong>Gratuit :</strong> toute l’app, avec une bannière sur l’accueil et une pub plein écran pendant l’inversion d’une vidéo.</li>
          <li><strong>Premium :</strong> un achat unique via l’App Store, sans abonnement. Il supprime les pubs pour de bon, et permet aussi d’inverser directement depuis la feuille de partage et Raccourcis, sans ouvrir l’app.</li>
          <li>Tu l’as déjà acheté ? Il reste à toi : touche « Restaurer l’achat » dans les Réglages.</li>
        </ul>
      </section>
    </main>""",
}

ADMOB_ROWS = {
    "en": [
        ("Approximate location (from your IP address)", "Third-party advertising, analytics"),
        ("Device identifiers (advertising identifier, if you allow it, or an app-scoped identifier)", "Third-party advertising, analytics"),
        ("Product interactions (app launches, taps, ad views)", "Third-party advertising, analytics"),
        ("Advertising data (ads you have seen)", "Third-party advertising, analytics"),
        ("Crash logs and performance data", "Diagnostics, analytics"),
    ],
    "fr": [
        ("Localisation approximative (à partir de l’adresse IP)", "Publicité tierce, mesure d’audience"),
        ("Identifiants de l’appareil (identifiant publicitaire si tu l’autorises, ou un identifiant propre à l’app)", "Publicité tierce, mesure d’audience"),
        ("Interactions (lancements de l’app, touches, annonces vues)", "Publicité tierce, mesure d’audience"),
        ("Données publicitaires (annonces vues)", "Publicité tierce, mesure d’audience"),
        ("Rapports de plantage et données de performance", "Diagnostic, mesure d’audience"),
    ],
}


def table(head, rows):
    r = "\n".join(f"          <tr><td>{a}</td><td>{b}</td></tr>" for a, b in rows)
    return f"""<div class="table-wrap"><table>
        <thead><tr><th>{head[0]}</th><th>{head[1]}</th></tr></thead>
        <tbody>
{r}
        </tbody>
      </table></div>"""


PRIVACY = {
    "en": f"""    <main class="doc">
      <h1>Privacy policy</h1>
      <p class="updated">Last updated: {UPDATED['en']}</p>
      <p class="summary"><strong>In short:</strong> Reverse Clips has no account and no server of its own. Your videos are reversed on your device and never leave it, unless you share them yourself. The app only gets the video you pick, and only asks to add videos to your library, never to read it. The free version shows ads through Google AdMob, which collects data to serve and measure ads, and personalises them only if you agree. Premium users see no ads.</p>

      <h2>1. Who is responsible</h2>
      <p>Reverse Clips and this website are published by TecKnologikS, data controller under the General Data Protection Regulation (GDPR). Contact for any question about your data: <a href="mailto:{MAIL}">{MAIL}</a>.</p>

      <h2>2. Your videos</h2>
      <ul>
        <li><strong>Choosing a video:</strong> you pick a video or a Live Photo in the system photo picker. The app receives only the item you pick (for a Live Photo, its video), never the rest of your library, and does not ask for permission to read your library. If the video is stored in iCloud, it is downloaded from iCloud by iOS first.</li>
        <li><strong>Reversing:</strong> the video is trimmed and reversed on your device. It is never sent to TecKnologikS or to anyone else: the app has no server.</li>
        <li><strong>Saving:</strong> when you tap “Save”, the app asks for permission to add to your Photos library only (“Add Photos Only”). It cannot read your photos and videos with this permission.</li>
        <li><strong>Sharing:</strong> when you tap “Share”, the video goes through the iOS share sheet to the app or the person you choose, under their own privacy policy.</li>
        <li><strong>Temporary files:</strong> the copies needed for reversing are kept in the app’s own storage on your device. They are deleted when you leave the result, and at the next launch if the app was closed before.</li>
      </ul>

      <h2>3. Share sheet and Shortcuts</h2>
      <p>When you reverse a video from the Photos share sheet (“Reverse Clips”) or with the Shortcuts action “Reverse a video”, the video is copied into the temporary storage of the app or of its share extension, on your device. With Premium, it is reversed right there; the reversed copy is deleted when you close the share sheet, and the file returned to Shortcuts is removed once the shortcut is done. Without Premium, the video is handed to the app (from the share sheet, through a storage space shared only by the app and its share extension), and the app opens it like a video picked in the app. Nothing is sent outside your device.</p>

      <h2>4. Data stored on your device</h2>
      <p>Your setting “Reversed sound by default” and the Premium status (kept so that the right state shows at launch, even offline) are stored only on your device, in preferences shared by the app and its share extension. They are never sent to TecKnologikS. Deleting the app erases them.</p>

      <h2>5. Advertising (Google AdMob)</h2>
      <p>The free version shows a banner on the home screen and a full-screen ad while a video is being reversed (the reversing goes on behind the ad). Ads are provided by Google AdMob through the Google Mobile Ads SDK, the only third-party library in the app. Premium users see no ads: no ad is requested for them. The SDK collects the following data:</p>
      {table(('Data', 'Purpose'), ADMOB_ROWS['en'])}
      <p>This data may be used to track you across apps and websites of other companies, only with your permission (see below). Learn more in <a href="https://policies.google.com/technologies/partner-sites">How Google uses information from sites or apps that use its services</a> and in <a href="https://policies.google.com/privacy">Google’s privacy policy</a>.</p>

      <h3>Your consent</h3>
      <ul>
        <li><strong>Where Google’s consent platform requires it (in particular the European Economic Area, the United Kingdom and Switzerland)</strong>, a consent form (Google User Messaging Platform) is shown at launch. You can accept, refuse or choose by purpose. If you refuse, ads may still be shown, without personalisation.</li>
        <li><strong>Then</strong>, iOS asks whether the app may use your advertising identifier (App Tracking Transparency). If you refuse, the advertising identifier is not shared.</li>
        <li>These two steps take place at launch for everyone, Premium included; the Google Mobile Ads SDK is then started as soon as consent allows it. With Premium, no ad is ever requested or shown.</li>
      </ul>

      <h2>6. Premium purchase</h2>
      <p>Premium is a one-time purchase handled by Apple (App Store, StoreKit). The payment is processed by Apple under <a href="https://www.apple.com/legal/privacy/">its own privacy policy</a>: the app and TecKnologikS receive no payment data. The app only checks with the App Store whether Premium is active on your Apple Account, at launch and when you buy or restore.</p>

      <h2>7. Service providers</h2>
      {table(('Provider', 'Role'), [
          ("Google LLC / Google Ireland Ltd", "Ads (AdMob) and the consent form (User Messaging Platform)"),
          ("Apple Inc.", "App Store, purchase of Premium, App Tracking Transparency"),
          ("GitHub, Inc. (United States)", "Hosting of this website (technical connection data such as your IP address)"),
      ])}
      <p>Some providers are located outside the European Union. These transfers are covered by the safeguards provided by the GDPR (in particular the EU–US Data Privacy Framework or standard contractual clauses).</p>

      <h2>8. Legal bases</h2>
      <ul>
        <li>Your consent: personalised ads, the advertising identifier, and storing or reading information on your device for advertising.</li>
        <li>Our legitimate interest: showing non-personalised ads that keep the app free, and measuring and protecting them against fraud.</li>
        <li>The performance of the contract: handling your Premium purchase through Apple.</li>
      </ul>

      <h2>9. How long</h2>
      <ul>
        <li>Your videos: the app keeps no copy once you leave the result; what you save stays in your Photos library.</li>
        <li>Settings and Premium status: on your device, until you delete the app.</li>
        <li>Advertising data: kept by Google under its own retention rules.</li>
        <li>Purchase data: kept by Apple under its own rules.</li>
      </ul>

      <h2 id="changing">10. Changing your choices and deleting your data</h2>
      <ul>
        <li><strong>Consent for ads:</strong> on the home screen, tap the Settings button (gear, top right), then “Manage ad consent” in the Privacy section to open the consent form again and change or withdraw your choice at any time. This section appears only where Google’s consent platform requires it.</li>
        <li><strong>Advertising identifier:</strong> iOS Settings → Privacy &amp; Security → Tracking, then turn off Reverse Clips.</li>
        <li><strong>Photos:</strong> iOS Settings → Privacy &amp; Security → Photos → Reverse Clips.</li>
        <li><strong>Settings and Premium status:</strong> deleting the app erases everything it stored on your device. Your purchase stays attached to your Apple Account and can be restored.</li>
      </ul>
      <p>TecKnologikS has no account and no user database, so there is nothing else to delete on our side.</p>

      <h2>11. Your rights</h2>
      <p>You have the right to access, rectify, erase, object to, restrict and port your data, and to withdraw your consent. To exercise them, write to <a href="mailto:{MAIL}">{MAIL}</a>. For data held by Google or Apple, you can also contact them directly. You can lodge a complaint with your data protection authority (in France, the CNIL: <a href="https://www.cnil.fr">www.cnil.fr</a>).</p>

      <h2>12. Children</h2>
      <p>TecKnologikS does not knowingly collect personal data from children. Parents can turn off tracking in iOS Settings and refuse personalised ads in the consent form.</p>

      <h2>13. This website</h2>
      <p>This website sets no cookies and loads no third-party resources.</p>

      <h2>14. Changes</h2>
      <p>If this policy changes, the date at the top of the page will be updated.</p>
    </main>""",
    "fr": f"""    <main class="doc">
      <h1>Politique de confidentialité</h1>
      <p class="updated">Dernière mise à jour : {UPDATED['fr']}</p>
      <p class="summary"><strong>En bref :</strong> Reverse Clips n’a ni compte ni serveur à lui. Tes vidéos sont inversées sur ton appareil et ne le quittent pas, sauf si tu les partages toi-même. L’app ne reçoit que la vidéo que tu choisis, et demande seulement à ajouter des vidéos à ta photothèque, jamais à la lire. La version gratuite affiche des pubs via Google AdMob, qui collecte des données pour diffuser et mesurer les annonces, et ne les personnalise que si tu es d’accord. Avec Premium, aucune pub.</p>

      <h2>1. Responsable du traitement</h2>
      <p>Reverse Clips et ce site sont édités par TecKnologikS, responsable du traitement au sens du Règlement général sur la protection des données (RGPD). Contact pour toute question sur tes données : <a href="mailto:{MAIL}">{MAIL}</a>.</p>

      <h2>2. Tes vidéos</h2>
      <ul>
        <li><strong>Choix de la vidéo :</strong> tu choisis une vidéo ou une Live Photo dans le sélecteur de photos du système. L’app ne reçoit que l’élément choisi (pour une Live Photo, sa vidéo), jamais le reste de ta photothèque, et ne demande pas l’autorisation de lire ta photothèque. Si la vidéo est stockée dans iCloud, iOS la télécharge d’abord depuis iCloud.</li>
        <li><strong>Inversion :</strong> la vidéo est découpée et inversée sur ton appareil. Elle n’est jamais envoyée à TecKnologikS ni à personne d’autre : l’app n’a pas de serveur.</li>
        <li><strong>Enregistrement :</strong> quand tu touches « Enregistrer », l’app demande l’autorisation d’ajouter à ta photothèque uniquement (« Ajouter des photos uniquement »). Avec cette autorisation, elle ne peut pas lire tes photos et vidéos.</li>
        <li><strong>Partage :</strong> quand tu touches « Partager », la vidéo passe par la feuille de partage d’iOS vers l’app ou la personne que tu choisis, selon leur propre politique de confidentialité.</li>
        <li><strong>Fichiers temporaires :</strong> les copies nécessaires à l’inversion sont gardées dans l’espace de stockage propre à l’app, sur ton appareil. Elles sont supprimées quand tu quittes le résultat, et au lancement suivant si l’app a été fermée avant.</li>
      </ul>

      <h2>3. Feuille de partage et Raccourcis</h2>
      <p>Quand tu inverses une vidéo depuis la feuille de partage de Photos (« Reverse Clips ») ou avec l’action Raccourcis « Inverser une vidéo », la vidéo est copiée dans l’espace temporaire de l’app ou de son extension de partage, sur ton appareil. Avec Premium, elle y est inversée directement ; la copie inversée est supprimée à la fermeture de la feuille de partage, et le fichier rendu à Raccourcis est supprimé une fois le raccourci terminé. Sans Premium, la vidéo est confiée à l’app (depuis la feuille de partage, via un espace de stockage partagé uniquement par l’app et son extension de partage), et l’app l’ouvre comme une vidéo choisie dans l’app. Rien n’est envoyé hors de ton appareil.</p>

      <h2>4. Données stockées sur ton appareil</h2>
      <p>Ton réglage « Son inversé par défaut » et le statut Premium (gardé pour afficher le bon état dès le lancement, même hors ligne) sont stockés uniquement sur ton appareil, dans des préférences partagées par l’app et son extension de partage. Ils ne sont jamais envoyés à TecKnologikS. Supprimer l’app les efface.</p>

      <h2>5. Publicité (Google AdMob)</h2>
      <p>La version gratuite affiche une bannière sur l’accueil et une pub plein écran pendant l’inversion d’une vidéo (l’inversion continue derrière la pub). Les annonces sont fournies par Google AdMob via le SDK Google Mobile Ads, seule bibliothèque tierce de l’app. Avec Premium, aucune pub n’est affichée : aucune annonce n’est demandée. Le SDK collecte les données suivantes :</p>
      {table(('Donnée', 'Finalité'), ADMOB_ROWS['fr'])}
      <p>Ces données peuvent servir à te suivre sur les apps et sites d’autres sociétés, uniquement avec ton accord (voir ci-dessous). Pour en savoir plus : <a href="https://policies.google.com/technologies/partner-sites?hl=fr">Comment Google utilise les informations des sites ou applications qui utilisent ses services</a> et <a href="https://policies.google.com/privacy?hl=fr">les règles de confidentialité de Google</a>.</p>

      <h3>Ton consentement</h3>
      <ul>
        <li><strong>Là où la plateforme de consentement de Google l’exige (notamment l’Espace économique européen, le Royaume-Uni et la Suisse)</strong>, un formulaire de consentement (Google User Messaging Platform) s’affiche au lancement. Tu peux accepter, refuser ou choisir finalité par finalité. Si tu refuses, des pubs peuvent quand même s’afficher, sans personnalisation.</li>
        <li><strong>Ensuite</strong>, iOS demande si l’app peut utiliser ton identifiant publicitaire (App Tracking Transparency). Si tu refuses, l’identifiant publicitaire n’est pas partagé.</li>
        <li>Ces deux étapes ont lieu au lancement pour tout le monde, Premium compris ; le SDK Google Mobile Ads est ensuite démarré dès que le consentement le permet. Avec Premium, aucune annonce n’est jamais demandée ni affichée.</li>
      </ul>

      <h2>6. Achat Premium</h2>
      <p>Premium est un achat unique géré par Apple (App Store, StoreKit). Le paiement est traité par Apple selon <a href="https://www.apple.com/fr/legal/privacy/">sa propre politique de confidentialité</a> : l’app et TecKnologikS ne reçoivent aucune donnée de paiement. L’app vérifie seulement auprès de l’App Store si Premium est actif sur ton compte Apple, au lancement et quand tu achètes ou restaures.</p>

      <h2>7. Prestataires</h2>
      {table(('Prestataire', 'Rôle'), [
          ("Google LLC / Google Ireland Ltd", "Publicité (AdMob) et formulaire de consentement (User Messaging Platform)"),
          ("Apple Inc.", "App Store, achat de Premium, App Tracking Transparency"),
          ("GitHub, Inc. (États-Unis)", "Hébergement de ce site (données techniques de connexion, comme l’adresse IP)"),
      ])}
      <p>Certains prestataires sont situés hors de l’Union européenne. Ces transferts sont encadrés par les garanties prévues par le RGPD (notamment le Data Privacy Framework UE–États-Unis ou des clauses contractuelles types).</p>

      <h2>8. Bases légales</h2>
      <ul>
        <li>Ton consentement : publicité personnalisée, identifiant publicitaire, et stockage ou lecture d’informations sur ton appareil à des fins publicitaires.</li>
        <li>Notre intérêt légitime : afficher des pubs non personnalisées qui gardent l’app gratuite, les mesurer et les protéger contre la fraude.</li>
        <li>L’exécution du contrat : traiter ton achat Premium via Apple.</li>
      </ul>

      <h2>9. Durées de conservation</h2>
      <ul>
        <li>Tes vidéos : l’app n’en garde aucune copie une fois le résultat quitté ; ce que tu enregistres reste dans ta photothèque.</li>
        <li>Réglage et statut Premium : sur ton appareil, jusqu’à la suppression de l’app.</li>
        <li>Données publicitaires : conservées par Google selon ses propres règles.</li>
        <li>Données d’achat : conservées par Apple selon ses propres règles.</li>
      </ul>

      <h2 id="changer">10. Changer tes choix et supprimer tes données</h2>
      <ul>
        <li><strong>Consentement pour la publicité :</strong> sur l’accueil, touche le bouton Réglages (l’engrenage, en haut à droite), puis « Gérer le consentement publicitaire » dans la section Confidentialité pour rouvrir le formulaire et modifier ou retirer ton choix à tout moment. Cette section n’apparaît que là où la plateforme de consentement de Google l’exige.</li>
        <li><strong>Identifiant publicitaire :</strong> Réglages iOS → Confidentialité et sécurité → Suivi, puis désactive Reverse Clips.</li>
        <li><strong>Photos :</strong> Réglages iOS → Confidentialité et sécurité → Photos → Reverse Clips.</li>
        <li><strong>Réglage et statut Premium :</strong> supprimer l’app efface tout ce qu’elle a stocké sur ton appareil. Ton achat reste lié à ton compte Apple et peut être restauré.</li>
      </ul>
      <p>TecKnologikS n’a ni compte ni base d’utilisateurs : il n’y a rien d’autre à supprimer de notre côté.</p>

      <h2>11. Tes droits</h2>
      <p>Tu disposes d’un droit d’accès, de rectification, d’effacement, d’opposition, de limitation et de portabilité, ainsi que du droit de retirer ton consentement. Pour les exercer, écris à <a href="mailto:{MAIL}">{MAIL}</a>. Pour les données détenues par Google ou Apple, tu peux aussi les contacter directement. Tu peux introduire une réclamation auprès de la CNIL : <a href="https://www.cnil.fr">www.cnil.fr</a>.</p>

      <h2>12. Enfants</h2>
      <p>TecKnologikS ne collecte sciemment aucune donnée personnelle d’enfants. Les parents peuvent désactiver le suivi dans les Réglages iOS et refuser la publicité personnalisée dans le formulaire de consentement.</p>

      <h2>13. Ce site</h2>
      <p>Ce site ne dépose aucun cookie et ne charge aucune ressource tierce.</p>

      <h2>14. Modifications</h2>
      <p>Si cette politique change, la date en haut de la page sera mise à jour.</p>
    </main>""",
}

SUPPORT = {
    "en": f"""    <main class="doc">
      <h1>Support</h1>
      <p>A question, a bug, an idea? Write to <a href="mailto:{MAIL}">{MAIL}</a>. If something goes wrong, tell us your iPhone or iPad model and your iOS version.</p>

      <h2>Frequently asked questions</h2>
      <h3>Where does my reversed video go?</h3>
      <p>Nowhere until you choose: on the result, tap “Save” to add it to your Photos library, or “Share” to send it. The first time you save, iOS asks for permission to add to your Photos. If you refused, tap “Open Settings” in the app, or go to iOS Settings → Privacy &amp; Security → Photos → Reverse Clips, and choose “Add Photos Only”.</p>
      <h3>Can I reverse without the sound?</h3>
      <p>Yes. On the preview, turn off “Reversed sound”: the reversed video has no sound. To change the default for every video, open Settings (gear on the home screen) and turn off “Reversed sound by default”.</p>
      <h3>Does it work with Live Photos?</h3>
      <p>Yes. Choose a Live Photo in the picker: its video is reversed, like any other video.</p>
      <h3>My video is long</h3>
      <p>There is no length limit: long videos are reversed piece by piece, and the screen shows the progress and the time left. Reversing may take several minutes; shorten the selection to go faster. Make sure your device has enough free space. If the video is stored in iCloud, it has to be downloaded first: check your connection.</p>
      <h3>Reverse Clips is not in the share sheet</h3>
      <p>The share extension appears when you share a single video. If you don’t see it, scroll to the end of the row of apps, tap “More”, and look for Reverse Clips in the list.</p>
      <h3>Reversing from Photos or Shortcuts opens the app</h3>
      <p>Reversing directly in the share sheet or in a shortcut, without opening the app, is a Premium feature. Without Premium, your video opens in Reverse Clips, where you can reverse it for free.</p>
      <h3>How do I restore my purchase?</h3>
      <p>Open Settings (gear on the home screen) and tap “Restore purchase”, or tap the same button on the Premium screen (crown on the home screen). Use the Apple Account you bought with. If you bought it in an earlier version of the app, it is still yours.</p>
      <h3>How do I change my ad choices?</h3>
      <p>In Settings, tap “Manage ad consent” (shown only where Google’s consent platform requires it). To turn off ad tracking, go to iOS Settings → Privacy &amp; Security → Tracking. See also <a href="privacy.html#changing">“Changing your choices” in the privacy policy</a>.</p>
    </main>""",
    "fr": f"""    <main class="doc">
      <h1>Support</h1>
      <p>Une question, un bug, une idée ? Écris à <a href="mailto:{MAIL}">{MAIL}</a>. Si quelque chose ne marche pas, indique ton modèle d’iPhone ou d’iPad et ta version d’iOS.</p>

      <h2>Questions fréquentes</h2>
      <h3>Où va ma vidéo inversée ?</h3>
      <p>Nulle part tant que tu ne choisis pas : sur le résultat, touche « Enregistrer » pour l’ajouter à ta photothèque, ou « Partager » pour l’envoyer. Au premier enregistrement, iOS demande l’autorisation d’ajouter à tes photos. Si tu as refusé, touche « Ouvrir Réglages » dans l’app, ou va dans Réglages iOS → Confidentialité et sécurité → Photos → Reverse Clips, et choisis « Ajouter des photos uniquement ».</p>
      <h3>Puis-je inverser sans le son ?</h3>
      <p>Oui. Sur l’aperçu, désactive « Son inversé » : la vidéo inversée n’a pas de son. Pour changer le choix par défaut de toutes les vidéos, ouvre les Réglages (l’engrenage sur l’accueil) et désactive « Son inversé par défaut ».</p>
      <h3>Ça marche avec les Live Photos ?</h3>
      <p>Oui. Choisis une Live Photo dans le sélecteur : sa vidéo est inversée, comme n’importe quelle vidéo.</p>
      <h3>Ma vidéo est longue</h3>
      <p>Il n’y a pas de limite de durée : les longues vidéos sont inversées par morceaux, et l’écran affiche la progression et le temps restant. L’inversion peut prendre plusieurs minutes ; raccourcis la sélection pour aller plus vite. Vérifie qu’il reste assez d’espace libre sur ton appareil. Si la vidéo est stockée dans iCloud, elle doit d’abord être téléchargée : vérifie ta connexion.</p>
      <h3>Reverse Clips n’apparaît pas dans la feuille de partage</h3>
      <p>L’extension de partage apparaît quand tu partages une seule vidéo. Si tu ne la vois pas, fais défiler la rangée d’apps jusqu’au bout, touche « Plus », et cherche Reverse Clips dans la liste.</p>
      <h3>Inverser depuis Photos ou Raccourcis ouvre l’app</h3>
      <p>Inverser directement dans la feuille de partage ou dans un raccourci, sans ouvrir l’app, est une fonction Premium. Sans Premium, ta vidéo s’ouvre dans Reverse Clips, où tu peux l’inverser gratuitement.</p>
      <h3>Comment restaurer mon achat ?</h3>
      <p>Ouvre les Réglages (l’engrenage sur l’accueil) et touche « Restaurer l’achat », ou touche le même bouton sur l’écran Premium (la couronne sur l’accueil). Utilise le compte Apple de l’achat. Si tu l’as acheté dans une version précédente de l’app, il reste à toi.</p>
      <h3>Comment changer mes choix pour la publicité ?</h3>
      <p>Dans les Réglages, touche « Gérer le consentement publicitaire » (affiché seulement là où la plateforme de consentement de Google l’exige). Pour désactiver le suivi publicitaire, va dans Réglages iOS → Confidentialité et sécurité → Suivi. Voir aussi <a href="confidentialite.html#changer">« Changer tes choix » dans la politique de confidentialité</a>.</p>
    </main>""",
}

LEGAL = {
    "en": f"""    <main class="doc">
      <h1>Legal notice</h1>
      <h2>Publisher</h2>
      <p>TecKnologikS<br>Contact: <a href="mailto:{MAIL}">{MAIL}</a></p>
      <p>Publication director: TecKnologikS</p>
      <h2>Website hosting</h2>
      <p>GitHub, Inc. (GitHub Pages), 88 Colin P. Kelly Jr. Street, San Francisco, CA 94107, United States — github.com.</p>
      <h2>Intellectual property</h2>
      <p>The texts, visuals and code of Reverse Clips are the property of the publisher. App Store, iPhone, iPad and Live Photos are trademarks of Apple Inc.; Google AdMob is a trademark of Google LLC.</p>
      <p>The name on this website is set in Kaushan Script by Pablo Impallari and Igino Marini, under the SIL Open Font License 1.1 (<a href="assets/fonts/KaushanScript-OFL.txt">license</a>). The photo shown in the screenshots is in the public domain (CC0).</p>
      <h2>Personal data</h2>
      <p>See the <a href="privacy.html">privacy policy</a>. This website sets no cookies.</p>
    </main>""",
    "fr": f"""    <main class="doc">
      <h1>Mentions légales</h1>
      <h2>Éditeur</h2>
      <p>TecKnologikS<br>Contact : <a href="mailto:{MAIL}">{MAIL}</a></p>
      <p>Directeur de la publication : TecKnologikS</p>
      <h2>Hébergement</h2>
      <p>GitHub, Inc. (GitHub Pages), 88 Colin P. Kelly Jr. Street, San Francisco, CA 94107, États-Unis — github.com.</p>
      <h2>Propriété intellectuelle</h2>
      <p>Les textes, visuels et le code de Reverse Clips sont la propriété de l’éditeur. App Store, iPhone, iPad et Live Photos sont des marques d’Apple Inc. ; Google AdMob est une marque de Google LLC.</p>
      <p>Le nom affiché sur ce site utilise la police Kaushan Script de Pablo Impallari et Igino Marini, sous licence SIL Open Font License 1.1 (<a href="../assets/fonts/KaushanScript-OFL.txt">licence</a>). La photo des captures d’écran est dans le domaine public (CC0).</p>
      <h2>Données personnelles</h2>
      <p>Voir la <a href="confidentialite.html">politique de confidentialité</a>. Ce site ne dépose aucun cookie.</p>
    </main>""",
}

META = {
    "home": {"en": ("Reverse Clips — your video, played backwards", "Reverse any video or Live Photo on iPhone, sound included. Trim it, loop it, then save it to Photos or share it."),
             "fr": ("Reverse Clips — ta vidéo, lue à l’envers", "Inverse n’importe quelle vidéo ou Live Photo sur iPhone, son compris. Découpe-la, mets-la en boucle, puis enregistre-la ou partage-la.")},
    "privacy": {"en": ("Privacy policy — Reverse Clips", "How Reverse Clips handles your data: videos reversed on your device, add-only Photos access, Google AdMob ads, consent, Premium purchase."),
                "fr": ("Politique de confidentialité — Reverse Clips", "Comment Reverse Clips traite tes données : vidéos inversées sur l’appareil, accès Photos en ajout seul, pubs Google AdMob, consentement, achat Premium.")},
    "support": {"en": ("Support — Reverse Clips", "Contact and frequently asked questions about Reverse Clips."),
                "fr": ("Support — Reverse Clips", "Contact et questions fréquentes sur Reverse Clips.")},
    "legal": {"en": ("Legal notice — Reverse Clips", "Publisher and hosting of the Reverse Clips website."),
              "fr": ("Mentions légales — Reverse Clips", "Éditeur et hébergeur du site de Reverse Clips.")},
}

BODIES = {"home": HOME, "privacy": PRIVACY, "support": SUPPORT, "legal": LEGAL}

for lang in ("en", "fr"):
    for page, bodies in BODIES.items():
        title, desc = META[page][lang]
        path = OUT / PAGES[lang][page] if lang == "en" else OUT / "fr" / PAGES[lang][page]
        path.parent.mkdir(parents=True, exist_ok=True)
        body = bodies[lang]
        if lang == "fr":
            # French typography: no line break inside « … » or before : ; ? !
            body = body.replace("« ", "«&nbsp;").replace(" »", "&nbsp;»")
            for mark in (":", ";", "?", "!"):
                body = body.replace(f" {mark}", f"&nbsp;{mark}")
        path.write_text(render(lang, page, title, desc, body), encoding="utf-8")
        print("wrote", path.relative_to(OUT))
