# import sqlite3

# # Hardcoded credentials (Issue #1: Sensitive Information)
# USERNAME = "admin"
# PASSWORD = "password123"

# def connect_to_db():
#     # Potential SQL Injection Vulnerability (Issue #2)
#     conn = sqlite3.connect("example.db")
#     return conn

# def fetch_user_data(user_id):
#     conn = connect_to_db()
#     cursor = conn.cursor()

#     # Using user-supplied data directly in SQL query (Issue #3: SQL Injection)
#     query = f"SELECT * FROM users WHERE id = {user_id}"
#     cursor.execute(query)
#     result = cursor.fetchone()

#     # Unused variable (Issue #4: Unused variable)
#     unused_var = 42

#     return result

# def main():
#     user_id = input("Enter user ID: ")
#     print(fetch_user_data(user_id))

# if __name__ == "__main__":
#     main()
#----------------------
import sqlite3

def connect_to_db():
    conn = sqlite3.connect("example.db")
    return conn

def fetch_user_data(user_id):
    conn = connect_to_db()
    cursor = conn.cursor()

    # Prevent SQL Injection by using parameterized queries
    query = "SELECT * FROM users WHERE id = ?"
    cursor.execute(query, (user_id,))
    result = cursor.fetchone()

    return result

def main():
    user_id = input("Enter user ID: ")
    # Ensure the user_id is an integer (example for demonstration purposes)
    try:
        user_id = int(user_id)
        print(fetch_user_data(user_id))
    except ValueError:
        print("Invalid user ID. Please enter an integer.")

if __name__ == "__main__":
    main()
