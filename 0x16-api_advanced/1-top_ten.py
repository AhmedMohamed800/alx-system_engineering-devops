#!/usr/bin/python3
"""0-subs"""
import requests


def top_ten(subreddit):
    """return the number of subscribers"""
    url = f'https://www.reddit.com/r/{subreddit}/hot.json?limit=10'
    header = {'User-Agent': 'My User Agent 1.0'}
    response = requests.get(url, headers=header, allow_redirects=False)
    if response.status_code == 200:
        json_data = response.json()
        children = json_data.get('data').get('children')
        if len(children) > 0:
            for child in children:
                print(child.get('data').get('title'))
        else:
            print(None)
    else:
        print(None)
