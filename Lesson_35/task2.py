"""Task 2 - Requests using concurrent and multiprocessing libraries
Download all comments from a subreddit of your choice using
URL: https://api.pushshift.io/reddit/comment/search/ .

As a result, store all comments in chronological order in JSON
and dump it to a file. For this task use concurrent and multiprocessing
libraries for making requests to Reddit API.

NOTE: For this task I am using the
URL: https://jsonplaceholder.typicode.com/posts/1/comments
to download fake comments.
"""
from concurrent.futures import ProcessPoolExecutor
import json
import requests


def get_comments(user_id):
    """Returns the comments for the user id"""
    url = f"https://jsonplaceholder.typicode.com/posts/{user_id}/comments"
    res = requests.get(url, timeout=(5, 5))
    return res.json()


if __name__ == "__main__":
    COMMENTS = {}

    with ProcessPoolExecutor() as executor:
        for index, data in zip(range(1, 6), executor.map(get_comments, range(1, 6))):
            COMMENTS[index] = data
            with open("comments.json", "w", encoding="UTF-8") as w_file:
                w_file.write(json.dumps(COMMENTS, indent=4))
