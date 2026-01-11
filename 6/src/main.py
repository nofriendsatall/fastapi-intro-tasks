from fastapi import FastAPI, Form
from fastapi.responses import JSONResponse

app = FastAPI()

# BEGIN (write your solution here)
@app.post("/login", response_class=JSONResponse)
async def login(username: str = Form(...), password: str = Form(...)):
    """Обработка POST-запроса на /login"""
    if username and password:
        return JSONResponse(status_code=200, content={
            "username": username,
            "password": password,
            "status": "Login successful"
        })
    else:
        return JSONResponse(status_code=422, content={
            "detail": "Username and password are required"
        })
# END