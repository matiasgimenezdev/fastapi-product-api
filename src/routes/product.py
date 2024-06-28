from typing import Annotated
from fastapi import APIRouter, HTTPException, Path, Query, status, Response
from pydantic import ValidationError
from data.mock_data import products
from models.product import Product

router = APIRouter(prefix="/api/product")


@ router.get("/")
async def get_products():
    try:
        return {"status": 200, "message": f"{len(products)} products found", "data": products}
    except Exception as exception:
        raise HTTPException(
            status_code=500, detail="Server error") from exception

@ router.get("/page")
async def get_products_page(limit: Annotated[int | None, Query(ge=0, le=20)] = 10, offset: Annotated[int | None, Query(ge=0)] = 0):
    try:
        return {"status": 200, "message": f"Limit: {limit} & Offset: {offset}", "data": products}
    except Exception as exception:
        raise HTTPException(
            status_code=500, detail="Server error") from exception


@ router.get("/{product_id}")
async def get_product_by_id(product_id: Annotated[int, Path(title="The ID of the product to get")], response: Response):
    try:
        for product in products:
            if (product_id == product.product_id):
                return {"status": 200, "message": f"Product {product_id} found", "data": product}

        response.status_code = status.HTTP_404_NOT_FOUND
        return {"status": 404, "message": f"Product {product_id} not found"}
    except Exception as exception:
        raise HTTPException(
            status_code=500, detail="Server error") from exception


@router.post("/")
async def create_product(new_product: Product, response: Response):
    try:
        for product in products:
            if new_product.product_id == product.product_id:
                response.status_code = status.HTTP_400_BAD_REQUEST
                return {"status": 400, "message": f"Product {product.product_id} already exists"}

        products.append(new_product)
        response.status_code = status.HTTP_201_CREATED
        return {"status": 201, "message": f"Product {new_product.product_id} created", "data": new_product}
    except Exception as exception:
        raise HTTPException(
            status_code=500, detail="Server error") from exception


@router.put("/")
async def update_product(updated_product: Product, response: Response):
    try:
        for index, product in enumerate(products):
            if updated_product.product_id == product.product_id:
                products[index] = updated_product
                return {"status": 200, "message": f"Product {product.product_id} updated"}

        response.status_code = status.HTTP_404_NOT_FOUND
        return {"status": 404, "message": f"Product {updated_product.product_id} not found"}
    except Exception as exception:
        raise HTTPException(
            status_code=500, detail="Server error") from exception


@ router.delete("/{product_id}")
async def delete_product(product_id: Annotated[int, Path(title="The ID of the product to delete")], response: Response):
    try:
        for index, product in enumerate(products):
            if product.product_id == product_id:
                del products[index]
                return {"status": 200, "message": f"Product {product_id} deleted"}

        response.status_code = status.HTTP_404_NOT_FOUND
        return {"status": 404, "message": f"Product {product_id} not found"}
    except Exception as exception:
        raise HTTPException(
            status_code=500, detail="Server error") from exception
