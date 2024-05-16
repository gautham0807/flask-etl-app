"""
May 6, 2024: Using GET to Connect to DB and fetching the data
"""

from flask import Flask, request
from typing import List

from services.utils import get_info
from services import student_service

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


def get_formated_students(data):
    return [student.to_dict() for student in data]

@app.route("/api/students", methods=["GET"])
def get_students():
    """"""
    #modified code
    result = student_service.fetch_all_students(10)
    students = [Student(*row).to_dict() for row in result]
    return {"success": True, "students": students, "status_code": 200}

@app.route("/api/students", methods=["POST"])
def add_student():
    name = request.get_json().get("name")
    age = request.get_json()["age"]
    is_active = request.get_json().get("is_active")
    student_service.save_student(name, age, is_active)
    return {"success": True, "saved_student": f"{name} is added", "status_code": 201}


# introducing path variable into the url
@app.route("/api/students/<int:id>", methods=["GET"])
def get_student_by_id(id):
    print(f"Path Variable: {id}")
    student_in_db = student_service.fetch_student_by_id(id)
    # for student in data:
    if student_in_db is not None:
        student = Student(*student_in_db).to_dict()
        return {"success": True, "students": student, "status_code": 200}
    return {"success": False, "msg": "Bad data", "desc": f"Student with id: {id} does not exist"}

@app.route("/api/students/<int:id>", methods=["DELETE"])
def del_student_by_id(id):
    print(id)
    student_in_db = student_service.fetch_student_by_id(id)
    # for student in data:
    if student_in_db is not None:
        res = student_service.delete_student_by_id(id)
        return {"success": True, "deleted_student_id": f"{student_in_db[0]} is Deleted", "status_code": 200}
    return {"success": False, "msg": "Bad data", "desc": f"Student with id: {id} does not exist"}

@app.route("/api/students/<int:id>", methods=["PATCH"])
def update_student_by_id(id):
    print(id)
    student_in_db = student_service.fetch_student_by_id(id)
    if student_in_db is None:
        return {"success": False, "msg": "Bad data", "desc": f"Student with id: {id} does not exist"}
    ## Get the data from Payload
    name = request.get_json().get("name")
    age = request.get_json()["age"]
    is_active = request.get_json().get("is_active")
    res = student_service.update_student_by_id(id, name, age, is_active)
    return {"success": True, "updated_student_id": f"{name} is Updated", "status_code": 200}


#backend data guy
@app.route("/", methods=["GET"])
def index():
    return get_info() # // FIXME: Dummy fix

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5001, debug=True)