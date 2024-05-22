from dotenv import load_dotenv

import os

load_dotenv()

#We can use two approaches to access environment k:v pairs
#Method 1 returns None if key doesn't exist
#Method 2 can return default values we set

print(os.getenv("SOME_KEY"))
# print(os.environ.get("SOME_KEY"))
# print(os.environ.get("DB_PASSWORD"))

print(os.environ)
print(os.environ.get("APP_NAME"))
print(os.environ.get("USERNAME"))
print(os.environ.get("DUMMY"), "IAmDummy")

