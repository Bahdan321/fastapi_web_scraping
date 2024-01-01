from fastapi import APIRouter
from view.movie import movieRouter

main_api_router = APIRouter(prefix='/v1')

main_api_router.include_router(movieRouter, prefix="movie")
