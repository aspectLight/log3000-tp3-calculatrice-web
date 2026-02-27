# Module `static/`

Ce répertoire contient les **fichiers statiques** servis par Flask (feuilles de style, images, etc.) et référencés dans les templates.

## Fichiers principaux

| Fichier      | Rôle |
|--------------|------|
| **`style.css`** | Feuille de style de la calculatrice : mise en page (grille de boutons, affichage), couleurs (thème sombre), états hover/active des boutons et des opérateurs. |

## Dépendances

- **Flask** : les fichiers sont exposés via la route `/static/` (gérée automatiquement par Flask).
- Les **templates** (ex. `templates/index.html`) y font référence avec `url_for('static', filename='style.css')`.

## Hypothèses

- Aucun JavaScript externe pour l’instant ; le script est inline dans `index.html`.
