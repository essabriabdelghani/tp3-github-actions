"""
#test avant 

import pytest

from app.web import create_app


@pytest.fixture
def client():
    app = create_app()
    app.config["TESTING"] = True
    return app.test_client()


def test_message_normal_est_autorise(client):
    response = client.post("/moderate", json={"message": "bonjour"})

    assert response.status_code == 200
    assert response.get_json() == {"decision": "autoriser"}


def test_message_spam_est_bloque(client):
    response = client.post("/moderate", json={"message": "ceci est du SPAM"})

    assert response.status_code == 200
    assert response.get_json() == {"decision": "bloquer"}


@pytest.mark.parametrize("payload", [{}, {"message": 42}])
def test_message_absent_ou_invalide(client, payload):
    response = client.post("/moderate", json=payload)

    assert response.status_code == 400
    assert response.get_json() == {"error": "Invalid message"}


def test_message_avec_espaces_uniquement(client):
    response = client.post("/moderate", json={"message": "   "})

    assert response.status_code == 400
    assert response.get_json() == {"error": "Invalid message"}

"""  
#test aprés
"""
import pytest

from app.web import create_app


@pytest.fixture
def client():
    app = create_app()
    app.config["TESTING"] = True
    return app.test_client()


# ---------- Questions 1 a 3 ----------
def test_message_normal_est_autorise(client):
    response = client.post("/moderate", json={"message": "bonjour"})

    assert response.status_code == 200
    assert response.get_json() == {"decision": "autoriser"}


def test_message_spam_est_bloque(client):
    response = client.post("/moderate", json={"message": "ceci est du SPAM"})

    assert response.status_code == 200
    assert response.get_json() == {"decision": "bloquer"}


@pytest.mark.parametrize("payload", [{}, {"message": 42}])
def test_message_absent_ou_invalide(client, payload):
    response = client.post("/moderate", json=payload)

    assert response.status_code == 400
    assert response.get_json() == {"error": "Invalid message"}


# ---------- Bonus ----------
def test_message_avec_espaces_uniquement(client):
    response = client.post("/moderate", json={"message": "   "})

    assert response.status_code == 400
    assert response.get_json() == {"error": "Invalid message"}


# ---------- Ajoutes apres l'analyse de couverture ----------
def test_corps_json_de_type_liste(client):
    response = client.post("/moderate", json=["bonjour"])

    assert response.status_code == 400
    assert response.get_json() == {"error": "JSON object required"}


def test_corps_qui_n_est_pas_du_json(client):
    response = client.post(
        "/moderate", data="ceci n'est pas du json", content_type="application/json"
    )

    assert response.status_code == 400
    assert response.get_json() == {"error": "JSON object required"}

"""    