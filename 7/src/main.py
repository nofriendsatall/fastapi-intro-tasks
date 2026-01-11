from fastapi import FastAPI, HTTPException,Form
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field, conint, condecimal
from typing import List


app = FastAPI()

# Временная база данных
product_list = []
product_id_counter = 1

# BEGIN (write your solution here)

# END
