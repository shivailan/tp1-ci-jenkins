# Fichier test_app.py
from app import addition

def test_addition_positive_numbers():
    """Vérifie l'addition de deux nombres positifs."""
    assert addition(2, 3) == 5

def test_addition_negative_numbers():
    """Vérifie l'addition de deux nombres négatifs."""
    assert addition(-1, -5) == -6

def test_addition_zero():
    """Vérifie l'addition avec zéro."""
    assert addition(0, 7) == 7
