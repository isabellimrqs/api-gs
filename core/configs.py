from pydantic.v1 import BaseSettings
from sqlalchemy.orm import declarative_base

class Settings(BaseSettings):
    API_V1_sTR: str = '/api/v1'
    DB_URL: str = 'mssql+aioodbc://sa:isateste123@CA-C-004UQ/SQLEXPRESS?driver=ODBC+Driver+17+for+SQL+Server&TrustServerCertificate=yes'

    DBBaseModel = declarative_base()

    class Config:
        case_sensitive = False
        env_file = "env"

settings = Settings()