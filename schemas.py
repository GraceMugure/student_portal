from pydantic import BaseModel

class StudentBase(BaseModel):
    name: str
    email: str
    age: int

class StudentCreate(StudentBase):
    pass

class Student(StudentBase):
    id: int

    class Config:
        orm_mode = True

