"""
from unittest.mock import patch

import pytest

from app.surveillance import surveiller


def test_surveiller_alerte_si_taux_eleve():
    with patch("app.surveillance.envoyer_notification") as notifier:
        resultat = surveiller(0.15)

        assert resultat == "alerte"
        notifier.assert_called_once_with("Taux eleve")


def test_surveiller_ok_si_taux_faible():
    with patch("app.surveillance.envoyer_notification") as notifier:
        resultat = surveiller(0.05)

        assert resultat == "ok"
        notifier.assert_not_called()


def test_surveiller_pas_d_alerte_au_seuil_exact():
    # 0.10 n'est pas strictement superieur a 0.10
    with patch("app.surveillance.envoyer_notification") as notifier:
        resultat = surveiller(0.10)

        assert resultat == "ok"
        notifier.assert_not_called()


# ---------- Bonus ----------
def test_surveiller_propage_la_panne_du_service():
    with patch("app.surveillance.envoyer_notification") as notifier:
        notifier.side_effect = RuntimeError("Service non configure")

        with pytest.raises(RuntimeError, match="Service non configure"):
            surveiller(0.15)

        notifier.assert_called_once_with("Taux eleve")

"""        