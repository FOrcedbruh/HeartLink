from pydantic_settings import BaseSettings
from pydantic import BaseModel
from dotenv import load_dotenv
import os


load_dotenv()


DB_URL: str = os.environ.get("DB_URL")

JWT_SECRET: str = os.environ.get("JWT_SECRET")
CORS_ORIGIN: str = os.environ.get("CORS_ORIGIN")

S3_ACCESS_KEY: str = os.environ.get("S3_ACCESS_KEY")
S3_SECRET_KEY: str = os.environ.get("S3_SECRET_KEY")
STORAGE_URL: str = os.environ.get("STORAGE_URL")
BUCKET_NAME: str = os.environ.get("BUCKET_NAME")
S3_GET_URL: str = os.environ.get("S3_GET_URL")

PORT: int = os.environ.get("PORT")

# Настройки запуска
class RunConfig(BaseModel):
    port: int = PORT


# Настройки CORS
class CORSConfig(BaseModel):
    origin: str = CORS_ORIGIN


# Настройки базы данных
class DBConfig(BaseModel):
    url: str = DB_URL
    echo: bool = True
    echo_pool: bool = True
    pool_size: int = 10


# Настройки JWT
class JWTConfig(BaseModel):
    secret: str = JWT_SECRET
    access_token_expires_minutes: int = 15
    refresh_token_expires_minutes: int = 60 * 24 * 30


# Настройки S3
class S3Storage(BaseModel):
    access_key: str = S3_ACCESS_KEY
    secret_key: str = S3_SECRET_KEY
    storage_url: str = STORAGE_URL
    bucket_name: str = BUCKET_NAME
    get_url: str = S3_GET_URL


#Точка входа для всех настроек ----------------------------------------------------------------
class Settings(BaseSettings):
    db: DBConfig = DBConfig()
    jwt: JWTConfig =JWTConfig()
    cors: CORSConfig = CORSConfig()
    s3: S3Storage = S3Storage()
    run: RunConfig = RunConfig()
    

settings = Settings()