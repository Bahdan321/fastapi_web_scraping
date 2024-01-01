from fastapi import APIRouter
from view.movie.movieRouter import movie_router

main_api_router = APIRouter(prefix='/v1')

main_api_router.include_router(movie_router, prefix="/movie")
