from typing import List

from fastapi import APIRouter, Depends, Query

from app.user.schemas import ExceptionResponseSchema
from app.user.schemas.user import (
    GetUserListResponseSchema,
    CreateUserResponseSchema,
    CreateUserRequestSchema,
)
from app.user.services import UserService
from core.fastapi.dependencies import PermissionDependency, IsAdmin

user_router = APIRouter()


@user_router.get(
    "",
    response_model=List[GetUserListResponseSchema],
    response_model_exclude={"id"},
    responses={"400": {"model": ExceptionResponseSchema}},
    dependencies=[Depends(PermissionDependency([IsAdmin]))],
)
async def get_user_list(
    limit: int = Query(10, description="Limit"),
    prev: int = Query(None, description="Prev ID"),
):
    return await UserService().get_user_list(limit=limit, prev=prev)


@user_router.post(
    "",
    response_model=CreateUserResponseSchema,
    responses={"400": {"model": ExceptionResponseSchema}},
)
async def create_user(
    request: CreateUserRequestSchema,
    user_service: UserService = Depends(),
):
    await user_service.create_user(**request.model_dump())

    return {"email": request.email, "nickname": request.nickname}
