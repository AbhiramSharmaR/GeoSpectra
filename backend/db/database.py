from motor.motor_asyncio import AsyncIOMotorClient
from backend.config import settings

client = AsyncIOMotorClient(settings.MONGO_DB_URL)
db = client[settings.MONGO_DB_NAME]

async def get_db():
    return db
