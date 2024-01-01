from fastapi import APIRouter
from view.movie.movieRouter import movie_router
from view.images.imagesRouter import images_router
from view.exchange_rates.exchange_ratesRouter import exchange_rates_router
from view.synonyms.synonymsRouter import synonyms_router

main_api_router = APIRouter(prefix='/v1')

main_api_router.include_router(movie_router, prefix="/movie")
main_api_router.include_router(images_router, prefix="/images")
main_api_router.include_router(exchange_rates_router, prefix="/rates")
main_api_router.include_router(synonyms_router, prefix="/synonyms")

