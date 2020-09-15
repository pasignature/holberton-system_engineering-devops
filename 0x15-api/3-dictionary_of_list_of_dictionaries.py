#!/usr/bin/python3
""" gets information about employee using requests """
import json
import requests
import sys


if __name__ == "__main__":
    endpoint = 'https://jsonplaceholder.typicode.com/'
    user = '{}users'.format(endpoint)
    result = requests.get(user)
    json_o = result.json()
    d_task = {}
    for user in json_o:
        name = user.get('username')
        userid = user.get('id')
        todos = '{}todos?userId={}'.format(endpoint, userid)
        result = requests.get(todos)
        tasks = result.json()
        l_task = []
        for task in tasks:
            dict_task = {"username": name,
                         "task": task.get('title'),
                         "completed": task.get('completed')}
            l_task.append(dict_task)

        d_task[str(userid)] = l_task
    filename = 'todo_all_employees.json'
    with open(filename, mode='w') as f:
        json.dump(d_task, f)
