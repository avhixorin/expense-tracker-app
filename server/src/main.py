from fastapi import FastAPI, Depends
from utils.database import connect_db, close_db, get_db
from schemas.user import UserCreate, UserResponse
import os
from dotenv import load_dotenv
from motor.motor_asyncio import AsyncIOMotorDatabase

load_dotenv()

app = FastAPI()

@app.on_event("startup")
async def startup_db():
    await connect_db()

@app.on_event("shutdown")
async def shutdown_db():
    await close_db()

@app.get("/")
def read_root():
    return {"message": "Hello, World!"}

@app.post("/users/", response_model=UserResponse)
async def create_user(user: UserCreate, db: AsyncIOMotorDatabase = Depends(get_db)):
    """Create a new user in MongoDB."""
    user_dict = user.dict()
    result = await db.users.insert_one(user_dict)
    return {"id": str(result.inserted_id), "username": user.username, "email": user.email}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=int(os.getenv("PORT", 8000)), reload=True)
