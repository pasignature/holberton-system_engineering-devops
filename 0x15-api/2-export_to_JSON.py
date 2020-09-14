#!/usr/bin/python3
""" gets information about employee using jsonplaceholder API"""
import json
import requests
import sys


if __name__ == "__main__":
    endpoint = 'https://jsonplaceholder.typicode.com/'

    userid = sys.argv[1]
    user = '{}users/{}'.format(endpoint, userid)
    result = requests.get(user)
    json_o = result.json()
    name = json_o.get('username')

    todos = '{}todos?userId={}'.format(endpoint, userid)
    result = requests.get(todos)
    tasks = result.json()
    l_task = []
    for task in tasks:
        dict_task = {"task": task.get('title'),
                     "completed": task.get('completed'),
                     "username": name}
        l_task.append(dict_task)

    d_task = {str(userid): l_task}
    filename = '{}.json'.format(userid)
    with open(filename, mode='w') as f:
        json.dump(d_task, f)
