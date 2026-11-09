import pytest

from app.reservation import Reservation, Stock


# ---------- Question 1 : fixture ----------
@pytest.fixture
def stock():
    return Stock(5)


# ---------- Question 2 ----------
def test_reservation_de_2_unites_est_confirmee(stock):
    reservation = Reservation(stock)

    statut = reservation.reserver(2)

    assert statut == "confirmee"
    assert stock.quantite == 3


# ---------- Question 3 ----------
def test_reservation_de_6_unites_est_refusee(stock):
    reservation = Reservation(stock)

    statut = reservation.reserver(6)

    assert statut == "refusee"
    assert stock.quantite == 5


# ---------- Question 4 ----------
def test_reservation_de_5_unites_vide_le_stock(stock):
    reservation = Reservation(stock)

    statut = reservation.reserver(5)

    assert statut == "confirmee"
    assert stock.quantite == 0


# ---------- Bonus ----------
@pytest.mark.parametrize("quantite", [0, -1], ids=["zero", "negative"])
def test_quantite_invalide_leve_valueerror_stock_intact(stock, quantite):
    reservation = Reservation(stock)

    with pytest.raises(ValueError, match="Quantité positive requise"):
        reservation.reserver(quantite)

    assert stock.quantite == 5