from other.parse_exchange_rates import parse_exchange_rates

from fastapi import APIRouter

exchange_rates_router = APIRouter()

@exchange_rates_router.get("/rates")
async def get_exchange_rates_route():
    return parse_exchange_rates()