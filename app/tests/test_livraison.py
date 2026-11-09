#avant la correction 

from app.livraison import frais_livraison


def test_livraison_panier_ordinaire():
    # Arrange
    montant = 120
    # Act
    resultat = frais_livraison(montant)
    # Assert
    assert resultat == 25


def test_livraison_299_dh_payante():
    # Arrange
    montant = 299
    # Act
    resultat = frais_livraison(montant)
    # Assert
    assert resultat == 25


def test_livraison_300_dh_gratuite():
    # Arrange : 300 inclus, donc gratuit
    montant = 300
    # Act
    resultat = frais_livraison(montant)
    # Assert
    assert resultat == 0


def test_livraison_301_dh_gratuite():
    # Arrange
    montant = 301
    # Act
    resultat = frais_livraison(montant)
    # Assert
    assert resultat == 0

def test_livraison_panier_zero():
    # Arrange : 0 n'est pas negatif et reste inferieur a 300
    montant = 0
    # Act
    resultat = frais_livraison(montant)
    # Assert
    assert resultat == 25


# ---------- Test supplementaire : la regle du montant negatif ----------
def test_livraison_montant_negatif():
    import pytest

    with pytest.raises(ValueError, match="Montant negatif"):
        frais_livraison(-1)    