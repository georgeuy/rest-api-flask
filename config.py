import os
from dotenv import load_dotenv

dotenv_file_path: str = os.path.join(os.path.dirname(__file__), '.env')

if os.path.exists(dotenv_file_path):
    load_dotenv(dotenv_file_path)

class Config:
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopmentConfig(Config):
    SQLALCHEMY_DATABASE_URI = "sqlite+pysqlite:///database.sqlite"
    

class ProductionConfig(Config):
    pass