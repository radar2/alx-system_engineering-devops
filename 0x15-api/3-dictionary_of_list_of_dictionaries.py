#!/usr/bin/python3
"""
Fetch todo list.
"""
import json
import requests


def get_todo():
    """fetch to do list.
    """
    users_result = requests.get(
        'https://jsonplaceholder.typicode.com/users')
    users_data = users_result.json()
    object_data = {}
    for user in users_data:
        user_id = user['id']
        username = user['username']
        to_do_result = requests.get(
            'https://jsonplaceholder.typicode.com/users/{}/todos'.format(
                user_id))
        to_do_list = to_do_result.json()
        tasks = []
        for todo in to_do_list:
            task = {
                "username": username,
                "task": todo['title'],
                "completed": todo['completed'],
            }
            tasks.append(task)
        object_data[str(user_id)] = tasks
    filename = "todo_all_employees.json"
    export_json(filename, object_data)


def export_json(filename, object_data):
    """Export data to json.
    """
    with open(filename, 'w', encoding='UTF-8', newline='') as f:
        json.dump(object_data, f)
        f.close()


if __name__ == '__main__':
    get_todo()
