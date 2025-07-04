"""
    Config module
"""
from pydantic_settings import BaseSettings


class Settings(BaseSettings):

    # DATABASE SETTINGS
    POSTGRES_SERVER: str
    POSTGRES_PORT: int
    POSTGRES_DB: str
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str

    # DWH DATABASE SETTINGS
    DWH_DB_DRIVER: str
    DWH_DB_HOST: str
    DWH_DB_NAME: str
    DWH_DB_USER: str
    DWH_DB_PASS: str

    # AWS SETTINGS
    AWS_ENDPOINT: str
    AWS_REGION: str
    AWS_BUCKET: str
    AWS_ACCESS_KEY: str
    AWS_SECRET_KEY: str


settings = Settings()
