"""
#test 1ere question

from app.texte import nettoyer_texte


def test_nettoyer_texte_exemple_principal():
    assert nettoyer_texte("  BONJOUR   monde  ") == "bonjour monde"

"""

#2eme , 3eme questions

import pytest

from app.texte import nettoyer_texte


# ---------- Question 2 : test parametre ----------
@pytest.mark.parametrize(
    "entree, attendu",
    [
        ("  BONJOUR   monde  ", "bonjour monde"),   # exemple 1
        (" déjà propre ", "déjà propre"),           # exemple 2
        ("", ""),                                   # exemple 3 : chaine vide
        ("     ", ""),                              # exemple 3 : espaces seuls
        ("PYTHON", "python"),                       # un seul mot en majuscules
    ],
    ids=[
        "espaces_et_majuscules",
        "deja_propre",
        "chaine_vide",
        "espaces_seulement",
        "un_mot_en_majuscules",
    ],
)
def test_nettoyer_texte(entree, attendu):
    assert nettoyer_texte(entree) == attendu


# ---------- Question 3 : entrees non textuelles ----------
@pytest.mark.parametrize("entree", [123, None], ids=["entier", "none"])
def test_nettoyer_texte_refuse_les_entrees_non_textuelles(entree):
    with pytest.raises(TypeError, match="Texte attendu"):
        nettoyer_texte(entree)


# ---------- Bonus : idempotence ----------
@pytest.mark.parametrize(
    "entree",
    ["  BONJOUR   monde  ", " déjà propre ", "", "     ", "PYTHON"],
    ids=[
        "espaces_et_majuscules",
        "deja_propre",
        "chaine_vide",
        "espaces_seulement",
        "un_mot_en_majuscules",
    ],
)
def test_nettoyer_texte_est_idempotent(entree):
    une_fois = nettoyer_texte(entree)
    deux_fois = nettoyer_texte(une_fois)

    assert deux_fois == une_fois