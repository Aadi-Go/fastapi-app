from fastapi import APIRouter
from DAO.database import add_user
from models.user_models import CreateUser
from core import settings

router = APIRouter()


@router.post("/register")
async def register_user(user: CreateUser):
    if await add_user(user.username, settings.bcrypt_context.hash(user.password)):
        return "User added successfully"
    else:
        return "Registration failed"


