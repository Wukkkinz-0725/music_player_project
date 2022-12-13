import requests
import json
from datetime import datetime

# test create_comment
url = 'http://localhost:9001/comments/create'
data = {'comment_id': 1, 'user_id':1, 'song_id': 1, 'content': 'hello world', 'date':str(datetime.now())}
requests.post(url, json=data, headers={'Content-Type': 'application/json'})

# test get_comment
print(requests.get('http://localhost:9001/comments/query/1').text)

# test update_comment
url = 'http://localhost:9001/comments/update/1'
data = {'user_id':2, 'song_id': 2, 'content': 'hello world 2', 'date':str(datetime.now())}
requests.post(url, json=data, headers={'Content-Type': 'application/json'})
print(requests.get('http://localhost:9001/comments/query/1').text)

# test delete_comment
requests.post('http://localhost:9001/comments/delete/1')
print(requests.get('http://localhost:9001/comments/query/1').text)