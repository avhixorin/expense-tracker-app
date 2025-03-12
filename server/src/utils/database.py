from motor.motor_asyncio import AsyncIOMotorClient
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017")

# Global variables for database
client = None
db = None

async def connect_db():
    """Connect to MongoDB and initialize the database."""
    global client, db
    client = AsyncIOMotorClient(MONGO_URI)
    db = client["expense_tracker"]
    print("✅ Connected to MongoDB")

async def close_db():
    """Close the MongoDB connection."""
    global client
    if client:
        client.close()
        print("❌ Disconnected from MongoDB")

# Dependency to get the database instance
async def get_db():
    """Provide the database instance to FastAPI routes."""
    if db is None:
        raise Exception("Database is not initialized. Call connect_db() first.")
    return db
