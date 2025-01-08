from pydantic_settings import BaseSettings
from pydantic import BaseModel
from dotenv import load_dotenv
import os

load_dotenv()

TEST_DB_URL: str = os.environ.get("TEST_DB_URL")


class DBConfig(BaseModel):
    url: str = TEST_DB_URL


class Settings_Test(BaseSettings):
    db: DBConfig = DBConfig()




settings_test = Settings_Test()