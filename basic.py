# # def hello(name):
# #     print(f"Hey {name}")
# #     return f"Hi {name}"

# # def hello(f, *args, **kwargs):
# #     # Some major processing
# #     return f


# # @hello
# # def wish():
# #     return "Good Morning"

# # hi = hello
# # print(hi)

# # msg = hi("Bob")

# # data = [{"id": 1, "name": "Bob"}, {}, {}]

# # for i, s in enumerate(data):
# #     if s['id'] == 1:
# #         del data[i]


# # print(data)

# import sqlite3

# # Connect to the SQLite database
# conn = sqlite3.connect('example.db')

# # Create a cursor object using the 'with' statement
# with conn.cursor() as c:
#     # Execute SQL statements
#     c.execute('''CREATE TABLE IF NOT EXISTS Employees (
#                     EmployeeID INTEGER PRIMARY KEY,
#                     FirstName TEXT,
#                     LastName TEXT,
#                     Age INTEGER,
#                     DepartmentID INTEGER,
#                     FOREIGN KEY (DepartmentID) REFERENCES Departments(DepartmentID)
#                 )''')

#     c.execute('''CREATE TABLE IF NOT EXISTS Departments (
#                     DepartmentID INTEGER PRIMARY KEY,
#                     DepartmentName TEXT
#                 )''')

# # Commit changes and close the connection
# conn.commit()
# conn.close()

tup = [1,2,3]

def split(a, b, c):
   return a + b +c

print(*tup)