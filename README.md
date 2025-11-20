# Python + MySQL – DELETE Operation (Record Removal)

This README explains how to safely delete records from a MySQL database using Python. It covers database connection, writing DELETE queries, executing commands, confirmation messages, and best practices like error handling and connection closing.

### Overview

The DELETE operation is an important part of CRUD (Create, Read, Update, Delete).
Python + MySQL का combination aapko backend systems me unwanted data ko safely remove karne ki capability deta hai.

Is guide me aap step-by-step seekhenge:

### How to connect Python to MySQL

How to write and execute DELETE queries

How to use WHERE conditions

How to safely commit changes

How to use try–except–finally for professional error handling

### Requirements

Before running the script, install MySQL connector:

pip install mysql-connector-python

🔗 Step 1: Connect Python with MySQL
import mysql.connector

try:
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="your_password",
        database="your_database"
    )

    cursor = conn.cursor()
    print("Database connected successfully!")

except mysql.connector.Error as e:
    print("Connection Error:", e)

🧾 Step 2: Write the DELETE SQL Query

IMPORTANT: Always use WHERE to prevent deleting all records.

delete_query = "DELETE FROM students WHERE roll_no = %s"
value = (101,)

▶️ Step 3: Execute DELETE Query
cursor.execute(delete_query, value)
conn.commit()
print("Record Deleted Successfully!")

⚠️ Step 4: Full Script with Error Handling
import mysql.connector

try:
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="your_password",
        database="your_database"
    )

    cursor = conn.cursor()

    delete_query = "DELETE FROM students WHERE roll_no = %s"
    value = (101,)

    cursor.execute(delete_query, value)
    conn.commit()

    if cursor.rowcount > 0:
        print("Record Deleted Successfully!")
    else:
        print("No matching record found.")

except mysql.connector.Error as e:
    print("Error occurred:", e)

finally:
    if cursor:
        cursor.close()
    if conn:
        conn.close()
    print("Connection closed.")

### Key Points to Remember

Always use WHERE — warna poora table delete ho sakta hai.

commit() is necessary to save changes.

Error handling makes your code safe and production-ready.

cursor.close() + conn.close() = good practice for resource cleanup.

### Real-World Use Cases

Removing inactive users

Deleting outdated records

Cleaning test data

Removing invalid entries from logs/tables
