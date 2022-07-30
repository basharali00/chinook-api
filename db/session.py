import sqlite3

con = sqlite3.connect("./db/chinook.sqlite", check_same_thread=False)

print("Database Connected Successfuly")