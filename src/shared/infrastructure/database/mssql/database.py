"""
    Sql alchemy database adapter
"""
from typing import Iterator

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from urllib.parse import quote_plus

from src.shared.config import Settings
from src.shared.dependencies import get_settings

__SETTINGS: Settings = get_settings()

dwh_params = quote_plus(
    f"DRIVER={__SETTINGS.DWH_DB_DRIVER};SERVER={__SETTINGS.DWH_DB_HOST};DATABASE={__SETTINGS.DWH_DB_NAME};"
    f"PORT=1443;UID={__SETTINGS.DWH_DB_USER};PWD={__SETTINGS.DWH_DB_PASS};TrustServerCertificate=YES"
)
dwh_engine = create_engine("mssql+pyodbc:///?odbc_connect=%s" % dwh_params)


SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=dwh_engine,
)


def get_dwh_session() -> Iterator[Session]:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()