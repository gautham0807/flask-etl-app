"""
1. save student
2. fetch student by id
3. fetch all students
4. update student by id
5. delete student  by id
"""

import sqlite3
students_db_file = "students.db"

# class Connection:
#     connection = sqlite3.connect("students.db")

#     def __init__(self, db_file):
#         self.db_file = db_file
#         self.connection = None

#     def __enter__(self):
#         return self.connection

#     def __exit__(self, exc_type, exc_value, traceback):
#         if self.connection:
#             self.connection.close()

class Connection:
    def __init__(self, db_file):
        self.db_file = db_file
        self.connection = None

    def __enter__(self):
        self.connection = sqlite3.connect(self.db_file)
        return self.connection

    def __exit__(self, exc_type, exc_value, traceback):
        if self.connection:
            self.connection.close()



def initialize_db():
    """This method is responsible for creation DDL for student class"""
    ddl_stmt = """
    CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        age INTEGER,
        is_active INTEGER
    );
    """
    with Connection(students_db_file) as c:
        c.execute(ddl_stmt)
        c.commit()
    print("Db has been initialized...")

initialize_db()

def save_student(name: str, age: int, is_active: bool = True):
    sql = f"INSERT INTO students(name, age, is_active) VALUES(?, ?, ?)"
    print(sql)
    with Connection(students_db_file) as c:
        c.execute(sql, (name, age, is_active))
        # saved_id = c.lastrowid()
        # print(saved_id)
        c.commit()

def fetch_all_students(n: int = 10):
    sql = f"SELECT * FROM students LIMIT {n}"
    with Connection(students_db_file) as c:
        res = c.execute(sql).fetchall()
        for id, name, age, is_active in res:
            print(id, name, age, is_active)

"""
function printData():
    createTable

fetch("")
.then(data => data.json())
.then(res => {
    printData(res)
})
"""


if __name__ == "__main__":
    # save_student("Mark", 23, 1)
    fetch_all_students(n=3)



# import sqlite3



# # Example usage
# db_file = 'example.db'

# # Using the custom connection class with a 'with' statement
# with CustomConnection(db_file) as conn:
#     cursor = conn.cursor()
#     cursor.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT)")
#     cursor.execute("INSERT INTO users (name) VALUES ('Alice')")
#     conn.commit()  # Remember to commit changes

#     cursor.execute("SELECT * FROM users")
#     rows = cursor.fetchall()
#     for row in rows:
#         print(row)
