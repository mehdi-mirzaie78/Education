from typing import Optional
from pydantic import BaseModel, EmailStr


# Properties required during user creation
class UserCreate(BaseModel):
    username: str
    email: Optional[EmailStr]
    password: str


