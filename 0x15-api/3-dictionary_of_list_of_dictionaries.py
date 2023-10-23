#!/usr/bin/python3
"""returns information about his/her TODO list progress. """
import json
import requests


if __name__ == "__main__":
    USER = "https://jsonplaceholder.typicode.com/users"
    response = requests.get(USER)

    if response.status_code == 200:
        with open('todo_all_employees.json', 'w') as file:
            dict_to_print = {}
            for user in response.json():
                dictTasks = []
                use = f"userId={user.get('id')}"
                TODOURL = f"https://jsonplaceholder.typicode.com/todos?{use}"
                for task in requests.get(TODOURL).json():
                    taskWithName = {}
                    taskWithName['username'] = user.get('username')
                    taskWithName['task'] = task.get('title')
                    taskWithName['completed'] = task.get('completed')
                    dictTasks.append(taskWithName)
                dict_to_print[user.get('id')] = dictTasks
            json.dump(dict_to_print, file)
    else:
        print(f"Request failed with status code: {response.status_code}")
