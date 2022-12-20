import requests
import json
from datetime import datetime

base_url = 'http://localhost:9001'
# eb_url = 'http://6156projectsongs-env.eba-zhpag7xk.us-east-1.elasticbeanstalk.com'

# ## TEST: TABLE [songs]

# url = 'http://6156projectsongs-env.eba-zhpag7xk.us-east-1.elasticbeanstalk.com/songs/create'
url = base_url + "/songs/create"
data = {'song_name':'ABC', 'artist': 'A', 'release_date': '2022-10-10'}
res = requests.post(url, json=data, headers={'Content-Type': 'application/json'})

res.json()

url = base_url + '/songs/create'
data = {'song_name':'ABC', 'artist': 'B', 'release_date': str(datetime.now())}
requests.post(url, json=data, headers={'Content-Type': 'application/json'}).json()

# +

url = 'http://6156projectsongs-env.eba-zhpag7xk.us-east-1.elasticbeanstalk.com/songs/create'
data = {'song_name':'ABCD', 'artist': 'B', 'release_date': str(datetime.now())}
requests.post(url, json=data, headers={'Content-Type': 'application/json'})
# -

print(requests.get('http://6156projectsongs-env.eba-zhpag7xk.us-east-1.elasticbeanstalk.com/songs/query/3').text)

print(requests.get('http://6156projectsongs-env.eba-zhpag7xk.us-east-1.elasticbeanstalk.com/songs/query/3').text)

print(requests.get('http://localhost:9001/songs/query/song_name/ABC').text)

print(requests.get(base_url+'/songs/all').text)

url = 'http://localhost:9001/songs/update/1'
data = {'song_name':'ABCDD', 'artist': 'DDABC'}
requests.post(url, json=data, headers={'Content-Type': 'application/json'}).json()

print(requests.get('http://localhost:9001/songs/all').text)

requests.post('http://localhost:9001/songs/delete/1')


def convert_word(w):
    s = sorted(list(set(list(w))))
    return ''.join(s)


w = convert_word('ddbca')

w


