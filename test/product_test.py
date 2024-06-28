from unittest.mock import patch
from server import app
from fastapi.testclient import TestClient
from data.products import products

client = TestClient(app)


def test_status_endpoint():
    response = client.get("/api/status")
    assert response.status_code == 200
    assert response.json() == {"message": "API is working!"}


def test_get_products():
    response = client.get("/api/product")

    # Verificar el código de estado
    assert response.status_code == 200

    # Verificar la estructura de la respuesta JSON
    json_response = response.json()
    assert "status" in json_response
    assert "message" in json_response
    assert "data" in json_response

    # Verificar el mensaje y la cantidad de productos
    assert json_response["status"] == 200
    assert "4 products found" in json_response["message"]
    assert len(json_response["data"]) == 4


def test_get_product_by_id():
    response = client.get("/api/product/1")

    # Verificar el código de estado
    assert response.status_code == 200

    # Verificar la estructura de la respuesta JSON
    json_response = response.json()
    assert "status" in json_response
    assert "message" in json_response
    assert "data" in json_response

    assert response.json() == {
        "status": 200,
        "message": f"Product 1 found",
        "data": {
            "product_id": 1, "description": "Apple Macbook Pro M2",
            "price": 1200.0, "tax": 200.0, "stock": 5
        }
    }
