## Users API

- Get user by id \
  `GET /users/query/{uid}`

```
// return
{
    "id" : "1",
    "username": "Charlie",
    "email": "abcde@columbia.edu",
    "age": "19",
    "description": "Welcome to Music Collection"
}
```

- Create user \
  `POST /users/create`
```
// request body
{
    "username": "Charlie",
    "email": "abcde@columbia.edu",
    "age": "19",
    "description": "Welcome to Music Collection"
}

// return 
{
    "uid" : 1
}
```

- Delete user \
  `POST /users/delele/{uid}`

```
return 
{
    "msg" : "Delete Successfully"
}
```

- Update user info \
  POST /users/update/{uid}

```
// request body
{
    "username": "Charlie",
    "email": "abcde@columbia.edu",
    "age": "19",
    "description": "Welcome to Music Collection"
}

// return
{
    "msg" : "Update Successfully"
}
```