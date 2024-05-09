import pytest
import requests

BASE_URL = "http://localhost:5000/routes/cliente"

cliente_data = {
    "nome": "Teste",
    "email": "teste@example.com",
    "senha": "senha123"
}


def test_registrar_cliente():
    response = requests.post("/cliente", json=cliente_data)
    assert response.status_code == 200
    assert response.json() == "Cliente cadastrado com sucesso"


def test_listar_clientes():
    response = requests.get(BASE_URL + "/cliente")
    assert response.status_code == 200
    assert len(response.json()) > 0


def test_cadastrar_cliente_sem_dados_obrigatorios():
    dados_faltantes = cliente_data.copy()
    dados_faltantes.pop("nome")
    response = requests.post("/cliente", json=dados_faltantes)
    assert response.status_code == 404
    assert response.json() == "Faltam dados obrigatórios"


if __name__ == "__main__":
    pytest.main()
