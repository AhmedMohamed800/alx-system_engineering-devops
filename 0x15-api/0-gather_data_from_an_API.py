#!/usr/bin/python3
"""returns information about his/her TODO list progress. """
import requests
import sys

if __name__ == "__main__":
    EMPLOYID = int(sys.argv[1])
    TODOURL = f"https://jsonplaceholder.typicode.com/todos?userId={EMPLOYID}"
    USER = f"https://jsonplaceholder.typicode.com/users/{EMPLOYID}"
    response = requests.get(USER)

    if response.status_code == 200:
        DATA = response.json()
        TASKS = requests.get(TODOURL).json()
        com = 0
        unfinished = 0
        for task in TASKS:
            if task.get('completed'):
                com += 1
            else:
                unfinished += 1
        to = com + unfinished
        print(f"Employee {DATA.get('name')} is done with tasks({com}/{to}):")
        for task in TASKS:
            if task.get('completed'):
                print(f"\t {task.get('title')}")
    else:
        print(f"Request failed with status code: {response.status_code}")
