from fastapi import APIRouter

from api.auth.router.auth import auth_router
from api.user.router.user import user_router

router = APIRouter()
router.include_router(user_router, prefix="/api/users", tags=["User"])
router.include_router(auth_router, prefix="/auth", tags=["Auth"])

__all__ = ["router"]
