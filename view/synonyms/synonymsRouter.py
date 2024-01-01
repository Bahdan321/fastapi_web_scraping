from other.parse_synonyms import get_synonyms

from fastapi import APIRouter

synonyms_router = APIRouter()

@synonyms_router.get("/synonyms")
async def get_synonyms_by_count(word: str, count: int):
    return get_synonyms(word, count)