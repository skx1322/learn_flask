from pydantic import BaseModel, Field, EmailStr

class UserSchema(BaseModel):
    username: str
    email: EmailStr
    password: str = Field(min_length=9, max_length=24)
    age: int = Field(gt=12, lt=120)

    