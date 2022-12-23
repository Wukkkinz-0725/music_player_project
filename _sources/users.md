## Users API

- Get user by id \
  GET /v1/users/query/{uid}

```
// return
{
    "UID" : "21312412849",
    "FirstName": "Ming",
    "LastName" : "Ming",
    "Sex": "male",
    "Age": "19",
    "Description": "A smart student",
    "Occupation" : "student"
}
```

- Create user \
  POST /v1/users/create

```
// request body
{
    "FirstName": "Ming",
    "LastName" : "Ming",
    "Sex": "male",
    "Age": "18",
    "Description" : "A smart student",
    "Occupation" : "Student"
}

// create a uid and store into db

// return 
{
    "msg" : "success"
}
```

- Delete user \
  POST /v1/users/del/{uid}

```
// return 
{
    "msg" : "success"
}
```

- Update user info \
  POST /v1/users/update/{uid}

```
// request body (if empty then don't modify)
{
    "FirstName": "Ming",
    "LastName" : "Ming",
    "Sex": "", 
    "Age": "18",
    "Description" : "A smart student",
    "Occupation" : "Student"
}

// return
{
    "msg" : "success"
}
```