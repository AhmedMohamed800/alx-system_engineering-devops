#!/usr/bin/python3
"""returns information about his/her TODO list progress. """
import json
import sys
import requests


if __name__ == "__main__":
    USER = f"https://jsonplaceholder.typicode.com/users"
    response = requests.get(USER)

    if response.status_code == 200:
        DATA = response.json()
        dictTasks = []
        for task in TASKS:
            taskWithName = {}
            taskWithName['task'] = task.get('title')
            taskWithName['completed'] = task.get('completed')
            taskWithName['username'] = DATA.get('username')
            dictTasks.append(taskWithName)

        csv_file = 'todo_all_employees'
        with open(csv_file, 'w') as file:
            dict_to_print = {}
            for user in USER:
                dictTasks = {}
                use = f"userId={user.get('name')}"
                TODOURL = f"https://jsonplaceholder.typicode.com/todos?{use}"
                for task in requests.get(TODOURL).json():
                    dict_to_print[user.get('')]
            json.dump(dict_to_print, file)
    else:
        print(f"Request failed with status code: {response.status_code}")
