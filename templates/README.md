# Module `templates/`

Ce répertoire contient les **templates Jinja2** utilisés par l’application Flask pour générer les pages HTML.

## Fichiers principaux

| Fichier        | Rôle |
|----------------|------|
| **`index.html`** | Page unique de la calculatrice : formulaire POST, zone d’affichage du résultat, grille de boutons (chiffres, opérateurs, C, =). Utilise `url_for('static', filename='style.css')` pour le style. Le résultat est injecté via la variable `{{ result }}`. |

## Dépendances

- **Flask** : `render_template()` dans `app.py` charge ces templates.
- Le répertoire **`static/`** fournit le CSS référencé dans les templates.

## Hypothèses

- Le moteur de templates par défaut de Flask (Jinja2) est utilisé ; aucun sous-dossier de templates n’est utilisé pour l’instant.
