# Module `tests/`

Contient la suite de tests de l’application : opérateurs arithmétiques (`operators.py`) et parsing des expressions (`app.calculate`).

## Prérequis

- Python 3.10+
- Dépendances du projet : `pip install -r requirements.txt` (à la racine du projet)

## Exécution des tests

Depuis la **racine du projet** (`TP3---LOG3000`) :

```bash
# Tous les tests
pytest tests/ -v

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
