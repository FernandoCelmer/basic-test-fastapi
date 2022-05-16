from fastapi import APIRouter
from app.api.v1.endpoints import items

router = APIRouter()
router.include_router(items.router, tags=["Items"])
