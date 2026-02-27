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

## Branches de correctifs (une branche par bogue)

Chaque bogue identifié par les tests est corrigé sur une **branche dédiée**. Après correction, le(s) test(s) qui échouaient passent sur cette branche.

| Branche | Test(s) concerné(s) | Correction |
|--------|----------------------|------------|
| `fix/subtract-operand-order` | `test_subtract`, `test_subtract_negative_result` ; `test_calculate_subtraction`, `test_calculate_with_spaces` | `subtract(a, b)` retourne `a - b` au lieu de `b - a` |
| `fix/multiply-use-multiplication` | `test_multiply`, `test_multiply_by_zero` ; `test_calculate_multiply` | `multiply(a, b)` retourne `a * b` au lieu de `a ** b` |
| `fix/divide-float-division` | `test_divide`, `test_divide_integer_result` ; `test_calculate_divide` | `divide(a, b)` retourne `a / b` au lieu de `a // b` |

Pour vérifier qu’une branche fait bien passer les tests concernés :

```bash
git checkout fix/subtract-operand-order
pytest tests/test_operators.py::test_subtract tests/test_operators.py::test_subtract_negative_result tests/test_calculate.py::test_calculate_subtraction -v
```

(Idem pour les autres branches en remplaçant par les tests listés ci‑dessus.)

## Création automatique d’issues GitHub

Le script `scripts/create_issues_from_test_failures.py` lance les tests, produit un rapport JUnit, puis crée une issue GitHub pour chaque test en échec (avec titre, description, étapes de reproduction et assignation). Voir le README principal du projet et les commentaires dans le script pour l’utilisation et les options.
