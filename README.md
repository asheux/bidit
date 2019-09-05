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

## Add item

- Request query

```
mutation {
    createItem(input: {
title: "The bomb",
description: "This is an example of an item",
reservePrice: 1399,
photo: "this",
}) {
        item {
            id,
                title,
                description,
                reservePrice,
                photo
        }
    }
}
```

## Get all items

```
query {
    items {
        edges {
            node {
                id,
                    title,
                    description,
                    reservePrice,
                    photo,
                    owner {
                        firstName,
                        lastName,
                        email,
                        phoneNumber
                    }
            }
        }
    }
}
```

## Get a single item

```
query {
    item(id: "2") {
        title,
            description,
            reservePrice,
            photo
    }
}
```

