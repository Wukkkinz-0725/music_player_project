import requests
import json
from datetime import datetime

# ## TEST: TABLE [songs]

url = 'http://e61561.cjmkumdiw0f0.us-east-1.rds.amazonaws.com:9001/songs/create'
data = {'song_name':'ABC', 'artist': 'A', 'release_date': str(datetime.now())}
requests.post(url, json=data, headers={'Content-Type': 'application/json'})

# +

url = 'http://localhost:9001/songs/create'
data = {'song_name':'ABC', 'artist': 'B', 'release_date': str(datetime.now())}
requests.post(url, json=data, headers={'Content-Type': 'application/json'})

# +

url = 'http://localhost:9001/songs/create'
data = {'song_name':'ABCD', 'artist': 'B', 'release_date': str(datetime.now())}
requests.post(url, json=data, headers={'Content-Type': 'application/json'})
# -

print(requests.get('http://localhost:9001/songs/query/3').text)

print(requests.get('http://localhost:9001/songs/query/song_name/ABC').text)

print(requests.get('http://localhost:9001/songs/all').text)

url = 'http://localhost:9001/songs/update/4'
data = {'song_name':'ABCDD', 'artist': 'DDABC'}
requests.post(url, json=data, headers={'Content-Type': 'application/json'})

print(requests.get('http://localhost:9001/songs/all').text)

requests.post('http://localhost:9001/songs/delete/1')

# ## 2. TEST Collections

url = 'http://localhost:9001/collections/create'
data = {'colid': 1, 'uid':1, 'sid':1, 'song_name': 'love the way you lie'}
requests.post(url, json=data, headers={'Content-Type': 'application/json'})

url = 'http://localhost:9001/collections/create'
data = {'colid': 3, 'uid':2, 'sid':1, 'song_name': 'love the way you lie'}
requests.post(url, json=data, headers={'Content-Type': 'application/json'})

requests.get('http://localhost:9001/collections/all').text

requests.get('http://localhost:9001/collections/query/colid/1').text

requests.get('http://localhost:9001/collections/query/colid/3').text

requests.get('http://localhost:9001/collections/query/sid/1').text

requests.get('http://localhost:9001/collections/query/uid/1').text

url = 'http://localhost:9001/collections/create'
data = {'colid': 4, 'uid':4, 'sid':1, 'song_name': 'love the way you lie'}
requests.post(url, json=data, headers={'Content-Type': 'application/json'})

url = 'http://localhost:9001/collections/create'
data = {'colid': 5, 'uid':2, 'sid':2, 'song_name': 'bye'}
requests.post(url, json=data, headers={'Content-Type': 'application/json'})

requests.get('http://localhost:9001/collections/all').text

requests.post('http://localhost:9001/collections/delete/uid/2')

requests.get('http://localhost:9001/collections/all').text


