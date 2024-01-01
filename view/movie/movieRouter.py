from other.parse_movies import parse_movies

from fastapi import APIRouter

movie_router = APIRouter()

@movie_router.get("/movies")
async def get_movies_by_year(year: int):
    return parse_movies(year)