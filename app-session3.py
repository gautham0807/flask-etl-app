from flask import Flask, request
from typing import List

from services.utils import get_info

app = Flask(__name__)
#loger = get_logger(__name__)


class Student:
    # id: int
    # name: str
    # age: int
    # is_active: bool

    def __init__(self, id, name, age, is_active) -> None:
        self.id = id
        self.name = name
        self.age = age
        self.is_active = is_active
    
    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "age": self.age,
            "is_active": self.is_active
        }

#
# data = [{"id": 1, "name": "Bob"}]
data: List[Student] = []

bob = Student(1, "Bob", 21, True)
data.append(bob)

def get_formated_students(data):
    return [student.to_dict() for student in data]

@app.route("/api/students", methods=["GET"])
def get_students():
    # students = [Student.to_dict(student) for student in data]
    # students = [student.to_dict() for student in data]
    return {"success": True, "students": get_formated_students(data), "status_code": 200}

@app.route("/api/students", methods=["POST"])
def add_student():
    id = request.get_json().get("id")
    name = request.get_json().get("name")
    age = request.get_json()["age"]
    is_active = request.get_json().get("is_active")
    student = Student(id, name, age, is_active)
    data.append(student)
    return {"success": True, "saved_student": student.to_dict(), "status_code": 201}

@app.route("/api/multi-students", methods=["POST"])
def add_multi_students():
    # print(request.get_json())
    for student in request.get_json():
        id = student.get("id")
        name = student.get("name")
        age = student["age"]
        is_active = student.get("is_active")
        new_student = Student(id, name, age, is_active)
        data.append(new_student)
    return {"success": True, "saved_student": get_formated_students(data), "status_code": 201}

#backend data guy
@app.route("/", methods=["GET"])
def index():
    return get_info()

# @app.route("/home")
# def home():
#     data = [{"id": 1, "name": "Bob"}, {"id": 2, "name": "Alex"}] # DB -> Postgres DB
#     html = "<html><h1 align='center'>Home Page</h1>"
#     for row in data:
#         html += f"<p>ID: {row['id']}, NAME: {row['name']}</p>"
#     html += "</html>"
#     return html

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5001, debug=True)