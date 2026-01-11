from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field, validator,condecimal
from typing import List


app = FastAPI()

# Временная база данных
product_list = []
product_id_counter = 1

# BEGIN (write your solution here)
class ProductSpecifications(BaseModel):
    size: str
    color: str
    material: str

    @validator("size", "color", "material")
    def validate_specification(cls, value, field):
        if not value.strip():
            raise ValueError(f"{field.name} cannot be empty.")
        return value

class Product(BaseModel):
    id: int
    name: str
    price: condecimal(ge=0) = Field(..., description="Price must be greater than zero.")
    specifications: ProductSpecifications

    @validator("name")
    def validate_name(cls, value):
        if not value.strip():
            raise ValueError("Name cannot be empty.")
        return value

@app.post("/product")
async def add_product(product: Product):
    global product_id_counter
    product.id = product_id_counter
    product_list.append(product.dict())
    product_id_counter += 1
    return {
        "product": product,
        "message": "Product added successfully"
    }

@app.get("/products")
async def get_products():
    return {
        "products": product_list
    }
# END
