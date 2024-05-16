import psycopg2


def get_conn():
    return psycopg2.connect(
        database="data-engineering", 
        user="postgres", 
        password="Gautham@123", 
        host="localhost"
    )



def save_student(name: str, age: int, is_active: bool = True):
    return None
    # sql = f"INSERT INTO students(name, age, is_active) VALUES(?, ?, ?)"
    # print(sql)
    # with Connection(students_db_file) as c:
    #     c.execute(sql, (name, age, is_active))
    #     # saved_id = c.lastrowid()
    #     # print(saved_id)
    #     c.commit()

def fetch_all_students(n: int = 10):
    sql = f"SELECT * FROM test.students LIMIT {n}"
    with get_conn().cursor() as c:
        c.execute(sql)
        return c.fetchall()

def fetch_student_by_id(id):
    return None
    # sql = "SELECT * FROM students where id = ?"
    # with Connection(students_db_file) as c:
    #     return c.execute(sql, (id,)).fetchone()
    
def delete_student_by_id(id):
    return None
    # sql = "DELETE FROM students where id = ?"
    # try:
    #     with Connection(students_db_file) as c:
    #         c.execute(sql, (id,))
    #         c.commit()
    #         return True
    # except Exception as e:
    #     print(e)
    # return False

def update_student_by_id(id: int, name: str, age: int, is_active: bool = True):
    return None
    # sql = "UPDATE students SET name = ?, age = ?, is_active =? where id = ?"
    # try:
    #     with Connection(students_db_file) as c:
    #         c.execute(sql, (name, age, is_active, id))
    #         c.commit()
    #         return True
    # except Exception as e:
    #     print(e)
    # return False
