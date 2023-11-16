"""Task 3 - Requests using multiprocessing
Download all comments from a subreddit of your choice using
URL: https://api.pushshift.io/reddit/comment/search/ .

As a result, store all comments in chronological
order in JSON and dump it to a file.
For this task use Threads for making requests to reddit API.

NOTE: For this task I am using the
URL: https://jsonplaceholder.typicode.com/posts/1/comments
to download fake comments.
"""
from concurrent.futures import ThreadPoolExecutor
import json
import requests

COMMENTS = {}


def get_comments(user_id):
    """Returns the comments for the user id"""
    url = f"https://jsonplaceholder.typicode.com/posts/{user_id}/comments"
    res = requests.get(url, timeout=(5, 5))

    COMMENTS[user_id] = res.json()


if __name__ == "__main__":
    with ThreadPoolExecutor() as executor:
        executor.map(get_comments, range(1, 6))

    with open("comments.json", "w", encoding="UTF-8") as file:
        file.write(json.dumps(COMMENTS, indent=4))
