import pytest, json
from app import app, potencia, es_par

@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client

def test_index(client):
    res = client.get("/")
    assert res.status_code == 200
    assert "Bienvenido" in res.get_data(as_text=True)

def test_sumar(client):
    res = client.get("/sumar/5/7")
    assert json.loads(res.data)["resultado"] == 12

def test_restar(client):
    res = client.get("/restar/10/4")
    assert json.loads(res.data)["resultado"] == 6

def test_es_primo(client):
    res = client.get("/es-primo/7")
    assert json.loads(res.data)["es_primo"] is True

def test_dividir(client):
    res = client.get("/dividir/10/2")
    assert json.loads(res.data)["resultado"] == 5

def test_division_por_cero(client):
    res = client.get("/dividir/10/0")
    assert res.status_code == 400

def test_potencia(): assert potencia(2, 3) == 8
def test_es_par(): assert es_par(6)
