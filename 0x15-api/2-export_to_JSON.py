#!/usr/bin/python3
"""returns information about his/her TODO list progress. """
import sys
import requests
import json


if __name__ == "__main__":
    EMPLOYID = int(sys.argv[1])
    TODOURL = f"https://jsonplaceholder.typicode.com/todos?userId={EMPLOYID}"
    USER = f"https://jsonplaceholder.typicode.com/users/{EMPLOYID}"
    response = requests.get(USER)

    if response.status_code == 200:
        DATA = response.json()
        TASKS = requests.get(TODOURL).json()
        dictTasks = []
        for task in TASKS:
            taskWithName = {}
            taskWithName['task'] = task.get('title')
            taskWithName['completed'] = task.get('completed')
            taskWithName['username'] = DATA.get('username')
            dictTasks.append(taskWithName)

        csv_file = f'{EMPLOYID}.json'
        with open(csv_file, 'w') as file:
            dict_to_print = {EMPLOYID: dictTasks}
            json.dump(dict_to_print, file)
    else:
        print(f"Request failed with status code: {response.status_code}")
