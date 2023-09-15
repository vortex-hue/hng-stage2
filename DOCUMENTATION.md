# How to use 'PERSON' CRUD API
    this is a crud api built using fastapi, which is a python framework for building fast api's, below are the endpoints and how to use them

## Tips
visit
 ```/docs```
this route contains the swagger docs which is an interactive docs to help you get started on the api, the swagger docs also helps you to see how to use the api, and also how it operates under the hood


*Below are some of the operations the api can perform too
Persons*


``` 
    Method GET
    route /api
    Function All
    param[
        `
        None
        `
    ]
```

```
Method POST
route /api
Function Create Person
param[
        `
        {
        "name": "string",
        "email": "string",
        "age": 0
        }
        `
    ]
```

```
    Method GET
    route /api/{id}
    Function Show person
    param[
        `
        {
        "id": int
        }
        `
    ]
```

```
    Method PUT
    route /api/{id}
    Function Update a person reocrd
    param[
        `
        {
        "id": int,
        "name": "string",
        "email": "string",
        "age": 0
        }
        `
    ]
```

```
    Method DELETE
    route /api/{id}
    Function Delete a person
    param[
        `
        {
        "id": int,
      
        }
        `
    ]
```