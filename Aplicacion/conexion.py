import os
import oracledb
from pathlib import Path
from dotenv import load_dotenv

load_dotenv(Path(__file__).with_name(".env"))


def obtener_conexion():
    conexion = oracledb.connect(
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        dsn=os.getenv("DB_DSN"),
        config_dir=os.getenv("DB_WALLET_PATH"),
        wallet_location=os.getenv("DB_WALLET_PATH"),
        wallet_password=os.getenv("DB_WALLET_PASSWORD")
    )

    return conexion