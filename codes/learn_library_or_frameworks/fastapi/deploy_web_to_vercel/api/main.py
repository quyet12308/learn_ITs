from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Student(BaseModel):
    msv: str
    name: str


@app.get("/")
async def health_check():
    return "the health check successful"


@app.get("/hello")
def hello_group():
    return "Hello nhóm 10"


@app.get("/student/{msv}")
def get_student(msv: str):
    # Thay thế phần này bằng logic để lấy tên sinh viên dựa trên msv
    # Ví dụ:
    students = {"001": "John Doe", "002": "Jane Smith", "003": "Alice Johnson"}
    if msv in students:
        return {"msv": msv, "name": students[msv]}
    else:
        return {"error": "Sinh viên không tồn tại"}


@app.post("/quadratic-equation")
def solve_quadratic_equation(a: float, b: float, c: float):
    # Giải phương trình bậc 2
    delta = b**2 - 4 * a * c
    if delta > 0:
        x1 = (-b + delta**0.5) / (2 * a)
        x2 = (-b - delta**0.5) / (2 * a)
        return {"x1": x1, "x2": x2}
    elif delta == 0:
        x = -b / (2 * a)
        return {"x": x}
    else:
        return {"error": "Phương trình vô nghiệm"}
