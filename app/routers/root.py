from fastapi import APIRouter
from fastapi.responses import JSONResponse

router = APIRouter()


@router.get("/")
def root():
    return JSONResponse(content={"message": "welcome to the cuizy API service", "status": True}, status_code=200)