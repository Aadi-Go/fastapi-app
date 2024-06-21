from fastapi import APIRouter, Depends
from typing import Annotated
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer
from dao.database import get_user
from models.user_models import AuthToken
from core import get_settings
import datetime
from jose import jwt


auth_router = APIRouter()
settings = get_settings()


@auth_router.post("/token", response_model=AuthToken)
async def login_and_fetch_token(form: Annotated[OAuth2PasswordRequestForm, Depends()]):
     user_from_db = await get_user(form.username)
     if not user_from_db:
          return False
     if not settings.bcrypt_context.verify(form.password, user_from_db['password']):
          return False
     else:
          data_to_encode = {'preffered_username': user_from_db["username"], "roles": ["Reader"], 'sub': 'FastAPI'}
          expiry = datetime.datetime.now() + datetime.timedelta(minutes=30)
          data_to_encode.update({'exp': expiry})
          return AuthToken(access_token=jwt.encode(data_to_encode, settings.SECRET, settings.ENCRYPTION_ALGORITHM),
                           token_type="bearer")
