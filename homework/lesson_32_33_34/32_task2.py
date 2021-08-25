"""Task 2

Load data

Download all comments from a subreddit of your choice using URL: https://api.pushshift.io/reddit/comment/search/ .

As a result, store all comments in chronological order in JSON and dump it to a file."""
import requests
from requests import request
import json

link = "https://api.pushshift.io/reddit/comment/search/"
comments = requests.get(link)
parsed_json = (json.loads(comments.text))
new_json = {'data': [{}]}
list_json = []
for comment in parsed_json['data']:
    print(f"Created at: {comment['created_utc']}\nAuthor: {comment['author']}\nText:\n{comment['body']}")



