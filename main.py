from fastapi import FastAPI, HTTPException
from typing import List
import schemas
import crud

app = FastAPI()

@app.post("/students/", response_model=schemas.Student)
def create_student(student: schemas.StudentCreate):
    return crud.create_student(student)

@app.get("/students/", response_model=List[schemas.Student])
def read_students():
    return crud.get_students()

@app.get("/students/{student_id}", response_model=schemas.Student)
def read_student(student_id: int):
    student = crud.get_student(student_id)
    if student is None:
        raise HTTPException(status_code=404, detail="Student not found")
    return student

@app.put("/students/{student_id}")
def update_student(student_id: int, student: schemas.StudentCreate):
    return crud.update_student(student_id, student)

@app.delete("/students/{student_id}")
def delete_student(student_id: int):
    return crud.delete_student(student_id)
