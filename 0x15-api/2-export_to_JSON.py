#!/usr/bin/python3
"""
Fetch todo list.
"""
import json
import requests
import sys


def get_todo():
    """fetch to do list.
    """
    user_id = int(sys.argv[1])
    user_result = requests.get(
        'https://jsonplaceholder.typicode.com/users/{}'.format(user_id))
    user_data = user_result.json()
    username = user_data['username']
    to_do_result = requests.get(
        'https://jsonplaceholder.typicode.com/users/{}/todos'.format(
            user_data['id']))
    to_do_list = to_do_result.json()
    tasks = []
    for todo in to_do_list:
        task = {
            "task": todo['title'],
            "completed": todo['completed'],
            "username": username
        }
        tasks.append(task)

    object_data = {
        str(user_id): tasks
    }
    filename = str(user_id) + '.json'
    export_json(filename, object_data)


def export_json(filename, object_data):
    """Export data to json.
    """
    with open(filename, 'w', encoding='UTF-8', newline='') as f:
        json.dump(object_data, f)
        f.close()


if __name__ == '__main__':
    get_todo()
