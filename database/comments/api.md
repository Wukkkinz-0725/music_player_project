## APIs

- Get comment by id \
  GET /comment/query/<cid>

```
// return
{
    'comment_id': 1, 
    'user_id':1, 
    'song_id': 1, 
    'content': 'hello world', 
    'date':'2022-12-13 18:52:59.250613'
}
```

- Create comment \
  POST /comment/create

```
// request body
{
    'comment_id': 1, 
    'user_id':1, 
    'song_id': 1, 
    'content': 'hello world', 
    'date':'2022-12-13 18:52:59.250613'
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

- Delete comment \
  POST /comment/delete/<cid>

```
// return 
{
    "msg" : "success"  # TODO: this will return res
}
{
    "msg" : "Fail to delete"
}
```

- Update comment info \
  POST /comment/update/<cid>

```
// request body
{
    'user_id':2, 
    'song_id': 2, 
    'content': 'hello world 2', 
    'date': '2022-12-13 18:52:59.250613'
}

// return
{
    "msg" : "success"  # TODO: this will return res
}
{
    "msg" : "Fail to update"
}
```