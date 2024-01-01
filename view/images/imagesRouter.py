from other.parse_images import parse_images

from fastapi import APIRouter

images_router = APIRouter()

@images_router.get("/images")
async def get_first_ten_images(query: str,api_key, cx):
    return parse_images(query,api_key, cx)