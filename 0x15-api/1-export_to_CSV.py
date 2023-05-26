#!/usr/bin/python3
"""
Fetch todo list.
"""
import csv
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
    rows = []
    for todo in to_do_list:
        row = [str(user_id), username, todo['completed'], todo['title']]
        rows.append(row)
    filename = str(user_id) + '.csv'
    export_csv(filename, rows)


def export_csv(filename, rows):
    """Export data to csv.
    """
    with open(filename, 'w', encoding='UTF-8', newline='') as f:
        writer = csv.writer(f, quoting=csv.QUOTE_ALL, dialect='excel')
        writer.writerows(rows)
        f.close()


if __name__ == '__main__':
    get_todo()
