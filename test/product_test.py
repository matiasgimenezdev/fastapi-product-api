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

    assert response.status_code == 200

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


def test_create_product():
    response = client.post(
        "/api/product",
        json={
            "product_id": 6,
            "description": "New product",
            "price": 1200.0,
            "tax": 200.0,
            "stock": 5
        },
    )

    assert response.status_code == 201
    assert response.json() == {
        "status": 201,
        "message": "Product 6 created",
        "data": {
            "product_id": 6,
            "description": "New product",
            "price": 1200.0,
            "tax": 200.0,
            "stock": 5
        }
    }


def test_update_product():
    response = client.put(
        "/api/product",
        json={
            "product_id": 1,
            "description": "Apple Macbook Pro M2",
            "price": 1200.0,
            "tax": 250.0,
            "stock": 1
        },
    )

    assert response.status_code == 200
    assert response.json() == {
        "status": 200,
        "message": "Product 1 updated",
    }


def test_delete_product():
    response = client.delete("/api/product/1")

    assert response.status_code == 200
    assert response.json() == {
        "status": 200,
        "message": "Product 1 deleted",
    }
