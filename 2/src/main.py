from fastapi import FastAPI, Query
from fastapi.responses import JSONResponse

app = FastAPI()

# BEGIN (write your solution here)
@app.get("/filter")
async def filter(min: int = Query(0, ge=0), max: int = Query(100, le=100)):
    if min < 0 or max > 100:
        return JSONResponse(status_code=422, content={"detail": "min should be greater than or equal to 0 and max should be less than or equal to 100"})
    return {"min": min, "max": max}
# END
