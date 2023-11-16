"""HTTP-requests"""

import requests

URL = "https://translate.google.com/"

response = requests.get(URL, timeout=(5, 5))

with open('html_example.html', "w", encoding="UTF-8") as file:
    file.write(response.text)
