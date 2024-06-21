from fastapi import APIRouter
from dao.database import add_user
from models.user_models import CreateUser
from core import get_settings

router = APIRouter()
settings = get_settings()


@router.post("/register")
async def register_user(user: CreateUser):
    if await add_user(user.username, settings.bcrypt_context.hash(user.password)):
        return "User added successfully"
    else:
        return "Registration failed"


