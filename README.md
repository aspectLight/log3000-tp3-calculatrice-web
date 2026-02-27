## Calculatrice Web - Devoir 3 LOG3000

Projet de calculatrice web simple développé dans le cadre du cours LOG3000, utilisant Flask (Python) pour le backend et une interface web minimale pour le frontend.

### Informations d’équipe

- **Numéro d’équipe** : Équipe 46

### Objectif du projet

L’objectif de ce projet est de :

- **Mettre en place un dépôt GitHub** propre et structuré.
- **Appliquer des bonnes pratiques de gestion de versions** (branches, pull requests, issues).
- **Documenter la base de code** pour faciliter l’arrivée de nouveaux développeurs.
- **Mettre en place des tests** et corriger les bogues identifiés.
- **Livrer une application de calculatrice web** fonctionnelle et maintenable.

### Prérequis d’installation

Avant de démarrer, assurez-vous d’avoir :

- **Python** (version 3.10 ou plus récente recommandée)
- **pip** (gestionnaire de paquets Python)
- **Git** installé localement
- Un **compte GitHub** (pour la gestion du dépôt distant)

### Instructions d’installation

1. **Cloner le dépôt**

   ```bash
   git clone <URL_DU_DEPOT_GITHUB>
   cd TP3---LOG3000
   ```

2. **Créer et activer un environnement virtuel (recommandé)**

   ```bash
   python -m venv .venv
   .venv\Scripts\activate
   ```

3. **Installer les dépendances Python**

   (Adapter cette étape une fois le fichier `requirements.txt` défini.)

   ```bash
   pip install -r requirements.txt
   ```

4. **Lancer l’application Flask**

   (Les commandes exactes pourront être ajustées après inspection du code.)

   ```bash
   set FLASK_APP=app.py
   set FLASK_ENV=development
   flask run
   ```

5. **Accéder à l’application**

   Ouvrez un navigateur et allez à l’adresse :

   ```text
   http://localhost:5000
   ```

### Tests

La suite de tests se trouve dans le répertoire `tests/`. Voir **`tests/README.md`** pour le détail de la couverture.

**Exécuter tous les tests :**

```bash
# Depuis la racine du projet (TP3---LOG3000)
pytest tests/ -v
```

**Créer automatiquement une issue GitHub pour chaque test en échec :**

1. Installer et authentifier [GitHub CLI](https://cli.github.com/) : `gh auth login`
2. Depuis la racine du projet :

   ```bash
   python scripts/create_issues_from_test_failures.py --assignee @me
   ```

   Options : `--dry-run` (n’exécute pas `gh`, affiche seulement les issues qui seraient créées), `--assignee USERNAME` pour assigner à un membre de l’équipe.

### Flux de contribution (branches, PR, issues)

Pour chaque **bogue** (ou test en échec) :

1. **Ouvrir une issue** (ou utiliser le script ci‑dessus) : décrire le problème, fournir les étapes de reproduction / le cas de test en échec, assigner à un membre de l’équipe.
2. **Créer une branche dédiée** par issue, par ex. `fix/nom-du-bogue` ou `fix/issue-XX-description`.
3. **Corriger le problème** sur cette branche uniquement.
4. **Réexécuter le(s) test(s) qui échouaient** : `pytest tests/test_operators.py::nom_du_test -v` (ou le chemin indiqué dans l’issue).
5. **Valider (commit)** avec un message clair expliquant *comment* la modification corrige le problème (ex. « Corrige subtract : retourner a - b au lieu de b - a »).
6. **Vérifier** que la branche fait passer les tests concernés, puis ouvrir une **Pull Request** vers `main` pour revue et fusion.

