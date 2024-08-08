#!/usr/bin/python3

import sys
import requests

def fetch_employee_todo_progress(employee_id):
    # URL for the API endpoints
    users_url = 'https://jsonplaceholder.typicode.com/users'
    todos_url = 'https://jsonplaceholder.typicode.com/todos'
    
    # Fetch user data
    user_response = requests.get(users_url)
    users = user_response.json()
    
    # Find the employee name
    employee_name = None
    for user in users:
        if user['id'] == employee_id:
            employee_name = user['name']
            break
    
    if not employee_name:
        print(f"Employee with ID {employee_id} not found.")
        return
    
    # Fetch TODO data
    todos_response = requests.get(todos_url)
    todos = todos_response.json()
    
    # Filter todos for the given employee ID
    employee_todos = [todo for todo in todos if todo['userId'] == employee_id]
    
    # Calculate completed and total tasks
    total_tasks = len(employee_todos)
    completed_tasks = sum(todo['completed'] for todo in employee_todos)
    
    # Print the progress
    print(f"Employee {employee_name} is done with tasks({completed_tasks}/{total_tasks}):")
    for todo in employee_todos:
        if todo['completed']:
            print(f"\t {todo['title']}")

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python3 0-gather_data_from_an_API.py EMPLOYEE_ID")
        sys.exit(1)
    
    try:
        employee_id = int(sys.argv[1])
    except ValueError:
        print("Employee ID must be an integer.")
        sys.exit(1)
    
    fetch_employee_todo_progress(employee_id)
