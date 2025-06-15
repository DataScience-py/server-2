from pydantic import BaseModel, EmailStr
from typing import Optional


class User(BaseModel):
    id: int
    username: str
    email: EmailStr
    firstname: str
    lastname: str
    hashed_password: str



class UserRegisterForm(BaseModel):
    username: str
    email: EmailStr
    firstname: str
    lastname: str
    password: str
    confirm_password: str
    

class UserExists(BaseModel):
    id: Optional[int] = None
    username: Optional[str] = None
    email: Optional[EmailStr] = None


class LoginUser(UserExists):
    password: str

class AddUser(BaseModel):
    username: str
    email: EmailStr
    firstname: str
    lastname: str
    hashed_password: str