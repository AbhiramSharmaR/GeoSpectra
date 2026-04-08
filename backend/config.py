import os

class Config:
    MONGO_DB_URL = os.getenv("MONGO_DB_URL", "mongodb://localhost:27017")
    MONGO_DB_NAME = os.getenv("MONGO_DB_NAME", "geospectra")
    SECRET_KEY = os.getenv("SECRET_KEY", "your-super-secret-key-geospectra")
    ALGORITHM = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES = 60 * 24 * 7  # 1 week

settings = Config()
