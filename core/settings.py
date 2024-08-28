from pydantic_settings import BaseSettings
from pydantic import BaseModel
from dotenv import load_dotenv
import os


load_dotenv()


DB_URL: str = os.environ.get("DB_URL")



class DBConfig(BaseModel):
    url: str = DB_URL
    echo: bool = True
    echo_pool: bool = True
    pool_size: int = 10




class Settings(BaseSettings):
    db: DBConfig = DBConfig()
    
    

settings = Settings()