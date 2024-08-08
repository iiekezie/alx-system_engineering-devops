#!/usr/bin/python3
"""Exports to-do list information for a given employee ID to CSV format."""
import sys
import requests
import csv

def main(employee_id):
    user_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    todos_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos"
    
    user_response = requests.get(user_url)
    todos_response = requests.get(todos_url)
    
    if user_response.status_code != 200:
        print(f"User with ID {employee_id} not found.")
        return

    if todos_response.status_code != 200:
        print("Error retrieving todos.")
        return
    
    user = user_response.json()
    todos = todos_response.json()
    
    username = user['username']
    
    filename = f"{employee_id}.csv"
    
    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)
        for todo in todos:
            writer.writerow([employee_id, username, todo['completed'], todo['title']])
    
    print(f"Data exported to {filename}")

if __name__ == "__main__":
    if len(sys.argv) != 2 or not sys.argv[1].isdigit():
        print("Usage: python3 1-export_to_CSV.py <employee_id>")
    else:
        main(int(sys.argv[1]))
