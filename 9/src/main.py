from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from typing import List, Optional


app = FastAPI()

# Временная база данных
product_list = []
product_id_counter = 1

# BEGIN (write your solution here)
class Specifications(BaseModel):
    size: str = Field(..., description="Размер продукта")
    color: str = Field(..., description="Цвет продукта")
    material: str = Field(..., description="Материал продукта")
    
class ProductResponse(BaseModel):
    id: int
    name: str
    price: float


class ProductDetailResponse(BaseModel):
    id: int
    name: str
    price: float
    specifications: Specifications


class Product(BaseModel):
    name: str
    price: float
    specifications: Specifications


def get_product_response(product: dict) -> ProductResponse:
    return ProductResponse(
        id=product["id"],
        name=product["name"],
        price=product["price"],
    )


def get_product_detail_response(product: dict) -> ProductDetailResponse:
    return ProductDetailResponse(
        id=product["id"],
        name=product["name"],
        price=product["price"],
        specifications=Specifications(
            size=product["specifications"]["size"],
            color=product["specifications"]["color"],
            material=product["specifications"]["material"],
        ),
    )


@app.get("/product/{product_id}", response_model=ProductDetailResponse)
async def get_product(product_id: int) -> ProductDetailResponse:
    product = next((item for item in product_list if item["id"] == product_id), None)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return get_product_detail_response(product)


@app.get("/products", response_model=List[ProductResponse])
async def get_products() -> List[ProductResponse]:
    return [get_product_response(product) for product in product_list]


@app.post("/product")
async def add_product(data: Product):
    global product_id_counter
    new_product = data.dict()
    new_product["id"] = product_id_counter
    product_id_counter += 1
    product_list.append(new_product)
    return get_product_response(new_product)
# END