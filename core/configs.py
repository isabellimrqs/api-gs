from typing import ClassVar
from pydantic_settings import BaseSettings
from sqlalchemy.orm import declarative_base

class Settings(BaseSettings):
    DB_URL: str = 'mssql+aioodbc://sa:isateste123@CA-C-004UQ\SQLEXPRESS/GS-PT?driver=ODBC+Driver+17+for+SQL+Server'
    DBBaseModel: ClassVar = declarative_base()

    class Config:
        env_file = ".env"

settings = Settings()
