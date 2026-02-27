# Module de tests – Calculatrice Flask

Ce répertoire contient la suite de tests du projet calculatrice web (LOG3000, Équipe 46). Les tests permettent de détecter les bogues dans les opérateurs et dans le parsing des expressions.

## Prérequis

- Python 3.10+
- Dépendances du projet : `pip install -r requirements.txt` (à la racine du projet)

## Exécution des tests

Depuis la **racine du projet** (`TP3---LOG3000`) :

```bash
# Tous les tests
pytest tests/ -v

# Avec rapport JUnit (pour le script de création d’issues)
pytest tests/ -v --junitxml=test-results.xml

# Un fichier ou un test précis
pytest tests/test_operators.py -v
pytest tests/test_operators.py::test_subtract -v
```

Sous Windows (PowerShell), si le projet n’est pas sur le `PYTHONPATH` :

```powershell
$env:PYTHONPATH = (Get-Location).Path
pytest tests/ -v
```

## Couverture des tests

### `test_operators.py`

- **add** : somme de deux nombres (positifs, négatifs).
- **subtract** : différence `a - b` (ordre des opérandes).
- **multiply** : produit `a * b` (multiplication, pas puissance).
- **divide** : quotient en virgule flottante `a / b`, et division par zéro (exception).

Un test qui échoue indique un bogue dans `operators.py` par rapport au comportement attendu documenté.

### `test_calculate.py`

- Expressions valides : `"2+3"`, `"5-3"`, `"10 - 2"`, `"3*4"`, `"10/4"`.
- Cas d’erreur : expression vide, `None`, deux opérateurs, format invalide (`+12`, `12+`), opérandes non numériques (`a+b`).

Les échecs peuvent venir du parsing dans `app.calculate` ou des opérateurs sous-jacents.

## Création automatique d’issues GitHub

Le script `scripts/create_issues_from_test_failures.py` lance les tests, produit un rapport JUnit, puis crée une issue GitHub pour chaque test en échec (avec titre, description, étapes de reproduction et assignation). Voir le README principal du projet et les commentaires dans le script pour l’utilisation et les options.
