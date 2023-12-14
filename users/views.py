from fastapi import APIRouter
from users.schemas import CreateUser
from users import crud

router_user = APIRouter(prefix="/users", tags=["users"])


@router_user.post("/")
def create_user(user: CreateUser):
    return crud.create_user(user_in=user)
