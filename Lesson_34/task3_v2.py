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
import threading
import json
import requests


def get_comments(user_id):
    """Returns the comments for the user id"""
    url = f"https://jsonplaceholder.typicode.com/posts/{user_id}/comments"
    res = requests.get(url, timeout=(5, 5))

    comments = []
    with open("comments.json", "r", encoding="UTF-8") as r_file:
        comments = json.loads(r_file.read())

    comments.append({user_id: res.json()})

    with open("comments.json", "w", encoding="UTF-8") as w_file:
        w_file.write(json.dumps(comments, indent=4))


if __name__ == "__main__":
    with open("comments.json", "w", encoding="UTF-8") as file:
        file.write("[]")

    treads = []
    for i in range(1, 6):
        t = threading.Thread(target=get_comments, args=(i,))
        treads.append(t)
        t.start()

    for tread in treads:
        tread.join()
