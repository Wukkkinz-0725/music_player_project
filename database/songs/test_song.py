import requests
import json
from datetime import datetime

# test create_comment
url = 'http://localhost:9001/song/create'
data = {'song_id': 2, 'song_name':'ABC', 'album_name': 'DEF', 'singer': 'A'}
requests.post(url, json=data, headers={'Content-Type': 'application/json'})

# test get_comment
print(requests.get('http://localhost:9001/song/query/2').text)

# test update_comment
url = 'http://localhost:9001/song/update/2'
data = {'song_id': 2, 'song_name':'ABCDD', 'album_name': 'DEDDF', 'singer': 'DDA'}
requests.post(url, json=data, headers={'Content-Type': 'application/json'})
print(requests.get('http://localhost:9001/song/query/1').text)

# test delete_comment
requests.post('http://localhost:9001/song/delete/1')
print(requests.get('http://localhost:9001/song/query/1').text)