import sys
import os

# Adiciona a pasta 'src' ao caminho de busca do Python
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

import pytest
from fastapi.testclient import TestClient
from main import app  # Agora ele vai procurar dentro de src/

client = TestClient(app)

# Seus 5 testes abaixo...
# Teste da Soma
def test_soma():
    response = client.get("/calcular?operacao=soma&a=10&b=5")
    assert response.status_code == 200
    assert response.json()["resultado"] == 15

# Teste da Subtração
def test_subtracao():
    response = client.get("/calcular?operacao=subtracao&a=10&b=5")
    assert response.status_code == 200
    assert response.json()["resultado"] == 5

# Teste da Multiplicação
def test_multiplicacao():
    response = client.get("/calcular?operacao=multiplicacao&a=10&b=5")
    assert response.status_code == 200
    assert response.json()["resultado"] == 50

# Teste da Divisão Normal
def test_divisao():
    response = client.get("/calcular?operacao=divisao&a=10&b=2")
    assert response.status_code == 200
    assert response.json()["resultado"] == 5

# Teste quando houver erro de Divisão por Zero
def test_divisao_por_zero():
    response = client.get("/calcular?operacao=divisao&a=10&b=0")
    assert response.status_code == 200
    assert response.json() == {"erro": "divisão por zero"}