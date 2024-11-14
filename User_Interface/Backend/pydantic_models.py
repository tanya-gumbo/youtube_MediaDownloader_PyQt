from pydantic import BaseModel


class UserCreate(BaseModel):
    user_name: str
    password: str

    class Config:
        from_attributes = True

class UserLogin(BaseModel):
    user_name: str
    password: str