import sqlite3

# Hardcoded credentials (Issue #1: Sensitive Information)
USERNAME = "admin"
PASSWORD = "password123"

def connect_to_db():
    # Potential SQL Injection Vulnerability (Issue #2)
    conn = sqlite3.connect("example.db")
    return conn

def fetch_user_data(user_id):
    conn = connect_to_db()
    cursor = conn.cursor()

    # Using user-supplied data directly in SQL query (Issue #3: SQL Injection)
    query = f"SELECT * FROM users WHERE id = {user_id}"
    cursor.execute(query)
    result = cursor.fetchone()

    # Unused variable (Issue #4: Unused variable)
    unused_var = 42

    return result

def main():
    user_id = input("Enter user ID: ")
    print(fetch_user_data(user_id))

if __name__ == "__main__":
    main()
