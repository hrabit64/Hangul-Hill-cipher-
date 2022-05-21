from fastapi import APIRouter
from app.hangul_hill.api.api_v1.endpoints.hill.route import hill_route

api_v1_route = APIRouter(prefix="/api/v1")
api_v1_route.include_router(hill_route)
