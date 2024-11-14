from fastapi import FastAPI
import pydantic_models

app = FastAPI()

@app.get("/")
async def read_root():
    return {"message": "server running successfully"}

@app.post("/register")
async def register_user():
    pass

@app.post("/login")
async def authenticate_user():
    pass
