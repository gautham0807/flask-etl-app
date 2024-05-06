"""
May 2, 2024
"""

from flask import Flask, request
from typing import List

from services.utils import get_info

app = Flask(__name__)


class Student:

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
    name = request.get_json().get("name")
    age = request.get_json()["age"]
    is_active = request.get_json().get("is_active")
    student = Student(len(data) + 1, name, age, is_active)
    data.append(student)
    return {"success": True, "saved_student": student.to_dict(), "status_code": 201}

@app.route("/api/multi-students", methods=["POST"])
def add_multi_students():
    """
    """
    for student in request.get_json():
        name = student.get("name")
        age = student["age"]
        is_active = student.get("is_active")
        new_student = Student(len(data) + 1, name, age, is_active)
        data.append(new_student)
    return {"success": True, "saved_student": get_formated_students(data), "status_code": 201}

#introducing path variable into the url
@app.route("/api/students/<int:id>", methods=["GET"])
def get_student_by_id(id):
    print(f"Path Variable: {id}")
    for student in data:
        if student.id == id:
            return {"success": True, "students": student.to_dict(), "status_code": 200}
    return {"success": False, "msg": "Bad data", "desc": f"Student with id: {id} doesnot exist"}

@app.route("/api/students/<int:id>", methods=["DELETE"])
def del_student_by_id(id):
    print(id)
    for i, student in enumerate(data):
        if student.id == id:
            del data[i]
            return {"success": True, "deleted_student_id": id, "status_code": 200}
    return {"success": False, "msg": "Bad data", "desc": f"Student with id: {id} doesnot exist"}

@app.route("/api/students/<int:id>", methods=["UPDATE"])
def update_student_by_id(id):
    # // TODO: Update the remaining functionality
    pass

#backend data guy
@app.route("/", methods=["GET"])
def index():
    return get_info() # // FIXME: Dummy fix

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5001, debug=True)