# 1. Import the connector and establish a connection
import mariadb
import sys # To exit on error

empno = input("Enter employee number : ")
empname = input("Enter employee name : ")

try:
    conn = mariadb.connect(
        user="root",
        password="admin",
        host="127.0.0.1", # or your MariaDB host
        database="employee"
    )
    cur = conn.cursor() # 2. Get a cursor object

    # 3. Define the SQL INSERT statement with placeholders
    sql = "INSERT INTO employee_data (empno, empname) VALUES (%s, %s)"
    val = (empno, empname) # 4. Create a tuple with your data

    # 5. Execute the query with the data
    cur.execute(sql, val)

    # 6. Commit the changes to the database
    conn.commit()

    print(f"{cur.rowcount} record inserted.")

except mariadb.Error as e:
    print(f"Error connecting to or writing to MariaDB: {e}")
    sys.exit(1) # Exit with an error code

finally:
    # 7. Close the cursor and connection
    if 'cur' in locals() and cur is not None:
        cur.close()
    if 'conn' in locals() and conn is not None:
        conn.close()
        print("Connection closed.")
