#livraison avec le bug
"""
def frais_livraison(montant):
    if montant < 0:
        raise ValueError("Montant negatif")
    if montant > 300:
        return 0
    return 25

"""
#la correction

def frais_livraison(montant):
    if montant < 0:
        raise ValueError("Montant negatif")
    if montant >= 300:
        return 0
    return 25