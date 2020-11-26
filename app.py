from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

db = []


class Student(BaseModel):
    name: str


@app.get('/')
def index():
    return 'Hello world!'


@app.get('/student')
def get_students():
    return db


@app.get('/student/{student_id}')
def get_student(student_id: int):
    return db[student_id-1]


@app.post('/student')
def create_student(student: Student):
    db.append(student.dict())
    return student


@app.delete('/student/{student_id}')
def delete_student(student_id: int):
    db.pop(student_id-1)
    return db


if __name__ == '__main__':
    # Use hypercorn to spawn as a server
    import asyncio
    from hypercorn.config import Config
    from hypercorn.asyncio import serve

    asyncio.run(serve(app, Config()))
