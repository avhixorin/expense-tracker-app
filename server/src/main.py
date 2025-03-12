from fastapi import FastAPI
# from .server.src.utils.dbConnect import connect_db, close_db
import os
from dotenv import load_dotenv
load_dotenv()
app = FastAPI()
# @app.on_event("startup")
# async def startup_db():
#     await connect_db()

# @app.on_event("shutdown")
# async def shutdown_db():
#     await close_db()

@app.get("/")
def read_root():
    return {"message": "Hello, World!"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=os.getenv("PORT"), reload=True)
