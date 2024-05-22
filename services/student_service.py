import psycopg2
import os

from dotenv import load_dotenv

load_dotenv() #searches for .env in the repo. Exports k:v pairs.

def get_conn():
    return psycopg2.connect(
        database= os.getenv("DB_NAME"), 
        user= os.getenv("DB_USR_NAME"), 
        password= os.getenv("DB_PWD"),
        host= os.getenv("DB_HOST")
    )

def save_student(name: str, age: int, is_active: bool = True):
    sql = f"INSERT INTO test.students(name, age, is_active) VALUES(%(name)s, %(age)s, %(is_active)s)"

    try:
        conn = get_conn()    

        with conn.cursor() as c:
            try:
                c.execute(sql, {"name": name, "age": age, "is_active": is_active})
                saved_id = c.lastrowid
                print(saved_id)
            except Exception as e:
                print(e)
        
        conn.commit()
    except Exception as e:
        print(f"Couldn't insert the record: {e}")



def fetch_all_students(n: int = 10):
    sql = f"SELECT * FROM test.students LIMIT {n}"
    with get_conn().cursor() as c:
        c.execute(sql)
        return c.fetchall()

def fetch_student_by_id(id):
    # return None
    sql = "SELECT * FROM test.students where id = %(id)s"
    with get_conn().cursor() as c:
        c.execute(sql, {"id":id})
        return c.fetchone()

    
def delete_student_by_id(id):

    sql = "DELETE FROM test.students where id = %(id)s"
    try:
        conn = get_conn()
        with conn.cursor() as c:
            c.execute(sql, {"id":id})
        conn.commit()
        return True
    except Exception as e:
        print(e)
        return False


def update_student_by_id(id: int, name: str, age: int, is_active: bool = True):
    # return None
    sql = "UPDATE test.students SET name = %(name)s, age = %(age)s, is_active = %(is_active)s where id = %(id)s"
    try:
        conn = get_conn()
        with conn.cursor() as c:
            c.execute(sql, {"name":name, "age": age, "is_active": is_active, "id":id})
        conn.commit()
        return True
    except Exception as e:
        print(e)
        return False
