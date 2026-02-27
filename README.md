# Calculatrice Web – LOG3000 (Équipe 46)

Application web de calculatrice simple : backend Flask (Python), interface HTML/CSS. L’utilisateur saisit une expression du type `nombre opérateur nombre` et obtient le résultat.

## Prérequis

- Python 3.10+
- pip

## Installation

1. Cloner le dépôt et se placer à la racine du projet :

   ```bash
   git clone <URL_DU_DEPOT_GITHUB>
   cd TP3---LOG3000
   ```

2. Créer un environnement virtuel (recommandé) et l’activer :

   ```bash
   python -m venv .venv
   .venv\Scripts\activate
   ```

3. Installer les dépendances :

   ```bash
   pip install -r requirements.txt
   ```

## Lancer l’application

```bash
set FLASK_APP=app.py
set FLASK_ENV=development
flask run
```

Puis ouvrir **http://localhost:5000** dans un navigateur.

## Tests

La suite de tests est dans le répertoire `tests/`. Voir **`tests/README.md`** pour la couverture.

Exécuter tous les tests depuis la racine du projet :

```bash
pytest tests/ -v
```

## Contribution

Une branche par correctif ou fonctionnalité, tests à jour, puis Pull Request vers `main`. Décrire les changements et lier les issues concernées (ex. `Fixes #12`) dans la PR.

