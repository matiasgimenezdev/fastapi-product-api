from typing import Annotated
from fastapi import APIRouter, HTTPException, Path, Query, status, Response
from pydantic import ValidationError
from data.products import products
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
async def get_products_with_pagination(limit: Annotated[int | None, Query(ge=0, le=20)] = 10, offset: Annotated[int | None, Query(ge=0)] = 0):
    try:
        """
            Obtiene una lista de productos con paginación.

            Parameters:
            - offset (int): Número de productos a skippear desde el principio. Default value = 0
            - limit (int): Número máximo de productos a devolver. Default value = 10
        """
        product_list = products[offset: offset + limit]
        return {"status": 200, "message": f"List of {limit} products with {offset} offset", "data": product_list}
    except Exception as exception:
        raise HTTPException(
            status_code=500, detail="Server error") from exception


@ router.get("/{product_id}")
async def get_product_by_id(product_id: Annotated[int, Path(title="The ID of the product to get")], response: Response):
    try:
        product_index = search_product(product_id)
        if (product_index == -1):
            response.status_code = status.HTTP_404_NOT_FOUND
            return {"status": 404, "message": f"Product {product_id} not found"}

        return {"status": 200, "message": f"Product {product_id} found", "data": products[product_index]}

    except Exception as exception:
        raise HTTPException(
            status_code=500, detail="Server error") from exception


@router.post("/")
async def create_product(new_product: Product, response: Response):
    try:
        product_index = search_product(new_product.product_id)

        if (product_index > -1):
            response.status_code = status.HTTP_400_BAD_REQUEST
            return {"status": 400, "message": f"Product {new_product.product_id} already exists"}

        products.append(new_product)
        response.status_code = status.HTTP_201_CREATED
        return {"status": 201, "message": f"Product {new_product.product_id} created", "data": new_product}
    except Exception as exception:
        raise HTTPException(
            status_code=500, detail="Server error") from exception


@router.put("/")
async def update_product(updated_product: Product, response: Response):
    try:
        product_index = search_product(updated_product.product_id)
        if (product_index < 0):
            response.status_code = status.HTTP_404_NOT_FOUND
            return {"status": 404, "message": f"Product {updated_product.product_id} not found"}

        products[product_index] = updated_product
        return {"status": 200, "message": f"Product {updated_product.product_id} updated"}
    except Exception as exception:
        raise HTTPException(
            status_code=500, detail="Server error") from exception


@ router.delete("/{product_id}")
async def delete_product(product_id: Annotated[int, Path(title="The ID of the product to delete")], response: Response):
    try:
        product_index = search_product(product_id)

        if (product_index == -1):
            response.status_code = status.HTTP_404_NOT_FOUND
            return {"status": 404, "message": f"Product {product_id} not found"}

        del products[product_index]
        return {"status": 200, "message": f"Product {product_id} deleted"}

    except Exception as exception:
        return {"message": f"{exception}"}
        raise HTTPException(
            status_code=500, detail="Server error") from exception


def search_product(product_id: int):
    for index, product in enumerate(products):
        if product.product_id == product_id:
            return index
    return -1
