"""Tests unitaires des opérateurs arithmétiques (operators.py).

Vérifie que add, subtract, multiply et divide se comportent selon
la sémantique attendue : addition, soustraction (a - b), multiplication
(a * b), division réelle (a / b). Les tests qui échouent révèlent
des bogues dans l'implémentation actuelle.
"""

import pytest
from operators import add, subtract, multiply, divide


def test_add_positive():
    """Vérifie que add(a, b) retourne la somme a + b pour des entiers positifs."""
    assert add(2, 3) == 5


def test_add_negative():
    """Vérifie que add gère les nombres négatifs correctement."""
    assert add(-1, 1) == 0


def test_subtract():
    """Vérifie que subtract(a, b) retourne a - b (premier opérande moins le second)."""
    # Comportement attendu : 5 - 3 = 2
    assert subtract(5, 3) == 2


def test_subtract_negative_result():
    """Vérifie que subtract(a, b) retourne a - b quand le résultat est négatif."""
    assert subtract(3, 5) == -2


def test_multiply():
    """Vérifie que multiply(a, b) retourne le produit a * b (multiplication, pas puissance)."""
    # Comportement attendu : 3 * 4 = 12
    assert multiply(3, 4) == 12


def test_multiply_by_zero():
    """Vérifie que multiply par zéro donne 0."""
    assert multiply(10, 0) == 0


def test_divide():
    """Vérifie que divide(a, b) retourne a / b en virgule flottante (division réelle)."""
    # Comportement attendu : 10 / 4 = 2.5
    assert divide(10, 4) == 2.5


def test_divide_integer_result():
    """Vérifie que divide retourne un float même quand le résultat est entier."""
    assert divide(6, 2) == 3.0


def test_divide_by_zero():
    """Vérifie que la division par zéro lève une exception."""
    with pytest.raises(ZeroDivisionError):
        divide(1, 0)
