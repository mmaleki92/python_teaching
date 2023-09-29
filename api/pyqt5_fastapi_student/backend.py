from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()

students = []

class Student(BaseModel):
    name: str
    age: int

@app.get("/students/", response_model=List[Student])
def get_students():
    return students

@app.post("/students/")
def create_student(student: Student):
    students.append(student.dict())
    return student

@app.delete("/students/{student_id}")
def delete_student(student_id: int):
    if 0 <= student_id < len(students):
        return students.pop(student_id)
    return {"error": "Student not found"}

