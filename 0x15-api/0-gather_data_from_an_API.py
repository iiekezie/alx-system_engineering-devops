#!/usr/bin/python3
"""Returns to-do list information for a given employee ID."""
import sys
import requests

def main(employee_id):
    url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    user_response = requests.get(url)
    
    if user_response.status_code != 200:
        print(f"User with ID {employee_id} not found.")
        return

    user = user_response.json()
    name = user['name']
    
    todos_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos"
    todos_response = requests.get(todos_url)
    
    if todos_response.status_code != 200:
        print("Error retrieving todos.")
        return
    
    todos = todos_response.json()
    
    total_tasks = len(todos)
    done_tasks = sum(1 for todo in todos if todo['completed'])
    
    print(f"Employee {name} is done with tasks({done_tasks}/{total_tasks}):")
    
    for todo in todos:
        if todo['completed']:
            print(f"\t {todo['title']}")

if __name__ == "__main__":
    if len(sys.argv) != 2 or not sys.argv[1].isdigit():
        print("Usage: python3 0-gather_data_from_an_API.py <employee_id>")
    else:
        main(int(sys.argv[1]))
