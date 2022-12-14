## APIs

- Get song by id \
  GET /song/query/<cid>

```
// return
{
    'song_id': 2, 
    'song_name':'ABC', 
    'album_name': 'DEF', 
    'singer': 'A'
}
```

- Create song \
  POST /song/create

```
// request body
{
    'song_id': 2, 
    'song_name':'ABC', 
    'album_name': 'DEF', 
    'singer': 'A'
}

// return 
{
    "msg" : "success"  # TODO: this will return res
}
{
    "msg" : "Fail to create"
}
{
   "msg" : 'Content-Type Not Supported'
}
```

- Delete song \
  POST /song/delete/<cid>

```
// return 
{
    "msg" : "success"  # TODO: this will return res
}
{
    "msg" : "Fail to delete"
}
```

- Update song info \
  POST /song/update/<cid>

```
// request body
{
    'song_id': 2, 
    'song_name':'ABCDD', 
    'album_name': 'DEDDF', 
    'singer': 'DDA'
}

// return
{
    "msg" : "success"  # TODO: this will return res
}
{
    "msg" : "Fail to update"
}
```