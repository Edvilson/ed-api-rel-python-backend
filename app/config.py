import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    DB_PATH = os.getenv("DB_PATH", "relatorio.db")
