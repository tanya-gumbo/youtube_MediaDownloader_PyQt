import asyncio

import uvicorn
import time
from fastapi import FastAPI
from fastapi.params import Depends
from User_Interface.Backend.database_table_setup import get_db, User, RecoveryTokens, SessionLocal
from User_Interface.Backend.pydantic_models import UserCreate, UserLogin
from User_Interface.Backend.utils import hash_password, create_user_tokens, verify_password, hash_token
from User_Interface.Frontend.Settings import JSON_file_methods as jsn
from sqlalchemy.orm import Session


app = FastAPI()

def warm_up_db():
    db = SessionLocal()
    time_start = time.monotonic()
    try:
        # Execute a simple query (e.g., count users)
        user_count = db.query(User).count()
        end_time = time.monotonic()
        print(f"The time taken is{end_time-time_start:.5f} seconds")
        print("Database warmed up successfully.")
    except Exception as e:
        print(f"Error warming up database: {e}")

# Call the warm-up function directly after the app instantiation
login_status = jsn.read_json_status()
if login_status != "logged in":
    warm_up_db()

@app.get("/")
async def read_root():
    return {"message": "server running successfully"}

@app.post("/register")
async def register_user(user: UserCreate, db: Session = Depends(get_db)):
    print("We are in ehehe")
    whole_func_start =time.monotonic()
    try:
        hashed_password = hash_password(user.password)
        start_time = time.monotonic()
        existing_db_user = db.query(User).filter(User.user_name == user.user_name).first()
        end_time = time.monotonic()
        print(f"The time it took for the query is{end_time-start_time:.4f} seconds")

        if existing_db_user:
            return {"message": "User already exists"}

        start_time2 = time.monotonic()
        db_user = User(user_name=user.user_name, hashed_password=hashed_password)
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
        end_time2 = time.monotonic()
        print(f"The time it took to commit user to database is{end_time2-start_time2:.4f}seconds")
        print("User registered successfully")

        token_list = create_user_tokens()
        hashed_token_list = []

        for x in range(5):
            token = token_list[x]
            hashed_token = hash_token(token)
            hashed_token_list.append(hashed_token)

        db_token_list = []

        for x in range(5):
            token = hashed_token_list[x]
            db_token_list.append(RecoveryTokens(user_id = db_user.user_name, hashed_token=token, use_status=False))

        start_time3 = time.monotonic()
        db.bulk_save_objects(db_token_list)
        db.commit()
        end_time3 = time.monotonic()
        print(f"The time it took to commit tokens to database is{end_time3-start_time3:.4} seconds")
        print("Tokens added to database")
        return_message = \
            f"""Sign up successful. These are your use once recovery tokens
                Token1: {token_list[0]}
                Token2: {token_list[1]}
                Token3: {token_list[2]}
                Token4: {token_list[3]}
                Token5: {token_list[4]}
                You only have 5 recovery tokens.
                Further information on recovery tokens and how to reset your 
                password are in the user profile section or on our
                'Need Help' page. Proceed to login."""
        whole_func_end = time.monotonic()
        print(f"The whole time for the whole function is {whole_func_end-whole_func_start:.5f} seconds")
        return {"message": return_message}
    except Exception as e:
        print("Exception in register method", e)
        return {"message": str(e)}

@app.post("/login")
async def authenticate_user(user: UserLogin, db: Session =Depends(get_db)):
    user_exists = db.query(User).filter(User.user_name == user.user_name).first()
    try:
        if user_exists is None:
            return {"message": "User doesn't exist"}

        if not verify_password(user.password, user_exists.hashed_password):
            return {"message": "Incorrect password"}
        else:
            return {"message": "logged in"}
    except Exception as e:
        print(e)


def start_fastapi():
    config = uvicorn.Config(app, host="127.0.0.1", port=8000, log_level="info")
    server = uvicorn.Server(config)
    server.run()
