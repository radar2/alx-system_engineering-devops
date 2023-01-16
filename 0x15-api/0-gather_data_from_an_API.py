#!/usr/bin/python3
"""Fetch informations of todo list"""
import requests
import sys


def get_todo():
    """
    List to do list
    """
    user_id = int(sys.argv[1])
    user_result = requests.get(
        "https://jsonplaceholder.typicode.com/users/{}".format(user_id))
    user_data = user_result.json()
    to_do_result = requests.get(
        "https://jsonplaceholder.typicode.com/users/{}/todos".format(
            user_data['id']))
    to_do_list = to_do_result.json()
    complete_count = 0
    uncompleted_count = 0
    for todo in to_do_list:
        if todo['completed']:
            complete_count = complete_count + 1
        else:
            uncompleted_count = uncompleted_count + 1
    print("Employee {} is done with tasks({}/{}):".format(
        user_data['name'], complete_count, len(to_do_list)))
    for todo in to_do_list:
        print("\t {}".format(todo['title']))


if __name__ == '__main__':
    get_todo()
