from typing import Optional
from fastapi import FastAPI, Cookie
from fastapi.responses import JSONResponse

app = FastAPI()

# BEGIN (write your solution here)
@app.get("/language")
async def get_language(language: Optional[str] = Cookie(None)):
    if language is None:
        return JSONResponse(status_code=200, content={"message": "Language not set"})
    return JSONResponse(status_code=200, content={"language": language})
# END
