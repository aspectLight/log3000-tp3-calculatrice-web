"""Tests de la fonction calculate (parsing et évaluation d'expressions).

Vérifie le comportement de app.calculate pour des expressions valides
(nombre opérateur nombre) et pour les cas d'erreur (expression vide,
plusieurs opérateurs, opérandes non numériques, format invalide).
"""

import pytest
from app import calculate


def test_calculate_addition():
    """Vérifie que calculate évalue correctement une addition."""
    assert calculate("2+3") == 5


def test_calculate_subtraction():
    """Vérifie que calculate évalue une soustraction (expression valide)."""
    # Résultat dépend de l'implémentation de subtract (5-3 attendu 2)
    assert calculate("5-3") == 2


def test_calculate_with_spaces():
    """Vérifie que les espaces dans l'expression sont ignorés."""
    assert calculate("10 - 2") == 8


def test_calculate_multiply():
    """Vérifie que calculate évalue une multiplication."""
    assert calculate("3*4") == 12


def test_calculate_divide():
    """Vérifie que calculate évalue une division en flottant."""
    assert calculate("10/4") == 2.5


def test_calculate_empty_raises():
    """Vérifie qu'une expression vide lève ValueError."""
    with pytest.raises(ValueError, match="empty expression"):
        calculate("")


def test_calculate_none_raises():
    """Vérifie qu'une entrée None (ou non-chaîne) lève ValueError."""
    with pytest.raises(ValueError, match="empty expression"):
        calculate(None)


def test_calculate_two_operators_raises():
    """Vérifie qu'une expression avec deux opérateurs lève ValueError."""
    with pytest.raises(ValueError, match="only one operator"):
        calculate("1+2+3")


def test_calculate_invalid_format_raises():
    """Vérifie qu'un opérateur en début ou fin d'expression lève ValueError."""
    with pytest.raises(ValueError, match="invalid expression"):
        calculate("+12")
    with pytest.raises(ValueError, match="invalid expression"):
        calculate("12+")


def test_calculate_non_numeric_operands_raises():
    """Vérifie que des opérandes non numériques lèvent ValueError."""
    with pytest.raises(ValueError, match="operands must be numbers"):
        calculate("a+b")
