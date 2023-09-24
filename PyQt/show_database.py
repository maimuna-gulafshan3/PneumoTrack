import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect('data.db')
cursor = conn.cursor()

# Retrieve and display user records
cursor.execute("SELECT * FROM users")
users = cursor.fetchall()

for user in users:
    print("ID:", user[0])
    print("Name:", user[1])
    print("Age:", user[2])
    print("Gender:", user[3])
    print("Username:", user[4])
    print("Password:", user[5])
    print("-------------------------")

# Close the connection
conn.close()
