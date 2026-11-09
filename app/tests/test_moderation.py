"""
from unittest.mock import Mock

import pytest

from app.moderation import decider


def test_decider_bloque_un_spam():
    # Arrange : faux modèle qui prédit "spam"
    modele = Mock()
    modele.predict.return_value = "spam"

    # Act
    decision = decider(modele, "Offre miracle")

    # Assert : 1) la décision, 2) l'appel au modèle
    assert decision == "bloquer"
    modele.predict.assert_called_once_with("Offre miracle")


def test_decider_autorise_un_message_normal():
    # Nouveau Mock, indépendant du test précédent
    modele = Mock()
    modele.predict.return_value = "normal"

    decision = decider(modele, "Bonjour, à demain")

    assert decision == "autoriser"


# ---------- Bonus ----------
def test_decider_propage_l_erreur_du_modele():
    modele = Mock()
    modele.predict.side_effect = RuntimeError("Modele indisponible")

    with pytest.raises(RuntimeError, match="Modele indisponible"):
        decider(modele, "Offre miracle")

"""        