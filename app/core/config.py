from pydantic_settings import BaseSettings
from passlib.context import CryptContext
from fastapi.security import OAuth2PasswordBearer
import logging
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)


class Settings(BaseSettings):
    DB_URI: str = ""
    SECRET: str = ""
    ENCRYPTION_ALGORITHM: str = ""
    bcrypt_context: CryptContext = CryptContext(schemes=['bcrypt'], deprecated="auto")
    oauth2_bearer: OAuth2PasswordBearer = OAuth2PasswordBearer(tokenUrl='token')

    class Config:
        env_file = "./env_vars.env"
        env_file_encoding = 'utf-8'
        case_sensitive = True

settings = Settings()

logger.debug(settings.DB_URI)