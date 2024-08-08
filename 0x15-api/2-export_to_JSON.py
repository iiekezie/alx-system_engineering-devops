#!/usr/bin/python3
import json
import requests
import sys

def fetch_data(user_id):
    url = f'https://jsonplaceholder.typicode.com/todos?userId={user_id}'
    response = requests.get(url)
    response.raise_for_status()
    return response.json()

def main(user_id):
    data = fetch_data(user_id)
    tasks = [{
        "task": task["title"],
        "completed": task["completed"],
        "username": "Antonette"  # This should be replaced with the actual username if available
    } for task in data]

    output = {user_id: tasks}

    with open(f"{user_id}.json", "w") as f:
        json.dump(output, f, indent=4)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 2-export_to_JSON.py USER_ID")
        sys.exit(1)

    user_id = sys.argv[1]
    main(user_id)
