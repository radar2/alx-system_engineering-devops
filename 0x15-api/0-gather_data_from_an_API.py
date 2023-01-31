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
        'https://jsonplaceholder.typicode.com/users/{}'.format(user_id))
    user_data = user_result.json()
    to_do_result = requests.get(
        'https://jsonplaceholder.typicode.com/users/{}/todos'.format(
            user_data['id']))
    to_do_list = to_do_result.json()
    completed_list = []
    for todo in to_do_list:
        if todo['completed']:
            completed_list.append(todo)
    print('Employee {} is done with tasks({}/{}):'.format(
        user_data['name'], len(completed_list), len(to_do_list)))
    for todo in completed_list:
        print('\t {}'.format(todo['title']))


if __name__ == '__main__':
    get_todo()
