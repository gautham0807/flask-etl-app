import psycopg2


conn = psycopg2.connect(
    database="data-engineering", 
    user="postgres", 
    password="Gautham@123", 
    host="localhost"
)


with conn.cursor() as c:
    c.execute("select 1")
    res = c.fetchone()
    print(f"Result: {res}")