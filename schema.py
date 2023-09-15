from pydantic import BaseModel

## Blog Model
class Person(BaseModel):
    name: str
    email: str
    age: int

    class Config:
        orm_mode = True
