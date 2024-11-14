from fastapi import FastAPI
from fastapi.params import Depends
from sqlalchemy.orm import Session

import pydantic_models
from User_Interface.Backend.database_table_setup import get_db, User, RecoveryTokens
from User_Interface.Backend.pydantic_models import UserCreate, UserLogin
from User_Interface.Backend.utils import hash_password, create_user_tokens, verify_password

app = FastAPI()

@app.get("/")
async def read_root():
    return {"message": "server running successfully"}

@app.post("/register")
async def register_user(user: UserCreate, db: Session = Depends(get_db())):
    try:
        hashed_password = hash_password(user.password)
        existing_db_user = db.query(User).filter(User.user_name == user.user_name).first()
        if existing_db_user:
            return {"message": "User already exists"}

        db_user = User(user_name=user.user_name, hashed_password=hashed_password)
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
        print("User registered successfully")

        token_list = create_user_tokens()
        db_token_list = []
        for x in range(3):
            token = token_list[x]
            db_token_list.append(RecoveryTokens(user_id = db_user.user_id, hashed_token=token, used=False))
        db.bulk_save_objects(db_token_list)
        db.commit()
        print("Tokens added to database")
        return_message = f"""Sign up successful. These are your use once recovery tokens\n
                        {db_token_list[0]}\n{db_token_list[1]}\n{db_token_list[2]}\nFurther information on recovery tokens
                        and how to reset your password are in the user profile section or our 'Need Help' page.\n
                        Proceed to login."""
        return {"message": return_message}
    except Exception as e:
        print("Exception in register", e)
        return {"message": e}

@app.post("/login")
async def authenticate_user(user: UserLogin, db: Session =Depends(get_db())):
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
