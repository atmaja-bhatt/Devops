# app.py

import os
import sqlite3

# Hardcoded credentials (security issue)
USERNAME = "admin"
PASSWORD = "12345"

# Vulnerable function: SQL Injection possibility
def get_user_details(username):
    connection = sqlite3.connect("example.db")
    cursor = connection.cursor()
    
    # Bad Practice: Concatenating SQL queries with untrusted input
    query = "SELECT * FROM users WHERE username = '" + username + "';"
    cursor.execute(query)
    
    result = cursor.fetchone()
    connection.close()
    return result

# Function with potential resource leak
def read_file(file_path):
    try:
        f = open(file_path, "r")
        return f.read()
    except Exception as e:
        print(f"Error: {e}")
    # Missing: File should be closed properly to avoid resource leaks

# Function with unused variable
def print_hello_world():
    message = "Hello, World!"  # Unused variable
    print("Hello, Earth!")  # Intentional error for demonstrating SonarCloud

# Function with infinite loop
def infinite_loop():
    while True:  # Bug: Infinite loop
        print("Looping forever...")

# Insecure hashing algorithm
def insecure_hash(data):
    import hashlib
    return hashlib.md5(data.encode()).hexdigest()  # MD5 is considered insecure

# Hardcoded sensitive information
def connect_to_db():
    connection_string = "server=example.com;database=example;uid=admin;pwd=secret"  # Hardcoded credentials
    print("Connecting to database...")

# Function with a catch-all exception handler
def divide_numbers(a, b):
    try:
        return a / b
    except:
        print("An error occurred")  # Catch-all exception is a bad practice

# Unreachable code
def check_age(age):
    if age < 18:
        return "Minor"
        print("You are under 18")  # This line will never be reached

# Main function
if __name__ == "__main__":
    print_hello_world()
    user_details = get_user_details("admin")
    print("User Details:", user_details)

    read_file("/path/to/file.txt")
    result = divide_numbers(10, 0)
    print("Result:", result)
    
    infinite_loop()  # This will run forever, intentionally added for demo purposes
