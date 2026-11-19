# reverse-site

Site de Reverse Clips (https://reverse.tecknologiks.com) : présentation, politique de confidentialité, support et mentions légales, en anglais (racine) et en français (`fr/`).

Site statique publié avec GitHub Pages (workflow `.github/workflows/pages.yml`, à chaque push sur `main`). Réglage à faire une fois sur GitHub : Settings → Pages → Source : « GitHub Actions ». Le domaine est donné par `CNAME` (enregistrement DNS `reverse` à créer côté domaine).

Les pages sont générées par `build.py` (textes et gabarit communs) : modifier `build.py`, puis lancer `python3 build.py .` et committer les HTML.

| Page | Rôle | URL à déclarer |
| --- | --- | --- |
| `index.html`, `fr/index.html` | Présentation, captures, lien App Store, Smart App Banner | App Store Connect → *Marketing URL* |
| `privacy.html`, `fr/confidentialite.html` | Politique de confidentialité (vidéos sur l'appareil, Photos en ajout seul, extension de partage et Raccourcis, AdMob, UMP, ATT, achat Premium) | App Store Connect → *Privacy Policy URL* ; AdMob → message RGPD |
| `support.html`, `fr/support.html` | Contact et FAQ | App Store Connect → *Support URL* |
| `legal.html`, `fr/mentions-legales.html` | Mentions légales | — |

## Ressources

- Icône : `assets/icon-512.png`, `icon-180.png` (apple-touch-icon, sur fond blanc) et `icon-64.png` (favicon), rendues depuis `iosApp/iosApp/AppIcon.icon` du dépôt de l'app avec `ictool` (rendition `Default`, voir `design/icon/README.md` de l'app).
- Captures : `assets/shots/<en|fr>/0X-*.webp`, captures 2.0.0 de l'iPhone redimensionnées à 600 px de large (WebP, `ffmpeg`). Photo du chat : CC0.
- Police du nom : Kaushan Script (`assets/fonts`, SIL OFL 1.1, licence `KaushanScript-OFL.txt`), auto-hébergée, fichier d'origine non modifié. La police de l'app (Tabuti) n'est pas embarquée : sa licence n'est pas vérifiée. Le reste du texte utilise les polices du système.

Aucune ressource externe, aucun cookie, aucun script.

## À garder à jour

La politique de confidentialité décrit le fonctionnement réel de l'app iOS (sélecteur `PhotosPicker`, autorisation « ajout seul », App Group pour l'extension de partage, consentement UMP puis ATT au lancement, bannière de l'accueil et interstitiel pendant l'inversion, achat `com.tecknologiks.reverse.premium`, libellés « Gérer le consentement publicitaire », « Restaurer l'achat »). Toute évolution qui touche aux données (nouveau SDK, analytics, compte, consentement sauté pour les premium, version Android…) doit être reportée ici avant sa mise en ligne, ainsi que dans la fiche « Confidentialité » d'App Store Connect. La date `UPDATED` aussi.

Ces textes ne remplacent pas un avis juridique.
