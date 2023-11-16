"""Task 2 - Load data
Download all comments from a subreddit of your choice using
URL: https://api.pushshift.io/reddit/comment/search/ .
As a result, store all comments in chronological order
in JSON and dump it to a file.

NOTE: For this task I am using the
URL: https://jsonplaceholder.typicode.com/posts/1/comments
to download fake comments. Since the received data
does not contain information about the date the comments
were created, sorting is done by the “name” field
"""
import json

import requests

URL = "https://jsonplaceholder.typicode.com/posts/1/comments"

response = requests.get(URL, timeout=(5, 5))
data = response.json()

sorted_data = sorted(data, key=lambda x: x["name"])

with open("comments.json", "w", encoding="UTF-8") as file:
    file.write(json.dumps(sorted_data, indent=4))
