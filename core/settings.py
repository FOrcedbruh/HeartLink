from pydantic_settings import BaseSettings
from pydantic import BaseModel
from dotenv import load_dotenv
import os


load_dotenv()


DB_URL: str = os.environ.get("DB_URL")
JWT_SECRET: str = os.environ.get("JWT_SECRET")
CORS_ORIGIN: str = os.environ.get("CORS_ORIGIN")

class CORSConfig(BaseModel):
    origin: str = CORS_ORIGIN

class DBConfig(BaseModel):
    url: str = DB_URL
    echo: bool = True
    echo_pool: bool = True
    pool_size: int = 10


class JWTConfig(BaseModel):
    secret: str = JWT_SECRET
    access_token_expires_minutes: int = 15
    refresh_token_expires_minutes: int = 60 * 24 * 30

class Settings(BaseSettings):
    db: DBConfig = DBConfig()
    jwt: JWTConfig =JWTConfig()
    cors: CORSConfig = CORSConfig()
    
    

settings = Settings()