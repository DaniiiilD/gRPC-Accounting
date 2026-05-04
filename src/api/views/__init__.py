from fastapi import APIRouter
from src.api.views.tariff import tariff_router

api_router = APIRouter(prefix="/api")

api_router.include_router(tariff_router)
