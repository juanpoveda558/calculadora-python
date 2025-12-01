from fastapi import APIRouter
from datetime import datetime

router = APIRouter()

@router.get("/local-time")
def get_local_time(format: str = "%Y-%m-%d %H:%M:%S"):
    current_time = datetime.now().strftime(format)
    return {"local_time": current_time}