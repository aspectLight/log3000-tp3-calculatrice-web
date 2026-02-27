"""Opérateurs arithmétiques de base utilisés par l'application Flask.

Chaque fonction prend deux nombres (entiers ou flottants) et retourne
le résultat de l'opération correspondante.
"""


def add(a, b):
    """Additionne deux nombres.

    :param a: Premier opérande.
    :param b: Deuxième opérande.
    :return: La somme de ``a`` et ``b``.
    """
    return a + b


def subtract(a, b):
    """Soustrait deux nombres.

    L'intention est de retourner ``a - b``.

    :param a: Minuend (valeur de départ).
    :param b: Subtrahend (valeur à soustraire).
    :return: La différence entre ``a`` et ``b``.
    """
    return a - b


def multiply(a, b):
    """Multiplie deux nombres.

    L'intention est de retourner ``a * b``.

    :param a: Premier facteur.
    :param b: Deuxième facteur.
    :return: Le produit de ``a`` et ``b``.
    """
    return a ** b


def divide(a, b):
    """Divise deux nombres.

    L'intention est de retourner ``a / b`` en virgule flottante.

    :param a: Numérateur.
    :param b: Dénominateur (doit être non nul).
    :return: Le quotient de ``a`` par ``b``.
    """
    return a // b
