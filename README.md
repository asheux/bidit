# bidit

## Application installation

- Virtual Environment

```
$ python3 -m venv venv
$ source venv/bin/activate
```

- Dependencies

```
$ pip install -r requirements/dev.txt
```

- Database

```
$ touch .env
```
> export all the the environment variables included in the .env.example, change value to your own
> or simply paste the ones in the .env.example and edit the values

- Migrations

```
$ python manage.py makamigrations
$ python manage.py migrate
```

- Server

```
$ python manage.py runserver
```

## Create a new user

- Request query

```
mutation {
    createUser(input: {
firstName: "Brian",
lastName: "Mboya",
email: "mboya9@gmail.com",
password: "mermaid"}) {
        user {
            id,
            firstName,
            lastName,
            email,
        }
    }
}
```

## Login user

- Request query

```
mutation {
    loginUser(email: "paxtonmboya@gmail.com", password: "darling") {
        token,
            user {
                id,
                email,
                firstName,
                lastName
            }
    }
}

```

