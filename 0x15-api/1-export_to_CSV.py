#!/usr/bin/python3
"""returns information about his/her TODO list progress. """
from csv import DictWriter, QUOTE_ALL
import sys
import requests


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
            taskWithName['user_ID'] = EMPLOYID
            taskWithName['username'] = DATA.get('username')
            taskWithName['completed'] = task.get('completed')
            taskWithName['task'] = task.get('title')
            dictTasks.append(taskWithName)

        csv_file = f'{EMPLOYID}.csv'
        with open(csv_file, mode='w', newline='') as file:
            head = ["user_ID", "username", "completed", "task"]
            writer = DictWriter(file, fieldnames=head, quoting=QUOTE_ALL)
            writer.writerows(dictTasks)
    else:
        print(f"Request failed with status code: {response.status_code}")
